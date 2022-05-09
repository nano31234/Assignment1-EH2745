#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 23:14:44 2022

@author: Yu-Chieh Hsiao
"""

class GeographicalRegion:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        
class SubGeographicalRegion(GeographicalRegion):
    def __init__(self, ID, name, Region):
        self.name = name
        self.ID = ID
        self.Region = Region