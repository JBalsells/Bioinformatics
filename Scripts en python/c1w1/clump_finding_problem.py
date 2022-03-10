import numpy as np

def FindClumps(text, k, L, t):
    n = len(text)
    out = []
    # FOR each window of size L
    for i in range(n-L):
        pattern = []
        window = text[i:i+L]
        # FOR each pattern present in window
        for j in range(len(window)-k):
            pattern.append(window[j:j+k])
        # find unique k-mers and their frequencies
        kmers, counts = np.unique(pattern, return_counts=True)        
        out += kmers[counts>=t].tolist()
    return np.unique(out, return_counts=True)

if __name__=="__main__":
    filename = "../Datasets/dataset_4_5.txt"
    with open(filename, 'r') as file:
        data = file.read()

    #data = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
    k = 9
    l = 28
    t = 3

    print(FindClumps(data,k,l,t))
 