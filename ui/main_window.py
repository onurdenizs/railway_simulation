import sys

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Railway Simulation UI")
        self.setGeometry(100, 100, 800, 600)

        self.canvas = FigureCanvas(plt.figure())
        self.initUI()

    def initUI(self):
        load_data_btn = QPushButton("Load Data", self)
        load_data_btn.clicked.connect(self.load_data)

        run_simulation_btn = QPushButton("Run Simulation", self)
        run_simulation_btn.clicked.connect(self.run_simulation)

        visualize_btn = QPushButton("Visualize", self)
        visualize_btn.clicked.connect(self.visualize)

        layout = QVBoxLayout()
        layout.addWidget(load_data_btn)
        layou
