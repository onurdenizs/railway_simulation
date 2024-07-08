import os

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd


def load_geojson_data(file_path):
    """Load GeoJSON data.

    Args:
        file_path (str): Path to the GeoJSON file.

    Returns:
        GeoDataFrame: Loaded GeoDataFrame.
    """
    return gpd.read_file(file_path)


def filter_line_data(line_data, line_id):
    """Filter the line data for a specific line ID.

    Args:
        line_data (GeoDataFrame): The GeoDataFrame containing the line data.
        line_id (int): The line ID to filter by.

    Returns:
        DataFrame: Filtered DataFrame containing only the specified line ID data.
    """
    return line_data[line_data["linienr"] == line_id][
        [
            "geo_point_2d",
            "x",
            "y",
            "km",
            "linienr",
            "linienr_km",
            "liniename",
            "geometry",
        ]
    ]


def load_csv_data(file_path):
    """Load CSV data.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        DataFrame: Loaded DataFrame.
    """
    return pd.read_csv(file_path)


def get_total_length(line_data):
    """Calculate the total length of the line segments.

    Args:
        line_data (DataFrame): The DataFrame containing the line segments data.

    Returns:
        float: Total length of the line segments.
    """
    return line_data["km"].sum()


def get_line_length_from_info(lines_info, line_id):
    """Get the line length from lines_info.csv for a specific line ID.

    Args:
        lines_info (DataFrame): The DataFrame containing the lines info.
        line_id (int): The line ID to get the length for.

    Returns:
        float or str: Line length if found, else "Not found".
    """
    line_info = lines_info[lines_info["line_id"] == line_id]
    return line_info["line_length"].values[0] if not line_info.empty else "Not found"


def plot_line_and_borders(switzerland_borders, line_segments, figure_path):
    """Plot the Switzerland borders and line segments.

    Args:
        switzerland_borders (GeoDataFrame): GeoDataFrame containing Switzerland borders.
        line_segments (GeoDataFrame): GeoDataFrame containing the line segments to plot.
        figure_path (str): Path to save the plot figure.
    """
    fig, ax = plt.subplots(figsize=(12, 12))
    switzerland_borders.plot(ax=ax, color="white", edgecolor="red")
    line_segments.plot(ax=ax, color="black")

    plt.title("Switzerland Borders with Railway Line (Line ID: 150)")
    ax.set_axis_off()

    plt.savefig(figure_path, bbox_inches="tight", format="jpeg")
    plt.show()


def main():
    """Main function to execute the script."""
    figures_dir = r"C:\PhD\Codes\railway_simulation\figures"
    os.makedirs(figures_dir, exist_ok=True)

    switzerland_borders = load_geojson_data(
        r"C:\PhD\Codes\railway_simulation\data\raw\gadm41_CHE_1.json"
    )
    line_data = load_geojson_data(
        r"C:\PhD\Codes\railway_simulation\data\raw\linienkilometrierung.geojson"
    )
    line_150_data = filter_line_data(line_data, 150)

    print("Individual segment lengths for line 150:")
    print(line_150_data["km"])

    total_length = get_total_length(line_150_data)

    lines_info_path = r"C:\PhD\Codes\railway_simulation\data\processed\lines_info.csv"
    lines_info = load_csv_data(lines_info_path)
    line_150_length_from_info = get_line_length_from_info(lines_info, 150)

    print("Rows related to line 150:")
    print(line_150_data)
    print(
        f"\nTotal length of line 150 from linienkilometrierung.geojson: {total_length} km"
    )
    print(
        f"Total length of line 150 from lines_info.csv: {line_150_length_from_info} km"
    )

    gdf_line_150 = gpd.GeoDataFrame(line_150_data, geometry="geometry", crs="EPSG:4326")
    figure_path = os.path.join(figures_dir, "switzerland_borders_with_line_150.jpeg")
    plot_line_and_borders(switzerland_borders, gdf_line_150, figure_path)


if __name__ == "__main__":
    main()
