__author__ = 'hemanth'


import sys
import glob
import os
import string
import time

from collections import deque


def load_words(base_dir, size):
    files = glob.glob1(base_dir, "*words.txt")
    print "count of files: ", len(files)
    words = []
    max_length = 0

    for f in files:
        fp = os.path.join(base_dir, f)
        wf = [w.strip() for w in open(fp)]
       # print "Found {0} words in {1}".format(len(wf), f)
        for w in wf:
            if len(w) == size:
                words.append(w)

    print "Total words is {0}".format(len(words))
    return words


def find_neighbours(w, words):
    i = 0
    neighbours_list = []
    count = 0
    while i < len(w):
        temp_list = list(w)
        for letter in string.ascii_lowercase:
            temp_list[i] = letter
            count += 1
            if "".join(temp_list) in words and "".join(temp_list) != w:
                neighbours_list.append("".join(temp_list))

        i += 1

    return neighbours_list


def create_graph(words, size):
    graph_dict = {}
    for w in words:
        if len(w) == size:
            neighbours_list = find_neighbours(w, words)
            graph_dict[w] = neighbours_list

    return graph_dict


class word_ladder():
    def __init__(self, value):
        self.prev = None
        self.word = value


'''def find_shortest_path(graph, start, end):
    queue = list()
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        if node in path[0:-1]:
            continue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)'''
def shortestpath(word1,word2,adjacency_list,previousnode,k):
    print '....',k
    allpaths=[]
    if  word2 in adjacency_list[word1]:

        return [word1,word2]
    else:

        lis=adjacency_list[word1]
        lenght=len(lis)
        for i in range(lenght):
            allpaths.append([])
        i=0
        while i<lenght:
            allpaths[i].append(word1)
            if lis[i] :
               if previousnode!=lis[i]:
                  x=shortestpath(lis[i],word2,adjacency_list,word1,k+1)
               if x!=None:
                   if k==0:
                       print x
                   allpaths[i].extend(x)
            i=i+1
        i=0
        while i<len(allpaths) and k!=0:
            if len(allpaths[i])==1:

                del allpaths[i]
            else:
                i=i+1

        if len(allpaths)==0:
            print 'than god getting here'
            return None
        else:
            if k==0:
                print 'returning all the paths'
                return allpaths
            else:
                print 'value of i is-------->>',i
                return min(allpaths,key=len)


def main(argv = sys.argv):
    # add arguments checks here...



        word1=raw_input('enter the word1')
        word2=raw_input('enter the another word2')
        words=load_words(r"C:\work\cl2013\gvp-vikramaditya\anagrams\EOWL-v1.1.2\LF Delimited Format",len(word1))
        print word1 in words
        print word2 in words
        if word1 in words and word2 in words:
            print 'entering into creation'
            graph_dict = create_graph(words, len(word1))
            print 'creation complete'
            if 'cut' in graph_dict['cat']:
                print 'iam happy'
            print 'success..'
            path = shortestpath(word1, word2,graph_dict,0)
            if None:
              print 'am wast'
            else:
                print path


        else:
            print 'entered words are not in dictionary'


if __name__ == "__main__":
    main()