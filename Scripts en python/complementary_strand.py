filename = "dataset_3_2.txt"

with open(filename, 'r') as file:
    data = file.read()

reversed = ""
index = len(data)-1

while index>=0:
    if(data[index]=="A" or data[index]=="a"):
        reversed += "T"
    elif(data[index]=="T" or data[index]=="t"):
        reversed += "A"
    elif(data[index]=="C" or data[index]=="c"):
        reversed += "G"
    elif(data[index]=="G" or data[index]=="g"):
        reversed += "C"

    index -= 1
reversed += "\n"
print(reversed)
