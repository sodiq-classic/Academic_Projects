# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 16:58:53 2023

@author: Sodiq Akinbolaji
ASSIGNMENT_2
PROJECT_5
"""
"""
TASK
 Create a dictionary containing five different categories, add specific items in each category.
 Print the complete category and also, print each category separately.
 """
 
 #This line creates a dictionary
store_inventory_dictionary  = {"electronics": ['socket','scanner','monitor'],
                               "food": ['fries','burger','beans'],
                               "hardware": ['keyboard', 'camera', 'mouse'],
                               "kitchen": ['oven', 'diches', 'fridge'],
                               "pets": ['cat', 'squirrel', 'bunny'],
                               }

#This line prints the complete dictionary
print("The complete dictionary is: ", store_inventory_dictionary)

#This line prints each category in the dictionary
print("The category, 'electronics' contains: ", store_inventory_dictionary["electronics"])
print("The category, 'food' contains: ", store_inventory_dictionary["food"])
print("The category, 'hardware' contains: ", store_inventory_dictionary["hardware"])
print("The category, 'kitchen' contains: ", store_inventory_dictionary["kitchen"])
print("The category, 'pets' contains: ", store_inventory_dictionary["pets"])
