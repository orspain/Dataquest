opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

genres = extract(11)

def freq_table(my_list):
    frequency_table = {}
    for value in my_list:
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
    return frequency_table

genres_ft = freq_table(genres)


def freq_table2(index):
    frequency_table = {}
    for row in apps_data[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
    return frequency_table

ratings_ft = freq_table2(7)

def freq_table3(index, data_set):
    frequency_table = {}
    
    for data_set in apps_data[1:]:
        value = data_set[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

ratings_ft = freq_table3(7, apps_data)

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    data_list = extract(data_set, index)
    return find_sum(data_list) / find_length(data_list)

avg_price = mean(apps_data, 4)