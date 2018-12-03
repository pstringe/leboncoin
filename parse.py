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
    no_of_rooms = 0
    superficy = 0
    ges = ""
    energy = ""
    pics = []

    def __init__(self, file):
        self.raw["name"] = file
        self.raw["file"] =  open(self.raw["name"], 'r')
        html = self.raw["file"].read()
        self.data = BeautifulSoup(html, 'html.parser')

    def print(self):
        print('title:\t{}'.format(self.raw["name"]))
        print('price:\t{}'.format(self.price))
        print('location:\t{}'.format(self.location))
        print('ges:\t{}'.format(self.ges))
        print('energy rating:\t{}'.format(self.energy))
    
    def getPrice(self):
        self.price = self.data.body.find("span", {"class": "_1F5u3"}).contents[1]
    
    def getLocation(self):
        location_data = self.data.body.find("div", {"class" : "_1aCZv"}).span.contents
        self.location["city"] = location_data[1]
        self.location["zip"] = location_data[7]

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
listing.print()

#retrieve ges
listing.getGes()
listing.print()

#retrive energy rating
listing.getEnergy()
listing.print()

#retrieve location
listing.getLocation()
listing.print()

#retrieve
