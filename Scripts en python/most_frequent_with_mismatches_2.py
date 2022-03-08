import itertools
import time
from collections import defaultdict
import numpy as np

def FrequentWordsWithMismatches(Genome, k, d):
    start = time.process_time()

    aprox_frq_words = []
    frequencies = defaultdict(lambda: 0)
    # all existent kmers with d mismatches of current kmer in genome
    for index in range(len(Genome) - k + 1):
        curr_kmer_and_neighbors = PermuteMotifDistanceTimes(Genome[index : index + k], d)
        for kmer in curr_kmer_and_neighbors:
            frequencies[kmer] += 1 

    end = time.process_time()

    print("Time:", end - start)
    return frequencies

def PermuteMotifOnce(motif, alphabet={"A", "C", "G", "T"}):
    """
    Gets all strings within hamming distance 1 of motif and returns it as a
    list.
    """

    return list(set(itertools.chain.from_iterable([[
        motif[:pos] + nucleotide + motif[pos + 1:] for
        nucleotide in alphabet] for
        pos in range(len(motif))])))

def PermuteMotifDistanceTimes(motif, d):
    workingSet = {motif}
    for _ in range(d):
        workingSet = set(itertools.chain.from_iterable(map(PermuteMotifOnce, workingSet)))
    return list(workingSet)

def MaximizingSum(frequencies):
    frequent_and_reverse = defaultdict(lambda: 0)
    for key in frequencies:
        inverse_key = ComplementaryStrand(key)

        inv_value=0
        inv_key=""
        if(inverse_key in frequencies):
            inv_value = frequencies[inverse_key]
            inv_key = inverse_key

        sum = frequencies[key] + inv_value
        
        far_key_1 = key + " " + inv_key
        far_key_2 = inv_key + " " + key

        if(not far_key_1 in frequent_and_reverse):
            if(not far_key_2 in frequent_and_reverse):
                frequent_and_reverse[far_key_1] = sum
    return dict(sorted(frequent_and_reverse.items(), key=lambda item: item[1]))


def ComplementaryStrand(pattern):
    reversed = ""
    index = len(pattern)-1

    while index>=0:
        if(pattern[index]=="A" or pattern[index]=="a"):
            reversed += "T"
        elif(pattern[index]=="T" or pattern[index]=="t"):
            reversed += "A"
        elif(pattern[index]=="C" or pattern[index]=="c"):
            reversed += "G"
        elif(pattern[index]=="G" or pattern[index]=="g"):
            reversed += "C"

        index -= 1
    return reversed

if __name__ == "__main__":
    filename = "Datasets/dataset_9_10.txt"
    #filename = "Datasets/E_coli.txt"

    with open(filename, 'r') as file:
        dna = file.read()
    k = 7
    d = 2

    #dna = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    #k = 4
    #d = 1

    frequencies = FrequentWordsWithMismatches(dna,k,d)
    #print(dict(sorted(frequencies.items(), key=lambda item: item[1])))

    print(MaximizingSum(frequencies))