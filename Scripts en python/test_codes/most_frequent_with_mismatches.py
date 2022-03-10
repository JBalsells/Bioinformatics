import numpy as np
import time

def k_mers(dna,k):
    words = {}
    for i in range(0,len(dna)-k+1):
        word = dna[i:i+k]
        cond = word in words
        if cond==False:
            words[word]=0
    return words


def FrequentWordsWithMismatches(text, k, d):
    patterns = np.array([])
    n = len(text)

    for i in range(0,n-k):
        pass


def main():
    filename = "Datasets/dataset_9_9.txt"
    #filename = "Datasets/E_coli.txt"
    with open(filename, 'r') as file:
        dna = file.read()
    k = 6
    d = 2

    neighbors = k_mers(dna,k)
    print(neighbors)

if __name__ == "__main__":
    main()