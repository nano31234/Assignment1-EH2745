#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 23:53:23 2022

@author: Yu-Chieh Hsiao
"""
class OperationalLimitSet:
    def __init__(self, ID, name, description, Terminal):
        self.ID = ID
        self.name = name
        self.description = description
        self.Terminal = Terminal
        
class OperationalLimitType:
    def __init__(self, ID, name, direction, acceptableDuration = None):
        
        if acceptableDuration == None:
            self.ID = ID
            self.name = name
            self.direction = direction
            
        else:
            self.ID = ID
            self.name = name
            self.direction = direction
            self.acceptableDuration = acceptableDuration