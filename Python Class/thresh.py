# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:22:38 2021

@author: daniella

module applies threshold to data. data lower than threshold returns the threshold.
"""

def apply_threshold(data, threshold):
    #function that thresholds some data
    if data > threshold:
        #data above threshold
        return data
    else:
        #data below threshold
        return threshold
    
def apply_threshold_list(data,threshold):
    """Data is assumed to be a list"""
    thresholded_data = []
    for element in data:
        thresholded_data.append(apply_threshold(element, threshold))
    return thresholded_data
    
def fbn(N):
    ff_numbers = [1,1]
    
    for i in range (2,N):
        
    