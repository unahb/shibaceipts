import boto3

# Document


def ocr(image_path):
    # Read document content
    with open(image_path, 'rb') as document:
        imageBytes = bytearray(document.read())

    # Amazon Textract client
    textract = boto3.client('textract')

    # Call Amazon Textract
    response = textract.detect_document_text(Document={'Bytes': imageBytes})

    # print(response)

    # Print detected text
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            if ("AMOUNT" in item["Text"]):
                data = item["Text"]
                return data.split(":")[1].strip()
                # print('\033[94m' + item["Text"] + '\033[0m')


# ocr("user_data/test.jpg")
