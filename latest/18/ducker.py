import duckdb


def readFromOverture():
    con = duckdb.connect()
    con.install_extension("spatial")
    con.load_extension("spatial")
    con.install_extension("httpfs")
    con.load_extension("httpfs")
    con.sql(
        f"COPY ( SELECT id, level, height, names.primary AS primary_name, "
        f"geometry "
        f"FROM read_parquet('s3://overturemaps-us-west-2/release/2024-11-13.0/theme=buildings/type=*/*', hive_partitioning=1) "
        f"WHERE bbox.xmin >= 8.527655 "
        f"AND bbox.ymin >= 50.068935 "
        f"AND bbox.xmax <= 8.835788 "
        f"AND bbox.ymax <= 50.163709 AND height > 0) TO 'ffm_buildings.geojson' (FORMAT GDAL, DRIVER 'GeoJSON') ")

if __name__ == "__main__":
    readFromOverture()
