#!/usr/bin/python3

filename = "../Datasets/dataset_3_5.txt"

substring = "AGCT"

with open(filename, 'r') as file:
    data = file.read()
data = "AGCTGCGAGCTACGTGAGCTCGAAATAAAGCTAGCTCGATA"


for i in range(0,len(data)-len(substring)):
    find_substring = data[i:i+len(substring)]
    if(find_substring == substring):
        #print(find_substring)
        print(i)