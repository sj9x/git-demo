#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:43:23 2023

@author: swatjain
"""


def helper_printer(slate, L,n):
    if len(slate)==n:
        L.append(slate)
        print(slate)
        return None
    
    ### append "0"
    helper_printer(slate+"0",L,n)
    
    ## append "1"
    helper_printer(slate+"1",L,n)
    
    return None
    

def helper_printer2(slate, L,n):
    if n==1:
        L.append(slate+"0")
        L.append(slate+"1")
        return 
    
    ### append "0"
    helper_printer2(slate+"0",L,n-1)
    
    ## append "1"
    helper_printer2(slate+"1",L,n-1)
    
    return None
    
def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    # Write your code here.
    L = []
    helper_printer2("",L,n)
    
    return L
