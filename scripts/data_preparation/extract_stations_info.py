import pandas as pd

# Load the data
file_path = r"C:\PhD\Codes\railway_simulation\data\raw\linie.csv"

# Read the CSV with the correct delimiter
line_data = pd.read_csv(file_path, delimiter=";")

# Rename columns for easier access (if needed)
line_data.columns = [
    "LineId",
    "LineName",
    "Start_OPK",
    "End_OPK",
    "KM_START",
    "KM_END",
    "Extra1",
    "Extra2",
    "Extra3",
    "geo_point_2d",
]

# Extract relevant information
stations_info = line_data[["LineId", "LineName", "geo_point_2d"]].copy()

# Split geo_point_2d into latitude and longitude
stations_info[["Latitude", "Longitude"]] = stations_info["geo_point_2d"].str.split(
    ",", expand=True
)

# Convert Latitude and Longitude to float
stations_info["Latitude"] = stations_info["Latitude"].astype(float)
stations_info["Longitude"] = stations_info["Longitude"].astype(float)

# Drop the original geo_point_2d column
stations_info = stations_info.drop(columns=["geo_point_2d"])

# Display the extracted information
print(stations_info.head())

# Save the cleaned data to a new CSV file
stations_info.to_csv(
    r"C:\PhD\Codes\railway_simulation\data\processed\stations_info.csv", index=False
)
