#!/usr/bin/python3
import matplotlib.pyplot as plt
from Bio import SeqIO

Data = SeqIO.parse("../Datasets/P0C6X7.fasta", "fasta")

for DataSeq in Data:
	Ac = DataSeq.seq.count('A')
	Cc = DataSeq.seq.count('C')
	Gc = DataSeq.seq.count('G')
	Tc = DataSeq.seq.count('T')

Den = Ac+Cc+Gc+Tc

ATperc = (Ac+Tc) / float(Den)
CGperc = (Cc+Gc) / float(Den)

print('A: ' + str(Ac) + ', C: ' + str(Cc) + ', G: ' + str(Gc) + ', T: ' + str(Tc))
print('Porcentaje AT: ' + str(ATperc) + ', porcentaje CG: ' + str(CGperc))
print(Den)

fig, axs = plt.subplots()

axs.bar('AT', ATperc)
axs.bar('CG', CGperc)

fig.suptitle('Porcentajes')

plt.show()