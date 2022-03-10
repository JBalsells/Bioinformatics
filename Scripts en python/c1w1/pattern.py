def PatternCount(text, pattern):
    window = len(pattern)
    count = 0

    for i in range(0,len(text)-window+1):
        word = text[i:i+window]
        if word==pattern:
            count += 1

    return count


if __name__ == "__main__":

    #filename = "Datasets/Vibrio_cholerae.txt"
    filename = "../Datasets/dataset_2_6.txt"
    with open(filename, 'r') as file:
        data = file.read()


    print(PatternCount(data, "AAACCTCAA"))