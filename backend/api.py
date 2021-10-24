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
import jsbeautifier

limit = 400

app = Flask(__name__, static_url_path='/static', static_folder='static')

opts = jsbeautifier.default_options()
opts.indent_size = 2


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

    if request.form['flip'] == 'yes':
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

    # need to update the following
    # 1. user data (shibas)
    # 2. user data (receipts)

    # update user data(profile)
    new_shibaceipt = {}
    new_shibaceipt['location'] = img_url
    new_shibaceipt['owner'] = userid
    new_shibaceipt['minter'] = userid
    new_shibaceipt['value'] = total
    shiba_wrapper = {}
    shiba_wrapper['shibaceipt'] = new_shibaceipt
    with open("./user_data/shibas.json", "r") as rf:
        decoded_data = json.load(rf)
        decoded_data['data'].append(shiba_wrapper)
    with open("./user_data/shibas.json", "w") as rf:
        rf.write(json.dumps(decoded_data))

    # update user data (receipts)
    new_receipt = {}
    # create the json version of the items bought and cost
    item_dict = {}
    for k, v in _receipt_items:
        item_dict[k] = v

    new_receipt['receipt'] = item_dict
    new_receipt['imgpath'] = annotated_path

    with open("./user_data/receipts.json", "r") as rf:
        decoded_data = json.load(rf)
        decoded_data['data'].append(new_receipt)
    with open("./user_data/receipts.json", "w") as rf:
        rf.write(json.dumps(decoded_data))
    return {}


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


@app.route('/purchase-shibaceipt', methods=['POST'])
def purchase_shibaceipt():
    price = int(request.form['price'])
    shibaceipt = request.form['shibaceipt']
    with open('./user_data/profile.json', 'r') as rf:
        decoded_data = json.load(rf)
        new_owner = decoded_data['username']
        if not price <= decoded_data['account_value']:
            return json.dumps({'status': 'failure'})
        else:
            decoded_data['account_value'] -= price
    with open('./user_data/profile.json', 'w') as rf:
        rf.write(jsbeautifier.beautify(json.dumps(decoded_data), opts))

    with open('./global_data/global.json', 'r') as rf:
        decoded_data = json.load(rf)
        i = 0
        shiba = decoded_data['data'][0]
        while shiba['shibaceipt']['location'] != shibaceipt:
            i += 1
            shiba = decoded_data['data'][i]
        shiba = shiba['shibaceipt']
        shiba['owner'] = new_owner
        del shiba['expiration']
        sliced = decoded_data['data'][0:i] + decoded_data['data'][i+1:]
    with open('./global_data/global.json', 'w') as rf:
        rf.write(jsbeautifier.beautify(json.dumps({'data': sliced}), opts))
    with open('./user_data/shibas.json', 'r') as rf:
        decoded_data = json.load(rf)
    decoded_data['data'].append({'shibaceipt': shiba})
    with open('./user_data/shibas.json', 'w') as rf:
        rf.write(jsbeautifier.beautify(json.dumps(decoded_data), opts))
    return json.dumps({'status': 'success'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30006, debug=True)
