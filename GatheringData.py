#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 22:05:31 2022

@author: Yu-Chieh Hsiao
"""
# This file contains the function for gathering data from the given EQ file
def GatheringData(targetType, grid, ns, ObjectList, constructor):
    for element in grid.findall(targetType, ns):
    
    # Here, temp contains the elements selected from each given object
        elements = []
        elements.append('#'+element.attrib.get(ns['rdf']+'ID'))
        for temp in element:
        
            # Ignore the item with entsoe
           if 'cim' in temp.tag:
               
               # If there are IDs contained, extract the ID as the attribute
               if ns['rdf']+'resource' in temp.attrib:
                   elements.append(temp.attrib.get(ns['rdf']+'resource'))
               else:
                   elements.append(temp.text)
                   
        ObjectList.append(constructor(*elements))
    return ObjectList