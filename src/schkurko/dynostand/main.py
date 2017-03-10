import functools

import PyQt5.uic
import pyqtgraph.Qt

from schkurko.dynostand.app import create_app, exec_app
from schkurko.dynostand.cells import cells_updater_factory, \
    get_our_cells, start_updating_cells
from schkurko.dynostand.data import get_input_data_generator
from schkurko.dynostand.window import create_window, show_window


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


def create_timer():
    return pyqtgraph.Qt.QtCore.QTimer()


if __name__ == '__main__':
    main()
