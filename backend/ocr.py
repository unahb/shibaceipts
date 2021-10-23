# import boto3
import json
from os import replace

# Document


def ocr(image_path):
    # Read document content
    with open(image_path, 'rb') as document:
        imageBytes = bytearray(document.read())

    # Amazon Textract client
    # textract = boto3.client('textract')

    # Call Amazon Textract
    # response = textract.detect_document_text(Document={'Bytes': imageBytes})
    # response = textract.analyze_expense(Document={'Bytes': imageBytes})
    with open("temp.json", 'r') as f:
        json_str = f.read().replace('\'', '\"')
        response = json.loads(json_str)

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
        raise ValueError("Could not find TOTAL in receipt")


    receipt_items = []
    for i in response["ExpenseDocuments"][0]["LineItemGroups"][0]["LineItems"]:
        j = i["LineItemExpenseFields"][0]["ValueDetection"]["Text"]
        k = i["LineItemExpenseFields"][1]["ValueDetection"]["Text"]
        receipt_items.append((j,k))



    # print(response["ExpenseDocuments"][0]["LineItemGroups"][0]["LineItems"][0]["LineItemExpenseFields"])
    # for item in response["Blocks"]:
    #     if item["BlockType"] == "LINE":
    #         if ("AMOUNT" in item["Text"]):
    #             data = item["Text"]
    #             print('\033[94m' + item["Text"] + '\033[0m')
    #             return data.split(":")[1].strip()
    return total, receipt_items


receipt_items = ocr("user_data/test.jpg")
print(receipt_items)
