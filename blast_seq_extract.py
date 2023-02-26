#!/usr/bin/env python3

"""
Run a BLAST command (blastn or blastp), and extract the relevant sections of any hits it returns

Must be run in a directory and enviornment from which the blast command will run cleanly

Returns the results to STDOUT in FASTA format
"""

import argparse
import os
from Bio import SeqIO

def get_blast_cmd_output(cmd):
	"""
	Run a blastn or blastp command (:param cmd)
	and return the results. Handle some failure cases
	"""
	pass

def get_sequence_hits_from_blast(fasta_file, hits):
	"""
	Given a FASTA file containing any possible hits,
	and a list of hists from BLAST, extract sections of segments
	that are hits, and return them in a FASTA file format
	"""
	pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-b", "--blast-command", type=str, required=True, help="BLAST command to run. Must have outfmt 0 specified.")
	parser.add_argument("-f", "--fasta-file", type=str, required=True, help="File in FASTA format containing any sequences that BLAST may return as hits.")
	args = parser.parse_args()
	hits = get_blast_cmd_output(args.blast_command)
	sequences_fasta get_sequence_hits_from_blast(args.fasta_file, hits)
