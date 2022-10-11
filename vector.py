#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:48:29 2022

@author: hernando
"""

from collections.abc import Iterable

def _isnumber(v):
    """
    Parameters
    ----------
    v : Any

    Returns
    -------
    bool: Return True if v is a number (int, float or complex)
    """
    
    if (not any([type(v) == t for t in [int, float, complex]])):
        raise TypeError("Must be a number (int, float, complex)")
    return True


class Vector:
    
    def __init__(self, values):
        """
        
        Create a Vector instance

        Parameters
        ----------
        values : Iterable, list of values

        Raises
        ------
        TypeError, if values if not an iterable of numbers

        Returns
        -------
        Create a Vector instance

        """
        
        values = values.values if isinstance(values, Vector) else values
        if (not isinstance(values, Iterable)):
            raise TypeError("Vector constructor: iterable required" )
        for v in values: _isnumber(v)
        self.values = list(values)
        self.length = len(values)
        for v in values: _isnumber(v)
        return
        
    def __add__(self, vector):
        """
        
        Add two vectors

        Parameters
        ----------
        vector : Vector or Iterable of Numbers
        
        Raises
        ------
        TypeError

        Returns
        -------
        c : Vector: The sum of two vectors: c = a + b

        """
        
        b = vector if isinstance(vector, Vector) else Vector(vector)
        if (b.length != self.length):
            raise TypeError("Vector add : same dimesion vector required")
        c = Vector([ai + bi for ai, bi in zip(self.values, b.values)])
        return c
    
    def __mul__(self, scalar):
        """
        
        Multiply a vector by an number

        Parameters
        ----------
        scalar : a number (int, float or complex)
            DESCRIPTION.

        Raises
        ------
        TypeError
            DESCRIPTION.

        Returns
        -------
        c : TYPE
            DESCRIPTION.

        """
        
        if (not _isnumber(scalar)):
            raise TypeError("Vector mul requires scalar")
        c = Vector([scalar * vi for vi in self.values])
        return c
        

    def __rmul__(self, scalar):
        """
        Right multiplication of a Vector by an scalar a * vector
        
        """
        
        return Vector.__mul__(self, scalar)


    def __getitem__(self, i):
        """
        

        Parameters
        ----------
        i : int, index of the coordinate

        Returns
        -------
        Number: value of the ith coordinate of the vector

        """
        return self.values[i]

    def __eq__(self, vector):
        """
        

        Parameters
        ----------
        vector : Vector of Iterable of Numbers

        Returns
        -------
        bool : if the two vector has identical components

        """
        b = vector if isinstance(vector, Vector) else Vector(vector)
        return all([xi == yi for xi, yi in zip(self.values, b.values)])


    def __str__(self):
        """
        

        Returns
        -------
        str, coverts vector into string
        """
        return str(self.values)

    
    def __repr__(self):
        """
        

        Returns
        -------
        str, converts vector into string
        """
        return str(self.values)
        