#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 23:22:47 2022

@author: Yu-Chieh Hsiao
"""
class CurrentLimit:
    def __init__(self, ID, name, description, value,
                 OperationalLimitSet, OperationalLimitType):
        self.ID = ID
        self.name = name
        self.description = description
        self.value = value
        self.OperationalLimitSet = OperationalLimitSet
        self.OperationalLimitType = OperationalLimitType
