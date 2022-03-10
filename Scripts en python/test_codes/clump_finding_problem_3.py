import time

def main():
    #filename = "Datasets/E_coli.txt"
    filename = "Datasets/dataset_4_5.txt"
    with open(filename, 'r') as file:
        inputString = file.read()

    length,window,minTimes = 10,24,4
    allKmer = []
    kmerList = {}

    #Kmers in the first window
    for i in range(0,window-length+1):
        addKmer = inputString[i:i+length]
        count = kmerList[addKmer] = kmerList.get(addKmer,0) + 1
        if count >= minTimes:
            allKmer.append(addKmer)

    #Slide windows by 1 bp per step
    for i in range(1,len(inputString)-window+1):
        removeKmer = inputString[i-1:i-1+length]
        addKmer = inputString[i+window-length:i+window]
        kmerList[removeKmer] = kmerList.get(removeKmer) - 1
        count = kmerList[addKmer] = kmerList.get(addKmer ,0) + 1
        if count >= minTimes:
            allKmer.append(addKmer)
            
    #remove duplicate
    allKmer = list(set(allKmer))
    
    #print(' '.join(allKmer))
    print(len(allKmer))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("time consumed: %lf" % (end-start))