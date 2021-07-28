import math
import re
from collections import Counter
import json

WORD = re.compile(r"\w+")

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def read_file(input_file):
    file_open = open(input_file)
    data = json.load(file_open)
    return data['hits'][0]['doc']['abstract'][0]

text = read_file("histone.json")

f=open('book.json','r')
for data in f:
    data=json.loads(data)
    break

text1 = str(data['title'])
text2 = str(data['container-title'])
text3 = str(data['subtitle'])

vector1 = text_to_vector(text)
vector2 = text_to_vector(text1)
cosine = get_cosine(vector1, vector2)
print("Cosine:", cosine)

vector1 = text_to_vector(text)
vector2 = text_to_vector(text2)
cosine = get_cosine(vector1, vector2)
print("Cosine:", cosine)

vector1 = text_to_vector(text)
vector2 = text_to_vector(text3)
cosine = get_cosine(vector1, vector2)
print("Cosine:", cosine)