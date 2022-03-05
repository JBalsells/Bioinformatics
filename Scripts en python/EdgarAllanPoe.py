#!/usr/bin/python3

filename = "EdgarAllanPoe.txt"
with open(filename, 'r') as file:
    #data = file.read()
    for line in file:
        print(line)
    #    for char in line:
    #        print(ord(char))

#print(data)
    