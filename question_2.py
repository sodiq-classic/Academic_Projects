"""
COMP 2040: ASSIGNMENT 4
-------------------------------------------------------------------------------
Ask the user to input a string. Create a dictionary that has each character 
found in the string as a key, with the number of times it is found 
(the frequency) as the corresponding value. Print out the characters and 
frequencies, in alphabetical order of the keys (you may use a sort function 
for this question. For example, if the input is 'baca', the dictionary should 
be: {'a': 2, 'b': 1, 'c': 1}.

@author: Owner
@date: Tue Jan 23, 2024

"""

# Ask the user to input a string
user_input = input("Enter a word: ")

# Create a dictionary to store letter frequencies
lett_freq = {}

# Count the frequency of each letter in the input string
for lett in user_input:
    # If the letter is already in the dictionary, increment its count
    if lett in lett_freq:
        lett_freq[lett] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        lett_freq[lett] = 1
        
# Sort the dictionary by values (frequencies) in descending order
sorted_lett_freq = dict(sorted(lett_freq.items()))
# Print the letters and frequencies in order from highest to lowest 
#frequency
#print("Letter frequencies:")
for lett, freq in sorted_lett_freq.items():
    print(f"'{lett}': {freq}")                                                                                                                                                                                                                                                          
 









                                                                                                                                                                                                                                                                               