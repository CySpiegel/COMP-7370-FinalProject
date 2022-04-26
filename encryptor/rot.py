# Python 3.10
def rotate(text, rot):
    output = []
    index = 0
    for character in text:
        pos = keyspace.find(character)
        index = (pos + rot) % 26
        decryptedLetter = keyspace[index]
        output.append(decryptedLetter)
    decyptedText = ' '.join(output)
    return decyptedText



if __name__ == '__main__':
    keyspace = "ABCDEFGHIJKLMNOPQRSTUVWXYZ. "
    possiblePlaneText = []
    for i in range(0, 26):
        possiblePlaneText.append(rotate(cipherText, i))

        
    counter = 0
    for possible in possiblePlaneText:
        print("ROT:", counter, " ",possible)
        counter += 1