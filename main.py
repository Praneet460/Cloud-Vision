import json

with open("./json_data/data.json", "r") as read_file:
    data = json.load(read_file)

texts = [text['description'] for text in data['textAnnotations']]

print(texts)
# for text in data['textAnnotations']:
#     print(text['description'])

# for text in data['textAnnotations']:
#     if text['boundingPoly']['vertices'][0]['x'] == 452 or text['boundingPoly']['vertices'][0]['y'] == 739 or text['boundingPoly']['vertices'][0]['x'] == 452:
#         print(text['description'])