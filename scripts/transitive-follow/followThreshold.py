import csv
import sys

THRESHOLD = 3.5
n = 100

def readScores():
    with open('combined_first_100_no_dupe.csv', 'rb') as csvfile:
        scores = {}

        # read csv
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        # counter = 0
        for index,row in enumerate(reader):
            if index != 0:
                scores[int(row[0])] = row[1]

    return scores

def readReference():
    lst = {}

    with open('first_100.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for index,row in enumerate(reader):
            lst[index+1] = row

    return lst

allScores = readScores()
first100 = readReference()

def followScore(ID, followed, writer):
    for Bindex,score in getScores(A(ID)).items():
        if float(score) > THRESHOLD and Bindex not in followed:
            # print first100[Bindex][0] + " " + str(score) + " " + str(first100[Bindex][3])
            writer.writerow([first100[Bindex][0], str(score), str(first100[Bindex][3])])
            followed.append(Bindex)
            followScore(start(Bindex), followed, writer)

def getScores(A):
    scores = {}

    for i in range(start(A),start(A)+n):
        if i in allScores:
            scores[B(i)] = allScores[i]

    return scores

def start(A):
    return (A - 1) * n + 1

def A(ID):
    if ID % n == 0:
        return int(ID / n)
    else:
        return int(ID / n) + 1

def B(ID):
    if (ID % n) == 0:
        return n
    else:
        return ID % n

for i in range(1,101):
    with open("output/output" + str(i).zfill(3) + ".csv", 'w') as o_file:
        writer = csv.writer(o_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['ID', 'Similarity', 'Requirement'])
        followScore(start(i), [], writer)
