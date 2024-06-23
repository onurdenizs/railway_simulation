import pandas as pd

# Define the file paths
raw_data_path = "C:\\PhD\\Codes\\railway_simulation\\data\\raw\\linie.csv"
processed_data_path = (
    "C:\\PhD\\Codes\\railway_simulation\\data\\processed\\linie_cleaned.csv"
)

# Load the raw CSV data
df = pd.read_csv(raw_data_path, delimiter=";")

# Rename columns to match the dataset schema
df.columns = [
    "LineId",
    "LineName",
    "Start_OPK",
    "End_OPK",
    "KM_Start",
    "KM_End",
    "Stationierung_Anfang",
    "Stationierung_Ende",
    "GeoShape",
    "GeoPoint_2d",
]

# Split the GeoPoint_2d column into separate latitude and longitude columns
df[["Latitude", "Longitude"]] = df["GeoPoint_2d"].str.split(",", expand=True)
df["Latitude"] = df["Latitude"].astype(float)
df["Longitude"] = df["Longitude"].astype(float)

# Drop the original GeoPoint_2d column
df = df.drop(columns=["GeoPoint_2d"])

# Save the cleaned data to a new CSV file
df.to_csv(processed_data_path, index=False)

print(f"Cleaned data saved to {processed_data_path}")
