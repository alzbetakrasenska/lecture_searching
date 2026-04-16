import os
import json
import math
from math import floor

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

def binary_searched(ordered_seq, searched_num):
    first_index = 0
    last_index = len(ordered_seq) - 1
    while len(ordered_seq) >= 1:
        middle_index = int(round((first_index + last_index) / 2, 2))
        if ordered_seq[middle_index] == searched_num:
            return middle_index
        elif ordered_seq[middle_index] < searched_num:
            first_index = middle_index + 1
        else:
            last_index = middle_index - 1
    return None




def main():
    sequence = read_data("sequential.json", "unordered_numbers")
    searched_num = 120

    ordered_seq = read_data("sequential.json", "ordered_numbers")
    print(binary_searched(ordered_seq, searched_num))
if __name__ == '__main__':
    main()