#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 23:57:44 2022

@author: Yu-Chieh Hsiao
"""

class ReactiveCapabilityCurve:
    def __init__(self, ID, curveStyle, xUnit, y1Unit, y2Unit, name):
        self.ID = ID
        self.curveStyle = curveStyle
        self.xUnit = xUnit
        self.y1Unit = y1Unit
        self.y2Unit = y2Unit
        self.name = name
    