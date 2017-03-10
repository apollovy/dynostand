import typing
from collections import namedtuple

import pyqtgraph as pg


Graph = namedtuple('Graph', 'points')
Point = namedtuple('Point', 'x, y')


def plot_graphs(widget, graphs: typing.Iterable[Graph]):
    widget.plot(clear=True)

    for graph in graphs:
        xs, ys = graph.points
        widget.plot(x=xs, y=ys)


def create_and_add_plot_to_layout(layout):
    plot = pg.plot()
    layout.addWidget(plot)

    return plot
