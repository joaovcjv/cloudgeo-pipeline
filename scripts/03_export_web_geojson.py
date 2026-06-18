from pathlib import Path
import geopandas as gpd
input_path = Path("data/processed/sample_points.geoparquet")
output_path = Path("dist/data/sample_points.geojson")
output_path.parent.mkdir(parents=True, exist_ok=True)
gdf = gpd.read_parquet(
input_path,
columns=["id", "name", "category", "geometry"]
)
gdf.to_file(output_path, driver="GeoJSON")
print(f"Web GeoJSON created: {output_path}")