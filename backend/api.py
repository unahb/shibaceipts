from flask import Flask
import json
import imgur-uploader

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
    # accept an image, run ocr

    return

@app.route("/spending", methods = ['POST'])
def spending():
    # get what user this is
    userid = "user1"
    with open("./user_data/" + userid + ".json", "r") as rf:
        decoded_data = json.load(rf)
    return json.dumps(decoded_data)

@app.route("/global-data", methods = ['GET'])
def get_global_data():
    return 

@app.route("/view-goals", methods = ['GET'])
def view_goals():
    # return json object eith budget goals
    return

@app.route("/get-friends")
def get_friends():
    return

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=30006, debug=True)