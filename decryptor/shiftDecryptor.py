# Python 3.10
import sys

def rotate(text, rot):
    output = []
    index = 0
    for character in text:
        if character.upper() in keyspace:
            pos = keyspace.find(character.upper())
            index = (pos - rot) % 28
            decryptedText = keyspace[index]
            output.append(decryptedText)
        else:
             output.append(character.upper())
    decryptedText = ''.join(output)
    return decryptedText



if __name__ == '__main__':
    keyspace = "ABCDEFGHIJKLMNOPQRSTUVWXYZ. "
    inputFile = str(sys.argv[1])
    rotKey = int(str(sys.argv[2]))


    with open(str(inputFile), "r") as input:
        planeText = input.read()
    input.close()

    outputFile = inputFile + ".decrypted"
    decryptedText = rotate(planeText, rotKey)
    f = open(outputFile, 'w')
    f.write(decryptedText)
    f.close
    print(decryptedText)
