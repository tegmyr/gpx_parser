# -*- coding: utf-8 -*-
"""
GPX_parser for MTB trails
Created on Wed Jan  6 09:42:37 2016

@author: Oscar Tegmyr
oscar.tegmyr@gmail.com
"""

import xml.etree.ElementTree
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

parsed_xml  = xml.etree.ElementTree.parse('example2.gpx')
root        = parsed_xml.getroot()

ns = {'topo': 'http://www.topografix.com/GPX/1/1'}

tracks = root.findall('topo:trk',ns)
for track in tracks:
    segments =  track.findall('topo:trkseg',ns)
    for segment in segments: 
        track_points    = segment.findall('topo:trkpt',ns)    
        lon, lat, elev  = np.zeros((3,len(track_points)))
         
        for index,track_point in  enumerate(track_points):
           lon[index]  = float(track_point.attrib['lon'])
           lat[index]  = float(track_point.attrib['lat'])
           elev[index] = track_point.find('topo:ele',ns).text

        ax.plot(lon,lat,zs=elev)
     