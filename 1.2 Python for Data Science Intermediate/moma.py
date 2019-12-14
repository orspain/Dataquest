from csv import reader

opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

age1 = "I am thirty-one years old"
age2 = age1.replace("thirty-one", "thirty-two")

for row in moma:
    nationality = row[2]
    nationality = nationality.replace("(","")
    nationality = nationality.replace(")","")
    row[2] = nationality
    gender = row[5]
    gender = gender.replace("(","")
    gender = gender.replace(")","")
    row[5] = gender

for row in moma:
    gender = row[5]
    nationality = row[2]
    # convert the gender to title case
    gender = gender.title()
    nationality = nationality.title()
    # if there is no gender, set
    # a descriptive value
    if not gender:
        gender = "Gender Unknown/Other"
    row[5] = gender
    if not nationality:
        nationality = "Nationality Unknown"
    row[2] = nationality

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date


for row in moma:
    birth_date = row[3]
    death_date = row[4]
    clean_and_convert(birth_date)
    row[3] = birth_date
    clean_and_convert(death_date)
    row[4] = death_date

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(date):
    if "-" in date:
        split_date = date.split("-")
        date_one = split_date[0]
        date_two = split_date[1]
        date = (int(date_one) + int(date_two)) / 2
        date = round(date)
    else: 
        date = int(date)
    return date

processed_test_data = []
                    
for d in stripped_test_data:
    date = process_date(d)
    processed_test_data.append(date)  

for row in moma:
    date = row[6]
    date = strip_characters(date)
    date = process_date(date)
    row[6] = date
    