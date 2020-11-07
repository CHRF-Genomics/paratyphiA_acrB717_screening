#!/bin/env python
'''
A SIMPLE SCRIPT TO DETECT AcrB-717 MUTATION in Salmoenlla Paratyphi A
Author: Arif Mohammad Tanmoy (arif.tanmoy@chrfbd.org)
'''
import sys, os
from Bio.Seq import Seq
from argparse import (ArgumentParser, FileType)
def parse_args():
	"Parse the input arguments, use '-h' for help"
	commands = ArgumentParser(description='Detect AcrB-717 mutation from mapped VCF file (One isolate per file).\nMapping has to be done against AKU12601 (FM200053.1)')
	commands.add_argument('--vcf', type=str, required=True,
						help='Mapped VCF file of one sample.')
	commands.add_argument('--id', type=str, required=True,
						help='Sample ID.')
	commands.add_argument('--output', type=str, required=False, default='AcrB717_mutation.txt',
						help='Location and name for output file.')
	return commands.parse_args()
args = parse_args()

def trans_codon(l):
	codon = 'C'+str(l)+'A'
	myseq = Seq(codon)
	trans = myseq.translate()
	return trans

def main():
	output=open(args.output, 'w')
	for line in open(args.vcf, 'r'):
		if line.startswith('#'):
			pass
		else:
			data = line.rstrip().split('\t')
			if int(data[1]) == 2338396:
				alt_code = str(trans_codon(data[4]))
				ref_code = str(trans_codon(data[3]))
				output.write(args.id+'\t'+'AcrB717-'+ref_code+'2'+alt_code+'\n')	
# call main function
if __name__ == '__main__':
	main()

