import random
from PIL import Image
import base64
import json
import requests
from base64 import b64encode
import math

def generate_index(amount, limit):
    hat = random.randint(1, int(amount))
    glasses = random.randint(1, int(amount))
    hat_limit = limit/4
    glasses_limit = limit/4
    hat_index = hat_limit/hat
    if (hat_index >= 4):
        hat_index = 4 - 1
    glasses_index = glasses_limit/glasses
    if (glasses_index >= 4):
        glasses_index = 4 - 1
    return (hat_index, glasses_index)

def generate_nft(amount, filename):
    hat_index, glasses_index = generate_index(amount, 5)

    # combine the hat and the glasses into one image
    background = Image.open("default_images/hat" + str(math.floor(hat_index)) + ".png").resize((2048, 2048))
    foreground = Image.open("default_images/glasses" + str(math.floor(glasses_index)) + ".png").resize((2048, 2048))
    result = Image.alpha_composite(background, foreground)
    result.save("generated_images/composite.png")

    # combine shiba and composite image
    background = Image.open("default_images/shiba.png").resize((2048, 2048)).convert('RGBA')
    foreground = Image.open("generated_images/composite.png").resize((2048, 2048)).convert('RGBA')
    result = Image.alpha_composite(background, foreground)
    result.save("generated_images/final.png")

    # upload the image to imgur
    client_id = '678b119f0fd6be0'
    headers = {"Authorization": 'Client-ID ' + client_id}
    api_key = 'bbe58733b5b752b0bca73eedb727d265e13f16c8'
    url = "https://api.imgur.com/3/upload.json"
    r = requests.post(
        url, 
        headers = headers,
        data = {
            'key': api_key, 
            'image': b64encode(open("generated_images/final.png", 'rb').read()),
            'type': 'base64',
            'name': filename,
            'title': filename
        }
    )
    return (r.json()['data']['link'])

# if __name__ == '__main__':
#     generate_nft(300, "test_1_varn")