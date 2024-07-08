"""
Script to process and extract line information from a raw CSV file containing railway data.
This script reads the raw data, processes it, and saves the cleaned data into a new CSV file.
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
    df = pd.read_csv(file_path, delimiter=";")

    # Rename columns for easier access
    df.columns = [
        "station_abbr",
        "stop_name",
        "line_id",
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
    df = df.astype(
        {
            "station_abbr": "string",
            "stop_name": "string",
            "line_id": "string",
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
    return df


def group_and_aggregate_data(df):
    """
    Group by line_id and aggregate station abbreviations and Didok numbers.

    Args:
        df (pd.DataFrame): Cleaned dataframe.

    Returns:
        pd.DataFrame: Aggregated dataframe with line information.
    """
    lines_info = (
        df.groupby("line_id")
        .agg(
            {
                "line_name": "first",
                "km": "sum",
                "station_abbr": lambda x: ",".join(x.unique()),
                "didok": lambda x: ",".join(x.astype(str).unique()),
            }
        )
        .reset_index()
    )

    # Rename columns
    lines_info.columns = [
        "line_id",
        "line_name",
        "line_length",
        "line_station_abbrs",
        "line_station_didoks",
    ]

    # Set line_id as index
    lines_info = lines_info.set_index("line_id")
    return lines_info


def save_to_csv(df, output_path):
    """
    Save the dataframe to a CSV file.

    Args:
        df (pd.DataFrame): Dataframe to be saved.
        output_path (str): Path to save the CSV file.
    """
    df.to_csv(output_path, index=True)
    print(f"Cleaned data saved to {output_path}")


def main():
    # Define file paths
    raw_data_path = (
        r"C:\PhD\Codes\railway_simulation\data\raw\linie-mit-betriebspunkten.csv"
    )
    processed_data_path = (
        r"C:\PhD\Codes\railway_simulation\data\processed\lines_info.csv"
    )

    # Load and clean data
    station_data = load_and_clean_data(raw_data_path)

    # Group and aggregate data
    lines_info = group_and_aggregate_data(station_data)

    # Display the transformed information
    print(lines_info.head())

    # Save the cleaned data to a new CSV file
    save_to_csv(lines_info, processed_data_path)

    # Print summary information
    print(f"Number of unique lines: {len(lines_info)}")
    print(lines_info.info())
    print(f"Total number of rows in the dataframe: {len(lines_info)}")


if __name__ == "__main__":
    main()
