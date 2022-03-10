#!/usr/bin/python3

filename = "../Datasets/Vibrio_cholerae.txt"
with open(filename, 'r') as file:
    data = file.read()
    

print(data)
print(len(data))
print(data.count('AATTT'))