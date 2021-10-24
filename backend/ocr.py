import boto3
import json
from os import replace
import requests
import random
from PIL import Image
import base64
import json
from base64 import b64encode
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import string
# Document


def ocr(image_path):
    # Read document content
    with open(image_path, 'rb') as document:
        imageBytes = bytearray(document.read())

    # Amazon Textract client
    textract = boto3.client('textract')

    # Call Amazon Textract
    # response = textract.detect_document_text(Document={'Bytes': imageBytes})
    # response = textract.analyze_expense(Document={'Bytes': imageBytes})
    with open("temp2.json", 'r') as f:
        json_str = f.read().replace('\'', '\"')
        response = json.loads(json_str)

    # with open('temp2.json', 'w') as f:
    #     json.dump(response, f)

    # print(response)

    # print(response)

    # Print detected text
    # print(response)
    # get the total
    total = None
    for sf in response["ExpenseDocuments"][0]["SummaryFields"]:
        # print(sf)
        if "LabelDetection" in sf and \
                sf["LabelDetection"]["Text"] == "TOTAL":
            total = float(sf["ValueDetection"]["Text"])
            break

    if total == None:
        total = 5
        # raise ValueError("Could not find TOTAL in receipt")

    receipt_items = []
    name_boxes = []
    price_boxes = []
    for i in response["ExpenseDocuments"][0]["LineItemGroups"][0]["LineItems"]:
        j = i["LineItemExpenseFields"][0]["ValueDetection"]["Text"]
        k = i["LineItemExpenseFields"][1]["ValueDetection"]["Text"]
        name_box = i["LineItemExpenseFields"][0]["ValueDetection"]["Geometry"]["BoundingBox"]
        price_box = i["LineItemExpenseFields"][1]["ValueDetection"]["Geometry"]["BoundingBox"]

        receipt_items.append((j, k))
        name_boxes.append(name_box)
        price_boxes.append(price_box)

    # print(response["ExpenseDocuments"][0]["LineItemGroups"][0]["LineItems"][0]["LineItemExpenseFields"])
    # for item in response["Blocks"]:
    #     if item["BlockType"] == "LINE":
    #         if ("AMOUNT" in item["Text"]):
    #             data = item["Text"]
    #             print('\033[94m' + item["Text"] + '\033[0m')
    #             return data.split(":")[1].strip()
    return total, receipt_items, name_boxes, price_boxes


def annotate_img(image_path, name_boxes, price_boxes):
    # path_split = image_path.split(".")
    # if len(path_split) == 1:
    #     new_path = "static/" + "_annotated"
    # else:
    #     new_path = "".join(path_split[:-1] + ["_annotated", path_split[-1]])

    letters = string.ascii_lowercase
    new_path = "static/" + ''.join(random.choice(letters)
                                   for i in range(10)) + "_annotated"
    # print(new_path)
    im = Image.open(image_path)
    w, h = im.size

    _, ax = plt.subplots()
    ax.imshow(im)

    for box in name_boxes:
        width, height, left, top = \
            box["Width"], box["Height"], box["Left"], box["Top"]
        rect = patches.Rectangle(
            (left*w, h*top), width*w, height*h, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

    for box in price_boxes:
        width, height, left, top = \
            box["Width"], box["Height"], box["Left"], box["Top"]
        rect = patches.Rectangle(
            (left*w, h*top), width*w, height*h, linewidth=1, edgecolor='g', facecolor='none')
        ax.add_patch(rect)

    plt.axis('off')
    plt.savefig(new_path, dpi=600)
    return new_path


# total, receipt_items, nb, pb = ocr("user_data/test_png.png")
# annotated_path = annotate_img("user_data/test_png.png", nb, pb)
# print(receipt_items)
# print(annotated_path)
# total, receipt_items, nb, pb = ocr(
# "user_data/IMG_20210925_133223.jpg")
# annotated_path = annotate_img(
# "user_data/IMG_20210925_133223.jpg", nb, pb)
# print(receipt_items)
# print(annotated_path)
# receipt_items = ocr("user_data/test.jpg")
# print(receipt_items)
