# Data cleaning basics

'''
 Workflow example (converting text to numeric):
    # Explore data in the column
    # ID patterns & special case
    # remove non-digit chars
    # Convert column to numeric
    # rename col if needed
'''


import pandas as pd
laptops = pd.read_csv('laptops.csv', encoding='Latin-1')
laptops.info()

def clean_col(col):

    # Strip whitespace 
    col = col.strip()
    col = col.replace("Operating System", "os")

    # replace spaces with underscores
    col = col.replace(" ", "_")

    # replace parens
    col = col.replace("(","")
    col = col.replace(")","")

    # all lowercase
    col = col.lower()
    return col

# loop through the columns to clean
new_columns = []
for c in laptops.columns:
    clean_c = clean_col(c)
    new_columns.append(clean_c)

laptops.columns = new_columns
print(laptops.columns)

# ID types of data 
unique_ram = laptops["ram"].unique()

# Change it to only numeric
laptops["ram"] = laptops["ram"].str.replace('GB','')
unique_ram = laptops["ram"].unique()

# Convert to int
laptops["ram"] = laptops["ram"].astype(int)


# Similar with screen size
laptops["screen_size"] = laptops["screen_size"].str.replace('"','')
laptops["screen_size"] = laptops["screen_size"].astype(float)

dtypes = (laptops.dtypes)

# rename the columns 
laptops.rename({"screen_size": "screen_size_inches"}, axis=1, inplace=True)

laptops.rename({"ram": "ram_gb"}, axis=1, inplace=True)

ram_gb_desc = laptops["ram_gb"].describe()


## Extracting values from strings

laptops["gpu_manufacturer"] = (laptops["gpu"]
                                       .str.split()
                                       .str[0]
                              )
print(laptops["gpu"].head().str.split().str[0])

laptops["cpu_manufacturer"] = (laptops["cpu"]
                                       .str.split()
                                       .str[0]
                              )

cpu_manufacturer_counts = laptops["cpu_manufacturer"].value_counts()

# Series.map 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}

laptops["os"] = laptops["os"].map(mapping_dict)

# Dropping missing values - normal for ML
laptops_no_null_rows = laptops.dropna()

laptops_no_null_cols = laptops.dropna(axis = 1)

# Filling missing vals

value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"

laptops.loc[laptops["os"] == "No OS", "os_version"] = "Version Unknown"

value_counts_after = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()


## Challenge: clean a string column

laptops["weight"] = laptops["weight"].str.replace('kgs','')
laptops["weight"] = laptops["weight"].str.replace('kg','')

laptops["weight"] = laptops["weight"].astype(float)

laptops.rename({"weight": "weight_kg"}, axis=1, inplace=True)

# save it as another csv file
laptops.to_csv('laptops_cleaned.csv', index=False)

