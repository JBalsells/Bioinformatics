filename = "../Datasets/dataset_9_4.txt"

with open(filename, 'r') as file:
    genome = file.read()

#genome = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
pattern = "GAGGCACTGTAG"
d = 5
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

for i in range(0,len(data)):
    print(data[i])