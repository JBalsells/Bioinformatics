def most_frequent():
    filename = "Vibrio_cholerae.txt"
    #filename = "E_coli.txt"

    with open(filename, 'r') as file:
        data = file.read()    

    window = 9
    words = {}
    sorted_words = {}
    print(len(data))

    for i in range(0,len(data)-window+1):
        word = data[i:i+window]
        cond = word in words
        if cond==False:
            words[word]=1
        elif cond==True:
            words[word]+=1

    sorted_words = dict(sorted(words.items(), key=lambda item: item[1]))
    print(sorted_words)


def main():
    most_frequent()

if __name__ == "__main__":
    main()