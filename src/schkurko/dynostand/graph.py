import collections
import functools
import random

import PyQt5.QtWidgets
import PyQt5.uic
import pyqtgraph.Qt

from schkurko.dynostand.app import create_app, exec_app

OUR_NAMES = ('PMPa', 'VLS', 'NObMin', 'celcia')
UPDATE_TIME_INTERVAL = 1000 * 0.5  # in milliseconds


def main():
    app = create_app()
    _ = create_payload()
    exec_app(app)


def create_payload():
    form_class = get_form_class()
    window = create_window(form_class)
    input_data_generator = get_input_data_generator()
    cells = tuple(get_our_cells(window))
    cells_updater = functools.partial(
        cells_updater_factory, cells, input_data_generator)
    timer = create_timer()
    start_updating_cells(timer, cells_updater)
    show_window(window)

    return window, timer


def get_form_class():
    form_class = PyQt5.uic.loadUiType("../../../ui/obuchenie_grafic.ui")[0]

    return form_class


def create_window(form_class):
    window_class = type(
        'MyMainWindow', (PyQt5.QtWidgets.QMainWindow, form_class), {})
    window = window_class()
    window.setupUi(window)

    return window


def get_our_cells(window):
    return get_cells(window, OUR_NAMES)


def cells_updater_factory(cells, input_data_generator):
    input_data = next(input_data_generator)
    return fill_cells(cells, input_data)


def create_timer():
    return pyqtgraph.Qt.QtCore.QTimer()


def start_updating_cells(timer, cells_updater):
    timer.timeout.connect(cells_updater)
    timer.start(UPDATE_TIME_INTERVAL)


def show_window(window):
    window.show()


def get_input_data_generator():
    return data_gen()


def fill_cells(cells, input_data):
    for cell, data in zip(cells, input_data):
        cell.setText(str(data))


def get_cells(window, names):
    for name in names:
        yield getattr(window, name)


def data_gen():
    while True:
        random_gen = (random.random() for _ in range(4))
        yield InputData(*random_gen)


InputData = collections.namedtuple('InputData', 'P, V, n, t')

if __name__ == '__main__':
    main()
