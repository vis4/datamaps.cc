
import csv

countryInfo_src = csv.reader(open('src/countryInfo.txt'), dialect='excel-tab')
head = countryInfo_src.next()
fips2iso = dict()
iso2cont = dict()
countries = []

for row in countryInfo_src:
    if len(row) > 0:
        c = dict()
        for h in range(len(head)):
            c[head[h]] = row[h]
        countries.append(c)
        fips = row[3]
        iso = row[1]
        cont = row[8]
        iso2cont[iso] = cont
        if fips != "":
            fips2iso[fips] = iso

s = csv.reader(open('src/country-center.csv'))
s.next()
iso2latlon = dict()
for iso, iso3, lat, lon in s:
    iso2latlon[iso3] = (float(lat), float(lon))
