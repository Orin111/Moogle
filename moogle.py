import crawl
import page_rank
import words_dict
import search
import sys

#################################################################
# FILE : moogle.py
# WRITER : orin pour , orin1 , 207377649
# EXERCISE : intro2cs2 ex6 2021
# DESCRIPTION:this file contain the hmain file of moogle ex
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################


def main():
    if sys.argv[1] == "crawl":
        if len(sys.argv) == 5:
            # save all parameters
            base_url = sys.argv[2]
            index_file = sys.argv[3]
            out_file = sys.argv[4]
            dict1 = crawl.count_all_reference(index_file, base_url)
            crawl.save_dict(out_file, dict1)
        else:
            print("Error: please enter all variables")
    elif sys.argv[1] == "page_rank":
        if len(sys.argv) == 5:
            # save all parameters
            iterations = int(sys.argv[2])
            dict_file = sys.argv[3]
            out_file = sys.argv[4]
            page_rank.page_rank(iterations, dict_file, out_file)
        else:
            print("Error: please enter all variables")
    elif sys.argv[1] == "words_dict":
        if len(sys.argv) == 5:
            # save all parameters
            base_url = sys.argv[2]
            index_file = sys.argv[3]
            out_file = sys.argv[4]
            words_dict.words_dict(base_url, index_file, out_file)
        else:
            print("Error: please enter all variables")
    elif sys.argv[1] == 'search':
        if len(sys.argv) == 6:
            # save all parameters
            query = sys.argv[2]
            ranking_dict_file = sys.argv[3]
            words_dict_file = sys.argv[4]
            max_results = int(sys.argv[5])
            search.search(query, words_dict_file, ranking_dict_file,
                          max_results)


if __name__ == '__main__':
    main()
