"""
Script to plot Switzerland borders, railway line segments, and stations.
This script processes the data and generates a plot for line_id 150, showing the line segments and stations on the map.
"""

import os

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd


def create_figures_directory(directory_path):
    """
    Create a directory if it does not exist.

    Args:
        directory_path (str): Path to the directory.
    """
    os.makedirs(directory_path, exist_ok=True)


def load_data():
    """
    Load necessary data for plotting.

    Returns:
        gpd.GeoDataFrame: Switzerland borders data.
        gpd.GeoDataFrame: Railway line segments data.
        pd.DataFrame: Stations information data.
    """
    switzerland_borders = gpd.read_file(
        r"C:\PhD\Codes\railway_simulation\data\raw\gadm41_CHE_1.json"
    )
    line_segments = gpd.read_file(
        r"C:\PhD\Codes\railway_simulation\data\processed\line_segments.geojson"
    )
    stations_info = pd.read_csv(
        r"C:\PhD\Codes\railway_simulation\data\processed\stations_info.csv"
    )

    return switzerland_borders, line_segments, stations_info


def extract_line_segments(line_segments, line_id):
    """
    Extract segments for a specific line_id.

    Args:
        line_segments (gpd.GeoDataFrame): DataFrame containing line segments.
        line_id (int): Line ID to filter.

    Returns:
        gpd.GeoDataFrame: Filtered line segments for the specified line_id.
    """
    return line_segments[line_segments["line_id"] == line_id]


def extract_stations_on_line(stations_info, line_segments):
    """
    Extract stations on a specific line based on line segments data.

    Args:
        stations_info (pd.DataFrame): DataFrame containing stations information.
        line_segments (gpd.GeoDataFrame): DataFrame containing line segments.

    Returns:
        pd.DataFrame: DataFrame containing stations on the specified line.
    """
    line_stations = (
        line_segments[["start_station", "end_station"]]
        .melt(value_name="station_abbr")
        .drop(columns=["variable"])
        .drop_duplicates()
    )
    return pd.merge(line_stations, stations_info, on="station_abbr")


def create_geodataframes(switzerland_borders, stations_on_line):
    """
    Create GeoDataFrames for plotting.

    Args:
        switzerland_borders (gpd.GeoDataFrame): DataFrame containing Switzerland borders.
        stations_on_line (pd.DataFrame): DataFrame containing stations on the specified line.

    Returns:
        gpd.GeoDataFrame: GeoDataFrame of Switzerland borders.
        gpd.GeoDataFrame: GeoDataFrame of stations on the specified line.
    """
    gdf_borders = gpd.GeoDataFrame(switzerland_borders)
    gdf_stations = gpd.GeoDataFrame(
        stations_on_line,
        geometry=gpd.points_from_xy(
            stations_on_line.longitude, stations_on_line.latitude
        ),
    )
    return gdf_borders, gdf_stations


def plot_data(gdf_borders, line_segments, gdf_stations, output_path):
    """
    Plot the data and save as JPEG.

    Args:
        gdf_borders (gpd.GeoDataFrame): GeoDataFrame of Switzerland borders.
        line_segments (gpd.GeoDataFrame): GeoDataFrame of line segments.
        gdf_stations (gpd.GeoDataFrame): GeoDataFrame of stations.
        output_path (str): Path to save the output JPEG file.
    """
    fig, ax = plt.subplots(figsize=(12, 12))
    gdf_borders.plot(ax=ax, color="white", edgecolor="red")
    line_segments.plot(ax=ax, color="black")
    gdf_stations.plot(ax=ax, color="blue", marker="o", markersize=5, label="Stations")

    plt.title("Switzerland Borders with Railway Line (Line ID: 150) and Stations")
    plt.legend()
    ax.set_axis_off()

    plt.savefig(output_path, bbox_inches="tight", format="jpeg")
    plt.show()


if __name__ == "__main__":
    # Define paths
    FIGURES_DIR = r"C:\PhD\Codes\railway_simulation\figures"
    OUTPUT_JPEG_PATH = os.path.join(
        FIGURES_DIR, "switzerland_borders_with_line_150.jpeg"
    )

    # Create figures directory
    create_figures_directory(FIGURES_DIR)

    # Load data
    switzerland_borders, line_segments, stations_info = load_data()

    # Extract line segments for line_id 150
    line_150_segments = extract_line_segments(line_segments, line_id=150)

    # Extract stations on line_id 150
    stations_on_line_150 = extract_stations_on_line(stations_info, line_150_segments)

    # Create GeoDataFrames
    gdf_borders, gdf_stations = create_geodataframes(
        switzerland_borders, stations_on_line_150
    )

    # Plot data and save as JPEG
    plot_data(gdf_borders, line_150_segments, gdf_stations, OUTPUT_JPEG_PATH)
