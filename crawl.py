import requests
import bs4
import urllib.parse
import collections
import pickle

#################################################################
# FILE : crawl.py
# WRITER : orin pour , orin1 , 207377649
# EXERCISE : intro2cs2 ex6 2021
# DESCRIPTION:this file contain the first part of the ex
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################


def create_traffic_dict(links_lst):
    """
    :param links_lst:a list of all relative links
    :return: a traffic dictionary with a key per link
    """
    traffic_dict = {}
    for link in links_lst:
        traffic_dict[link] = {}
    return traffic_dict


def get_links(r_link, links_lst, page_url):
    """
    :param page_url: a base url
    :param r_link: a relative link of a page
    :param links_lst: a list of all links
    :return: a list of all words in a page
    """
    response = requests.get(urllib.parse.urljoin(page_url, r_link))
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    links = []
    for p in soup.find_all("p"):
        for link in p.find_all('a'):
            target = link.get('href')
            if target in links_lst:
                links.append(target)
    return links


def count_page_reference(traffic_dict, r_link, links_lst, page_url):
    """

    :param page_url: a base url
    :param traffic_dict: a dictionary
    :param r_link:  a relative link of a page
    :param links_lst:  a list of all links
    :return: a dictionary of count references
    """
    references = get_links(r_link, links_lst, page_url)
    references_dict = {}
    # count references
    count_references = collections.Counter(references)
    # update count_references
    for r in count_references:
        traffic_dict[r_link][r] = traffic_dict[r_link].get(r, 0) + \
                                  count_references[r]
    return traffic_dict


def count_all_reference(links_doc, page_url):
    """
    :param links_doc:
    :param page_url:
    :return: a dict
    """
    links_lst = create_links_list(links_doc)
    traffic_dict = create_traffic_dict(links_lst)
    for page in links_lst:
        traffic_dict = count_page_reference(traffic_dict, page, links_lst,
                                            page_url)
    return traffic_dict


def create_links_list(file):
    """

    :param file:
    :return:
    """
    key_file = open(file)
    key_lst = []
    for line in key_file:
        key_lst.append(line.split()[0])
    return key_lst


def save_dict(out_file, dict2):
    with open(out_file, 'wb') as file:
        pickle.dump(dict2, file)


