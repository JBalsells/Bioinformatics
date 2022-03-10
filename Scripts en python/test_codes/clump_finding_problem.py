#!/usr/bin/python3

import math

def find_clumps(adn, l):
    clump = []

    total_of_clumps = math.ceil(len(adn)/l)
    for i in range(0,total_of_clumps):
        clump.append(adn[l*i:l*i+l])

    return clump

def most_frequent(adn, window):
    words = {}

    for i in range(0,len(data)-window+1):
        word = data[i:i+window]
        cond = word in words
        if cond==False:
            words[word]=1
        elif cond==True:
            words[word]+=1

    return(dict(sorted(words.items(), key=lambda item: item[1])))

if __name__=="__main__":
    filename = "Datasets/dataset_4_5.txt"
    with open(filename, 'r') as file:
        data = file.read()
    data = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
    k = 5
    l = 50
    t = 4

    clumps = find_clumps(data, l)

    most_freq = most_frequent(clumps[0], k)
    print(most_freq)