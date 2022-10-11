#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:46:34 2022

@author: hernando
"""

from vector import Vector
import random
#import pytest as pt


def inputs():
    
    n = random.sample(range(2, 11), 1)[0]
    a = [random.uniform(-1, 1) for i in range(n)]
    b = [random.uniform(-1, 1) for i in range(n)]
    return Vector(a), Vector(b)


def test_vector_add():

    a, b = inputs()
    
    null = 0 * a
    
    assert a + b       == b + a
    assert a + null    == null + a
    assert a + (a + b) == (a + a) + b
    
    return True
    
    
def test_vector_mul():
    
    a, b = inputs()
    
    assert 0 * a      == 0 * a
    assert 1 * a      == a
    alpha = b[1]
    assert a * alpha  == alpha * a
            
    
    return True
    