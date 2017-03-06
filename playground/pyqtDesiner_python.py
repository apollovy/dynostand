import sets_serial
import random
import sys

import pyqtgraph as pg
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from pyqtgraph.Qt import QtCore

form_class = uic.loadUiType("obuchenie_grafic.ui")[0]  # вызываем файл

ydata = []
davlenie=[]
Vlitr=[]
#oboroti=[]
tata = [0] * 10

# a=pg.plot(x=xd,y=yd)
class MyWindowClass(QMainWindow, form_class):
    #_my_graph_obj = None

    def __init__(self, parent):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self._my_graph_obj = Mygrafic()
        a1 = self._my_graph_obj.widget
        #a2 = self._my_graph_obj.widget2
        self.box.addWidget(a1)
        #self.box.addWidget(a2)
        self.time = QtCore.QTimer()
        self.time.timeout.connect(self.Ddavlenie)
        self.time.start(0.1)

    def Ddavlenie(self) -> object:
        data = float(sets_serial.com4()[5:8])
        # data = random.random() * 10
        davlenie.append(data)
        self.PMPa.setText(str(davlenie))
        del davlenie[:]
class Mygrafic:
    def __init__(self):
        #self.widget= pg.plot()
        self.widget=pg.plot(ydata, clear=True)
        #self.wid2=self.widget.plot(Vlitr, clear=True)
        super().__init__()
        self.time = QtCore.QTimer()
        self.time.timeout.connect(self.graf)
        self.time.start(0.1)

    def graf(self):
        data = float(sets_serial.com4()[0:4])
        data2 = float(sets_serial.com4()[5:8])
        #data = random.random() * 10
        #data2 = random.random() * 5

        ydata.append(data)
        Vlitr.append(data2)

        self.widget.plot(x=ydata,y=Vlitr, clear=True)
        #wid2=self.widget.plot(Vlitr, clear=True)

        #del ydata[0]
        #del Vlitr[0]
        #del tata[0]




#rtr= float(sets_serial.com4()[0:4])
#print(rtr)
app = QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()

app.exec_()
