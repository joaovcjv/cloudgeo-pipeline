import duckdb

con = duckdb.connect()

con.execute("INSTALL spatial;")
con.execute("LOAD spatial;")

result = con.execute("SELECT ST_AsText(ST_Point(1, 2)) AS geom;").fetchall()

print("DuckDB Spatial OK")
print(result)