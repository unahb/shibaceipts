import ocr
import nft
from datetime import datetime
import json

limit = 400


def new_receipt():
    # accept an image, save it
    file_name = "user_data/test.jpg"
    userid = "oof"

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
    new_entry["expiration"] = datetime.now()

    user_entry = {}
    user_entry["username"] = userid
    user_entry["avatar"] = img_url

    global_entry = {}
    global_entry["user"] = user_entry
    global_entry["shibaceipt"] = new_entry

    # update the global data
    with open("./global_data/global.json", "w") as rf:
        decoded_data = json.load(rf)
        decoded_data.update(global_entry)
        json.dumps(decoded_data)
        rf.write(decoded_data)

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
    print("here1")
    with open("./user_data/receipts.json", "w") as rf:
        print("here")
        decoded_data = json.load(rf)
        decoded_data.update(json_obj)
        json.dumps(decoded_data)
        rf.write(decoded_data)

    # return nft url to the frontend
    return json.dumps(decoded_data)


new_receipt()
