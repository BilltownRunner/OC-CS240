# Greg Lutzke 
#GPS Unit for Hikers
#10/17/12
#Version 1 - A program that loops and prompts the user for functionality provided by the GPS unit. Lists distances from various LotR places.

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

    def distance(self):
        radius = 6371 #kilometers

        if len(self.waypoints) < 2:
            return 0 
        distance1 = 0
        
        for index in range(1,len(self.waypoints)):
            w1=self.waypoints[index-1]
            w2=self.waypoints[index]
            
            #Converts our coordinates into radians
            distancelatitude = math.radians(w2.latitude-w1.latitude)
            distancelongitude = math.radians(w2.longitude-w1.longitude)
            a = math.sin(distancelatitude/2) * math.sin(distancelatitude/2) + math.cos(math.radians(w1.latitude)) \
            * math.cos(math.radians(w2.latitude)) * math.sin(distancelongitude/2) * math.sin(distancelongitude/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            distance1 += radius * c
        return distance1

w1=waypoint(-70,110, 'TheShire')
w2=waypoint(85,175, 'Misty Mountains')
w3=waypoint(75,-140, 'The Black Gate')
w4=waypoint(80,-145, 'Mount Doom')
w5=waypoint(25,-45, 'HelmsDeep')

#'add waypoints' under 'path' choose the locations of where we are travelling - if we want all waypoints we must include (w1)(w2)(w3)(w4) and so forth
p1=path('There and back again - A Hobbit\'s tale')
p1.add_waypoint(w1)
p1.add_waypoint(w2)
p1.add_waypoint(w1)

p2=path('The Black Gate to Mount Doom')
p2.add_waypoint(w3)
p2.add_waypoint(w4)

p3=path('TheShire to HelmsDeep')
p3.add_waypoint(w1)
p3.add_waypoint(w5)

print 'There and back again - A Hobbit\'s tale:'
print p1.distance()
print 'Distance from The Black Gate to Mount Doom:'
print p2.distance()
print 'Distance from The Shire to Helms Deep:'
print p3.distance()


