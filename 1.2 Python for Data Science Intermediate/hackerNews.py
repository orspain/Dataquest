opened_file = open("hacker_news.csv")
from csv import reader
read_file = reader(opened_file)
hn = list(read_file)
print(hn[0:5])

headers = hn[0]
hn = hn[1:]
print(hn[0:5])

# Create three empty lists called ask_posts, show_posts, and other_posts
ask_posts = []
show_posts = []
other_posts = []

# Loop through each row in hn.
for row in hn:
    title = row[1]  # Assign the title in each row, data is at index 1
    # If the lowercase version of title starts with ask hn, append the row to ask_posts.
    if title.lower().startswith('ask hn'): 
        ask_posts.append(row)
    # Elif the lowercase version of title starts with show hn, append the row to show_posts.
    elif title.lower().startswith('show hn'):
        show_posts.append(row)
    else:  # Else append to other_posts.
        other_posts.append(row)

# Check the number of posts in ask_posts, show_posts, and other_posts  
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))

# determine if ask posts or show posts receive more comments on average

# Find the total number of comments in ask posts and assign it to total_ask_comments.

ask_comments = [int(row[4]) for row in ask_posts]
show_comments = [int(row[4]) for row in show_posts]

avg_ask_comments = sum(ask_comments)/len(ask_comments)
avg_show_comments = sum(show_comments)/len(show_comments)

print("Average Ask Comments: ",avg_ask_comments)
print("Average Show Comments: ",avg_show_comments)

"""
Do show posts or ask posts receive more comments on average? 
Write a markdown cell explaining your findings.

"""
import datetime as dt
result_list = []
for row in ask_posts:
    sublist = []
    createdtime = row[6]
    comments = int(row[4])
    sublist.append(createdtime)
    sublist.append(comments)
    result_list.append(sublist)
       
result_list[0:4]


counts_by_hour = {}
comments_by_hour = {}

for row in result_list:
    dt_object = row[0]
    dt_parsed = dt.datetime.strptime(dt_object, "%m/%d/%Y %H:%M")
    hr = dt.datetime.strftime(dt_parsed,"%H")
    #print(hr)
    
    if hr not in counts_by_hour:
        counts_by_hour[hr] = 1
        comments_by_hour[hr] = int(row[1])
    else:
        counts_by_hour[hr] = counts_by_hour[hr] + 1
        comments_by_hour[hr] = comments_by_hour[hr] + int(row[1])

print(comments_by_hour)
print(counts_by_hour)


avg_by_hour = []

for hour in comments_by_hour:
    avg_by_hour.append([hour,comments_by_hour[hour]/counts_by_hour[hour]])
    
avg_by_hour   

swap_avg_by_hour = []
for row in avg_by_hour:
    #print(key)
    #creating a sublist and appending it
    sublist = []
    sublist.append(row[1])
    sublist.append(row[0])
    swap_avg_by_hour.append(sublist)
print(swap_avg_by_hour)


#sorted function to arrange 
sorted_swap = sorted(swap_avg_by_hour, reverse = True)
print("Top 5 hours for Ask Posts Comments")

for i in range(0,5):
    hr_obj = dt.datetime.strptime(sorted_swap[i][1],"%H") # Assigns what is what
    hr_obj_string = dt.datetime.strftime(hr_obj, "%H:%M") #To final string
    avg = sorted_swap[i][0]
    template = '''
    {}: {:.2f} average comments per post    
    '''
    print(template.format(hr_obj_string,avg))