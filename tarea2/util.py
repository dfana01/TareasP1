from os import getpid
from psutil import Process
from matplotlib import pyplot as plt
from time import time
from string import ascii_letters
from random import choice, randint


N_REPETITION = 5
N_TIMES = 1000


def graph_men_and_time(data, title):
    """
    :param title
    :param data
        {
            "data": [
                (i, men, tm, z_men, x_time)
            ],
            "title": "Label"
        }
    """
    x_axis, y_men_axis, y_time_axis = [], [], []
    for i, men, tm, z_men, x_time in data:
        x_axis.append(i)
        y_time_axis.append(tm)
        y_men_axis.append(men)
    graph(x_axis, y_time_axis, title, "N", "Time")
    graph(x_axis, y_men_axis, title, "N", "Memory")


def graph(x, y, title, x_label, y_label):
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def get_current_ram():
    """
    :return ran memory in KB
    """
    return Process(getpid()) \
        .memory_info() \
        .rss


def get_current_time():
    """
    :return current time in second
    """
    return time()


def generate_range_numbers():
    return [i for i in range(0, N_TIMES)]


def get_avg(arr):
    return sum(arr) / len(arr)


def get_deviation(avg, arr):
    acc = 0
    for v in arr:
        acc += (v - avg) ** 2
    return (acc / (len(arr) - 1)) ** 0.5


def standardize_sample(dic_sample):
    sample = []
    for key, values in dic_sample.items():
        men_values = values[0]
        tm_values = values[1]

        avg_men = get_avg(men_values)
        dev_men = get_deviation(avg_men, men_values)

        avg_time = get_avg(tm_values)
        dev_time = get_deviation(avg_time, tm_values)

        sample.append((key, avg_men, avg_time, dev_men, dev_time))
    return sample


def with_rep_and_standardize(func, rep=N_REPETITION):
    sample = {}
    for _ in range(rep):
        func(sample)
    return standardize_sample(sample)


def add_to_sample(n, delta, men, sample):
    if n in sample:
        sample[n][0].append(men)
        sample[n][1].append(delta)
    else:
        sample[n] = [[men], [delta]]
    return sample


def get_random_str(size):
    s = size * "".join([choice(ascii_letters),
                        choice(ascii_letters),
                        choice(ascii_letters),
                        choice(ascii_letters)])
    return s[:size]


def random_number_between(start=0, end=N_TIMES):
    return randint(start, end)
