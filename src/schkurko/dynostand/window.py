import PyQt5


def create_window(form_class):
    window_class = type(
        'MyMainWindow', (PyQt5.QtWidgets.QMainWindow, form_class), {})
    window = window_class()
    window.setupUi(window)

    return window


def show_window(window):
    window.show()
