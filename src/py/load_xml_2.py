
from lib.aec import *

# importing element tree
import xml.etree.ElementTree as ET 
from xml.dom import minidom

filename = 'C:\\Users\\clair\\AEC\\24310\\Detailed\\Preload\\aec-mediafeed-Detailed-Preload-24310-20190517164959\\xml\\aec-mediafeed-pollingdistricts-24310.xml'


file = minidom.parse(filename)


#use getElementsByTagName() to get tag
models = file.getElementsByTagName('PollingDistrictList')

first = models.item(0)

print(first)

# get the parent tag 
#root = tree.getroot() 


# print the root (parent) tag along with its memory location 
#print(root.attrib) 
'''
# print the attributes of the first tag  
print(root[0].attrib) 

# print the text contained within first subtag of the 5th tag from the parent 
print(root[5][0].text) 

'''