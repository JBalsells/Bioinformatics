import itertools
import time
from collections import defaultdict
import numpy as np

def FrequentWordsWithMismatches(Genome, k, d):
    start = time.process_time()

    aprox_frq_words = []
    frequencies = defaultdict(lambda: 0)
    # all existent kmers with d mismatches of current kmer in genome
    for index in range(len(Genome) - k):
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

if __name__ == "__main__":
    filename = "../Datasets/dataset_9_9.txt"
    #filename = "Datasets/E_coli.txt"

    with open(filename, 'r') as file:
        dna = file.read()
    k = 6
    d = 3

    frequencies = FrequentWordsWithMismatches(dna,k,d)
    print(dict(sorted(frequencies.items(), key=lambda item: item[1])))