"""
COMP 2040: ASSIGNMENT 5
-------------------------------------------------------------------------------
-->Import the lrm module you made above.
-->Create two LinRegModel objects, one using the default values for slope and 
bias, the other setting slope = -1 and bias = 4.
-->Use print to display the attributes of each linear regression model.
-->Use the predict method you created to obtain predictions from each model for 
the input xlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]; store each list of 
predictions in a variable.
-->Use the rmse function to calculate the root-mean-squared-error of each 
function, using your predictions and 
ylist = [4, 3, 2, 1, 0, -1, -2, -3, -4, -5]. Print the result for each model.

@author: Sodiq
@date: Wed Jan 31, 2024

"""

#import the lrm module 
import lrm

#prompt users to input values for slope and bias
slope = int(input("Give a number for slope: "))
bias = int(input("Give a number for bias: "))

#create two variables that store the default and input values
value_default = lrm.LinRegModel()
value_input = lrm.LinRegModel(slope, bias)

#display the attributes of each linear regression model.
print("Linear regression model, default values\n", value_default)    
print("Linear regression model, input values\n", value_input) 

x_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#create two variables that store the predicted values for each model
predictions = value_input.prdt_mtd(x_list) 
predictionss = value_default.prdt_mtd(x_list) 

#display the results of the predicted values for each model  
print("The predictions of the input values are: ", predictions)
print("The predictions of the default values are: ", predictionss)

y_list = [4, 3, 2, 1, 0, -1, -2, -3, -4, -5]

#cteate two variables that store the rmse answer for each model
rmse_value = lrm.rmse(predictions, y_list)
rmse_values = lrm.rmse(predictionss, y_list)

#display the results of the rmse values for each mode
print(f"Root Mean Squared Error for input values: {rmse_value}")
print(f"Root Mean Squared Error for default values: {rmse_values}")



   