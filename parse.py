#leboncon coin realestate data parser
#parses raw html data from leboncoin for relevant features and stores information in 
#objects
import  sys
from bs4 import BeautifulSoup

#definition for listing class
class Listing(object):
    raw = {}
    data = {}
    lattitude = ""
    longitude = ""
    price = 0
    location = {}
    zipcode = ""
    agency_or_individual = False
    rooms = 0
    superficy = 0
    ges = ""
    energy_class = ""
    surface_area = 0
    pics = []

    def __init__(self, file):
        self.raw["name"] = file
        self.raw["file"] =  open(self.raw["name"], 'r')
        html = self.raw["file"].read()
        self.data = BeautifulSoup(html, 'html.parser')

    def print(self):
        print('title: {}'.format(self.raw["name"]))
        print('price: {}'.format(self.price))
        print('location: {}'.format(self.location))
        print('ges: {}'.format(self.ges))
        print('energy class: {}'.format(self.energy_class))
        print('rooms: {}'.format(self.rooms))
        print('surface area: {}'.format(self.surface_area))
        print('pictures: {}'.format(self.pics))

    def parseInfo(self):        
        self.getPrice()
        self.getGes()
        self.getEnergy()
        self.getLocation()
        self.getRooms()
        self.getSurfaceArea()
        self.getPics()
        
    def getPrice(self):
        self.price = self.data.body.find("span", {"class": "_1F5u3"}).contents[1]
    
    def getLocation(self):
        location_data = self.data.body.find("div", {"class" : "_1aCZv"}).span.contents
        self.location["city"] = location_data[1]
        self.location["zip"] = location_data[7]

    def getRooms(self):
        criterea = self.data.body.find_all("div", {"class" : "_3Jxf3"})
        self.rooms = criterea[1].contents[0]

    def getSurfaceArea(self):
        criteria = self.data.body.find("div", {"data-qa-id" : "criteria_container"})
        criteria = criteria.find("div", {"data-qa-id" : "criteria_item_square"})
        criteria = criteria.find("div", {"class" : "_3Jxf3"})
        self.surface_area = criteria.contents[0].split(" ", 1)[0]
        
    def getGes(self):
        criteria = self.data.body.find("div", {"class" : "_277XW"})
        criteria = criteria.find("div", {"data-qa-id" : "criteria_item_ges"})
        self.ges = criteria.find("div", {"class" : "_1sd0z"}).contents[0] 
    def getEnergy(self):
        criteria = self.data.body.find("div", {"class" : "_277XW"})
        criteria = criteria.find("div", {"data-qa-id" : "criteria_item_energy_rate"})
        self.energy_class = criteria.find("div", {"class" : "_1sd0z"}).contents[0] 
    
    def getPics(self):
        self.pics.append(self.data.find("div", {"class": "_2x8BQ"}).find("img")['src'])

#loop through input files, store listing objects in an array, listings
listings = []
for arg in sys.argv[1:]:
    #initialize listing object
    listings.append(Listing(arg))

    #retrieve document info
    listings[-1].parseInfo()

    #print the listing data
    listings[-1].print()
