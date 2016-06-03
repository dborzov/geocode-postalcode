import re

with open('names.csv', 'wb') as namefile:
    for line in open('geo_undone.csv', 'rb'):
        matches = re.match('"(.+)",(.+),(.+)', line)
        if not matches:
            continue
        full_name, langt, longt = matches.group(1), matches.group(2), matches.group(3)
        name = full_name.split(",")[-1]
        namefile.write('"{name}",{latt},{longt}\n'.format(name=name, latt=langt, longt=longt))
