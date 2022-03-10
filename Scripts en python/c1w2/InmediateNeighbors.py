"""import itertools
import time
from collections import defaultdict
import numpy as np

def InmediateNeighbors():
    pass

def PermuteMotifOnce(motif, alphabet={"A", "C", "G", "T"}):
    return list(set(itertools.chain.from_iterable([[
        motif[:pos] + nucleotide + motif[pos + 1:] for
        nucleotide in alphabet] for
        pos in range(len(motif))])))

def PermuteMotifDistanceTimes(motif, d):
    workingSet = {motif}
    for _ in range(d):
        workingSet = set(itertools.chain.from_iterable(map(PermuteMotifOnce, workingSet)))
    return list(workingSet)

def main():
    print(PermuteMotifDistanceTimes("ACG",1))

if __name__ == "__main__":
    main()"""

chars = "ACGT"

def neighbors(pattern, d):
    assert(d <= len(pattern))

    if d == 0:
        return [pattern]

    r2 = neighbors(pattern[1:], d-1)
    r = [c + r3 for r3 in r2 for c in chars if c != pattern[0]]

    if (d < len(pattern)):
        r2 = neighbors(pattern[1:], d)
        r += [pattern[0] + r3 for r3 in r2]

    return r

values = neighbors("ACGT", 3)

print(len(values))

#for i in range(0,len(values)):
#    print(values[i])