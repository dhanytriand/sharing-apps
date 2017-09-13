import random
import sys
import os
import math

class Client_app:
    __name = None
    __longitude = None
    __latitude = None

    def __init__(self, name, longitude, latitude):
        self.__name = name
        self.__longitude = longitude
        self.__latitude = latitude

    def set_name(self, name):
        self.__name = name
    
    def set_longitude(self, longitude):
        self.__longitude = longitude
    
    def set_latitude(self, latitude):
        self.__latitude = latitude

    def get_name(self):
        return self.__name

    def get_longitude(self):
        return str(self.__longitude)

    def get_latitude(self):
        return str(self.__latitude)

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says".format(self.__name,self.__longitude,self.__latitude)

    def show(self):
        return "customer name is {} and have longitude {} and latitude {}".format(self.__name,self.__longitude,self.__latitude)
    
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

    def __init__(self, latitude_1, latitude_2, longitude_1, longitude_2, unit):
        self.__latitude_1 = latitude_1
        self.__latitude_2 = latitude_2
        self.__longitude_1 = longitude_1
        self.__longitude_2 = longitude_2
        self.__unit = unit

    def set_latitude_1(self, latitude_1):
        self.__latitude_1 = latitude_1

    def set_latitude_2(self, latitude_2):
        self.__latitude_2 = latitude_2
    
    def set_longitude_1(self, longitude_1):
        self.__longitude_1 = longitude_1
    
    def set_longitude_2(self, longitude_2):
        self.__longitude_2 = longitude_2

    def set_unit(self, unit):
        self.__unit = unit

    def check(self):
        radlat1 = Math.pi * self.__
    
print("Client Name: ")
name = sys.stdin.readline()
print("Longitude: ")
longitude = sys.stdin.readline()
print("Latitude: ")
latitude = sys.stdin.readline()

client_1 = Client_app(name,longitude,latitude)

print(client_1.show())

