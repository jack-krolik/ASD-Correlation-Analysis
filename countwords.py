#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jack Krolik 
File Function: Create a graph for outlets demonstrating usage of abelist to 
non-abelist terms
4/27/22

"""

import matplotlib.pyplot as plt


def read_sentiment_words(filename):
    '''
    Function: Read file lines into a list
    Parameters: filename (string)
    Returns: returns lines of the given file in a list
    '''
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    return [w.strip() for w in lines]

def get_article(filename):
    '''
    Function: reads an article into a list of sentences
    Parameters: filename (string)
    Returns: a list of the articles sentences (list)
    '''
    with open(filename, 'r', encoding = "utf8", errors='ignore') as file:
        data = file.read()
        
        return data.split(".")

def clean_article(lst):
    '''
    Function: removes all uneccessary punctuation from article 
    Parameters: list of article sentences
    Returns: a list of the cleaned sentences
    '''
    non_letters = "0123456789!@#$%^©„â¢&™*()_|+-=';:.,></?\""
    
    for string_index in range(len(lst)):
        lst[string_index] =  lst[string_index].lower()
        lst[string_index] =  lst[string_index].replace("\n", " ")\
            .replace("\t", " ")
        for char in lst[string_index]:
            if char in non_letters:
                lst[string_index] = lst[string_index].replace(char, "")
                
    cleaned_article = []
    for string in lst:
        if string != "" or " ":
            cleaned_article.append(string.strip())
            
    return cleaned_article

def add_articles_to_dict(news_dict, num_articles, directory = ''):
    '''
    Function: add articles to a dictionary as values
    Parameters: dictionary, number of articles (num), & directory (string) 
    Returns: a dictionary that containes the same keys as the 
    parameter dictionary and value as list of articles
    '''
    for site in news_dict:       
        for num in range(1,(num_articles + 1)):
            article = get_article(directory + site + str(num) + '.txt' )
            cleaned_article = clean_article(article)
            news_dict[site].append(cleaned_article)
            
    return news_dict

def count_poswords(articles):
    '''
    Function: counts the # of alternative words to albeist terms in an article
    Parameters: articles (list)
    Returns: list of the most popular alternative albeist terms 
    and the number of times they occur in the article (list of tuples)
    '''
    pos = read_sentiment_words('positive.txt')
    pos_dict = {}
    pop_poswords = []
    for article in articles: 
        for sentence in article:
            for word in pos:
                if word not in pos_dict:
                    pos_dict[word] = 0
                
                if word in sentence:
                    pos_dict[word] += 1
                    
    sorted_dict = sorted(pos_dict.items(), key = lambda x: x[1], \
                         reverse = True)
    for tup in sorted_dict:
        if tup[1] != 0:
            pop_poswords.append(tup)
    return pop_poswords
            
def count_negwords(articles):
    '''
    Function: counts the # of albeist terms in an article
    Parameters: articles (list)
    Returns: list of the most popular albeist terms and the number of times 
    they occur in the article (list of tuples)
    '''
    neg = read_sentiment_words('negative.txt')
    neg_dict = {}
    pop_negwords = []
    for article in articles: 
        for sentence in article:
            for word in neg:
                if word not in neg_dict:
                    neg_dict[word] = 0
                if word in sentence:
                   neg_dict[word] +=1
                   
    sorted_dict = sorted(neg_dict.items(), key = lambda x: x[1], \
                         reverse = True)              
    for tup in sorted_dict:
        if tup[1] != 0:
            pop_negwords.append(tup)

    
    return pop_negwords
    
def words_dict(news_dict):
    '''
    Function: creates a dictionary of the most popular words, both positive 
    and negative, specific to describing autism as values (dictionary) and 
    the news source as a key (string)
    Parameters: dictionary
    Returns: a dictionary of news source as key (string) and values as dicitionary of 
    popular words
    '''
    words_dict = {}
    for site in news_dict:        
        words_dict[site] = {'pos' : count_poswords(news_dict[site]), \
                            'neg' : count_negwords(news_dict[site])}
    
    return words_dict
    
def graph(dict_list, sites, colors, labels, title):
    '''
    Function: graphs a list of dictionaries
    Parameters: list of dictionaries, sites (list), colors (list), 
    labels (list), title (string)
    Returns: a plot of the dictionaries keys on the x axis (string) 
    and the ratio between the number of positive words and negative words in 
    the articles on the y axis (float)
    '''
    i = 0
    j = 0
    label = labels[j]
    for words_dict in dict_list:
        for site in words_dict:
            pos_lst = []
            neg_lst = []
            for value in words_dict[site]:
                # print(words_dict[site][value])
                for tup in words_dict[site][value]:
                    # print(tup)
                    if value == 'pos':
                        pos_lst.append(tup[1])
                
                    else:
                        
                        neg_lst.append(tup[1])
                        
            ratio = sum(pos_lst) / sum(neg_lst)
            if colors[i] != colors[i - 1] and i != 0:
                label = labels[j + 1]
                j += 1
            elif colors[i] == colors[i - 1]:
                label = "_nolegend_"
            else:
                label = labels[j]
               
            plt.bar(sites[i], ratio, .3, color = colors[i], label = label)
            plt.text(i, ratio + .03, str(round(ratio, 2)), ha = 'center')
            i += 1
            
    plt.xticks(rotation = 45, ha = 'right')
    plt.xlabel('News Source')
    plt.ylabel('Positive/Negative Ableist Word Usage Ratio', ha = 'center')
    plt.title(title)
    plt.legend(bbox_to_anchor =(1, .75))

def main():
    # left wing sites and dictionary
    left_wing = {'HP': [], 'CNN': [],'MSNBC': [], 'NYT': []}
    left_wing = add_articles_to_dict(left_wing, 5, 'LeftWingArticles/')
    left = words_dict(left_wing)
    
    # moderate left sites and dictionary    
    moderate_left_wing = {'WP': []}
    moderate_left_wing = add_articles_to_dict(moderate_left_wing, 5, \
                                              'LeftWingArticles/')
    mleft = words_dict(moderate_left_wing)
    
    # right wing sites and dictionary
    right_wing = {'Breit': [], 'Daily': [], 'Fox': [], 'CBN': []}
    right_wing = add_articles_to_dict(right_wing, 5, 'RightWingArticles/')
    right = words_dict(right_wing)
    
    # moderate right sites and dictionary    
    moderate_right_wing =  {'WT': []}
    moderate_right_wing = add_articles_to_dict(moderate_right_wing, 5, \
                                               'RightWingArticles/')
    mright = words_dict(moderate_right_wing)
    
    sites = ['Huntington Post', 'CNN', 'MSNBC', 'New York Times', \
             'Washtington Post', 'Washington Times', 'Breitbart', 'Daily Mail', 'Fox News',\
                 'CBN']
    dict_list = [left, mleft, mright, right]
    colors = ['blue', 'blue', 'blue', 'blue', 'deepskyblue', 'red', \
              'firebrick', 'firebrick', 'firebrick', 'firebrick' ]
    labels = ['Left Wing', 'Moderate Left Wing', 'Right Wing', \
              'Moderate Right Wing']
    title = 'News Sites Positive to Negative Ableist Word Usage Ratio'
    
    graph(dict_list, sites, colors, labels, title)
    plt.show()
       

main() 
    
    