import os
import json
from math import floor
from generators import unordered_sequence, ordered_sequence
import time
import random
import matplotlib.pyplot as plt


cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as file_obj:
        data = json.load(file_obj)
        if field in data.keys():
            return data[field]
        else:
            return None

def linear_search(sequence, searched_num):
    seq_dict = {
        "positions": [],
        "count": 0
    }
    for i, num in enumerate(sequence):
        if num == searched_num:
            seq_dict["count"] += 1
            seq_dict["positions"].append(i)
    return seq_dict

def binary_search(ordered_seq, searched_num):
    first_index = 0
    last_index = len(ordered_seq) - 1
    while first_index <= last_index:
        middle_index = int(round((first_index + last_index) / 2, 2))
        if ordered_seq[middle_index] == searched_num:
            return middle_index
        elif ordered_seq[middle_index] < searched_num:
            first_index = middle_index + 1
        else:
            last_index = middle_index - 1
    return None


def time_graph(sizes):

    linear_times = []
    binary_times = []
    set_times = []
    for i in range(len(sizes)):

        unordered_seq = unordered_sequence(sizes[i])
        searched_unordered = random.choice(unordered_seq)
        ordered_seq = ordered_sequence(sizes[i])
        searched_ordered = random.choice(ordered_seq)
        set_seq = set(ordered_seq)

        # unordered start
        start_unordered = time.perf_counter()

        linear_search(unordered_seq, searched_unordered)

        end_unordered = time.perf_counter()

        duration_unordered = end_unordered - start_unordered
        linear_times.append(duration_unordered)
        # unordered end

        start_ordered = time.perf_counter()

        binary_search(ordered_seq, searched_ordered)

        end_ordered = time.perf_counter()

        duration_ordered = end_ordered - start_ordered
        binary_times.append(duration_ordered)
        #ordered end

        start_set = time.perf_counter()

        if searched_ordered in set_seq:
            val = True

        end_set = time.perf_counter()

        duration_set = end_set - start_set
        set_times.append(duration_set)


    plt.plot(sizes, linear_times, label="linearni vyhledavani")
    plt.plot(sizes, binary_times, label="binarni vyhledavani")
    plt.plot(sizes, set_times, label="set")

    plt.legend()
    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas [s]")
    plt.title("cas pro ruzne velikosti vstupu")
    plt.show()
    # grafy odpovidaji teoretickym zavislostem, nekdy trochu "uskoci" graf linearni zavislosti

def main():
    sequence = read_data("sequential.json", "unordered_numbers")
    searched_num = 48
    linear_search(sequence, searched_num)
    ordered_seq = read_data("sequential.json", "ordered_numbers")
    binary_search(ordered_seq, searched_num)
    sizes = [100, 500, 1000, 5000, 10000]
    time_graph(sizes)
if __name__ == '__main__':
    main()