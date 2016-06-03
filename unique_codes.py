import re

codes = {}
for i, line in enumerate(open("postal_codes.csv", 'rb').readlines()):
    matches = re.match('"(.+)",(.+)', line)
    if not matches:
        continue
    name, postal_code = matches.group(1), matches.group(2).rstrip().replace(" ","")
    postal_code = postal_code
    codes[postal_code] = codes.get(postal_code, 0) + 1

print 'total number: ', len(codes.keys())
for key, val in codes.iteritems():
    print key, ": ", val
