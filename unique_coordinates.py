import re

codes = {}
for i, line in enumerate(open("geo_undone.csv", 'rb').readlines()):
    matches = re.match('"(.+)",(.+),(.+)', line)
    if not matches:
        continue
    name, langt, longt = matches.group(1), matches.group(2), matches.group(3)
    key = langt + "," + longt
    codes[key] = codes.get(key, []) + [name]

print 'total number: ', len(codes.keys())
for key, val in codes.iteritems():
    if len(val) >1:
        print "     ", key, ": ", val
