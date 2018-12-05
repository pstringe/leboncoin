import sys
import json
from pprint import pprint

#load file
with open(sys.argv[1]) as f:
    data = f.readlines()

#load json
records = []
for datum in data:
    print(datum)
    records.append(json.loads(datum))

complete = []
#Here are your objects
for r in records:
    if (r["location"] and r["location"]["coords"]):
        complete.append(r)
pprint("complete records:{}".format(len(complete)))
pprint("total records:{}".format(len(data)))
