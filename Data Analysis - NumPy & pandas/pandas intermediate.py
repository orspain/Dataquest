# Pandas - intermediate

import pandas as pd
# read the data set into a pandas dataframe
#
# f500 = pd.read_csv("f500.csv", index_col=0)
#f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
#500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

# f500_selection = f500[["rank", "revenues", "revenue_change"]].head(5)

# More conventional way
f500 = pd.read_csv("f500.csv")
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

# 
first_three_rows = f500[:3]

# Use iloc -> rows 1 to 7 and first 5 columns
first_seventh_row_slice = f500.iloc[[0, 6], :5]

# methods to create bool masks

null_previous_rank = f500[f500["previous_rank"].isnull()][
    ["company", "rank", "previous_rank"]]

# returning top 5 using iloc
top5_null_prev_rank = null_previous_rank.iloc[0:5]

# Index alignment is done when adding a new column, ignoring order

previously_ranked = f500[f500["previous_rank"].notnull()]

rank_change = previously_ranked["previous_rank"] - previously_ranked["rank"]

f500["rank_change"] = rank_change


# Using Bool 
large_revenue = f500["revenues"] > 100000
negative_profits = f500["profits"] < 0
combined = large_revenue & negative_profits

# Same as:
combined = (f500["revenues"] > 100000) & (f500["profits"] < 0)

big_rev_neg_profit = f500[combined]

# all at once
big_rev_neg_profit = f500[(f500["revenues"] > 100000) & (f500["profits"] < 0)]

# more Bool filtering 
filter_brazil_venezuela = (f500["country"] == "Brazil") | (f500["country"] == "Venezuela")
brazil_venezuela = f500[filter_brazil_venezuela]

filter_tech_outside_usa = (f500["sector"] == "Technology") & ~(f500["country"] == "USA")
tech_outside_usa = f500[filter_tech_outside_usa].head()

# Selecting and Sorting

selected_rows = f500[f500["country"] == "Japan"]

# sort by our selection depending on a value, in descending order
sorted_rows = selected_rows.sort_values("employees", ascending=False)

top_japanese_employer = sorted_rows.iloc[0]["company"]


# Using loops in pandas

# Create an empty dictionary to store the results
top_employer_by_country = {}

# Create an array of unique countries
countries = f500["country"].unique()

# Use a for loop to iterate over the countries
for c in countries:
    # Use boolean comparison to select only rows that
    # correspond to a specific country
    selected_rows = f500[f500["country"] == c]
    
    # sort by num of employees
    sorted_rows = selected_rows.sort_values("employees", ascending=False)
    
    # Select first row from sorted DataFrame object
    top_employer = sorted_rows.iloc[0]
    
    # Get the company name
    employer_name = top_employer["company"]
    
    # country name as the key
    top_employer_by_country[c] = employer_name



    ### Another example 
# Vector division
f500["roa"] = f500["profits"] / f500["assets"]

# Create an empty dictionary to store the results
top_roa_by_sector = {}

# Use a for loop to iterate over the countries
# with an array of unique sectors
for sector in f500["sector"].unique():
    # Use boolean comparison to select only rows that
    # correspond to a specific country
    selected_rows = f500["sector"] == sector
    sector_companies = f500.loc[selected_rows]
    # sort by roa and 
    # Select first row from sorted DataFrame object
    top_company = sector_companies.sort_values("roa", ascending=False).iloc[0]
    
    # Get the company name
    company_name = top_company["company"]
    
    # country name as the key
    top_roa_by_sector[sector] = company_name