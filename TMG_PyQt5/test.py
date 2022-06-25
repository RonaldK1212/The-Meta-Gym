from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os
from random import randint

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        
        self.x = list(range(100))
        self.y = [randint(0,100) for _ in range(100)]
        pg.setConfigOptions(antialias=False)        
        pen = pg.mkPen(color=(255,255,0), width = 1.5)
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
        
    def update_plot_data(self):
        
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)
        
        self.y = self.y[1:]
        self.y.append(randint(0,100))
        
        self.data_line.setData(self.x, self.y)
        
app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())