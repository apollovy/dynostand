def cells_updater_factory(cells, input_data_generator):
    input_data = next(input_data_generator)
    return fill_cells(cells, input_data)


def fill_cells(cells, input_data):
    for cell, data in zip(cells, input_data):
        cell.setText(str(data))


def get_cells(window, names):
    for name in names:
        yield getattr(window, name)


OUR_NAMES = ('PMPa', 'VLS', 'NObMin', 'celcia')


def get_our_cells(window):
    return get_cells(window, OUR_NAMES)


UPDATE_TIME_INTERVAL = 1000 * 0.5  # in milliseconds


def start_updating_cells(timer, cells_updater):
    timer.timeout.connect(cells_updater)
    timer.start(UPDATE_TIME_INTERVAL)
