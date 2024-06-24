"""
Script to process railway line data from CSV and GeoJSON formats.
This script extracts specific columns and saves the processed data into new CSV and GeoJSON files.
"""

import geopandas as gpd
import pandas as pd


def load_and_process_csv(file_path):
    """
    Load and process CSV data.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Processed DataFrame.
    """
    data_csv = pd.read_csv(file_path, delimiter=";")
    print("CSV Data:")
    print(data_csv.head())

    lines_info_csv = data_csv[
        ["Linie", "Line", "TRACK GAUGE", "Geo point", "Geo shape"]
    ]
    print("Extracted CSV Data:")
    print(lines_info_csv.head())

    return lines_info_csv


def load_and_process_geojson(file_path):
    """
    Load and process GeoJSON data.

    Args:
        file_path (str): Path to the GeoJSON file.

    Returns:
        gpd.GeoDataFrame: Processed GeoDataFrame.
    """
    data_geojson = gpd.read_file(file_path)
    print("GeoJSON Data:")
    print(data_geojson.head())

    lines_info_geojson = data_geojson[["linienr", "liniename", "spurweite", "geometry"]]
    print("Extracted GeoJSON Data:")
    print(lines_info_geojson.head())

    return lines_info_geojson


def save_to_csv(data, file_path):
    """
    Save DataFrame to CSV file.

    Args:
        data (pd.DataFrame): Data to save.
        file_path (str): Path to save the CSV file.
    """
    data.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")


def save_to_geojson(data, file_path):
    """
    Save GeoDataFrame to GeoJSON file.

    Args:
        data (gpd.GeoDataFrame): Data to save.
        file_path (str): Path to save the GeoJSON file.
    """
    data.to_file(file_path, driver="GeoJSON")
    print(f"Data saved to {file_path}")


if __name__ == "__main__":
    # File paths to the data
    FILE_PATH_CSV = "C:/PhD/Codes/railway_simulation/data/raw/linie-mit-polygon.csv"
    FILE_PATH_GEOJSON = (
        "C:/PhD/Codes/railway_simulation/data/raw/linie-mit-polygon.geojson"
    )

    # Process CSV data
    lines_info_csv = load_and_process_csv(FILE_PATH_CSV)
    save_to_csv(
        lines_info_csv,
        "C:/PhD/Codes/railway_simulation/data/processed/lines_info_csv.csv",
    )

    # Process GeoJSON data
    lines_info_geojson = load_and_process_geojson(FILE_PATH_GEOJSON)
    save_to_geojson(
        lines_info_geojson,
        "C:/PhD/Codes/railway_simulation/data/processed/lines_info_geojson.geojson",
    )
