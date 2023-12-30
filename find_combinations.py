#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 07:24:35 2023

@author: swatjain
"""


def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    if k > n:
        return []
    
    if n == 1:
        return [[1]]
    
    if k == 1:
        return [[w] for w in list(range(1,n+1))]
    
    L = find_combinations(n-1,k-1)
    L2 = find_combinations(n-1,k)
    print(L)
    
    
    
    return [w+[n] for w in L]+L2
