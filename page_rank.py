import pickle
import crawl

#################################################################
# FILE : page_rank.py
# WRITER : orin pour , orin1 , 207377649
# EXERCISE : intro2cs2 ex6 2021
# DESCRIPTION:this file contain the second part of the ex
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################


def load_dict(t_dict):
    """

    :param t_dict:
    :return:
    """
    with open(t_dict, 'rb') as file:
        dict1 = pickle.load(file)
    return dict1


def create_rank_dict(traffic, v):
    """

    :param traffic:
    :param v:
    :return:
    """
    r_dict = {}
    for link in traffic:
        r_dict[link] = v
    return r_dict


def rank_iterations(r_dict, traffic, iterations):
    for k in range(iterations):
        new_r_dict = create_rank_dict(traffic, 0)
        for i in traffic:
            for j in traffic[i]:
                total_sum = sum(traffic[i].values())
                new_r_dict[j] += r_dict[i] * (traffic[i][j] / total_sum)
        r_dict = new_r_dict
    return r_dict


def page_rank(iterations, dict_file, out_file):
    traffic_dict = load_dict(dict_file)
    rank_dict = create_rank_dict(traffic_dict, 1.0)
    rank = rank_iterations(rank_dict, traffic_dict, iterations)
    crawl.save_dict(out_file, rank)
