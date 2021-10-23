import random
from PIL import Image
import base64
import json
import requests
from base64 import b64encode


def generate_index(amount, num_hats, num_glasses, limit):
    hat = random.randint(1, int(amount))
    glasses = random.randint(1, int(amount))
    hat_limit = limit/num_hats
    glasses_limit = limit/num_glasses
    hat_index = hat_limit/hat
    if (hat_index >= num_hats):
        hat_index = num_hats - 1
    glasses_index = glasses_limit/glasses
    if (glasses_index >= num_glasses):
        glasses_index = num_glasses - 1
    return (hat_index, glasses_index)


def generate_nft(amount, filename, num_hats, num_glasses, limit):
    hat_index, glasses_index = generate_index(
        amount, num_hats, num_glasses, limit)

    # combine the hat and the glasses into one image
    background = Image.open("default_images/hat" + str(hat_index) + ".jpg")
    foreground = Image.open("default_images/glasses" +
                            str(glasses_index) + ".jpg")
    Image.alpha_composite(background, foreground).save(
        "generated_images/composite.jpg")

    # combine shiba and composite image
    background = Image.open("default_images/shiba.jpg")
    foreground = Image.open("generated_images/composite.jpg")
    Image.alpha_composite(background, foreground).save(
        "generated_images/final.jpg")

    # upload the image to imgur
    client_id = '678b119f0fd6be0'
    headers = {"Authorization": 'Client-ID ' + client_id}
    api_key = 'bbe58733b5b752b0bca73eedb727d265e13f16c8'
    url = "https://api.imgur.com/3/upload.json"
    r = requests.post(
        url,
        headers=headers,
        data={
            'key': api_key,
            'image': b64encode(open("generated_images/final.jpg", 'rb').read()),
            'type': 'base64',
            'name': filename,
            'title': filename
        }
    )
    return (r.json()['data']['link'])
