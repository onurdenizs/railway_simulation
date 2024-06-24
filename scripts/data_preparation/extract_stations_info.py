"""
Script to clean and process station information from the linie-mit-betriebspunkten dataset.
This script reads the raw data, processes it, and saves the cleaned data into a CSV file.
"""

import pandas as pd


def load_and_clean_data(file_path):
    """
    Load and clean the raw CSV data.

    Args:
        file_path (str): Path to the raw CSV file.

    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    # Read the CSV with the correct delimiter
    station_data = pd.read_csv(file_path, delimiter=";")

    # Rename columns for easier access
    station_data.columns = [
        "station_abbr",
        "stop_name",
        "line",
        "km",
        "line_name",
        "geo_position",
        "didok",
        "bpuic",
        "stop_name_duplicate",
        "lod",
        "sloid",
    ]

    # Convert columns to appropriate data types
    station_data = station_data.astype(
        {
            "station_abbr": "string",
            "stop_name": "string",
            "line": "int32",
            "km": "float32",
            "line_name": "string",
            "geo_position": "string",
            "didok": "int64",
            "bpuic": "int64",
            "stop_name_duplicate": "string",
            "lod": "string",
            "sloid": "string",
        }
    )

    # Extract relevant information
    stations_info_df = station_data[
        ["station_abbr", "stop_name", "geo_position", "didok", "bpuic", "sloid"]
    ].copy()

    # Split geo_position into latitude and longitude
    stations_info_df[["latitude", "longitude"]] = (
        stations_info_df["geo_position"].str.strip("[]").str.split(",", expand=True)
    )

    # Convert latitude and longitude to float
    stations_info_df["latitude"] = stations_info_df["latitude"].astype(float)
    stations_info_df["longitude"] = stations_info_df["longitude"].astype(float)

    # Drop the original geo_position column
    stations_info_df = stations_info_df.drop(columns=["geo_position"])

    # Filter out rows with non-unique Didok numbers
    stations_info_df = stations_info_df.drop_duplicates(subset=["didok"])

    return stations_info_df


def save_to_csv(stations_info_df, processed_data_path):
    """
    Save the cleaned data to a new CSV file.

    Args:
        stations_info_df (pd.DataFrame): DataFrame containing the station information.
        processed_data_path (str): Path to save the CSV file.
    """
    stations_info_df.to_csv(processed_data_path, index=False)
    print(f"Cleaned data saved to {processed_data_path}")


def print_summary(stations_info_df):
    """
    Print summary information about the cleaned data.

    Args:
        stations_info_df (pd.DataFrame): DataFrame containing the station information.
    """
    print(f"Number of unique Didok numbers: {stations_info_df['didok'].nunique()}")
    print(
        f"Number of unique station abbreviations: {stations_info_df['station_abbr'].nunique()}"
    )
    print(f"Number of unique station names: {stations_info_df['stop_name'].nunique()}")
    print(stations_info_df.info())

    # Print total number of rows
    print(f"Total number of rows in the dataframe: {len(stations_info_df)}")


if __name__ == "__main__":
    # File paths
    RAW_DATA_PATH = (
        r"C:\PhD\Codes\railway_simulation\data\raw\linie-mit-betriebspunkten.csv"
    )
    PROCESSED_DATA_PATH = (
        r"C:\PhD\Codes\railway_simulation\data\processed\stations_info.csv"
    )

    # Load and clean data
    stations_info_df = load_and_clean_data(RAW_DATA_PATH)

    # Save cleaned data to CSV
    save_to_csv(stations_info_df, PROCESSED_DATA_PATH)

    # Print summary information
    print_summary(stations_info_df)
