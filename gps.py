#Greg Lutzke
#GPS Unit for Hikers
#10/17/12
#Version 1 - A program that loops and prompts the user for functionality provided by the GPS unit. 

import random
import math

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
	
	def distance(origin,destination):
		latitude1, longitude1 = origin
		latitude2, longitude2 = destination
		radius = 6371 #kilometers

		distancelatitude = math.radians(latitude2-latitude1)
		distancelongitude = math.radians(longitude2-longitude1)
		a = math.sin(distancelatitude/2) * math.sin(distancelatitude/2) + math.cos(math.radians(latitude1)) \
        * math.cos(math.radians(latitude2)) * math.sin(distancelongitude/2) * math.sin(distancelongitude/2)
    	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    	d = radius * c
    	return d

w1=waypoint(-70,110, 'TheShire')
w2=waypoint(85,175, 'Misty Mountains')
w3=waypoint(75,-140, 'The Black Gate')
w4=waypoint(80,-145, 'Mount Doom')

p1=path('There and back again - A Hobbit\'s tale')
p1.add_waypoint(w1)
p1.add_waypoint(w2)
p1.add_waypoint(w1)

p2=path('The Black Gate to Mount Doom')
p2.add_waypoint(w3)
p2.add_waypoint(w4)

HelmsDeep = [25, -45]
TheShire = [-70, 110]
distance(TheShire, HelmsDeep) 
