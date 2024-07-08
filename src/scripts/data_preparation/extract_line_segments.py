"""
Script to extract and process line segments from the linie-mit-polygon dataset.
This script reads the raw data, processes it, and saves the cleaned data into CSV and GeoJSON files.
"""

import geopandas as gpd
import pandas as pd
from shapely.geometry import shape


def load_and_clean_data(file_path):
    """
    Load and clean the raw CSV data.

    Args:
        file_path (str): Path to the raw CSV file.

    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    # Read the CSV with the correct delimiter
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
    line_segments["geometry"] = line_segments["geo_shape"].apply(
        lambda x: shape(eval(x))
    )

    # Sort by line_id and segment_start
    line_segments = line_segments.sort_values(by=["line_id", "segment_start"])

    return line_segments


def save_to_files(line_segments, csv_path, geojson_path):
    """
    Save the line segments to CSV and GeoJSON files.

    Args:
        line_segments (pd.DataFrame): DataFrame containing the line segments.
        csv_path (str): Path to save the CSV file.
        geojson_path (str): Path to save the GeoJSON file.
    """
    # Save to CSV
    line_segments.to_csv(csv_path, index=False)

    # Save to GeoJSON
    gdf = gpd.GeoDataFrame(line_segments, geometry="geometry", crs="EPSG:4326")
    gdf.to_file(geojson_path, driver="GeoJSON")


def print_line_info(line_segments):
    """
    Print detailed information about the line segments.

    Args:
        line_segments (pd.DataFrame): DataFrame containing the line segments.
    """
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


if __name__ == "__main__":
    # File paths
    raw_data_path = r"C:\PhD\Codes\railway_simulation\data\raw\linie-mit-polygon.csv"
    processed_csv_path = (
        r"C:\PhD\Codes\railway_simulation\data\processed\line_segments.csv"
    )
    processed_geojson_path = (
        r"C:\PhD\Codes\railway_simulation\data\processed\line_segments.geojson"
    )

    # Load and clean data
    line_segments = load_and_clean_data(raw_data_path)

    # Save cleaned data to files
    save_to_files(line_segments, processed_csv_path, processed_geojson_path)

    print(f"Line segments saved to {processed_csv_path} and {processed_geojson_path}")

    # Print additional line segment details
    print_line_info(line_segments)

    # Count the number of unique line IDs
    unique_line_ids_count = line_segments["line_id"].nunique()

    # Print the number of unique line IDs
    print(f"\nNumber of unique line IDs: {unique_line_ids_count}")
