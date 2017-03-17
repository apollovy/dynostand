# import sets_serial
import random
import sys

import pyqtgraph as pg
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from pyqtgraph.Qt import QtCore

form_class = uic.loadUiType("../ui/obuchenie_grafic.ui")[0]  # вызываем файл

ydata = []
ydata2 = []
davlenie = [0] * 2
Vlitr = [0] * 1
oboroti = [0] * 2
oboroti_dvig = [0] * 2
celcia = [] * 1


# a=pg.plot(x=xd,y=yd)
class MyWindowClass(QMainWindow, form_class):
    # _my_graph_obj = None
    _my_cells = None

    def __init__(self, parent) -> object:
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self._my_graph_obj = Mygrafic()
        self._my_cells = myCells(self)

        a1 = self._my_graph_obj.widget
        self.box.addWidget(a1)

        # self._myCells_obj = myCells()
        # self._myCells_obj.Ddavlenie()
        # self.myCells_obj
        self.play.clicked.connect(self.start_cells)
        self.stop.clicked.connect(self.stop_timer)

    def Pplay(self):
        self._my_graph_obj = Mygrafic()
        a1 = self._my_graph_obj.widget
        self.box.addWidget(a1)
        # def Sstop (self):

    def start_cells(self):
        self._my_graph_obj.time.start(100)
        self._my_cells.time.start(100)

    def stop_timer(self):
        self._my_cells.time.stop()
        self._my_graph_obj.time.stop()


class Mygrafic():
    def __init__(self):
        self.widget = pg.plot()
        self.time = QtCore.QTimer()
        self.time.timeout.connect(self.graf)
        self.time.timeout.connect(self.graf2)

    def Pplay(self):
        self.time.start(0.1)

    def Sstop(self):
        self.time.stop()

    def graf(self):
        # data = float(sets_serial.com4()[0:4])
        # data2 = float(sets_serial.com4()[5:8])
        data = random.random() * 10
        ydata.append(data)
        self.widget.plot(ydata, pen='g')

    def graf2(self):
        data = random.random() * 5
        ydata2.append(data)
        self.widget.plot(ydata2, pen='r')

    def Sstop(self):
        self.time.stop()
        print('privet')


class myCells():
    _window = None

    def __init__(self, window):
        # self.PMPa.setText(str(111))
        self._window = window
        self.time = QtCore.QTimer()
        self.time.timeout.connect(self.Ddavlenie)
        self.time.timeout.connect(self.vVlitr)
        self.time.timeout.connect(self.Ccelcia)
        self.time.timeout.connect(self.Ooboroty)
        self.time.timeout.connect(self.Ooboroty_dvig)

    def _set_text(self, button_name, value):
        field = getattr(self._window, button_name)
        field.setText(str(value))

    def Ddavlenie(self):
        # data = float(sets_serial.com4()[5:8])
        data = random.random() * 10
        davlenie.append(data)
        self._set_text('PMPa', davlenie)
        del davlenie[:]
        # return a

    def vVlitr(self):
        # data = float(sets_serial.com4()[5:8])
        data = random.random() * 10
        Vlitr.append(data)
        self._set_text('VLS', Vlitr)
        del Vlitr[:]

    def Ccelcia(self):
        # data = float(sets_serial.com4()[5:8])
        data = random.random() * 10
        celcia.append(data)
        self._set_text('celcia', celcia)
        del celcia[:]

    def Ooboroty(self):
        # data = float(sets_serial.com4()[5:8])
        data = random.random() * 10
        oboroti.append(data)
        self._set_text('NObMin', oboroti)
        del oboroti[:]

    def Ooboroty_dvig(self):
        # data = float(sets_serial.com4()[5:8])
        data1 = 1

        try:
            k = float(self._read_text('k_NObMin'))
        except ValueError:
            k = 1
            self._set_text('k_NObMin', k)

        # data = float(self.NObMin.text())
        data = k * data1

        # oboroti_dvig.append(data)
        self._set_text('NObMin_Dvig', data)
        # del oboroti_dvig[:]

    def _read_text(self, field_name):
        field = getattr(self._window, field_name)
        return field.text()


# rtr= float(sets_serial.com4()[0:4])
# print(rtr)
app = QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()

app.exec_()
