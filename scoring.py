from typing import List

import nltk

#open file with raw data, and open/create file for processed data
inFile = open("output/output_wordvec_unscored.txt", "r")
outFile = open("output/scoring_baseline_happy.tsv", "a")

prevLine = ""

for line in inFile:
    if line[0:0] == "OUTSCORE: ":
        outFile.write(prevLine[9:len(prevLine)] + '\t' + line[10:len(line)] + '\n')
    else:
        prevLine = line
