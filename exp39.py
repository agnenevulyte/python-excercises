cities = {
    'Kaunas': 'KNS',
    'Vilnius': 'VLN',
    'Panevezys': 'PNVZ',
    'Klaipeda': 'KLP',
    'Jonava': 'JNV',
}

regions = {
    'KNS': 'Suvalkija',
    'VLN': 'Dzukija',
    'PNVZ': 'Aukstaitija',
    'KLP': 'Zemaitija',
    'JNV': 'Suvalkija'
}

# printing in which regions are cities
print '-' * 10
print "'KNS' city is in: ", regions['KNS']
print "'PNVZ' city is in: ", regions['PNVZ']

# printing some cities
print '-' * 10
print "Kaunas abbrevation is: ", cities['Kaunas']
print "Panevezys abbrevation is: ", cities['Panevezys']

# printing both together
print '-' * 10
print "Kaunas is in: ", regions[cities['Kaunas']]
print "Panevezys is in: ", regions[cities['Panevezys']]

# print every city abbreviation
print '-' * 10
for city, abbrev in cities.items():
    print "%s is abbreviated %s" % (city, abbrev)

# print every city abbreviation in region
print '-' * 10
for abbrev, region in regions.items():
    print "%s is in region %s" % (abbrev, region)

# now do both at the same time
print '-' * 10
for city, abbrev in cities.items():
    print "%s city abbreviation is %s and this city is in %s region" % (city, abbrev, regions[abbrev])