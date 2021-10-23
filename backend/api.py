from flask import Flask, request
import json
import imgur-uploader
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/get-shibaceipts", methods = ['GET'])
def get_shibaceipts():
    with open("./global_data/shibas.json", "r") as rf:
        decoded_data = json.load(rf)
        return json.dumps(decoded_data)

@app.route("/new-receipt", methods = ['POST'])
def new_receipt():
    # poopoo

    # accept an image, save it
    userid = request.form['userid']
    file_name = str(userid) + "_" + str(time.time())
    request.files.save(file_name)

    # run ocr on image
    



    # categorize the data
    # generate string to use to make nft image

    # update the global data
    with open("./global_data/global.json", "w") as rf:
        decoded_data = json.load(rf)
        decoded_data.update({'"username:"' + userid + ':"' + img_url + '"'})
        json.dumps(decoded_data)
        rf.write(decoded_data)

    return

@app.route("/spending", methods = ['POST'])
def spending():
    userid = request.form['userid']
    with open("./user_data/" + userid + ".json", "r") as rf:
        decoded_data = json.load(rf)
    return json.dumps(decoded_data)

@app.route("/global-data", methods = ['GET'])
def get_global_data():
    with open("./global_data/global.json", "r") as rf:
        decoded_data = json.load(rf)
    return json.dumps(decoded_data)

@app.route("/view-goals", methods = ['GET'])
def view_goals():
    # return json object eith budget goals
    return

@app.route("/get-friends")
def get_friends():
    return

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=30006, debug=True)