# Part 2 scratch - NumPy

import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

taxi = np.array(converted_taxi_list) #create a numpy array from the list of lists

taxi_shape = taxi.shape  # show number of columns & rows
print(taxi_shape)   

row_0 = taxi[0]   # select single row 
rows_391_to_500 = taxi[391:501] # select range of rows
row_21_column_5 = taxi[21, 5] # select single element

# Select every row for the columns at indexes 1, 4, and 7
cols = [1,4,7] 
columns_1_4_7 = taxi[:,cols]

# Select the columns at indexes 5 to 8 inclusive for the row at index 99
row_99_columns_5_to_8 = taxi[99, 5:9]

# Select the rows at indexes 100 to 200 inclusive for the column at index 14
rows_100_to_200_column_14 = taxi[100:201, 14]


# perform addition on two columns - can do directly without variables too
fare_amount = taxi[:,9]
fees_amount = taxi[:,10]

fare_and_fees = fare_amount + fees_amount


# calculate avg speed of each trip 
# mph = miles traveled / time in hours

trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]

trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour

trip_mph = trip_distance_miles / trip_length_hours

mph_min = trip_mph.min()
mph_max = trip_mph.max()  # very large value here
mph_mean = trip_mph.mean()

# we'll compare against the first 5 rows only
taxi_first_five = taxi[:5]
# select these columns: fare_amount, fees_amount, tolls_amount, tip_amount
fare_components = taxi_first_five[:,9:13]

# using ndarray.sum() method with axis to return the sum of each row
fare_sums = fare_components.sum(axis=1)  
fare_totals = taxi_first_five[:,13]
print(fare_sums)
print(fare_totals)

