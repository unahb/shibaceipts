from flask import Flask, request
import json
#import imgur-uploader
import time
import ocr
import nft
import datetime
from base64 import decodestring

limit = 400

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get-shibaceipts", methods=['GET'])
def get_shibaceipts():
    with open("./global_data/global.json", "r") as rf:
        decoded_data = json.load(rf)
        return json.dumps(decoded_data)

@app.route("/get-current-user", methods=['GET'])
def get_current_user():
    with open("./user_data/profile.json", "r") as rf:
        decoded_data = json.load(rf)
        return json.dumps(decoded_data)

@app.route("/new-receipt", methods=['POST'])
def new_receipt():
    # accept an image, save it
    userid = request.form['userid']
    file_name = "raw_images/" + str(userid) + "_" + str(time.time()) + ".png"
    # get image from base64
    b64_image = request.form['receipt']
    with open(file_name, "wb") as fh:
        fh.write(decodestring(b64_image))

    # run ocr on image and get the total value
    total, _receipt_items = ocr.ocr(file_name)

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
    new_entry["expiration"] = str(datetime.now())

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30006, debug=True)
