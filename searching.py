import os
import json


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


def main():
    read_data("sequential.json", "unordered_numbers")


if __name__ == '__main__':
    main()