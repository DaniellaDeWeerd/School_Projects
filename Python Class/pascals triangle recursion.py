# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:26:15 2021

@author: danie
"""

first_row_for_use = [0,1,0]
first_row_for_print = [1]
last_row = []
current_row=[]

def pascals_triangle(how_far):
    global first_row_for_print
    global first_row_for_use
    global last_row
    i = 0
    while i <= how_far:
        if len(last_row) == 0:
            print('{:^24s}'.format(str(*first_row_for_print)))
            last_row = first_row_for_use
        else:
            calculate_new_row()
            print_new_row()
        i = i + 1

def calculate_new_row():
    global last_row
    global current_row
    current_row = []
    last_row_number = len(last_row)
    i = 2
    while i <= last_row_number:
        number_1 = last_row[i-2]
        number_2 = last_row[i-1]
        current_row.append(number_1 + number_2)
        i = i + 1
    last_row = current_row.copy()

def print_new_row():
    global current_row
    string = str(current_row)
    print('{:^24s}'.format(string))

def main():
    user_input = input("Please type how many rows you would like your triangle to have.")
    user_input = int(user_input)
    pascals_triangle(user_input)
        
if __name__ == "__main__":
    main()



