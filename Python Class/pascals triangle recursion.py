# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:26:15 2021

@author: danie
"""


first_row = [1]
second_row = [1,1]
last_row = []
current_row=[]
how_far = 0

def listToString(list1): 
    string = "" 
    
    for element in list1: 
        string += str(element)
        string += " "
    return string 

def pascals_triangle():
    global first_row_for_print
    global first_row_for_use
    global last_row
    global how_far
    spacing = how_far * (round(how_far/10)*3)
    i = 0
    while i <= how_far:
        if len(last_row) == 0:
            string = listToString(first_row)
            print(string.center(spacing))
            last_row = first_row.copy()
        elif len(last_row) == 1:
            string = listToString(second_row)
            print(string.center(spacing))
            last_row = second_row.copy()
        else:
            calculate_new_row()
        i = i + 1

def calculate_new_row():
    global last_row
    global current_row
    current_row = []
    current_row.append(1)
    last_row_number = len(last_row)
    i = 0
    while i < (last_row_number - 1):
        number_1 = last_row[i]
        if number_1 == (last_row_number):
            i = i + 1
        else:
            number_2 = last_row[i+1]
            current_row.append(number_1 + number_2)
            i = i + 1
    current_row.append(1)
    print_new_row()
    last_row = current_row.copy()

def print_new_row():
    global current_row
    global how_far
    spacing = how_far * (round(how_far/10)*3)
    string = listToString(current_row)
    print(string.center(spacing))

def main():
    user_input = input("Please type how many rows you would like your triangle to have.\n")
    global how_far
    how_far = int(user_input)
    pascals_triangle()
        
if __name__ == "__main__":
    main()



