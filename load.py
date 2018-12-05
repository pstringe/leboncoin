import json
from pprint import pprint

#load file
with open('sample.json') as f:
    data = f.readlines()

#load json
records = []
for datum in data:
    print(datum)
    records.append(json.loads(datum))

#Here are your objects
for r in records:
    pprint(r)
