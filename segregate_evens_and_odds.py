# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    if len(numbers)<=1:
        return numbers
    
    i = 0 
    j = len(numbers)-1
    while i<j:
        if numbers[i]%2 != 0:
            #swap
            tmp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = tmp
            j = j - 1
            
        else: 
            i = i + 1

    
    return numbers