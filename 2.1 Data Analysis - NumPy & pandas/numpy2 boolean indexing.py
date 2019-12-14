# boolean indexing with numpy

# https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html

# Boolean arrays AKA boolean vectors or boolean masks

import numpy as np

# numpy has a file utility, no need to import csv 
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')

taxi_shape = taxi.shape


# 
# we can skip the header
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=1)

taxi_shape = taxi.shape

# Calculate the number of rides in the taxi ndarray that are from a given month
pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool] # index the month
january_rides = january.shape[0] # find the num of items, in index 0 of the tuple

february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]

# the boolean array must have the same length as the dimension we index

# we can use a boolean array of one column of our array to index the whole array

# finding the tips over 50 
tip_amount = taxi[:,12]

tip_bool = tip_amount > 50
top_tips = taxi[tip_bool,5:14]


# Modifying values within a numpy array

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()

# set element at row, column to a certain value
taxi_modified[28214,5] = 1

# set column 0 a value
taxi_modified[:,0] = 16

# set rows in a range at column location to the mean value for that column
taxi_modified[1800:1802, 7] = taxi_modified[:,7].mean()

# Assignment using Boolean array

# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()
total_amount = taxi_copy[:,13] # select the 13th column

# for all values in the 13th column < 0, set to 0
total_amount[total_amount < 0] = 0   


# filter values and set default to new value, in this case 0
# create a new column filled with `0`.
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)

# pickup_location_code = column[5]
# For rows where column[5] is 2 (JFK Airport), assign  1.
taxi_modified[taxi_modified[:, 5] == 2, 15] = 1

# same for 3 (La Guardia)
taxi_modified[taxi_modified[:, 5] == 3, 15] = 1

# also for 5 (Newark Airport)
taxi_modified[taxi_modified[:, 5] == 5, 15] = 1


# Which is the most popular airport drop-off?

# drop_off_location_code = column[6]

# JFK will be 2, find those
jfk = taxi[taxi[:,6] == 2]  

# return the count through ndarray.shape 
jfk_count = jfk.shape[0]  # Answer 11832

laguardia = taxi[taxi[:,6] == 3]
laguardia_count = laguardia.shape[0]  # Answer 16602

newark = taxi[taxi[:,6] == 5]
newark_count = newark.shape[0]  # Answer 63

# calculating stats on trips on cleana data
# Finding the mph for trips
trip_mph = taxi[:,7] / (taxi[:,8] / 3600)

# only accept those less than 100 mph
cleaned_taxi = taxi[trip_mph < 100]

# print(cleaned_taxi.shape)
# taxi_modified[1800:1802, 7] = taxi_modified[:,7].mean()
mean_distance = cleaned_taxi[:,7].mean()
mean_length = cleaned_taxi[:,8].mean()
mean_total_amount = cleaned_taxi[:,13].mean()