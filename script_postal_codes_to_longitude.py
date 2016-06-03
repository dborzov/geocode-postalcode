import requests
import re

API_URL = "http://geocoder.ca/?locate=%{}&geoit=xml&json=1"
with open('geo.csv', 'wb') as geofile:
    for i, line in enumerate(open("postal_codes.csv", 'rb').readlines()):
        matches = re.match('"(.+)",(.+)\r', line)
        name, postal_code = matches.group(1), matches.group(2)
        print ' geocoding {i} ({name})..'.format(i=i,name=name)
        import pdb; pdb.set_trace()
        response = requests.get(API_URL.format(postal_code))
        geofile.write('"{name}",{latt},{longt}\n'.format(name=name, latt=response.json()[u'latt'], longt=response.json()[u'longt']))
