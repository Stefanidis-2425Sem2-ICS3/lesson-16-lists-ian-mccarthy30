# Name: Ian McCarthy
# Title: Lists
# Date: April 10, 2025
# Description: creates a list of 100 random numbers between 0 and 100 and gets the average of all of them

import random

#Creats a list of 100 random numbers and then prints them
Hundid_Nums = [random.randint(0,100) for i in range(100)] 
print("The 100 random numbers are:")
print (Hundid_Nums)

#Finds the average of those 100 numbers and prints that average
Average = sum(Hundid_Nums)/len (Hundid_Nums)
print ("The average of these numbers is:") 
print(Average)