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
    energy = ""
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
        print('energy class: {}'.format(self.energy))
        print('rooms: {}'.format(self.rooms))
        print('surface area: {}'.format(self.surface_area))
    
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
        criterea = self.data.body.find_all("div", {"class" : "_3Jxf3"})
        self.surface_area = criterea[2].contents[0].split(" ", 1)[0]
        
    #needs to be narrowed down
    def getGes(self):
        self.ges = self.data.body.find("div", {"class" : "_1sd0z"}).contents[0]
    
    #needs to be narrowed
    def getEnergy(self):
        self.energy = self.data.body.find("div", {"class" : "_2RkBA _1jK6m _1sd0z"})
    


#create new listing
listing = Listing("listing_sample.html")

#retrieve price
listing.getPrice()

#retrieve ges
listing.getGes()

#retrive energy rating
listing.getEnergy()

#retrieve location
listing.getLocation()

#retrieve number of rooms
listing.getRooms()

#retrieve Surface Area
listing.getSurfaceArea()

#print the listing data
listing.print()
