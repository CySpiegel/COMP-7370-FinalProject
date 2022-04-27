# Modified Simple Substitution Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import sys, random
argument0 = str(sys.argv[0])
inputFile = str(sys.argv[1])
outputFile = str(sys.argv[2])

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .'

def main():
    # myMessage = '''
# You should copy some other gutenberg books in here to test on a known plaintext-ciphertext mapping!
# '''

    # Read encrypted book 
    with open(str(inputFile), "r") as input:
        myMessage = input.read()
    input.close()

    file1 = open(outputFile,"w") 
    



    # myKey = 'OUCJISRYF KNZGALWMHD.VQEXTBP'
    
    
    l = list(LETTERS)
    random.shuffle(l)
    myKey = ''.join(l)


    myMode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.

    if not keyIsValid(myKey):
        sys.exit('There is an error in the key or symbol set.')
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The %sed message is:' % (myMode))
    # print(translated)
    #pyperclip.copy(translated)
    # print()
    file1.write(translated)
    file1.close()


def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    return keyList == lettersList


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
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


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
