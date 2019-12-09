''' pandas - extends numpy 

Dataframe - equiv. to 2D ndarray
    Axis values can have string labels, not only numeric
    Multiple data types: int, float, str,
'''
import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None

f500_type = type(f500)
f500_shape = f500.shape


f500_head = f500.head(6)
f500_tail = f500.tail(8)
#print(f500_head)
#print(f500_tail)

f500.info()

# Select a column from a DataFrame by label: df.loc[row_label, column_label]

industries = f500["industry"]
industries_type = type(industries) # returns 1D series object 

# Selecting columns part 2

# Select column by label
countries = f500["country"]

# Select continous columns - double brackets!  - DataFrame object
revenues_years = f500[["revenues", "years_on_global_500_list"]]

# Select range of columns 
ceo_to_sector = f500.loc[:,"ceo":"sector"]


# Selecting Rows from a DataFrame

# Single row  - 1D series object
toyota = f500.loc["Toyota Motor"]

# multiple rows - double brackets!   DataFrame object
drink_companies = f500.loc[["Anheuser-Busch InBev", "Coca-Cola", "Heineken Holding"]]

# range of rows with range of columns
middle_companies = f500.loc["Tata Motors":"Nationwide", "rank":"country"]

# Value Counts Method - works for series objects!
countries = f500_sel["country"]
country_counts = countries.value_counts()


# Selecting items from a series by label
countries = f500['country']
countries_counts = countries.value_counts()

india = countries_counts["India"]
north_america = countries_counts[["USA", "Canada", "Mexico"]]

# multiple rows with multiple columns - each w/ brackets sep. comma
big_movers = f500.loc[["Aviva","HP","JD.com","BHP Billiton"],["rank","previous_rank"]]

# range of rows w/ multiple columns - note the different syntax!
bottom_companies = f500.loc["National Grid":"AutoNation",["rank","sector","country"]]


### Vectorized ops 
rank_change = f500["previous_rank"] - f500["rank"]

# Series data exploration methods -

# Finding max and min in a series 
rank_change =  f500["previous_rank"] - f500["rank"]
rank_change_max = rank_change.max()
rank_change_min = rank_change.min()


# Series describe method
rank = f500["rank"]
rank_desc = rank.describe()

prev_rank = f500["previous_rank"]
prev_rank_desc = prev_rank.describe()

## Example of method chaining
# without
countries = f500["country"]
countries_counts = countries.value_counts()

# with method chaining 
countries_counts = f500["country"].value_counts()


zero_previous_rank = (f500["previous_rank"].value_counts().loc[0])

# filter for numeric values in columns

max_f500 = f500.max(numeric_only=True) 

# Dataframe Describe Method
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html

f500_desc = f500.describe()


# Assignment to update value
f500.loc["Dow Chemical", "ceo"] = "Jim Fitterling"

# Using Bool indexing 

# Returns true for the 'industry' column when 'value'
motor_bool = f500["industry"] == "Motor Vehicles and Parts"

# creates index by country
motor_countries = f500.loc[motor_bool, "country"]


## Use Bool array to assign values
ampersand_bool = f500["sector"] == "Motor Vehicles & Parts"
f500.loc[ampersand_bool, "sector"] = "Motor Vehicles and Parts"

# Shorter, does the same
f500.loc[f500["sector"] == "Motor Vehicles & Parts","sector"] = "Motor Vehicles and Parts"


# Here we are including the NaN values 
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()

# Assign a NaN where it's zero - wrong data
f500.loc[f500["previous_rank"] == 0,"previous_rank"] = np.nan

prev_rank_after = f500["previous_rank"].value_counts(dropna=False).head()


## Create New Column - here based on diff of two other columns 
f500["rank_change"] = f500["previous_rank"] - f500["rank"]

# See what we did
rank_change_desc = f500["rank_change"].describe()

# Top performers by country using method chaining

# grouped by industry, what are the top 2 in USA?
industry_usa = f500["industry"][f500["country"] == "USA"].value_counts().head(2)

# grouped by sector, which are the top 3 in China?
sector_china = f500["sector"][f500["country"] == "China"].value_counts().head(3)