"""
COMP 2040: ASSIGNMENT 3
----------------------------------------
This program will prompt a user to input a word, and then check if the word is 
palindrome(word spelled the same forward and backward).

@author: Sodiq
@date: Wed Jan 17, 2024

"""

import time

#Prompt a user to input a word
input_word = input("Please enter a word: ")

#convert the word to lower case
upper_case = (input_word.upper())

#display a statement that spell the word as it is inserted
print("By spelling forward, the word you input is spelt as: ", upper_case)
time.sleep(3)
#display a statement that tells the user if the word given is palindrome
print("Let's see if the word you gave is an example of palindrome")
time.sleep(3)
#let's make the word to be spelt from the back
#start spelling from the last letter to the first
spelt_backward = upper_case[::-1]

#now lets check if the word given is the same when spelt backward
if upper_case == spelt_backward:
    print("The word you provided when spelt backward is: ", spelt_backward)
    print("There you go! Your word is an example of palindrome")
    time.sleep(3)
else:
    print("The word you provided is not an example of palindrome")
    time.sleep(3)

