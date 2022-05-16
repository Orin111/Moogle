import requests
import bs4
import urllib.parse
import collections
import crawl

#################################################################
# FILE : words_dict.py
# WRITER : orin pour , orin1 , 207377649
# EXERCISE : intro2cs2 ex6 2021
# DESCRIPTION:this file contain the 3 part of the ex
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

def get_counted_words(page_url, r_link):
    """

    :param page_url:
    :param r_link:
    :return:
    """
    response = requests.get(urllib.parse.urljoin(page_url, r_link))
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    words = []
    for p in soup.find_all("p"):
        content = str.split(p.text)
        words += content
    return words


def create_page_words_dict(page_url, r_link, words_dict):
    words = get_counted_words(page_url, r_link)
    counted_words = collections.Counter(words)
    for word in words:
        if word not in words_dict:
            words_dict[word] = {}
        words_dict[word][r_link] = counted_words[word]
    return words_dict


def create_words_dict(page_url, index):
    link_lst = crawl.create_links_list(index)
    words_dict1 = {}
    for link in link_lst:
        create_page_words_dict(page_url, link, words_dict1)
    return words_dict1


def words_dict(base_url, index_file, out_file):
    word_dic = create_words_dict(base_url, index_file)
    crawl.save_dict(out_file, word_dic)
