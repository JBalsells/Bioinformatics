filename = "Datasets/dataset_3_2.txt"

with open(filename, 'r') as file:
    data = file.read()
print(len(data))

compl = {'A':'T','T':'A','C':'G','G':'C'}

def reverser(text):
    x = ''
    for i in range(len(text)):
        x += compl[text[len(text) - i - 1]]
    return x

print(len(reverser(data)))