import geopandas as gpd
import matplotlib.pyplot as plt
import osmnx as ox
import pandas as pd

print("Environment is set up correctly!")

# Example code to test libraries
G = ox.graph_from_place("Piedmont, California, USA", network_type="drive")
fig, ax = ox.plot_graph(G)

df = pd.DataFrame({"Column1": [1, 2], "Column2": [3, 4]})
print(df)
