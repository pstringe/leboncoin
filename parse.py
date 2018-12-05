"""
Poitier Stringer
    leboncon coin realestate data parserparses raw html data from leboncoin.com
    for relevant features and stores information in array of objects
"""

import  sys
from geopy.geocoders import Nominatim
import  time
from bs4 import BeautifulSoup
from json import JSONEncoder
import json

#Listing class
class Listing(object):
    raw = {}
    data = {}
    
    def __init__(self, file):
        self.raw["name"] = file
        self.raw["file"] =  open(self.raw["name"], 'r')
        self.name = self.raw["name"]

    def print(self):
        print('\n')
        print('file: {}'.format(self.name))
        print('price: {}'.format(self.price))
        print('location: {}'.format(self.location))
        print('ges: {}'.format(self.ges))
        print('energy class: {}'.format(self.energy_class))
        print('rooms: {}'.format(self.rooms))
        print('surface area: {}'.format(self.surface_area))
        print('pictures: {}'.format(self.pics))

    def parseInfo(self, data):        
        self.setPrice(data)
        self.setGes(data)
        self.setEnergy(data)
        self.setLocation(data)
        self.setRooms(data)
        self.setSurfaceArea(data)
        self.setPics(data)
        
    def setPrice(self, data):
        self.price = None
        if (data.body):
            self.price = data.body.find("span", {"class": "_1F5u3"}).contents[1]
    
    def setLocation(self, data):
        self.location = None
        if (data.body):
            location_data = data.body.find("div", {"class" : "_1aCZv"}).span.contents
            self.location = {}
            self.location["city"] = location_data[1]
            self.location["zip"] = location_data[7]
            self.location["coords"] = geoCode(self.location)

    def setRooms(self, data):
        self.rooms = None
        if (data.body):
            criteria = data.body.find("div", {"data-qa-id" : "criteria_container"})
            criteria = criteria.find("div", {"data-qa-id" : "criteria_item_rooms"})
            if (criteria):
                criteria = criteria.find("div", {"class" : "_3Jxf3"})
                self.rooms = criteria.contents[0]

    def setSurfaceArea(self, data):
        self.surface_area = None
        if (data.body):
            criteria = data.body.find("div", {"data-qa-id" : "criteria_container"})
            if (criteria):
                criteria = criteria.find("div", {"data-qa-id" : "criteria_item_square"})
                if (criteria):
                    criteria = criteria.find("div", {"class" : "_3Jxf3"})
                    self.surface_area = criteria.contents[0].split(" ", 1)[0]
        
    def setGes(self, data):
        self.ges = None
        if (data.body):
            criteria = data.body.find("div", {"class" : "_277XW"})
            criteria = criteria.find("div", {"data-qa-id" : "criteria_item_ges"})
            if (criteria and criteria.find("div", {"class" : "_1sd0z"})):
                self.ges = criteria.find("div", {"class" : "_1sd0z"}).contents[0]
    
    def setEnergy(self, data):
        self.energy_class = None
        if (data.body):
            criteria = data.body.find("div", {"class" : "_277XW"})
            criteria = criteria.find("div", {"data-qa-id" : "criteria_item_energy_rate"})
            if (criteria and  criteria.find("div", {"class" : "_1sd0z"})):
                self.energy_class = criteria.find("div", {"class" : "_1sd0z"}).contents[0] 
   
    #need to correct this
    def setPics(self, data):
        self.pics = None
        if (data.find("div", {"class": "_2x8BQ"})):
            self.pics = data.find("div", {"class": "_2x8BQ"}).find("img")['src']

#custom json encoder
class ListingEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

#retrieve longitude/lattitudes
def geoCode(loc):
    time.sleep(1)
    g = Nominatim(user_agent="leboncoin scraper")
    coords = g.geocode(loc["zip"])
    return([coords.longitude, coords.latitude])

    

#loop through input files, store listing objects in an array, listings
listings = []
outputFile = open("out.json", "w")

for arg in sys.argv[1:]:
    listing = Listing(arg)
    #init data
    html = listing.raw["file"].read()
    data = BeautifulSoup(html, 'html.parser')
    
    #initialize listing object
    listings.append(listing)
    
    #retrieve document info
    listings[-1].parseInfo(data)
    
    #save data
    ListingEncoder().encode(listings[-1])
    s = json.dumps(listings[-1], cls=ListingEncoder)
    print(s)
    outputFile.write(s)
    
#make sure listings are being stored correctly
for listing in listings:
    print(json.dumps(listing))
