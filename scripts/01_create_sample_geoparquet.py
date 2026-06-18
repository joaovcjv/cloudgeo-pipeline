from pathlib import Path

import geopandas as gpd
from shapely.geometry import Point


output_path = Path("data/processed/sample_points.geoparquet")
output_path.parent.mkdir(parents=True, exist_ok=True)

data = {
    "id": [1, 2, 3],
    "name": ["Point A", "Point B", "Point C"],
    "category": ["education", "health", "transport"],
    "geometry": [
        Point(-8.6538, 40.6405),
        Point(-8.6500, 40.6420),
        Point(-8.6600, 40.6380),
    ],
}

gdf = gpd.GeoDataFrame(data, crs="EPSG:4326")

gdf.to_parquet(output_path)

print(f"GeoParquet created: {output_path}")
print(gdf)