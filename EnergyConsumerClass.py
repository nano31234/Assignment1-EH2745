#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 23:27:05 2022

@author: Yu-Chieh Hsiao
"""

class EnergyConsumer:
    def __init__(self, ID, name, description, aggregate, EquipmentContainer,
                 LoadResponse = None, p = 0, q = 0):
        
        self.type = 'EnergyConsumer'
        self.pd_bus = 'null'
        self.pd_EC = 'null'
        
        if LoadResponse == None:
            self.ID = ID
            self.name = name
            self.description = description
            self.aggregate = aggregate
            self.EquipmentContainer = EquipmentContainer
            self.p = p
            self.q = q
            
        else:
            self.ID = ID
            self.name = name
            self.description = description
            self.aggregate = aggregate
            self.EquipmentContainer = EquipmentContainer
            self.LoadResponse = LoadResponse
            self.p = p
            self.q = q