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
- `figures/`: Directory to save generated figures.
- `src/`: Source code for data handling, visualization, and simulation.
  - `scripts/`: Python scripts for various tasks.
    - `data_preparation/`: Scripts for data loading and cleaning.
      - `clean_and_process_csv.py`: Script to clean and process raw CSV data.
      - `extract_line_info.py`: Script to extract line information.
      - `extract_line_segments.py`: Script to extract and process line segments.
      - `linie_mit_polygon_processing.py`: Script to process `linie-mit-polygon` data.
      - `extract_stations_info.py`: Script to extract station information.
      - `plot_new_line_segments.py`: Script to plot new line segments.
      - `plot_switzerland_borders_and_line_150.py`: Script to plot Switzerland borders and line segments for line ID 150.
  - `__init__.py`: Makes `src` a Python package.
- `tests/`: Unit tests for the project.
  - `test_sample.py`: Sample test file.
  - `__init__.py`: Makes `tests` a Python package.
- `ui/`: User interface components.
  - `main_window.py`: Main window script for the UI.
  - `test_pyqt5.py`: Script to test PyQt5 installation and setup.
- `.gitignore`: Files and directories to ignore in Git.
- `LICENSE`: Project license.
- `matplotlibrc`: Matplotlib configuration file.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies.

## Getting Started

### Prerequisites

Ensure you have Conda installed. If not, you can install it from [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

### Setting Up the Environment

1. **Clone the repository**:

    ```sh
    git clone https://github.com/onurdenizs/railway_simulation.git
    cd railway_simulation
    ```

2. **Create and activate the Conda environment**:

    ```sh
    conda create --name railway_env python=3.9
    conda activate railway_env
    ```

3. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run data preparation scripts to clean and process the data**:

    ```sh
    python src/scripts/data_preparation/clean_and_process_csv.py
    python src/scripts/data_preparation/extract_line_info.py
    python src/scripts/data_preparation/extract_line_segments.py
    python src/scripts/data_preparation/linie_mit_polygon_processing.py
    python src/scripts/data_preparation/extract_stations_info.py
    ```

### Running the Project

To run the main application or any specific scripts, use:

```sh
python src/<script_name>.py
