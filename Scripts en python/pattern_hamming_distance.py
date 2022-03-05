"""import numpy as np

def pattern_hamming_distance(DNA, pattern, distance):
    for i in range(0,len(DNA)-len(pattern)+1):
        count = 0
        for j in range(0,len(pattern)):
            if(pattern[j]!=DNA[i+j]):
                count+=1
        if count<=3:
            print(i)
        
    return

if __name__ == "__main__":

    filename = "dataset_9_4.txt"
    with open(filename, 'r') as file:
        DNA = file.read()
    #DNA = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
    pattern = "GTATATGAC"
    distance = 6

    print(pattern_hamming_distance(DNA, pattern, distance))"""

#filename = "dataset_9_4.txt"
filename = "dataset_9_6.txt"
with open(filename, 'r') as file:
    genome = file.read()
#genome = "AACAAGCTGATAAACATTTAAAGAG"
#genome = "TTTAGAGCCTTCAGAGG"
pattern = "TTAAGTG"
d = 3
position = []

def approx_pat(pattern, genome, d):
    for i in range (len(genome) - len(pattern)+1):
        if hamming_distance(pattern, genome[i:i + len(pattern)]) <= int(d):
            position.append(i)
    return position

def hamming_distance(q, p):
        dist = 0
        for i in range(len(p)):
            if p[i] != q[i]:
                dist += 1
        return dist

data = approx_pat(pattern, genome, d)
print(data)
print(len(data))