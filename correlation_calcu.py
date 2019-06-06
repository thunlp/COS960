from numpy import linalg
import numpy as np
import scipy.stats as stats
import sys

wordvecFile = sys.argv[1]
wordVecDict = {}
file = open(wordvecFile, 'r', encoding='utf-8', errors='ignore')
print_writer_filename = sys.argv[2]
fprint = open(print_writer_filename, 'a', encoding='utf-8')
# tmp = file.readline()
num = 0
for line in file:
    num += 1
    if num % 1000 == 0:
        print("Reading the %d-th word" % num)

    items = line.strip().split()
    items = [item.strip('[],') for item in items]
    word = items[0]
    vec = list(map(float, items[1:]))
    if linalg.norm(vec) != 0:
        wordVecDict[word] = vec / linalg.norm(vec)
file.close()
print('Word embeddings reading completes and total number of words is:', num)
fprint.write('Word embeddings reading completes and total number of words is:'+str(num)+'\n\n')

for cos in ['COS960_all.txt',
            'COS960_adj.txt',
            'COS960_noun.txt',
            'COS960_verb.txt']:
    file = open(cos, 'r', encoding='utf-8')
    testPairNum = 0
    skipPairNum = 0

    wordSimStd = []
    wordSimPre = []
    for line in file:
        word1, word2, valStr = line.strip().split()[0:3]
        if (word1 in wordVecDict) and (word2 in wordVecDict):
            testPairNum += 1
            wordSimStd.append(float(valStr))
            wordVec1 = wordVecDict[word1]
            wordVec2 = wordVecDict[word2]
            cosSim = np.dot(wordVec1, wordVec2) / np.linalg.norm(wordVec1) / np.linalg.norm(wordVec2)
            wordSimPre.append(cosSim)
        else:
            skipPairNum += 1
            print('Skip:', word1, word2)
            fprint.write('Skip: ' + word1 + '  ' + word2 + ' \n')
    corrCoef = np.corrcoef(wordSimStd, wordSimPre)[0, 1]
    SpearCoef = stats.spearmanr(wordSimStd, wordSimPre).correlation
    SqrtCoef = np.sqrt(corrCoef * SpearCoef)
    print(wordvecFile + ' on ' + cos[-15:])
    print("WordSim960 Pearson Score:" + str(corrCoef))
    print("WordSim960 Spearman Score:" + str(SpearCoef))
    print("WordSim960 Sqrt of r and rho Score:" + str(SqrtCoef))
    print('TestPair:', testPairNum, 'SkipPair:', skipPairNum)
    print()
    fprint.write(wordvecFile + ' on ' + cos[-15:])
    fprint.write("WordSim960 Pearson Score:" + str(corrCoef) + '\n')
    fprint.write("WordSim960 Spearman Score:" + str(SpearCoef) + '\n')
    fprint.write("WordSim960 Sqrt of r and rho Score:" + str(SqrtCoef) + '\n')
    fprint.write('TestPair:' + str(testPairNum) + 'SkipPair:' + str(skipPairNum) + '\n\n')
    file.close()

fprint.close()
