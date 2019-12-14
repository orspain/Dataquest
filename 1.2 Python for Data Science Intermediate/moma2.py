from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate and deathdate values
for row in moma:
    birth_date = row[3]
    death_date = row[4]
    date = row[6]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date
    if date != "":
        date = int(date)
    row[6] = date



####  Clean the dates


ages = []

for row in moma:
    date = row[6]
    birth = row[3]
    if type(birth) == int:
        age = date - birth 
    else:
        age = 0
    ages.append(age)
    
final_ages = []

for age in ages:
    if age > 20: 
        final_age = age
    else:
        final_age = "Unknown"
    final_ages.append(final_age)

## Convert the ages to a string so that we can treat them as "within a decade"

decades = []

for age in final_ages:
    if age == "Unknown":
        decade = age
    else: 
        decade = str(age)
        decade = decade[:-1]
        decade = decade + "0s"
    decades.append(decade)

## Build a frequency dictionary based on decades

decade_frequency = {}

for decade in decades:
    if decade not in decade_frequency:
        decade_frequency[decade] = 1
    else:
        decade_frequency[decade] += 1


# too bad we can't use f strings in the course:
artist = "Pablo Picasso"
birth_year = 1881

output = "{0}'s birth year is {1}".format(artist, birth_year)
print (output)


# build a frequency dictionary for artists in the MoMa list of lists
artist_freq = {}

for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else: 
        artist_freq[artist] += 1

# a function to display artwork by a given artist 
def artist_summary(artist):
    num_artworks = artist_freq[artist]
    template = "There are {num} artworks by {name} in the data set"
    output = template.format(name=artist, num=num_artworks)
    print(output)
    
artist_summary("Henri Matisse")

# build gender frequency dict

gender_freq = {}

for row in moma:
   
    gender = row[5]
    if gender not in gender_freq:
        gender_freq[gender] = 1
    else: 
        gender_freq[gender] += 1

# use the dict to display artworks by gender

for gender, num in gender_freq.items():
    template = "There are {n:,} artworks by {g} artists"
    
    print(template.format(n=num, g=gender)

