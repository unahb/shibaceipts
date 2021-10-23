import random
from PIL import Image
import base64
import json
import requests
from base64 import b64encode
import math

# defining the total number of images for each
num_hats = 1
num_glasses = 4
num_neck = 4
num_shiba = 6
num_poop = 9

def generate_index(amount, limit):
    hat = random.randint(1, int(amount))
    glasses = random.randint(1, int(amount))
    neck = random.randint(1, int(amount))
    shiba = random.randint(1, int(amount))
    poop = random.randint(1, int(amount))

    hat_limit = limit/num_hats
    glasses_limit = limit/num_glasses
    neck_limit = limit/num_neck
    shiba_limit = limit/num_shiba
    poop_limit = limit/num_poop

    hat_index = hat/hat_limit
    if (hat_index >= num_hats):
        hat_index = num_hats - 1

    glasses_index = glasses/glasses_limit
    if (glasses_index >= num_glasses):
        glasses_index = num_glasses - 1

    neck_index = neck/neck_limit
    if (neck_index >= num_neck):
        neck_index = num_neck - 1

    shiba_index = shiba/shiba_limit
    if (shiba_index >= num_shiba):
        shiba_index = num_shiba - 1
    
    poop_index = poop/poop_limit
    if (poop_index >= num_poop):
        poop_index = num_poop - 1

    index_list = [hat_index, glasses_index, neck_index, shiba_index, poop_index]
    return index_list

def generate_nft(amount, file_name, limit):
    index_list = generate_index(amount, limit)

    # combine the hat and the glasses into one image
    background = Image.open("default_images/hat" + str(math.floor(index_list[0])) + ".png").resize((2048, 2048))
    foreground = Image.open("default_images/glasses" + str(math.floor(index_list[1])) + ".png").resize((2048, 2048))
    result = Image.alpha_composite(background, foreground)
    result.save("generated_images/composite1.png")

    # combine the neck and the poop into one image
    background = Image.open("default_images/neck" + str(math.floor(index_list[2])) + ".png").resize((2048, 2048))
    foreground = Image.open("default_images/poop" + str(math.floor(index_list[4])) + ".png").resize((2048, 2048))
    result = Image.alpha_composite(background, foreground)
    result.save("generated_images/composite2.png")

    # combine the accessories
    background = Image.open("generated_images/composite1.png").resize((2048, 2048))
    foreground = Image.open("generated_images/composite2.png").resize((2048, 2048))
    result = Image.alpha_composite(background, foreground)
    result.save("generated_images/composite3.png")

    # combine shiba and composite image
    background = Image.open("default_images/shiba" + str(math.floor(index_list[3])) + ".png").resize((2048, 2048)).convert('RGBA')
    foreground = Image.open("generated_images/composite3.png").resize((2048, 2048)).convert('RGBA')
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
            'name': file_name,
            'title': file_name
        }
    )
    return (r.json()['data']['link'])


# if __name__ == '__main__':
#     generate_nft(800, "file", 400)