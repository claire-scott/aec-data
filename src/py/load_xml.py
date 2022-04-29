from bs4 import BeautifulSoup
from xml.dom import minidom

 
# Reading the data inside the xml
# file to a variable under the name
# data

filename = 'C:\\Users\\clair\\AEC\\24310\\Detailed\\Preload\\aec-mediafeed-Detailed-Preload-24310-20190517164959\\xml\\aec-mediafeed-pollingdistricts-24310.xml'

with open(filename, 'r') as f:
    data = f.read()

# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object
Bs_data = BeautifulSoup(data, "lxml")

# Finding all instances of tag
# `unique`
district_list = Bs_data.find_all('MediaFeed')

print(district_list)

'''
# Using find() to extract attributes
# of the first instance of the tag
b_name = Bs_data.find('child', {'name':'Frank'})
 
print(b_name)
 
# Extracting the data stored in a
# specific attribute of the
# `child` tag
value = b_name.get('test')
 
print(value)
'''