import re
import json
from mapbox import Static

service = Static()

points = []
for line in open('names.csv', 'rb'):
    matches = re.match('"(.+)",(.+),(.+)', line)
    if not matches:
        continue
    name, langt, longt = matches.group(1), matches.group(2), matches.group(3)
    points.append({
        'type': 'Feature',
        'properties': {'name': name},
        'geometry': {
            'type': 'Point',
            'coordinates': [float(longt),float(langt)]}
    })


with open('looool.geojson', 'wb') as output:
    j = json.dumps({'type': 'FeatureCollection', 'features': points}, separators=(',', ':'))
    output.write(j)
