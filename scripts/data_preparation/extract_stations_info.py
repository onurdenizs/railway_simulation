import pandas as pd

# Load the data
file_path = r"C:\PhD\Codes\railway_simulation\data\raw\linie-mit-betriebspunkten.csv"

# Read the CSV with the correct delimiter
station_data = pd.read_csv(file_path, delimiter=";")

# Rename columns for easier access (if needed)
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
stations_info = station_data[
    ["station_abbr", "stop_name", "geo_position", "didok", "bpuic", "sloid"]
].copy()

# Split GeoPosition into latitude and longitude
stations_info[["latitude", "longitude"]] = (
    stations_info["geo_position"].str.strip("[]").str.split(",", expand=True)
)

# Convert Latitude and Longitude to float
stations_info["latitude"] = stations_info["latitude"].astype(float)
stations_info["longitude"] = stations_info["longitude"].astype(float)

# Drop the original GeoPosition column
stations_info = stations_info.drop(columns=["geo_position"])

# Filter out rows with non-unique Didok numbers
stations_info = stations_info.drop_duplicates(subset=["didok"])

# Display the filtered information
print(stations_info.head())

# Save the cleaned data to a new CSV file
stations_info.to_csv(
    r"C:\PhD\Codes\railway_simulation\data\processed\stations_info.csv",
    index=False,
)

# Print summary information
print(f"Number of unique Didok numbers: {stations_info['didok'].nunique()}")
print(
    f"Number of unique station abbreviations: {stations_info['station_abbr'].nunique()}"
)
print(f"Number of unique station names: {stations_info['stop_name'].nunique()}")
print(stations_info.info())

# Print total number of rows
print(f"Total number of rows in the dataframe: {len(stations_info)}")
