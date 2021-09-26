# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 00:54:11 2021

@author: Daniella
"""

class binomial_coefficients: # class to find binomial coeeficients using Pascal's rule
    def get_n(self,n): # find row
        global row #create list to contain row that can be used in other functions
        row = [] #initialize empty row list
        num_of_k = n + 1 #figure out how many times k will have to be found
        for k in range(num_of_k): #run the function to find k that many times
            number = self.get_nk(n, k) #find k in the n,k position
            row.append(number) #add result to row list
        return row
    
    def get_nk(self,n,k): #find k for certain row
        global row #making it able to look at that global row variable
        if (k == 0): #if it is first number in row, it is 1
            return 1
        elif (k == n): #if it is last number in row, it is 1
            return 1
        else: #if not the first or last number:
            previous_num = row[k-1] #find previous number in row
            new_num = int(previous_num * ((n+1-k)/k)) #run formula to find the next number in that row
            return new_num #return that number
            
    def save_pt(self,n,file_name = 'pascal_triangle.txt'): #find n number of rows and write the resulting triangle to a particular file
        global row #again ensuring access to the gloabl row (list)
        triangle ="" #initializing triangle string
        for num in range(n): #for each row until you hit the row's wanted
            spacing = n * (round(n/10)*3) #This line is for centering the numbers in the file. 
            row = self.get_n(num) #get row n
            string = self.listToString(row) #turn the row list into a string of the elements seperated by a space
            string = string.center(spacing) #center that string
            triangle += string #add it to the triangle string
            triangle += "\n" #add a new line for the next row
        print(triangle) #for checking purposes without looking at the file
        f = open(file_name, "w") #open string to file (will overwrite file if it already exists)
        f.write(triangle) #write triangle string to file
        f.close #close file
    
    def listToString(self, list1): #turn list into string
        string = "" #initialize string
        for element in list1: #for each element:
            string += str(element) #add the element to the string
            string += " " #add space behind it
        return string #return the completed string
        
def main(): #all for testing purposes only
        user_input = input("Please type how many rows you would like your triangle to have.\n")
        global how_far
        how_far = int(user_input)
        BC = binomial_coefficients()
        BC.save_pt(how_far)   

if __name__ == "__main__":
    main()
            
            
                