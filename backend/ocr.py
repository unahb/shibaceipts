import boto3

# Document
documentName = "./user_data/test.jpg"

kms = boto3.client('kms', region_name='us-west-2')

# Read document content
with open(documentName, 'rb') as document:
    imageBytes = bytearray(document.read())

# Amazon Textract client
textract = boto3.client('textract')

# Call Amazon Textract
response = textract.detect_document_text(Document={'Bytes': imageBytes})

# print(response)

# Print detected text
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        print('\033[94m' + item["Text"] + '\033[0m')
