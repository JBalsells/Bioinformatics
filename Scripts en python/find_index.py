#!/usr/bin/python3

#filename = "dataset_3_5.txt"
#substring = "AACTGAAAA"
filename = "Vibrio_cholerae1.txt"
substring = "CTTTCACTT"
#substring = "CTTGATCAT"

with open(filename, 'r') as file:
    data = file.read()

for i in range(0,len(data)-len(substring)):
    find_substring = data[i:i+len(substring)]
    if(find_substring == substring):
        #print(find_substring)
        print(i)