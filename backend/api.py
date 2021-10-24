from flask import Flask, request
import json
# import imgur-uploader
import time
import ocr
import nft
import datetime
import base64
import PIL
from PIL import Image

limit = 400

app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get-shibaceipts", methods=['GET'])
def get_shibaceipts():
    with open("./global_data/global.json", "r") as rf:
        decoded_data = json.load(rf)
        return json.dumps(decoded_data)


@app.route("/get-current-user-shibaceipts", methods=['GET'])
def get_current_user_shibaceipts():
    with open("./user_data/shibas.json", "r") as rf:
        decoded_data = json.load(rf)
        return json.dumps(decoded_data)


@app.route("/get-current-user", methods=['GET'])
def get_current_user():
    with open("./user_data/profile.json", "r") as rf:
        decoded_data = json.load(rf)
        return json.dumps(decoded_data)


@app.route("/new-receipt", methods=['POST'])
def new_receipt():
    # return json.dumps("{}") #disabled by Marc for now
    # accept an image, save it
    userid = request.form['userid']

    file_name = "raw_images/" + str(userid) + "_" + str(time.time()) + ".png"
    # get image from base64
    b64_image = request.form['receipt']

    # ugly hard coded
    header = "data:image/png;base64,"
    with open(file_name, "wb") as fh:
        fh.write(base64.b64decode(b64_image[len(header):]))

    if(request.form['flip']):
        im = Image.open(file_name)
        out = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        out.save(file_name)
    # run ocr on image and get the total value
    # total, _receipt_items = ocr.ocr(file_name)
    total, _receipt_items, nb, pb = ocr.ocr(file_name)
    annotated_path = ocr.annotate_img(file_name, nb, pb)

    # generate string to use to make nft image using the total amount
    # higher value = better nft
    img_url = nft.generate_nft(
        total, file_name, limit)

    # create the entry to be appended to global.json
    new_entry = {}
    new_entry["owner"] = userid
    new_entry["minter"] = userid
    new_entry["location"] = img_url
    new_entry["value"] = total
    new_entry["expiration"] = str(datetime.datetime.now())

    user_entry = {}
    user_entry["username"] = userid
    user_entry["avatar"] = img_url

    global_entry = {}
    global_entry["user"] = user_entry
    global_entry["shibaceipt"] = new_entry

    # update the global data
    with open("./global_data/global.json", "r") as rf:
        decoded_data = json.load(rf)
        decoded_data.update(global_entry)
    with open("./global_data/global.json", "w") as rf:
        rf.write(json.dumps(decoded_data))

    # create the json version of the items bought and cost
    item_dict = {}
    for k, v in _receipt_items:
        item_dict[k] = v

    # update location, owner, minter and total value
    json_obj = {}
    json_obj["location"] = img_url
    json_obj["owner"] = userid
    json_obj["minter"] = userid
    json_obj["value"] = total
    json_obj["data"] = item_dict
    json_obj["imgpath"] = annotated_path

    # update the user data
    with open("./user_data/receipts.json", "r") as rf:
        decoded_data = json.load(rf)
        decoded_data.update(json_obj)
    with open("./user_data/receipts.json", "w") as rf:
        json.dumps(rf.write(json.dumps(decoded_data)))

    # return nft url to the frontend
    return json.dumps(decoded_data)


@app.route("/spending", methods=['POST'])
def spending():
    userid = request.form['userid']
    with open("./user_data/" + userid + ".json", "r") as rf:
        decoded_data = json.load(rf)
    return json.dumps(decoded_data)


@app.route("/global-data", methods=['GET'])
def get_global_data():
    with open("./global_data/global.json", "r") as rf:
        decoded_data = json.load(rf)
    return json.dumps(decoded_data)


@app.route("/view-goals", methods=['GET'])
def view_goals():
    # return json object eith budget goals
    return


@app.route("/get-friends")
def get_friends():
    return


@app.route("/get-current-user-receipts", methods=['GET'])
def get_current_user_receipts():
    with open("./user_data/receipts.json", "r") as rf:
        decoded_data = json.load(rf)
        return json.dumps(decoded_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30006, debug=True)
