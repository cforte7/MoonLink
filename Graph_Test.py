import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas)

    


class MatplotlibWidget(FigureCanvas):
    def __init__(self, parent=None, title='Title', xlabel='x label', ylabel='y label', dpi=100, hold=False):
        super(MatplotlibWidget, self).__init__(Figure())       
        self.setParent(parent)
        self.figure = Figure(dpi=dpi)
        self.canvas = FigureCanvas(self.figure)

        self.theplot = self.figure.add_subplot(111)
        self.theplot.set_title(title)
        self.theplot.set_xlabel(xlabel)
        self.theplot.set_ylabel(ylabel)


    def plotChart(self,oOxyName):
        print("DoStuff")     

test = MatplotlibWidget()
#if __name__ == '__main__':
	#pass
    #app = QtGui.QApplication(sys.argv)
    #main = Terminal()
    #main.show()

    #app.exec_()