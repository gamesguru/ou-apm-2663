#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 02:50:11 2024

@author: shane
"""

divis = []

for i in range(1, 600 + 1):
    if i % 5 == 0 or i % 7 == 0 or i % 17 == 0:

        # common_factor = 0
        # if i % 5 == 0:
        #     if  i % 7:
        #         if i % 13:
        #             print(f"divisible by all three: {i}")
        #     common_factor += 1
        # if i % 7 == 0:
        #     common_factor += 1
        # if i % 17 == 0:
        #     common_factor += 1

        # if common_factor > 1:
        #     print(i)

        divis.append(i)

print(f"{len(divis)} are divisible by at least one of 5, 7, and 17!")
