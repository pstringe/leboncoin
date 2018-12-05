import sys
import json
from pprint import pprint

class   JsonData():
    def __init__(self, jsonFile):
        self.loadFile(jsonFile);    
        self.loadRecords();
        self.setComplete();

    def loadFile(self, jsonFile):
        self.file = jsonFile
        with open(self.file) as f:
            self.data = f.readlines()

    def loadRecords(self):
        self.records = []
        for datum in self.data:
            print(datum)
            self.records.append(json.loads(datum))

    def setComplete(self):
        self.complete = [] 
        for r in self.records:
            if (r["location"] and r["location"]["coords"]):
                self.complete.append(r)

if (sys.argv[1] == "load"):
    if (sys.argv[2]):
        data = JsonData(sys.argv[2])

pprint("complete records:{}".format(len(data.complete)))
pprint("total records:{}".format(len(data.records)))
