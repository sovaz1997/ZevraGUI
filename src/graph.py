from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class GraphView(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.initUI()
    
    def initUI():
        pass
