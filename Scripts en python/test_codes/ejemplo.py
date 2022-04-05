#print(sorted([9,1,0,7,2,8,4,5,6,3]))
#print(sorted(['G','C','I','B','J','E','G','A','H','D']))
#print(dict(zip(sorted(['G','C','I','B','J','E','G','A','H','D']), sorted([9,1,0,7,2,8,4,5,6,3]))))

#st = "AGAGAGATAAGAACAGGA"
#print("B"+str(st.count("A"))+str(st.count("T"))+"NF"+str(st.count("X"))+"RM"+st[0]+st[7]+str(st.count("C"))+st[13]+st[9])


"""
def nucleotide_hamming_distance(DNA):
    DNA1 = DNA[0]
    DNA2 = DNA[1]
    len1 = len(DNA1)
    len2 = len(DNA2)
    count = 0
    if(len1==len2):
        for i in range(0,len1):
            if(DNA1[i]!=DNA2[i]):
                count += 1
        return count
    else:
        return "dna strands are of different dimensions"

if __name__ == "__main__":

    DNA = []
    DNA.append("CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT")
    DNA.append("CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG")

    print(nucleotide_hamming_distance(DNA))
"""


"""def approx_pat(pattern, genome, mutation):
    position = []
    for i in range (0,len(genome)-len(pattern)+1):
        if hamming_distance(pattern,genome[i:i+len(pattern)]) <= mutation:
            position.append(i)
    return position

def hamming_distance(q, p):
        dist = 0
        for i in range(0,len(p)):
            if p[i] != q[i]:
                dist += 1
        return dist

print(approx_pat("AAA","TACGCATTACAAAGCACA",1))"""



#st = "AGAGAGATAAGAACAGGA"
#print("B"+str(st.count("A"))+str(st.count("T"))+"NF"+str(st.count("X"))+"RM"+st[0]+st[7]+str(st.count("C"))+st[13]+st[9])

x = range(0,11)
for i in x:
    print(i)