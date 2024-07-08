# Railway Simulation

This project aims to simulate railway networks, focusing initially on the Swiss railway network, and potentially expanding to other countries' networks. The simulation will model railway vehicle movements with and without virtual coupling.

## Project Structure

- `data/`: Contains raw and processed datasets.
  - `raw/`: Raw datasets from various sources.
    - `linie.csv`: Raw line data.
    - `linie-mit-betriebspunkten.csv`: Raw station and line segment data.
    - `linie-mit-polygon.csv`: Raw line segment data with polygons.
    - `gadm41_CHE_1.json`: GeoJSON for Switzerland borders.
    - `gadm41_CHE_3.json`: Detailed GeoJSON for Switzerland borders.
  - `processed/`: Cleaned and processed datasets ready for analysis.
    - `linie_cleaned.csv`: Cleaned line data.
    - `lines_info.csv`: Aggregated line information.
    - `line_segments.csv`: Processed line segments data.
    - `line_segments.geojson`: GeoJSON for line segments.
    - `stations_info.csv`: Processed station information.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and prototyping.
- `scripts/`: Python scripts for various tasks.
  - `data_preparation/`: Scripts for data loading and cleaning.
    - `clean_and_process_csv.py`: Script to clean and process raw CSV data.
    - `extract_line_info.py`: Script to extract line information.
    - `extract_line_segments.py`: Script to extract and process line segments.
    - `linie_mit_polygon_processing.py`: Script to process `linie-mit-polygon` data.
    - `extract_stations_info.py`: Script to extract station information.
  - `visualization/`: Scripts for visualizing data.
    - `plot_switzerland_borders_and_line_150.py`: Script to plot Switzerland borders and line segments for line ID 150.
- `src/`: Source code for data handling, visualization, and simulation.
  - `data/`: Data handling functions.
  - `visualization/`: Visualization functions.
  - `simulation/`: Simulation functions.
- `tests/`: Unit tests for the project.
- `figures/`: Directory to save generated figures.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies.
- `.gitignore`: Files and directories to ignore in Git.

## Getting Started

1. **Clone the repository**:
   ```sh
   git clone https://github.com/onurdenizs/railway_simulation.git
   cd railway_simulation

2. **Set up the virtual environment and install dependencies**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
3. **Run data preparation scripts to clean and process the data**:
   ```sh
   python scripts/data_preparation/clean_and_process_csv.py
   python scripts/data_preparation/extract_line_info.py
   python scripts/data_preparation/extract_line_segments.py
   python scripts/data_preparation/linie_mit_polygon_processing.py
   python scripts/data_preparation/extract_stations_info.py

## Contributing
If you would like to contribute to this project, please fork the repository and use a feature branch. Pull requests are welcome.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please contact [onurdnz@gmail.com].
