#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adrian
#
# Created:     22/09/2015
# Copyright:   (c) Adrian 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import xml.etree.ElementTree as ET
class City_XML():

    tree = ET.parse('data/CitiesData.xml')
    root = tree.getroot()
    for city_loop in root.iter("value"):
        print(city_loop.text)
