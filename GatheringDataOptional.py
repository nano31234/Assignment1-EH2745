#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 22:51:22 2022

@author: Yu-Chieh Hsiao
"""
# This file contains the function for gathering data from the given EQ file
# This file can ignore gathering optional data
def GatheringDataOptional(targetType, grid, ns, ObjectList, constructor, optional):
    for element in grid.findall(targetType, ns):
    
    # Here, temp contains the elements selected from each given object
        elements = []
        elements.append('#'+element.attrib.get(ns['rdf']+'ID'))
        for temp in element:
        
           if optional in temp.tag:
               continue
            # Ignore the item with entsoe
           if 'cim' in temp.tag:
               
               # If there are IDs contained, extract the ID as the attribute
               if ns['rdf']+'resource' in temp.attrib:
                   elements.append(temp.attrib.get(ns['rdf']+'resource'))
               else:
                   elements.append(temp.text)
                   
        ObjectList.append(constructor(*elements))
    return ObjectList

