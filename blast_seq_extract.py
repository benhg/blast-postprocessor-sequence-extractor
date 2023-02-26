#!/usr/bin/env python3

"""
Run a BLAST command (blastn or blastp), and extract the relevant sections of any hits it returns

Must be run in a directory and enviornment from which the blast command will run cleanly
"""

import argparse
import os
from Bio import SeqIO


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument()
	parser.add_argument()
	args = parser.parse_args()