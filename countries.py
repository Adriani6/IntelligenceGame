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

class XML():




    def searchCountryInDB(country):
        tree = ET.parse('data/data.xml')
        root = tree.getroot()
        for country_loop in root.iter("value"):

            ctry = str(country_loop.text)
            if(str.lower(ctry) == str.lower(country)):
                print("Match found !")
