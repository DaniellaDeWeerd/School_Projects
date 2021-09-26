# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 12:13:08 2021

@author: danie
"""

def readFile(fileName): #splits file into a list by line
    fileObj = open(fileName, "r") #opens the file in read mode
    the_list = fileObj.read().splitlines() #puts the file into a list split by lines
    fileObj.close()
    return the_list

def create_array(list): # takes each list element and splits them into another list
    the_array = []
    for element in list:
        new_element = element.split("\t")
        new_element = new_element[0:7] #removes extra elements which are just spaces
        the_array.append(new_element)
    return the_array #results is a list of lists which looks like an array, thus the name.

def change_first_element(big_array, column): #used to bring the body site to the front to be used later in a sort.
    for the_list in big_array:
        the_list.insert(0, the_list.pop(column))
    return big_array

def list_of_body_sites(the_array): #to count number of each body site
    return_list = []
    for the_list in the_array:
        return_list.append(the_list[0])
    return return_list

def new_body_site(the_array): #function to create files for each body site
    first_list = the_array[0] #grab list at the top of the array
    body_site = first_list[0] #grab first element which is a body site
    list_to_count = list_of_body_sites(the_array) #create list of remaining body sites
    count = list_to_count.count(body_site) #use list to count that particular body site
    seperated_array = the_array[0:count] 
    old_array = the_array[count:]
    file_name = str(body_site) + ".txt"
    textfile = open(file_name, "w")
    for element in seperated_array:
        ID = element[1]
        textfile.write(str(ID) + "\t")
        textfile.write("\n")
    textfile.close()
    return old_array

def find_count_for_one_visit(the_array):
    count = 0
    for the_list in the_array:
        if the_list[2] == "1":
            count += 1
    return count

def main(): #auto run functions
    array = readFile('v13_map_uniquebyPSN.txt')
    new_array = create_array(array)
    visitor_count = find_count_for_one_visit(new_array)
    print("number of people with 1 visit: ", visitor_count)
    column_for_body_site = 5
    body_site_array = change_first_element(new_array, column_for_body_site)
    body_site_array.sort()
    while body_site_array:
        body_site_array = new_body_site(body_site_array)
    
if __name__ == "__main__":
    main()
            