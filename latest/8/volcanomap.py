import requests
import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.colors as mcolors

url = ("https://data.humdata.org/dataset/a60ac839-920d-435a-bf7d-25855602699d/resource/7234d067-2d74-449a-9c61"
       "-22ae6d98d928/download/volcano.json")

response = requests.get(url)
geojson_data = response.json()
gdf = gpd.GeoDataFrame.from_features(geojson_data["features"])
gdf['marker_size'] = gdf['PEI'].fillna(1) * 10
# Set up the color map
cmap = plt.cm.Reds  # Use the 'Reds' colormap for color variation
norm = mcolors.Normalize(vmin=gdf['PEI'].min(), vmax=gdf['PEI'].max())  # Normalize based on PEI range

# Set up the map using Cartopy
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_global()

# Add base features to the map
ax.add_feature(cfeature.LAND, edgecolor='black', zorder=0)
ax.add_feature(cfeature.OCEAN, color='lightblue', zorder=0)
ax.add_feature(cfeature.BORDERS, linestyle=':', zorder=1)
ax.add_feature(cfeature.COASTLINE, zorder=1)

# Plot volcanoes as points with color and size based on PEI
scatter = ax.scatter(
    gdf.geometry.x, gdf.geometry.y,
    c=gdf['PEI'], cmap=cmap, norm=norm,  # Color based on PEI
    s=gdf['marker_size'],  # Size based on PEI
    transform=ccrs.PlateCarree(),
    label="Volcano",
    alpha=0.7, edgecolor="k"
)

# Add a color bar for the PEI values
cbar = plt.colorbar(scatter, ax=ax, orientation='vertical', shrink=0.7, pad=0.05)
cbar.set_label('Population Exposure Index (PEI)')
plt.title("Volcanoes by Population Exposure Index", fontsize=15)
plt.legend()

plt.show()
