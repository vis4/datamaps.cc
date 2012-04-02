
from kartograph import Kartograph
from kartograph.errors import KartographError
from countryInfo import countries
from countryInfo import iso2latlon
import json

tpl = open('src/templates/admin1.json').read()
K = Kartograph()

for country in countries:
    iso = country['ISO3']
    print iso
    cfg = json.loads(tpl.replace('{{ ISO }}', iso))
    if iso in iso2latlon:
        (lat, lon) = iso2latlon[iso]
    else:
        lat = lon = 'auto'
    cfg['proj']['lat0'] = lat
    cfg['proj']['lon0'] = lon
    try:
        K.generate(cfg, 'maps/' + country['Continent'] + '/' + country['ISO3'] + '.svg')
    except KartographError, e:
        print e
