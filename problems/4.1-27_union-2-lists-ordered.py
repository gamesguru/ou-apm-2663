#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:11:21 2024

@author: shane
"""

# NOTE: evens start off larger but lose: 8>7 but 10<11 and finally 14<13

# primes
a = [1, 3, 5, 7, 11, 13, 17, 19]

# evens
b = [2, 4, 6, 8, 10, 12, 14, 16]

# main algorithm
c = []

i = 0
while i < max(len(a), len(b)):
    i += 1
