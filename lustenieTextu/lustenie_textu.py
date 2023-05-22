import os
import pickle
import json

files = os.listdir()

text = ""

for file in files:
    if file.endswith("txt"):
        f = open(file, "r", encoding='cp1250')
        text += f.read() + " "
        f.close()

for file in files:
    if file.endswith("obj"):
        objects = []
        with open(file, 'rb') as openfile:
            objects.append(pickle.load(openfile))

        text += objects[0] + " "

for file in files:
    if file.endswith("json"):
        with open(file, 'rb') as openfile:
            text_in_file = json.load(openfile)
            text += text_in_file + " "

print(text)