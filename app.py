import random
import sys
import os
import math
import time

class Client_app:
    __name = None
    __longitude = None
    __latitude = None
    __role = None
    def __init__(self, name, longitude, latitude, role):
        self.__name = name
        self.__longitude = longitude
        self.__latitude = latitude
        self.__role = role

    def set_name(self, name):
        self.__name = name
    
    def set_longitude(self, longitude):
        self.__longitude = longitude
    
    def set_latitude(self, latitude):
        self.__latitude = latitude

    def set_role(self, latitude):
        self.__role = role

    def get_name(self):
        return self.__name

    def get_longitude(self):
        return str(self.__longitude)

    def get_latitude(self):
        return str(self.__latitude)

    def get_role(self):
        return self.__role

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says".format(self.__name,self.__longitude,self.__latitude)

    def show(self):
        return "{} name is {} and have longitude {} and latitude {}".format(self.__role,self.__name,self.__longitude,self.__latitude)
    
    def connect(self):
        return "client name {} want to connect".format(self.__name)

    def sendPresence(self):
        return "this client presence"


class Driver_app(Client_app):
    __accept_request = None

    def set_accept_request(self, accept_request):
        self.__accept_request = accept_request
        
    def connect(self):
        return "driver name : {} want to connect".format(self.__name)

    def sendPresence(self):
        return "this driver presence"

    def get_accept_request(self):
        return str(self.__accept_request)

class Check_distance:
    __latitude_1 = None
    __latitude_2 = None
    __longitude_1 = None
    __longitude_2 = None
    __unit = None
    __distance = None

    def __init__(self, latitude_1, latitude_2, longitude_1, longitude_2):
        self.__latitude_1 = latitude_1
        self.__latitude_2 = latitude_2
        self.__longitude_1 = longitude_1
        self.__longitude_2 = longitude_2

    def set_latitude_1(self, latitude_1):
        self.__latitude_1 = latitude_1

    def set_latitude_2(self, latitude_2):
        self.__latitude_2 = latitude_2
    
    def set_longitude_1(self, longitude_1):
        self.__longitude_1 = longitude_1
    
    def set_longitude_2(self, longitude_2):
        self.__longitude_2 = longitude_2

    def check(self):
        radlat1 = math.pi * self.__latitude_1/180
        radlat2 = math.pi * self.__latitude_2/180
        theta = self.__longitude_1 - self.__longitude_2
        radtheta = math.pi * theta/180
        dist = math.sin(radlat1) * math.sin(radlat2) + math.cos(radlat1) * math.cos(radlat2) * math.cos(radtheta)
        dist = math.acos(dist)
        dist = dist * 180/math.pi
        dist = dist * 60 * 1.1515
        # dalam km
        dist = dist * 1.609344
        self.__distance = dist
        return "their distance is {}".format(dist)
    
    def get_distance(self):
        return self.__distance
    
print("Client Name: ")
name = sys.stdin.readline()
print("Longitude: ")
longitude = float(sys.stdin.readline())
print("Latitude: ")
latitude = float(sys.stdin.readline())
# longitude = float(raw_input("Longitude:"))
# latitude = float(raw_input("Latitude:"))

client_1 = Client_app(name,longitude,latitude,"Customer")

print("Driver Name: ")
name_driver = sys.stdin.readline()
print("Longitude: ")
long_driver = float(sys.stdin.readline())
print("Latitude: ")
lat_driver = float(sys.stdin.readline())
# long_driver = float(raw_input("Longitude:"))
# lat_driver = float(raw_input("Latitude:"))

driver_1 = Driver_app(name_driver,long_driver,lat_driver,"Driver")

print(client_1.show())
print(driver_1.show())

distance = Check_distance(latitude,lat_driver,longitude,long_driver)

print(distance.check())

distance = int(distance.get_distance())
print(distance)

while distance >= 0:
    # this logic should be api get lat long from mobile
    print(distance)
    distance -= 50
    # this logic should be api get lat long from mobile
    time.sleep(60)


