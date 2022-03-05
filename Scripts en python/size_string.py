filename = "Datasets/E_coli.txt"

with open(filename, 'r') as file:
    data = file.read()

print(len(data))