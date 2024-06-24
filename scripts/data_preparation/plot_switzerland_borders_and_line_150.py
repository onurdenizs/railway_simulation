import os

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# Create figures directory if it does not exist
figures_dir = r"C:\PhD\Codes\railway_simulation\figures"
os.makedirs(figures_dir, exist_ok=True)

# Load Switzerland borders data
switzerland_borders = gpd.read_file(
    r"C:\PhD\Codes\railway_simulation\data\raw\gadm41_CHE_1.json"
)

# Load line segments data from GeoJSON file
line_segments = gpd.read_file(
    r"C:\PhD\Codes\railway_simulation\data\processed\line_segments.geojson"
)

# Load station information
stations_info = pd.read_csv(
    r"C:\PhD\Codes\railway_simulation\data\processed\stations_info.csv"
)

# Extract the segments for line_id = 150
line_150_segments = line_segments[line_segments["line_id"] == 150]

# Extract station abbreviations for line_id = 150
line_150_stations = (
    line_150_segments[["start_station", "end_station"]]
    .melt(value_name="station_abbr")
    .drop(columns=["variable"])
    .drop_duplicates()
)

# Match stations with their geo locations from stations_info
stations_on_line_150 = pd.merge(line_150_stations, stations_info, on="station_abbr")

# Create GeoDataFrames
gdf_borders = gpd.GeoDataFrame(switzerland_borders)
gdf_stations = gpd.GeoDataFrame(
    stations_on_line_150,
    geometry=gpd.points_from_xy(
        stations_on_line_150.longitude, stations_on_line_150.latitude
    ),
)

# Plotting
fig, ax = plt.subplots(figsize=(12, 12))
gdf_borders.plot(ax=ax, color="white", edgecolor="red")
line_150_segments.plot(ax=ax, color="black")
gdf_stations.plot(ax=ax, color="blue", marker="o", markersize=5, label="Stations")

# Customize plot
plt.title("Switzerland Borders with Railway Line (Line ID: 150) and Stations")
plt.legend()
ax.set_axis_off()

# Save the figure as JPEG
figure_path = os.path.join(figures_dir, "switzerland_borders_with_line_150.jpeg")
plt.savefig(figure_path, bbox_inches="tight", format="jpeg")
plt.show()
