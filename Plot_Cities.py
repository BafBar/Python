import urllib
import json
import googlemaps
from IPython.display import Image

city = raw_input('Enter City Name: ')
key = raw_input('Enter google API  geocode key: ')
key_sm = raw_input('Enter google API staticmap key: ')

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
attributes = {'address':city,'key':key}
    
url = serviceurl+urllib.urlencode(attributes)
uh = urllib.urlopen(url)
    
data = uh.read()
print 'Retrieved',len(data),'characters'

try: js = json.loads(data)
except: js = None
if 'status' not in js:
    print '==== Failure To Retrive ===='
    print data
        
    
#print json.dumps(js,indent=4)    

loca = {}
for result in range(len(js['results'])):
    lat = js['results'][result]['geometry']['location']['lat']
    lng = js['results'][result]['geometry']['location']['lng']
    address = js['results'][result]['formatted_address']
    loca[address] = (lat,lng)
    
def create_string(dict):
    string ='%7C'
    values = dict.values()
    for i in range(len(values)):
        lat = str(values[i][0])
        lng = str(values[i][1])
        string = string+lat+','+lng+'%7C'
    return(string)  

s = create_string(loca)

sm_url = 'https://maps.googleapis.com/maps/api/staticmap?'
url_sm = sm_url+'markers=color:red'+s
attribute = {"size":'900x900','key':key_sm}
url = url_sm+urllib.urlencode(attribute)

get_map_img = urllib.urlretrieve(url, "staticmap.png")

print("There is "+str(len(loca))+" cities called "+city)
for city in loca.keys():
    print(city)
    
print(url)

Image(filename="staticmap.png")