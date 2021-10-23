from flask import Flask, request
import json
#import imgur-uploader
import time
import ocr
import nft

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
    file_name = "raw_images/" + str(userid) + "_" + str(time.time())
    request.files.save(file_name)

    # run ocr on image and get the total value
    total = ocr.ocr(file_name)

    # TODO: categorize the data

    # generate string to use to make nft image using the total amount
    # higher value = better nft
    img_url = nft.generate_nft(
        total, file_name, limit)

    # update the global data
    with open("./global_data/global.json", "w") as rf:
        decoded_data = json.load(rf)
        decoded_data.update(
            {'"username":' + userid + '","url":' + img_url + '"'})
        json.dumps(decoded_data)
        rf.write(decoded_data)

    # return nft url to the frontend
    return {'"url":' + img_url}


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
