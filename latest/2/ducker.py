import duckdb


def readFromOverture():
    con = duckdb.connect()
    con.install_extension("spatial")
    con.load_extension("spatial")
    con.install_extension("httpfs")
    con.load_extension("httpfs")
    con.sql(
        f"COPY ( SELECT * FROM read_parquet('s3://overturemaps-us-west-2/release/2024-10-23.0/theme=transportation/type=segment/*', union_by_name = True) "
        f"WHERE bbox.xmin >= 8.527655 "
        f"AND bbox.ymin >= 50.068935 "
        f"AND bbox.xmax <= 8.835788 "
        f"AND bbox.ymax <= 50.163709) TO 'ffm_segments.parquet'")

if __name__ == "__main__":
    readFromOverture()
