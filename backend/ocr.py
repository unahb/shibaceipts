import boto3

# Document


def ocr(image_path):
    # Read document content
    with open(image_path, 'rb') as document:
        imageBytes = bytearray(document.read())

    # Amazon Textract client
    textract = boto3.client('textract')

    # Call Amazon Textract
    # response = textract.detect_document_text(Document={'Bytes': imageBytes})
    response = textract.analyze_expense(Document={'Bytes': imageBytes})

    # print(response)

    # Print detected text
    # print(response)
    for i in response["ExpenseDocuments"][0]["LineItemGroups"][0]["LineItems"]:
        for j in i["LineItemExpenseFields"][0]["ValueDetection"]["Text"]:
            print(j)

    # print(response["ExpenseDocuments"][0]["LineItemGroups"][0]["LineItems"][0]["LineItemExpenseFields"])
    # for item in response["Blocks"]:
    #     if item["BlockType"] == "LINE":
    #         if ("AMOUNT" in item["Text"]):
    #             data = item["Text"]
    #             print('\033[94m' + item["Text"] + '\033[0m')
    #             return data.split(":")[1].strip()


ocr("user_data/test.jpg")
