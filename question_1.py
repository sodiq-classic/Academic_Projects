"""
COMP 2040: ASSIGNMENT 4
-------------------------------------------------------------------------------
Ask the user to input five integers and store these in a list; reject any 
input that is not a valid integer and ask again, so that you receive five 
valid integers at the end of this input process. Write a code to sort the 
numbers from smallest to largest (do not use the sort() method). Print out the 
original list and the sorted list.

@author: Sodiq
@date: Tue Jan 23, 2024

"""

#create an empty list
original_list = []

def get_valid_integer():
    while True:
        #prompt a user to inpur a value
        user_input = input("Enter an integer number: ")
        try:
            #convert the value to an integer
            integer_value = int(user_input)
            #store the value in the empty list above
            original_list.append(integer_value)
            return integer_value
        #ask the user to re-input a value if the one fiven is not an integer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

#create another empty list
numbers = []

# Get five valid integers from the user
for x in range(5):
    #insert the number provided by the user into the empty list(numbers) above
    numbers.append(get_valid_integer())
# Sort the list so that it shows the numbers provided in ascending order
# iterates through each index i in the list numbers.
for i in range(len(numbers)):
#iterates through each index j starting from i+1 to the end of the list numbers.
    for j in range(i + 1, len(numbers)):
#check if the element at index i is greater than the element at index j.        
        if numbers[i] > numbers[j]:
#swaps the values of numbers[i] and numbers[j] in-place.            
            numbers[i], numbers[j] = numbers[j], numbers[i]

# Print the original and sorted lists
print("Original List:",original_list )
print("Sorted List:", numbers)
