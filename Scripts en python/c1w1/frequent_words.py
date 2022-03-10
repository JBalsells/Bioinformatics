#filename = "../Datasets/Vibrio_cholerae.txt"
#filename = "E_coli.txt"
filename = "../Datasets/dataset_2_13.txt"
#filename = "dataset_3_2.txt"


with open(filename, 'r') as file:
    data = file.read()
    
data = "ACGTTGCATGTCGCATGATGCATGAGAGCT"

window = 4

words = {}

print(len(data))

for i in range(0,len(data)-window+1):
    word = data[i:i+window]
    cond = word in words
    if cond==False:
        words[word]=1
    elif cond==True:
        words[word]+=1

print(dict(sorted(words.items(), key=lambda item: item[1])))
#print(words)
