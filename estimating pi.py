# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 20:42:15 2022

@author: MUSTAFA
"""

import numpy as np
import random
import matplotlib.pyplot as plt

# Part a)

# Declare a square of side length 1 m:
    
r= 1 # side length of the square in meters.

# Notice that side length of the square equals to the radius of the shaded circle.

# We also have to declare the number of throws:
    
throws= 50000 # Number of throws (arbitrarly assigned for part a)).

# We also have to count the throws that hit inside the shaded circle:
    
count_circle= 0 # For counting the throws hit inside the shaded circle.

# Using for loops:
    
for i in range (1, throws+1): # (1, throws+1) means 1, 2, ,3 ,4, ..., # of throws.
    x_throw= random.uniform(0, r) # x coordinate of the throw.
    y_throw= random.uniform(0, r) # y coordinate of the throw.
    if (x_throw**2+y_throw**2)<= r**2: # For checking if the throw is inside the shaded circle.
        count_circle+=1 # Update the count.
        
# Notice that we assume all the throws hit inside the square but not all of them inside the shaded circle.

# Number of throws that hit inside the square is:
    
count_square= throws

# Pi is given by:
    
pi= 4*(count_circle/count_square)

# Part b)

# For plotting # of throws vs error ((real pi value-pi estimate)/real pi value), declare an array including different numbers of throws:
    
throw_array= np.arange(100, 1000100, 10000) # Notice that we examine 100, 10010, 20010, ..., 990100, throws. 

# Notice also that we start from 100 throws since # of throws less than 100 does not give very good errors.

# We have to repeat the estimate process, and we also need an estimate array:
    
pi_estimate= [] # This will be filled in the for loop below.

# Also an error array:
    
error_array= []

count_circle_2= 0 # For counting (again) the throws hit inside the shaded circle.

for i in throw_array: # (1, throws+1) means 1, 2, ,3 ,4, ..., # of throws.
    count_circle_2= 0 # Make the counting zero before every value in the throw_array.
    for j in range (1, i+1): # This is for every # of throws value.
        x_throw= random.uniform(0, r) # x coordinate of the throw.
        y_throw= random.uniform(0, r) # y coordinate of the throw.
        if (x_throw**2+y_throw**2)<= r**2: # For checking if the throw is inside the shaded circle.
            count_circle_2+=1 # Update the count.
    pi= 4*(count_circle_2/i) # We use the formula given for estimating pi.
    error= (np.pi-pi)/np.pi # Error is given by (real value of pi - estimated value of pi)/ real value of pi).
    pi_estimate.append(pi) # Save the estimated pi value for each # of throw values.
    error_array.append(abs(error)*100) # Error percentage is abs(error)*100.
    

# Plotting the results:

plt.xlabel('# of Throws')
plt.ylabel('Estimated $\pi$ Value (Radians) ')
plt.title('Estimated $\pi$ Value vs # of Throws') 
plt.plot(throw_array, pi_estimate, 'k', label='Estimated $\pi$ Value (Radians)')
plt.axhline(y=np.pi, color='r',label='Real $\pi$ Value (Radians)', linestyle='-') # This is the real pi value.
plt.legend()
plt.show()


plt.xlabel('# of Throws')
plt.ylabel('Error Percentage (Unitless)')
plt.title('Error Percentage vs # of Throws') 
plt.plot(throw_array, error_array, 'k')
plt.show()

# Name: Ahmet Mustafa Baraz
# ID: 21702127
# Title of the Program: Approximating the pi value.


