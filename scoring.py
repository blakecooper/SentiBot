from typing import List

import nltk

# dictionary to store the DM++ scores
dm = {}

# array of arrays, each one the average scores for a line
scores = []

# array of arrays, each one the distance in sentiment for each turn in conversation
distances = []

# parse DepecheMood++
print("Opening DepecheMood++ data...")
dmFile = open("dm++.tsv", "r")
for line in dmFile:
    wordList: List[str] = line.split('\t')
    dm[wordList[0]] = [float(wordList[1]), float(wordList[2]), float(wordList[3]), float(wordList[4]),
                       float(wordList[5]), float(wordList[6]), float(wordList[7])]
print("Number of lexical items added:")
print(len(dm))

# tokenize each line to score, score each word, get average scores, add them to the array
print("Scoring data...")
scoringFile = open("output_unscored.txt", "r")
for line in scoringFile:
    wordsInLine = nltk.word_tokenize(line)
    mood = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    numScores = 0
    for word in wordsInLine:
        if word in dm:
            for i in range(0, 7):
                mood[i] = mood[i] + dm[word][i]
                numScores = numScores + 1
    for i in mood:
        if (numScores > 0):
            i = i / numScores
    scores.append(mood)
print('Number of lines scored:')
print(len(scores))

# get distances for each turn
print("Calculating distances in each turn...")
for x in range(0, len(scores)):
    distance = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    if ((2 * x) + 1) < len(scores):
        for i in range(0, 7):
            distance[i] = abs(scores[(2 * x) + 1][i] - scores[2 * x][i])
        distances.append(distance)
print("Turns analyzed for distance:")
print(len(distances))

# compute average
print("Computing average distances...")
averages = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
for x in range(0, 7):
    for arr in distances:
        averages[x] = averages[x] + arr[x]
    averages[x] = averages[x] / len(distances)
print("Average mood distances:")
print(averages)
