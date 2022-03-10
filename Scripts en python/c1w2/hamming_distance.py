import numpy as np

def nucleotide_hamming_distance(DNA):
    DNA1 = DNA[0]
    DNA2 = DNA[1]
    len1 = len(DNA1)
    len2 = len(DNA2)
    count = 0
    if(len1==len2):
        for i in range(0,len1):
            if(DNA1[i]!=DNA2[i]):
                count += 1
        return count
    else:
        return "dna strands are of different dimensions"

if __name__ == "__main__":

    DNA = np.array([])

    #filename = "../Datasets/dataset_9_3.txt"
    #with open(filename, 'r') as file:
    #    for line in file:
    #        DNA = np.append(DNA,line)

    DNA = np.append(DNA, "CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT")
    DNA = np.append(DNA, "CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG")

    print(nucleotide_hamming_distance(DNA))