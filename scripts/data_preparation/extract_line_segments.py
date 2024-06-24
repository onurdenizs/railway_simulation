import geopandas as gpd
import pandas as pd
from shapely.geometry import shape

# Load the data
file_path = r"C:\PhD\Codes\railway_simulation\data\raw\linie-mit-polygon.csv"
line_data = pd.read_csv(file_path, delimiter=";")

# Rename columns for easier access (if needed)
line_data.columns = [
    "geo_point_2d",
    "geo_shape",
    "track_gauge",
    "segment_start",
    "segment_end",
    "start_station",
    "start_station_name",
    "end_station",
    "end_station_name",
    "line_id",
    "line_name",
]

# Extract relevant columns
line_segments = line_data[
    [
        "line_id",
        "line_name",
        "track_gauge",
        "segment_start",
        "segment_end",
        "geo_shape",
        "start_station",
        "end_station",
    ]
].copy()

# Convert to appropriate data types
line_segments["track_gauge"] = line_segments["track_gauge"].astype("category")
line_segments["geometry"] = line_segments["geo_shape"].apply(lambda x: shape(eval(x)))

# Sort by line_id and segment_start
line_segments = line_segments.sort_values(by=["line_id", "segment_start"])

# Save to CSV
line_segments.to_csv(
    r"C:\PhD\Codes\railway_simulation\data\processed\line_segments.csv", index=False
)

# Save to GeoJSON
gdf = gpd.GeoDataFrame(line_segments, geometry="geometry", crs="EPSG:4326")
gdf.to_file(
    r"C:\PhD\Codes\railway_simulation\data\processed\line_segments.geojson",
    driver="GeoJSON",
)

print(
    "Line segments saved to C:\\PhD\\Codes\\railway_simulation\\data\\processed\\line_segments.csv and C:\\PhD\\Codes\\railway_simulation\\data\\processed\\line_segments.geojson"
)

# Additional code to print line segment details
line_info = (
    line_segments.groupby("line_id")
    .agg(
        segments_count=("line_id", "count"),
        start_km=("segment_start", "min"),
        end_km=("segment_end", "max"),
    )
    .reset_index()
)

print("\nLine Segment Information:")
print(line_info)

# Print detailed information
for _, row in line_info.iterrows():
    print(
        f"Line ID: {row['line_id']}, Segments: {row['segments_count']}, Start KM: {row['start_km']}, End KM: {row['end_km']}"
    )
# Count the number of unique line IDs
unique_line_ids_count = line_segments["line_id"].nunique()

# Print the number of unique line IDs
print(f"\nNumber of unique line IDs: {unique_line_ids_count}")
