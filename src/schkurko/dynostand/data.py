import collections
import random


def get_input_data_generator():
    return data_gen()


def data_gen():
    while True:
        random_gen = (random.random() for _ in range(4))
        yield InputData(*random_gen)


InputData = collections.namedtuple('InputData', 'P, V, n, t')
