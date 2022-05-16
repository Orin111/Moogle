import copy
import page_rank

#################################################################
# FILE : search.py
# WRITER : orin pour , orin1 , 207377649
# EXERCISE : intro2cs2 ex6 2021
# DESCRIPTION:this file contain the 4 part of the ex
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################


def search_words(query, words_dict_file):
    words_dict = page_rank.load_dict(words_dict_file)
    small_words_dict = {}
    words = str.split(query)
    for w in words:
        if w in words_dict:
            small_words_dict[w] = words_dict[w]
    return small_words_dict


def grade(query, words_dict_file, ranking_dict_file):
    small_words_dict = search_words(query, words_dict_file)
    ranking_dict = page_rank.load_dict(ranking_dict_file)
    grades = {}
    for link in ranking_dict:
        for word in small_words_dict:
            if small_words_dict.get(word).get(link):
                if grades.get(link):
                    grades[link].append(small_words_dict[word][link])
                else:
                    grades[link] = [small_words_dict[word][link]]
    return small_words_dict, ranking_dict, grades


def calculate_results(query, words_dict_file, ranking_dict_file, maxi):
    small_words_dict, ranking_dict, grades = \
        grade(query, words_dict_file, ranking_dict_file)
    result = copy.deepcopy(ranking_dict)
    for link in ranking_dict:
        if grades.get(link) and len(grades[link]) == len(small_words_dict):
            grades[link] = grades[link]
        else:
            del result[link]
    result = dict(sorted(result.items(), key=lambda item: item[1],
                               reverse=True)[:maxi])
    for link in result:
        result[link] = min(grades[link]) * result[link]
    return result


def search(query, words_dict_file, ranking_dict_file, maxi):
    result = calculate_results(query, words_dict_file, ranking_dict_file, maxi)
    result = sorted(result.items(), key=lambda item: item[1], reverse=True)
    for i in result:
        print(i[0] + " " + str(i[1]))

