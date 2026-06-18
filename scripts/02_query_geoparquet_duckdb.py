import duckdb
from pathlib import Path
file_path = Path("data/processed/sample_points.geoparquet")
con = duckdb.connect()
query = f"""
SELECT
category,
COUNT(*) AS total
FROM read_parquet('{file_path.as_posix()}')
GROUP BY category
ORDER BY total DESC;
"""
result = con.execute(query).fetchdf()
print(result)