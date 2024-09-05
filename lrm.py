"""
COMP 2040: ASSIGNMENT 5
-------------------------------------------------------------------------------
A class named LinRegModel which is used for working with linear regression 
models. This class should have the __init__, __repr__, and a predict method 
function. A function named rsme should be created outside the class.

@author: Sodiq
@date: Wed Jan 31, 2024

"""
#create a class 
class LinRegModel:
    #create a function that holds the variables needed for this problem
    def __init__(self, slope = 0, bias = 0):
        """creates two attributes: slope and bias, 
        each with a default value of 0.""" 
        self.slope = slope
        self.bias = bias
        
    #create a function that provides a nice visual for the print statement
    def __repr__(self):
        """this method neatly displays the value of slope and bias 
        for a LinRegModel object"""
        a = ('*********************************\n')
        b = 'Model parameters:' + '\n'
        c = 'slope = ' + str(self.slope) + '\n'
        d = 'bias = ' + str(self.bias) + '\n'
        return a + b + c + d + a
    
    #create a function that solves a problem provided there are given values
    def prdt_mtd(self, i):
        """this method takes a list of floats (x) as input 
        and returns a list of predictions (y) according to the equation
        of a straight line"""
        #the equation used to solve the problem
        #equation of a straight line
        prediction = [self.bias + self.slope * x for x in i]
        return prediction
    
#import the math module        
import math

#create a function that takes in two values        
def rmse(predictions, y_list):
    """this function inputs two lists of floats (each with the same length), 
    one with predictions (yhat) and the other with true values (y). 
    The function will return the root-mean-squared-error"""
    #these lines demonstate the root mean squared error(formula)
    square_error = [(yhat - y) ** 2 for yhat, y in zip(predictions, y_list)]
    mean_square_error = sum(square_error) / len(predictions)
    root_mean_square_error = math.sqrt(mean_square_error)
    return root_mean_square_error
                
        
    

    
    
    
    
    
    
    
    
    
    