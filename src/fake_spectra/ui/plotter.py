from PySide6.QtWidgets import (QWidget, QVBoxLayout)
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    """
    Matplotlib canvas using Qt5Agg backend
    """
    def __init__(self, width=400, height=400):

        fig = Figure(figsize=(width, height))

        self.ax = fig.add_subplot()
        super().__init__(fig)

class BasicPlot(QWidget):
    def __init__(self, parent=None):
        super(BasicPlot, self).__init__(parent)
        self.setGeometry(0, 0, 400, 400)
        self.parent = parent

        self.layout = QVBoxLayout()
        self.canvas = MplCanvas()
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

       
