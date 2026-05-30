from pathlib import Path
import json

#Read data as a string and convert to a python object
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# path = Path('eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents, encoding='utf-8')

all_eq_dicts = all_eq_data['features']
#print(f'Total number of earthquakes in 24Hr: {len(all_eq_dicts)}')

#Extracting magnitudes, longitudes, and latitudes of earthquakes
mags, lons, lats = [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

