# [30DayMapChallenge](https://github.com/tjukanovt/30DayMapChallenge)

## 1 - [Points](https://felipedeaujaques.github.io/30daysmapchallenge/Points/qgis2web/index.html)

Map of table tennis locations from OSM

| Data  | Source |
|---|---|
|  Table tennis locations |  OSM data via https://overpass-turbo.eu/ |
| Streets of Frankfurt | https://raw.githubusercontent.com/frankfurt-gestalten/data/master/frankfurter_strassen.geojson |
| City districts of Frankfurt  | https://opendata-esri-de.opendata.arcgis.com/datasets/esri-de-content::stadtteile-frankfurt-am-main |
|   |   |

Overpass query:
```
{{geocodeArea:Frankfurt}}->.searchArea;
(
  node["leisure"="pitch"]["sport"="table_tennis"](area.searchArea);
  way["leisure"="pitch"]["sport"="table_tennis"](area.searchArea);
);
out body;
>;
out skel qt;
```

## 2 - [Lines](https://felipedeaujaques.github.io/30daysmapchallenge/Lines/OSMlinesFFM.png)

Exported OSM line geometries for bbox of central Frankfurt

| Data  | Source |
|---|---|
|  Line geometries |  OSM data via https://overpass-turbo.eu/ |

Overpass query:

```
[out:json][timeout:25];
(
  way({{bbox}});
);
out body;
>;
out skel qt;
```

## 3 - [Polygons](https://felipedeaujaques.github.io/30daysmapchallenge/Polygons/qgis2web/index.html)

Country polygons simplified in QGIS

| Data | Source |
|---|---|
| Country Polygons as GeoJSON | https://datahub.io/core/geo-countries/r/countries.geojson |
