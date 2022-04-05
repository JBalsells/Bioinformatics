#Alálisis de bioinformática
#import Bio #importar librería
#from Bio.Seq import Seq

#dna = Seq("ACGTTGCAC")
#print(dna)


from Bio import SeqIO
for record in SeqIO.parse("GCA_001292785.1.fasta", "fasta"):
    print(record.seq, len(record.seq))
