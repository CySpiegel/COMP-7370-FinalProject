import sys, simpleSubCipher, simpleSubHacker
from collections import OrderedDict


# Global defined variables
symbolSet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .'

# argument0 = str(sys.argv[0])
inputFile = str(sys.argv[1])
outputFile = str(sys.argv[2])
masterStringOriginal = ""

encryptedCharacterFrequancyDictionary = {} 

# Most common frequancy
frequancyTable = [' ','E','T','A','O','N','I','H','S','R','D','L','U','M','C','W','F','Y','G','P','B','.','V','K','J','X','Q','Z']
gutenbergString = "START OF THIS PROJECT GUTENBERG"
gutenbergStringAlternate = "START OF THE PROJECT GUTENBERG"
ebookMarker = "EBook"
encryptedPeriodFreq = {}

def swapCharInDecryptionKey(encryptedCharMap, indexA, indexB):
    encryptedCharMap[indexA], encryptedCharMap[indexB] = encryptedCharMap[indexB], encryptedCharMap[indexA]
    return encryptedCharMap

def decryptMessage(key, encrypCharFreq, message):
    return translateMessage(key, encrypCharFreq, message, 'decrypt')

def translateMessage(currentDecryptionKey, encrypCharFreq, message, mode):
    translated = ''
    print("currentDecrypt key: ", currentDecryptionKey)
    charsA = currentDecryptionKey
    charsB = encrypCharFreq
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # Loop through each symbol in message:
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Symbol is not in LETTERS; just add it
            translated += symbol

    return translated




if __name__ == '__main__':

    # Read encrypted book 
    with open(str(inputFile), "r") as input:
        masterStringOriginal = input.read()
    input.close()


    # Loop through masterStringOriginal and store all uppercase variants into dictionary.
    for keys in masterStringOriginal:
        if keys.upper() in symbolSet:
            encryptedCharacterFrequancyDictionary[keys.upper()] = encryptedCharacterFrequancyDictionary.get(keys.upper(), 0) + 1

    # Sort encrypted
    encryptedCharacterFrequancySorted = OrderedDict(sorted(encryptedCharacterFrequancyDictionary.items(), key=lambda x: x[1], reverse=True))
    encryptedCharacterFrequencymap = list(encryptedCharacterFrequancySorted.keys())

    # index = 0
    # for k, v in encryptedCharacterFrequancySorted.items():
    #     print(frequancyTable[index], ": ", k, ": ", encryptedCharacterFrequencymap[index], index)
    #     index += 1


    # Finding WWW. if present, if found short circuit decrypting HTTP://www.
    if(masterStringOriginal.find("://")):
        location = masterStringOriginal.find("://")
        # print(location)
        startOfWWW = masterStringOriginal[location + 3]
        # match pattern if found
        if masterStringOriginal[location + 3] == startOfWWW and masterStringOriginal[location + 4] == startOfWWW and masterStringOriginal[location + 5] == startOfWWW:
            wLocation = frequancyTable.index('W')
            encCharForWindex = encryptedCharacterFrequencymap.index(startOfWWW.upper())
            swapCharInDecryptionKey(frequancyTable, wLocation, encCharForWindex)
            
            # www was found so . must also exist in predicted spot
            encPeriodCharacter = masterStringOriginal[location + 6]
            encCharForPeriodIndex = encryptedCharacterFrequencymap.index(encPeriodCharacter.upper())
            periodLocationIndex = frequancyTable.index('.')
            swapCharInDecryptionKey(frequancyTable, periodLocationIndex, encCharForPeriodIndex)

            # finding H
            encryptedHcharacter = masterStringOriginal[location - 4]
            encCharForHindex = encryptedCharacterFrequencymap.index(encryptedHcharacter.upper())
            planeTextHcharacterIndex = frequancyTable.index('H')
            swapCharInDecryptionKey(frequancyTable, planeTextHcharacterIndex, encCharForHindex)


            # Finding TT
            encryptedTcharacter = masterStringOriginal[location - 3]
            encCharForTindex = encryptedCharacterFrequencymap.index(encryptedTcharacter.upper())
            planeTextTcharacterIndex = frequancyTable.index('T')
            swapCharInDecryptionKey(frequancyTable, planeTextTcharacterIndex, encCharForTindex)
            
            # Finding P
            encryptedPcharacter = masterStringOriginal[location - 1]
            encCharForPindex = encryptedCharacterFrequencymap.index(encryptedPcharacter.upper())
            planeTextPcharacterIndex = frequancyTable.index('P')
            swapCharInDecryptionKey(frequancyTable, planeTextPcharacterIndex, encCharForPindex)
    
    safetyAdvanced = 0
    indexLocationOfStar = masterStringOriginal.find("***")
    if(masterStringOriginal[indexLocationOfStar + 4] == "*"):
        print("Safety Triggered")
        safetyAdvanced = 505
    else:
        safetyAdvanced = masterStringOriginal.find("***")

    # Locating astrisk pattern
    if(masterStringOriginal.find("***", safetyAdvanced)):
        starLocation = masterStringOriginal.find("***", safetyAdvanced)
        # Checking if first character matches found encrypted character for space if not its the start of S
        if (masterStringOriginal[starLocation + 3].upper() == encryptedCharacterFrequencymap[0]):
            encryptedGutenbergString = masterStringOriginal[starLocation + 4 : (starLocation + 4) + 31]
            # Check if pattern has been matched, if found its the gutenberString if not check for gutenbergStringAlternate
            if(encryptedGutenbergString[1] == encryptedGutenbergString[4] == encryptedGutenbergString[9] == encryptedGutenbergString[20]):
                if (len(encryptedGutenbergString) == len(gutenbergString)):
                    for i in range(0, len(gutenbergString)):
                        decryptedLetterIndex = frequancyTable.index(gutenbergString[i].upper())
                        encryptedCharacterIndex = encryptedCharacterFrequencymap.index(encryptedGutenbergString[i].upper())
                        swapCharInDecryptionKey(frequancyTable, decryptedLetterIndex, encryptedCharacterIndex)
            else:
                encryptedGutenbergString = masterStringOriginal[starLocation + 3 : (starLocation + 3) + 30]
                if(encryptedGutenbergString[1] == encryptedGutenbergString[4] == encryptedGutenbergString[9] == encryptedGutenbergString[19]):
                    if (encryptedGutenbergString[5] == encryptedGutenbergString[13]):
                        print("GutenBerg String Found")
                    elif (encryptedGutenbergString[5] == encryptedGutenbergString[12]):
                        print("Gutenberg alternate string found")
                    if (len(encryptedGutenbergString) == len(gutenbergStringAlternate)):
                        for i in range(0, len(gutenbergStringAlternate)):
                            decryptedLetterIndex = frequancyTable.index(gutenbergStringAlternate[i].upper())
                            encryptedCharacterIndex = encryptedCharacterFrequencymap.index(encryptedGutenbergString[i].upper())
                            swapCharInDecryptionKey(frequancyTable, decryptedLetterIndex, encryptedCharacterIndex)
        # checking gutenberg string without a space after ***
        else:
            encryptedGutenbergString = masterStringOriginal[starLocation + 3 : (starLocation + 3) + 31]
            if(encryptedGutenbergString[1] == encryptedGutenbergString[4] == encryptedGutenbergString[9] == encryptedGutenbergString[20]):
                if (encryptedGutenbergString[5] == encryptedGutenbergString[13]):
                    print("GutenBerg String Found right after space")
                elif (encryptedGutenbergString[5] == encryptedGutenbergString[12]):
                    print("Gutenberg alternate string found")
                if (len(encryptedGutenbergString) == len(gutenbergString)):
                    for i in range(0, len(gutenbergString)):
                        decryptedLetterIndex = frequancyTable.index(gutenbergString[i].upper())
                        encryptedCharacterIndex = encryptedCharacterFrequencymap.index(encryptedGutenbergString[i].upper())
                        swapCharInDecryptionKey(frequancyTable, decryptedLetterIndex, encryptedCharacterIndex)
            
            else:
                # testing alternate string
                encryptedGutenbergString = masterStringOriginal[starLocation + 3 : (starLocation + 3) + 30]
                if(encryptedGutenbergString[1] == encryptedGutenbergString[4] == encryptedGutenbergString[9] == encryptedGutenbergString[19]):
                    if (encryptedGutenbergString[5] == encryptedGutenbergString[13]):
                        print("GutenBerg String Found")
                    elif (encryptedGutenbergString[5] == encryptedGutenbergString[12]):
                        print("Gutenberg alternate string found")
                    if (len(encryptedGutenbergString) == len(gutenbergStringAlternate)):
                        for i in range(0, len(gutenbergStringAlternate)):
                            decryptedLetterIndex = frequancyTable.index(gutenbergStringAlternate[i].upper())
                            encryptedCharacterIndex = encryptedCharacterFrequencymap.index(encryptedGutenbergString[i].upper())
                            swapCharInDecryptionKey(frequancyTable, decryptedLetterIndex, encryptedCharacterIndex)
                else:
                    print("failed alternate check")

    # # Printing index of frequancy table and compairing to encrypted character frequancy table
    # index = 0
    # for k, v in encryptedCharacterFrequancySorted.items():
    #     print(frequancyTable[index], ": ", k, ": ", encryptedCharacterFrequencymap[index], index)
    #     index += 1


    # Locating Ebook
    # locationOfFirstOpenBracket = masterStringOriginal.find("[")
    # encryptedEbookMarkerString = masterStringOriginal[locationOfFirstOpenBracket + 1 : (locationOfFirstOpenBracket + 6)]
    # if (masterStringOriginal.find('[')):
    #     for i in range(0, len(ebookMarker)):
    #         decryptedLetterIndex = frequancyTable.index(ebookMarker[i].upper())
    #         encryptedCharacterIndex = encryptedCharacterFrequencymap.index(encryptedEbookMarkerString[i].upper())
    #         swapCharInDecryptionKey(frequancyTable, decryptedLetterIndex, encryptedCharacterIndex)




    # Decrypt with current key
    encryptCharFreq = ''.join(encryptedCharacterFrequencymap)
    myKey = ''.join(frequancyTable)
    # print(myKey)
    translated = decryptMessage(myKey, encryptCharFreq, masterStringOriginal)
    
    zipped_pairs = zip(myKey, encryptCharFreq) 
    z = [x for _, x in sorted(zipped_pairs)]
    
    decryptedList = z[2:].copy()
    decryptedList.append(z[0])
    decryptedList.append(z[1])
    print("Symbol Set: ", symbolSet)
    print("Key: ",''.join(decryptedList))

    # translated2 = simpleSubCipher.decryptMessage(''.join(frequancyTable), translated)
    # letterMapping = simpleSubHacker.hackSimpleSub(translated2)
    # translatedDecryption = simpleSubHacker.decryptWithCipherletterMapping(translated, letterMapping)
    # letterList = list(symbolSet)
    # decryptionKey = []

    # for i in range(0, len(symbolSet)):
    #     indexedEncrypt = letterList.index(encryptCharFreq[i].upper())
    #     decryptionKey.append(frequancyTable[indexedEncrypt])

    # print(symbolSet)
    # decryptedKey = ''.join(decryptionKey)
    # print(encryptCharFreq)



    translated = simpleSubCipher.decryptMessage(''.join(decryptedList), masterStringOriginal)
    letterMapping = simpleSubHacker.hackSimpleSub(translated)
    translatedDecryption = simpleSubHacker.decryptWithCipherletterMapping(translated, letterMapping)

    file1 = open(outputFile,"w")

    file1.write(translatedDecryption)
    file1.close()


    # print(encryptedCharacterFrequencymap.index('A'))

