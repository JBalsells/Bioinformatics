#!/usr/bin/python3
import re

Amino = {
	'Ala':{
		'Name':'Alanine',
		'Symbol':'A',
		'Molar_Mass':89.094,
		'Polarity':'apolar',
		'Abbreviation':'Ala',
		},
	'Arg':{
		'Name':'Arginine',
		'Symbol':'R',
		'Molar_Mass':174.203,
		'Polarity':'polar',
		'Abbreviation':'Arg',
		},
	'Asn':{
		'Name':'Aspargine',
		'Symbol':'N',
		'Molar_Mass':132.119,
		'Polarity':'polar',
		'Abbreviation':'Asn',
		},
	'Asp':{
		'Name':'Aspartic acid',
		'Symbol':'D',
		'Molar_Mass':133.104,
		'Polarity':'polar',
		'Abbreviation':'Asp',
		},
	'Cys':{
		'Name':'Cysteine',
		'Symbol':'C',
		'Molar_Mass':121.154,
		'Polarity':'polar',
		'Abbreviation':'Cys',
		},
	'Gln':{
		'Name':'Glutamine',
		'Symbol':'Q',
		'Molar_Mass':146.146,
		'Polarity':'polar',
		'Abbreviation':'Gln',
		},
	'Glu':{
		'Name':'Glutamic acid',
		'Symbol':'E',
		'Molar_Mass':147.131,
		'Polarity':'polar',
		'Abbreviation':'Glu',
		},
	'Gly':{
		'Name':'Glycine',
		'Symbol':'G',
		'Molar_Mass':75.067,
		'Polarity':'apolar',
		'Abbreviation':'Gly',
		},
	'His':{
		'Name':'Histidine',
		'Symbol':'H',
		'Molar_Mass':155.156,
		'Polarity':'polar',
		'Abbreviation':'His',
		},
	'Ile':{
		'Name':'Isoleucine', 
		'Symbol':'I',
		'Molar_Mass':131.175,
		'Polarity':'apolar',
		'Abbreviation':'Ile',
		},
	'Leu':{
		'Name':'Leucine', 
		'Symbol':'L',
		'Molar_Mass':131.175,
		'Polarity':'apolar',
		'Abbreviation':'Leu',
		},
	'Lys':{
		'Name':'Lysine',
		'Symbol':'K',
		'Molar_Mass':146.189,
		'Polarity':'polar',
		'Abbreviation':'Lys',
		},
	'Met':{
		'Name':'Methionine / Start',
		'Symbol':'M',
		'Molar_Mass':149.208,
		'Polarity':'apolar',
		'Abbreviation':'Met',
		},
	'Phe':{
		'Name':'Phenylalanine', 
		'Symbol':'F',
		'Molar_Mass':165.192,
		'Polarity':'apolar',
		'Abbreviation':'Phe',
		},
	'Pro':{
		'Name':'Proline',
		'Symbol':'P',
		'Molar_Mass':115.132,
		'Polarity':'apolar',
		'Abbreviation':'Pro',
		},
	'Ser':{
		'Name':'Serine', 
		'Symbol':'S',
		'Molar_Mass':105.093,
		'Polarity':'polar',
		'Abbreviation':'Ser',
		},
	'Stp':{
		'Name':'Stop', 
		'Symbol':'Stop',
		'Molar_Mass':0,
		'Polarity':'',
		'Abbreviation':'Stop',
		},
	'Thr':{
		'Name':'Threonine',
		'Symbol':'T',
		'Molar_Mass':119.119,
		'Polarity':'polar',
		'Abbreviation':'Thr',
		},
	'Trp':{
		'Name':'Tryptophan',
		'Symbol':'W',
		'Molar_Mass':204.228,
		'Polarity':'apolar',
		'Abbreviation':'Trp',
		},
	'Tyr':{
		'Name':'Tyrosine',
		'Symbol':'Y',
		'Molar_Mass':181.191,
		'Polarity':'polar',
		'Abbreviation':'Tyr',
		},
	'Val':{
		'Name':'Valine',
		'Symbol':'V',
		'Molar_Mass':117.148,
		'Polarity':'apolar',
		'Abbreviation':'Val',
		},
	}

Codons = {
	'UUU':Amino['Phe'], 
	'UUC':Amino['Phe'],
	'UUA':Amino['Leu'],
	'UUG':Amino['Leu'],
	'CUU':Amino['Leu'],
	'CUC':Amino['Leu'],
	'CUA':Amino['Leu'],
	'CUG':Amino['Leu'],
	'AUU':Amino['Ile'],
	'AUC':Amino['Ile'],
	'AUA':Amino['Ile'],
	'AUG':Amino['Met'],	
	'GUU':Amino['Val'],
	'GUC':Amino['Val'],
	'GUA':Amino['Val'],
	'GUG':Amino['Val'],
	'UCU':Amino['Ser'],
	'UCC':Amino['Ser'],
	'UCA':Amino['Ser'],
	'UCG':Amino['Ser'],
	'CCU':Amino['Pro'],
	'CCC':Amino['Pro'],
	'CCA':Amino['Pro'],
	'CCG':Amino['Pro'],
	'ACU':Amino['Thr'],
	'ACC':Amino['Thr'],
	'ACA':Amino['Thr'],
	'ACG':Amino['Thr'],
	'GCU':Amino['Ala'],
	'GCC':Amino['Ala'],
	'GCA':Amino['Ala'],
	'GCG':Amino['Ala'],
	'UAU':Amino['Tyr'],
	'UAC':Amino['Tyr'],
	'UAA':Amino['Stp'],
	'UAG':Amino['Stp'],
	'CAU':Amino['His'],
	'CAC':Amino['His'],
	'CAA':Amino['Gln'],
	'CAG':Amino['Gln'],
	'AAU':Amino['Asn'],
	'AAC':Amino['Asn'],
	'AAA':Amino['Lys'],
	'AAG':Amino['Lys'],
	'GAU':Amino['Asp'],
	'GAC':Amino['Asp'],
	'GAA':Amino['Glu'],
	'GAG':Amino['Glu'],
	'UGU':Amino['Cys'],
	'UGC':Amino['Cys'],
	'UGA':Amino['Stp'],
	'UGG':Amino['Trp'],
	'CGU':Amino['Arg'],
	'CGC':Amino['Arg'],
	'CGA':Amino['Arg'],
	'CGG':Amino['Arg'],
	'AGU':Amino['Ser'],
	'AGC':Amino['Ser'],
	'AGA':Amino['Arg'],
	'AGG':Amino['Arg'],
	'GGU':Amino['Gly'],
	'GGC':Amino['Gly'],
	'GGA':Amino['Gly'],
	'GGG':Amino['Gly'],
	}

DNAChain = input('Ingrese cadena: \n')

DNAChain = "".join(re.findall("[cgatuCGATU]", DNAChain)) #""/join, tupla a string, findall Expresiones regulares

DNAChain = DNAChain.upper();
DNAChain = DNAChain.replace('T','U')

#Filtrar caracteres, solo CGAT

"""Start = DNAChain.find('AUG')
if(Start==-1):
	print('No se encontro codon de inicio.')
	exit()

End	= DNAChain.find('UAA')
if(End==-1):
	End	= DNAChain.find('UAG')
	if(End==-1):
		End	= DNAChain.find('UGA')

if(End==-1):
	print('No se encontro codon de finalizacion.')
	exit()

DNAChain = DNAChain[Start:End+3]"""

div,mod = divmod(len(DNAChain), 3)
if(mod>0):
	print(DNAChain)
	print('Uno o varios codones no estan completos.')
	exit()

print(DNAChain)

Counter=0
while(Counter<len(DNAChain)):
	Codon = DNAChain[Counter:Counter+3]
	AminoAcid = Codons[Codon]

	print('\nNombre: ' + AminoAcid['Name'] + '\nAbreviatura: ' + AminoAcid['Abbreviation'] + '\nSimbolo: ' + AminoAcid['Symbol'] + '\nMasa Molar:' + str(AminoAcid['Molar_Mass']) + '\nPolaridad: ' + AminoAcid['Polarity'])

	Counter+=3