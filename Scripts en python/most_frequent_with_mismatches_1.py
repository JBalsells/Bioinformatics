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

    for kmer in frequencies:
        if frequencies[kmer] == max(frequencies.values()):
            aprox_frq_words.append(kmer)
    end = time.process_time()

    print("Time:", end - start)
    return aprox_frq_words, frequencies

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

def MaximizingSum(dna,patterns,frequencies):
    pass      

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
    k = 6
    d = 3

    dna = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    d = 1

    patterns, frequencies = FrequentWordsWithMismatches(dna,k,d)
    print(dict(sorted(frequencies.items(), key=lambda item: item[1])))