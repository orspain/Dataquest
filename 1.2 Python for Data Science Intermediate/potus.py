# Potus exercise

from csv import reader
opened_file = open('potus_visitors_2015.csv')
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]     # remove first row which contains the header

# example of datetime (year, month, day, hour, minute, second)
import datetime as dt
ibm_founded = dt.datetime(1911, 6, 16)
man_on_moon = dt.datetime(1969, 7, 20, 20, 17)


## converting appointment start in potus lists of lists
date_format = "%m/%d/%y %H:%M"
    
for row in potus:
    appointment = row[2]
    appointment = dt.datetime.strptime(appointment, date_format)
    row[2] = appointment


# working with deltas in time method
dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

answer_1 = dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(days=56)
answer_3 = dt_4 - dt.timedelta(seconds=3600)


# finding the appointment lengths from potus lists of lists
for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date
    
appt_lengths = {}  # assign the dictionary

for row in potus:
    start_date = row[2]
    end_date = row[3]
    length = end_date - start_date
    if length not in appt_lengths:
        appt_lengths[length] = 1
    else:
        appt_lengths[length] += 1
    min_length = min(appt_lengths)   # find the min and max 
    max_length = max(appt_lengths)