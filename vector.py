#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:48:29 2022

@author: hernando
"""

from collections.abc import Iterable

def _isnumber(v):
    """ return true if v is a number (int, float or complex)
    """
    
    if (not any([type(v) == t for t in [int, float, complex]])):
        raise TypeError
    return True

class Vector:
    
    def __init__(self, values):
        
        values = values.values if isinstance(values, Vector) else values
        if (not isinstance(values, Iterable)):
            raise TypeError("Vector constructor: iterable required" )
        self.values = list(values)
        self.length = len(values)
        for v in values: _isnumber(v)
        
    def __add__(self, vector):
        
        b = vector if isinstance(vector, Vector) else Vector(vector)
        if (b.length != self.length):
            raise TypeError("Vector add : same dimesion vector required")
        c = Vector([ai + bi for ai, bi in zip(self.values, b.values)])
        return c
    
    def __mul__(self, scalar):
        
        if (not _isnumber(scalar)):
            raise TypeError("Vector mul requires scalar")
        c = Vector([scalar * vi for vi in self.values])
        return c
        
    def __rmul__(self, scalar):
        
        return Vector.__mul__(self, scalar)

    def __getitem__(self, i):
        return self.values[i]

    def __eq__(self, vector):
        b = vector if isinstance(vector, Vector) else Vector(vector)
        return all([xi == yi for xi, yi in zip(self.values, b.values)])


    def __str__(self):
        return str(self.values)

    
    def __repr__(self):
        return str(self.values)
        