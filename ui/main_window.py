import sys

from flask import Flask
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QApplication, QLabel

print("Starting the application...")

app = QApplication(sys.argv)
print("Application created successfully...")

label = QLabel("Hello, PyQt5!")
label.show()
print("Label created and shown successfully...")

fig = Figure()
canvas = FigureCanvas(fig)
canvas.show()
print("FigureCanvas created successfully...")

print("Entering the application event loop...")
sys.exit(app.exec_())
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
