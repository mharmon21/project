#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 00:52:03 2023

@author: micaelaharmon
#Micaela Harmon
#00001435104
#INF308
"""

message = ""

vegetarian = input("Is anyone in your party a vegetarian? ")

if vegetarian == "Yes" or vegetarian == "No":
    vegan = input("Is anyone in your party a vegan? ")

    if vegan == "Yes" or vegan == "No":
        gluten_free = input("Is anyone in your party gluten-free? ")

        if gluten_free == "Yes" or gluten_free == "No":
            keto = input("Is anyone in your party on a keto diet?")
            if keto == "Yes" or keto == "No":
                message = "\nPlease go to one of these restaurant choices:\n"
            if vegetarian == "Yes":
                
                if vegan == "Yes":

                    if gluten_free == "Yes" or gluten_free == "No":
                        message += "Peaches Cafe\n" + \
                                   "California Pizza Kitchen\n"
                else: 
                    if gluten_free == "Yes":
                        message += "City Line\n" + \
                                   "Peaches Cafe\n" + \
                                   "California Pizza Kitchen\n"
                    else:
                        message += "City Line\n" + \
                                   "Peaches Cafe\n" + \
                                   "Vincents Italian\n" + \
                                   "California Pizza Kitchen\n"
            else: # vegetarian == "no"

                if vegan == "Yes":

                    if gluten_free == "Yes" or gluten_free == "No":
                        message += "Peaches Cafe\n California Pizza Kitchen\n"

                else: # vegan == "no"

                    if gluten_free == "Yes":
                        message += "City Line\n" + \
                                   "Peaches Cafe\n" + \
                                   "California Pizza Kitchen\n"
                                   
                    else: # gluten free == "no"
                        message += "Black & Blue Steakhouse\n" + \
                                   "City Line\n" + \
                                   "Peaches Cafe\n" + \
                                   "Vincents Italian\n" + \
                                   "California Pizza Kitchen\n"
            
                                   
            
        else:
            message = "Enter either 'Yes' or 'No'.\nRerun the program and try again."
    
    else:
        message = "Enter either 'Yes' or 'No'.\nRerun the program and try again."

else:
    message = "Enter either 'Yes' or 'No'.\nRerun the program and try again."


print(message)