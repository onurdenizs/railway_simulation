# File: scripts/data_preparation/linie_mit_polygon_processing.py

import geopandas as gpd
import pandas as pd

# File paths to the data
file_path_csv = "C:/PhD/Codes/railway_simulation/data/raw/linie-mit-polygon.csv"
file_path_geojson = "C:/PhD/Codes/railway_simulation/data/raw/linie-mit-polygon.geojson"

# Load the CSV data
data_csv = pd.read_csv(file_path_csv, delimiter=";")

# Display the first few rows of the CSV data
print("CSV Data:")
print(data_csv.head())

# Extract specific columns for further processing from CSV
lines_info_csv = data_csv[["Linie", "Line", "TRACK GAUGE", "Geo point", "Geo shape"]]
print("Extracted CSV Data:")
print(lines_info_csv.head())

# Save the extracted information to a new CSV file
lines_info_csv.to_csv(
    "C:/PhD/Codes/railway_simulation/data/processed/lines_info_csv.csv", index=False
)

# Load the GeoJSON data
data_geojson = gpd.read_file(file_path_geojson)

# Display the first few rows of the GeoJSON data
print("GeoJSON Data:")
print(data_geojson.head())

# Extract specific columns for further processing from GeoJSON
lines_info_geojson = data_geojson[["linienr", "liniename", "spurweite", "geometry"]]
print("Extracted GeoJSON Data:")
print(lines_info_geojson.head())

# Save the extracted information to a new GeoJSON file
lines_info_geojson.to_file(
    "C:/PhD/Codes/railway_simulation/data/processed/lines_info_geojson.geojson",
    driver="GeoJSON",
)
