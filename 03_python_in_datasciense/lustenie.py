from pathlib import Path
import codecs
import json

files = Path("Files").glob('*')
textlist = {}


def addtolist(file_name, text):
    textlist[file_name] = text

for file in files:
    with codecs.open(file, "r", encoding='utf-8', errors='ignore') as fdata:
        open_file = fdata.read()
        file_name = str(file).replace("Files/", "")
        addtolist(file_name, open_file)
    
textlist = sorted(textlist.items())
print(textlist)
