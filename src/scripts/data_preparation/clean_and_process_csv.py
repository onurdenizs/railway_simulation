"""
This module cleans and processes raw railway line CSV data.

The script reads raw CSV data, renames columns to match the dataset schema,
splits the GeoPoint_2d column into separate latitude and longitude columns, and
saves the cleaned data to a new CSV file.
"""

import pandas as pd


def clean_and_process_csv(raw_data_path, processed_data_path):
    """
    Cleans and processes the raw CSV data.

    This function reads the raw CSV data, renames columns to match the dataset schema,
    splits the GeoPoint_2d column into separate latitude and longitude columns, and
    saves the cleaned data to a new CSV file.

    Args:
        raw_data_path (str): The file path of the raw CSV data.
        processed_data_path (str): The file path where the processed CSV data will be saved.

    Returns:
        None
    """
    # Load the raw CSV data
    df = pd.read_csv(raw_data_path, delimiter=";")

    # Rename columns to match the dataset schema
    df.columns = [
        "line_id",
        "line_name",
        "start_opk",
        "end_opk",
        "km_start",
        "km_end",
        "stationierung_anfang",
        "stationierung_ende",
        "geo_shape",
        "geo_point_2d",
    ]

    # Split the geo_point_2d column into separate latitude and longitude columns
    df[["latitude", "longitude"]] = df["geo_point_2d"].str.split(",", expand=True)
    df["latitude"] = df["latitude"].astype(float)
    df["longitude"] = df["longitude"].astype(float)

    # Drop the original geo_point_2d column
    df = df.drop(columns=["geo_point_2d"])

    # Save the cleaned data to a new CSV file
    df.to_csv(processed_data_path, index=False)

    print(f"Cleaned data saved to {processed_data_path}")


if __name__ == "__main__":
    # Define the file paths
    RAW_DATA_PATH = "C:\\PhD\\Codes\\railway_simulation\\data\\raw\\linie.csv"
    PROCESSED_DATA_PATH = (
        "C:\\PhD\\Codes\\railway_simulation\\data\\processed\\linie_cleaned.csv"
    )

    # Execute the cleaning and processing function
    clean_and_process_csv(RAW_DATA_PATH, PROCESSED_DATA_PATH)
