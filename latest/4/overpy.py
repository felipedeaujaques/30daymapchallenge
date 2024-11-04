import requests
import numpy as np
import matplotlib.pyplot as plt

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json][timeout:30];
area[name="Deutschland"];
(node["generator:source"="wind"](area);
way["generator:source"="wind"](area);
relation["generator:source"="wind"](area);
);
out body;
>;
out skel qt;
"""

try:
    response = requests.post(overpass_url, data=overpass_query)
    response.raise_for_status()  # Check if the request was successful
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"HTTP Request failed: {e}")
except ValueError as e:
    print(f"JSON decoding failed: {e}")

coords = []

for element in data['elements']:
    if element['type'] == 'node':
        lon = element['lon']
        lat = element['lat']
        coords.append((lon, lat))
    elif 'center' in element:
        lon = element['center']['lon']
        lat = element['center']['lat']
        coords.append((lon, lat))

X = np.array(coords)
plt.hexbin(X[:, 0], X[:, 1], gridsize=15, cmap="Greens")
plt.colorbar()
plt.title('Wind Turbines in Germany')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis('equal')
plt.show()
