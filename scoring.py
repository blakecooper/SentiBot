from typing import List

import nltk

#open file with raw data, and open/create file for processed data
inFile = open("data/output_baseline_unscored_sad.txt", "r")
outFile = open("data/output_baseline_scored_sad.csv", "w")

prevLine = ""

for line in inFile:
    if line[0:9] == "OUTSCORE:":
        outFile.write(prevLine[9:len(prevLine)] + ',' + line[10:(len(line)-2)] + ',')
    else:
        prevLine = line
