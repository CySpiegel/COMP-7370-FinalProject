import os
import sys
from collections import OrderedDict

symbolSet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ. '
AlphaFrequencyTable = {'A':0.0805, 
                        'B': 0.0167,
                        'C': 0.0223,
                        'D': 0.0510,
                        'E': 0.1222,
                        'F': 0.0214,
                        'G': 0.0230,
                        'H': 0.0662,
                        'I': 0.0628,
                        'J': 0.0019,
                        'K': 0.0095,
                        'L': 0.0408,
                        'M': 0.0233,
                        'N': 0.0695,
                        'O': 0.0763,
                        'P': 0.0166,
                        'Q': 0.0006,
                        'R': 0.0529,
                        'S': 0.0602,
                        'T': 0.0967,
                        'U': 0.0292,
                        'V': 0.0082,
                        'W': 0.0260,
                        'X': 0.0011,
                        'Y': 0.0204,
                        'Z': 0.0006,
                        '.': 0.0079,
                        ' ': 0.1838}


def analysis(file):
    analysisTable = {}

    
    totalSymbolCount = 1
    for char in file:
        if char.upper() in symbolSet:
            totalSymbolCount += 1
            if char.upper() in analysisTable:
                analysisTable[char.upper()] += 1
            else:
                analysisTable[char.upper()] = 1

    for key, value in analysisTable.items():
        analysisTable[key] = value / totalSymbolCount
    

    probabilityOfKey = detectShiftCipher(analysisTable)

    print(probabilityOfKey)
    return analysisTable


# detects if shift cipher is valid
def detectShiftCipher(analysisTable):
    # Sort both Dictionaries by frequency table
    AlphaFrequencyTableSorted = OrderedDict(sorted(AlphaFrequencyTable.items(), key=lambda x: x[1], reverse=True))
    analysisTable = OrderedDict(sorted(analysisTable.items(), key=lambda x: x[1], reverse=True))
    symbolSet = list(AlphaFrequencyTableSorted.keys())
    encryptedSymbolSet = list(analysisTable.keys())
    
    print(symbolSet)
    print(encryptedSymbolSet)

    # loop through and build dictionary of mathing offsets
    lengthOfSet = len(symbolSet)
    offsetProbabilities  = {}
    for index in range(0, lengthOfSet):
        # get the current character
        encryptedChar = encryptedSymbolSet[index]
        unencryptedChar = symbolSet[index]

        #find how far this char is from actual space
        offset = findCharInSymbolSetOffset(encryptedChar, unencryptedChar)

        if offset != 1:
            print("offset", offset)
            print(encryptedChar, unencryptedChar)

        if offset in offsetProbabilities:
            offsetProbabilities[offset] += 1
        else:
            offsetProbabilities[offset] = 1
    offsetProbabilitiesSorted = OrderedDict(sorted(offsetProbabilities.items(), key=lambda x: x[1], reverse=True))
    return offsetProbabilitiesSorted


def findCharInSymbolSetOffset(encryptedChar, unencryptedChar):
    possibleShift = 0
    keyspaceSize = 28
    encryptedCharPos = symbolSet.index(encryptedChar)
    unencryptedCharPos = symbolSet.index(unencryptedChar)
    possibleShift = (encryptedCharPos - unencryptedCharPos) % keyspaceSize  
    return possibleShift


if __name__ == "__main__":
    inputFile = str(sys.argv[1])

    with open(str(inputFile), "r") as input:
        masterStringOriginal = input.read()
    input.close()

    encryptedFrequencyTable = analysis(masterStringOriginal)

    encryptedFrequencyTableSorted = OrderedDict(sorted(encryptedFrequencyTable.items(), key=lambda x: x[1], reverse=True))

    # for key, value in encryptedFrequencyTableSorted.items():
    #     print(key, value)

