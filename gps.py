#Greg Lutzke
#GPS Unit for Hikers
10/17/12
Version 1 - A program that loops and prompts the user for functionality provided by the GPS unit. 

import random

def gpsGetLongLat():
    longitude = (random.random()*360) - 180
    latitude = 0.0
    return longitude, latitude 

class waypoint(object):
    def __init__(self, latitude, longitude, name=''):
		self.latitude = latitude
		self.longitude = longitude
		self.name = name

class path(object):
	def __init__(self,name =''):
		self.waypoints = []
		self.name = name
	
	def add_waypoint(self,waypoint):
		self.waypoints.append(waypoint)


