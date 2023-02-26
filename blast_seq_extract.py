#!/usr/bin/env python3

"""
Run a BLAST command (blastn or blastp), and extract the relevant sections of any hits it returns

Must be run in a directory and enviornment from which the blast command will run cleanly

Returns the results to STDOUT in FASTA format
"""

import argparse
import os
import sys
from Bio import SeqIO

def get_blast_cmd_output(cmd) -> str:
	"""
	Run a blastn or blastp command (:param cmd)
	and return the results. Handle some failure cases
	"""
	pass

def get_sequence_hits_from_blast(fasta_file, hits) -> None:
	"""
	Given a FASTA file containing any possible hits,
	and a list of hists from BLAST, extract sections of segments
	that are hits, and return them in a FASTA file format
	"""
	with open(fasta_file, "rU") as input_handle:
		seq_dict = SeqIO.to_dict(SeqIO.parse(input_handle, "fasta"))
		# TSV of hits
		for hit in hits:
			hit_details = hit.split("\t")
			hit_name = hit_details[1]
			hit_start = hit_details[2]
			hit_end = hit_details[3]
			try:
				hit = str(seq_dict[hit_name])[hit_start:hit_end]
			except KeyError:
				print(f"ERROR: No matches found in FASTA file for hit {hit_name}")
				sys.exit(-1)
			if (hit_name != seq_dict[hit_name].id):
				print(f"ERROR: Hit name and FASTA file mismatch between {hit_name} and {seq_dict[hit_name].id}")
				sys.exit(-1)
			print(f">{hit_name}")
			print(f"{hit}")

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-b", "--blast-command", type=str, required=True, help="BLAST command to run. Must have outfmt 0 specified.")
	parser.add_argument("-f", "--fasta-file", type=str, required=True, help="File in FASTA format containing any sequences that BLAST may return as hits.")
	args = parser.parse_args()
	hits = get_blast_cmd_output(args.blast_command)
	if len(hits) == 0:
		print(f"ERROR: No hits returned by BLAST for command {args.blast_command}")
		sys.exit(-1)
	get_sequence_hits_from_blast(args.fasta_file, hits)
