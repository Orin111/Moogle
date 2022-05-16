# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import pickle
import collections


def load_t_dict(t_dict):
    """

    :param t_dict:
    :return:
    """
    with open(t_dict, 'rb') as file:
        traffic = pickle.load(file)
    return traffic


def create_rank_dict(t_dict, value):
    """

    :param value:
    :param t_dict:
    :return:
    """
    traffic = load_t_dict(t_dict)
    r_dict = {}
    for link in traffic:
        r_dict[link] = value
    return r_dict, traffic


def rank_iteration(r_dict, traffic):
    new_r_dict = create_rank_dict(traffic, 0.0)
    count_references = {}
    # for key, value in traffic.items():
    for i in traffic:
        for j in traffic[i]:
            new_r_dict[j] += r_dict[i] * (
                        traffic[i][j] / sum(traffic[i].values()))
    pass


# traffic_dict[l][r_link] = traffic_dict[l].get(r_link, 0) + \
#                           count_references[l]
iterations = 5
dict_file = 'traffic.pickle'
out_file = 'rank_pickle'
rank_dict, traffic_dict = create_rank_dict(dict_file, 1.0)
rank_iteration(rank_dict, traffic_dict)
