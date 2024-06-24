import pandas as pd

# Load the dataset
file_path = r"C:\PhD\Codes\railway_simulation\data\processed\stations_info.csv"
stations_info = pd.read_csv(file_path)

# Count unique values for Didok numbers, station abbreviations, and station names
unique_didok = stations_info["didok"].nunique()
unique_abbr = stations_info["station_abbr"].nunique()
unique_name = stations_info["stop_name"].nunique()

print(f"Number of unique Didok numbers: {unique_didok}")
print(f"Number of unique station abbreviations: {unique_abbr}")
print(f"Number of unique station names: {unique_name}")

duplicate_didok = stations_info[stations_info.duplicated("didok", keep=False)]
print(duplicate_didok)
