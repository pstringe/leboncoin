import sys
import json
from pprint import pprint

class   JsonData():
    def __init__(self, jsonFile):
        self.loadFile(jsonFile);    
        self.loadRecords();
        self.setComplete();

    def show(self):
        pprint("complete records:{}".format(len(self.complete)))
        pprint("total records:{}".format(len(self.records)))
    
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
    
    #merge two JsonData objects into cureent object
    def mergeComplete(self, d1, d2):
        for d1 in d1.complete:
            if (d1 not in d2.complete):
                self.records.append(d1)
        for d2 in d2.complete:
            if (d2 not in d1.complete):
                self.records.append(d2)
        self.setComplete()
    
d1 = None
d2 = None
d3 = None
data = None

if (sys.argv[1] == "load"):
    if (sys.argv[2]):
        data = JsonData(sys.argv[2])
elif (sys.argv[1] == "merge"):
    if (sys.argv[2] and sys.argv[3]):
        d1 = JsonData(sys.argv[1])
        d2 = JsonData(sys.argv[2])
        res = sys.argv[3] if JsonData(sys.argv[3]) else JsonData("out.json")
else:
    pass

if (data):
    data.show()
if (d1):
    d1.show()
if (d2):
    d2.show()
if (d3):
    d3.show()
