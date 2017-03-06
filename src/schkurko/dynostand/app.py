import sys

import PyQt5.QtWidgets


def create_app():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    return app


def exec_app(app):
    app.exec_()
