"""
Poitier Stringer
    leboncon coin realestate data parserparses raw html data from leboncoin.com
    for relevant features and stores information in array of objects
"""

import  sys
import  geocoder
import  time
from bs4 import BeautifulSoup

#definition for listing class
class Listing(object):
    raw = {}
    data = {}
    
    def __init__(self, file):
        self.raw["name"] = file
        self.raw["file"] =  open(self.raw["name"], 'r')
        self.name = self.raw["name"]
        html = self.raw["file"].read()
        self.data = BeautifulSoup(html, 'html.parser')

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

    def parseInfo(self):        
        self.setPrice()
        self.setGes()
        self.setEnergy()
        self.setLocation()
        self.setRooms()
        self.setSurfaceArea()
        self.setPics()
        
    def setPrice(self):
        self.price = self.data.body.find("span", {"class": "_1F5u3"}).contents[1]
    
    def setLocation(self):
        location_data = self.data.body.find("div", {"class" : "_1aCZv"}).span.contents
        self.location = {}
        self.location["city"] = location_data[1]
        self.location["zip"] = location_data[7]
        #self.location["coords"] = geoCode(self.location)

    def setRooms(self):
        self.rooms = None
        criteria = self.data.body.find("div", {"data-qa-id" : "criteria_container"})
        criteria = criteria.find("div", {"data-qa-id" : "criteria_item_rooms"})
        if (criteria):
            criteria = criteria.find("div", {"class" : "_3Jxf3"})
            self.rooms = criteria.contents[0]

    def setSurfaceArea(self):
        self.surface_area = None
        criteria = self.data.body.find("div", {"data-qa-id" : "criteria_container"})
        if (criteria):
            criteria = criteria.find("div", {"data-qa-id" : "criteria_item_square"})
            if (criteria):
                criteria = criteria.find("div", {"class" : "_3Jxf3"})
                self.surface_area = criteria.contents[0].split(" ", 1)[0]
        
    def setGes(self):
        self.ges = None
        criteria = self.data.body.find("div", {"class" : "_277XW"})
        criteria = criteria.find("div", {"data-qa-id" : "criteria_item_ges"})
        if (criteria and criteria.find("div", {"class" : "_1sd0z"})):
            self.ges = criteria.find("div", {"class" : "_1sd0z"}).contents[0]
    
    def setEnergy(self):
        self.energy_class = None
        criteria = self.data.body.find("div", {"class" : "_277XW"})
        criteria = criteria.find("div", {"data-qa-id" : "criteria_item_energy_rate"})
        if (criteria and  criteria.find("div", {"class" : "_1sd0z"})):
            self.energy_class = criteria.find("div", {"class" : "_1sd0z"}).contents[0] 
   
    #need to correct this
    def setPics(self):
        self.pics = None
        if (self.data.find("div", {"class": "_2x8BQ"})):
            self.pics = self.data.find("div", {"class": "_2x8BQ"}).find("img")['src']

#geocoding to obtain longitutde and lattitude. (Not yet working)
"""
def geoCode(location):
    time.sleep(1)
    g = geocoder.google(location['zip'])
    if g.status == 'OK':
        print(g.status)
        return g.latlong
    else:
        print('status: {}'.format(g.status))
        return {}
"""

#loop through input files, store listing objects in an array, listings
listings = []
for arg in sys.argv[1:]:
    listing = Listing(arg)
    
    #initialize listing object
    listings.append(listing)
    
    #retrieve document info
    listings[-1].parseInfo()
    listings[-1].print()
    
#make sure listings are being stored correctly
for listing in listings:
    listing.print()
