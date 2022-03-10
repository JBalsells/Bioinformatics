#!/usr/bin/python3

import math

def most_frequent(adn, window):
    words = {}

    for k in range(0,len(data)-window+1):
        word = data[k:k+window]
        cond = word in words
        if cond==False:
            words[word]=1
        elif cond==True:
            words[word]+=1

    return(words)

if __name__=="__main__":
    #filename = "dataset_4_5.txt"
    filename = "Datasets/E_coli.txt"
    with open(filename, 'r') as file:
        data = file.read()
    
    k=9
    L=500
    t=3
    
    clumps = {''}

    for i in range(0,len(data)-L):
        short_chain = data[i:i+L]

        most_freq = most_frequent(short_chain, k)
        for word_key in most_freq:
            if(most_freq[word_key]==t):
                clumps.add(word_key)
                print(len(clumps))
    for cl in clumps:
        print(len(cl)) 