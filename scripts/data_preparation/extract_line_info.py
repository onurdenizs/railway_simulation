import pandas as pd

# Load the data
file_path = r"C:\PhD\Codes\railway_simulation\data\raw\linie-mit-betriebspunkten.csv"

# Read the CSV with the correct delimiter
station_data = pd.read_csv(file_path, delimiter=";")

# Rename columns for easier access (if needed)
station_data.columns = [
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
station_data = station_data.astype(
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

# Group by line_id and aggregate station abbreviations and Didok numbers
lines_info = (
    station_data.groupby("line_id")
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

# Display the transformed information
print(lines_info.head())

# Save the cleaned data to a new CSV file
lines_info.to_csv(
    r"C:\PhD\Codes\railway_simulation\data\processed\lines_info.csv",
    index=True,  # Save with index
)

# Print summary information
print(f"Number of unique lines: {len(lines_info)}")
print(lines_info.info())

# Print total number of rows
print(f"Total number of rows in the dataframe: {len(lines_info)}")
print(f"lines_info[line_station_didoks].head(): {lines_info["line_station_didoks"].head()}")
