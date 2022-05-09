#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 23:48:00 2022

@author: Yu-Chieh Hsiao
"""

class LoadResponseCharacteristic:
    def __init__(self, ID, name, exponentModel, pConstantCurrent,
                 pConstantImpedance, pConstantPower, pFrequencyExponent,
                 qConstantCurrent, qConstantImpedance, qConstantPower,
                 pVoltageExponent, qFrequencyExponent, qVoltageExponent):
        self.ID = ID
        self.name = name
        self.exponentModel = exponentModel
        self.pConstantCurrent = pConstantCurrent
        self.pConstantImpedance = pConstantImpedance
        self.pConstantPower = pConstantPower
        self.pFrequencyExponent = pFrequencyExponent
        self.qConstantCurrent = qConstantCurrent
        self.qConstantImpedance = qConstantImpedance
        self.qConstantPower = qConstantPower
        self.pVoltageExponent = pVoltageExponent
        self.qFrequencyExponent = qFrequencyExponent
        self.qVoltageExponent = qVoltageExponent
