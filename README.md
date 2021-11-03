# 30daysmapchallenge

Link: https://github.com/tjukanovt/30DayMapChallenge

## 1 - Points

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