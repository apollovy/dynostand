import collections
import random
import itertools


def get_input_data_generator():
    return data_gen()


def data_gen():
    counter = itertools.count(step=10)

    while True:
        random_data = [random.random() for _ in range(3)]
        yield InputData(*random_data[:2], next(counter), random_data[2])


InputData = collections.namedtuple('InputData', 'P, V, n, t')
