import xmlschema
from pprint import pprint
import xml.etree.ElementTree as ET


schemafile = 'C:\\Users\\clair\\AEC\\24310\\Detailed\\Preload\\aec-mediafeed-Detailed-Preload-24310-20190517164959\\schema\\AEC\\aec-mediafeed-pollingdistricts-v3-0.xsd'
filename = 'C:\\Users\\clair\\AEC\\24310\\Detailed\\Preload\\aec-mediafeed-Detailed-Preload-24310-20190517164959\\xml\\aec-mediafeed-pollingdistricts-24310.xml'


xs = xmlschema.XMLSchema(schemafile)

data = xs.to_dict(filename)




events = []
polling_districts = []
polling_places = []

polling_district_list = data['PollingDistrictList']

event = {}
event['Id'] = polling_district_list['eml:EventIdentifier']['@Id']
event['Name'] = polling_district_list['eml:EventIdentifier']['eml:EventName']

for district in polling_district_list['PollingDistrict']:
    polling_district = {}
    polling_district['Id'] = district['PollingDistrictIdentifier']['@Id']
    polling_district['Event_Id'] = district['PollingDistrictIdentifier']['@Id']
    polling_district['ShortCode'] = district['PollingDistrictIdentifier']['@ShortCode']
    polling_district['Name'] = district['PollingDistrictIdentifier']['Name']
    polling_district['State_Code'] = district['PollingDistrictIdentifier']['StateIdentifier']['@Id']
    polling_district['NameDerivation'] = district['NameDerivation']
    polling_district['ProductsIndustry'] = district['ProductsIndustry']
    polling_district['Location'] = district['Location']
    polling_district['Demographic'] = district['Demographic']
    polling_district['Area'] = district['Area']

    for place in district['PollingPlaces']['PollingPlace']:
        polling_place = {}
        polling_place['Id'] = place['PollingPlaceIdentifier']['@Id']
        polling_place['Name'] = place['PollingPlaceIdentifier']['@Name']
        polling_place['EventId'] = event['Id']
        polling_place['DistrictId'] = polling_district['Id']
        polling_place['Channel'] = place['@Channel']
        polling_place['PhysicalLocationId'] = place['eml:PhysicalLocation']['@Id']
        polling_place['datum'] = place['eml:PhysicalLocation']['eml:Address']['xal:PostalServiceElements']['@Type']
        polling_place['lat'] = place['eml:PhysicalLocation']['eml:Address']['xal:PostalServiceElements']['xal:AddressLatitude']
        polling_place['lon'] = place['eml:PhysicalLocation']['eml:Address']['xal:PostalServiceElements']['xal:AddressLongitude']
        polling_place['address'] = place['eml:PhysicalLocation']['eml:Address']['xal:AddressLines']['xal:AddressLine']

        polling_places.append(polling_place)        

    polling_districts.append(polling_district)




events.append(event)

print(len(events))
print(len(polling_districts))
print(len(polling_places))

#pprint(data)



#tree = ET.parse(filename)
#root = tree.getroot()

#polling_district_list = root.findAll('PollingDistrictList')

#print(polling_district_list)