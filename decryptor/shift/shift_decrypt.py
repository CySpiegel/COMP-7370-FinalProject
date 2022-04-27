##############################################################
# Definition: Brute force shift ciphers, ceaser/rot/etc.
# Team: Matthew Stroble and Hannah Reinbolt
# Date: 4-24-2022
##############################################################

# libraries
import decryptor.shift.best_guess as bg


# rotate characters through every possible keyspace iteration
def rotate(text, rot, keyspace):
    output = []
    index = 0
    for character in text:
        # apply brute force to characters in keymap
        if character.upper() in keyspace:
            pos = keyspace.find(character.upper())
            index = (pos - rot) % 28
            decryptedLetter = keyspace[index]
            output.append(decryptedLetter)

        # ignore characters that are not in keymap
        else:
            output.append(character.upper())
    decyptedText = ''.join(output)
    return decyptedText


# brute force all combinations
def decrypt_shift(file_path):
    # variables
    cipherText = ""
    guess = {}

    # open end file and best guess files
    result = open("results/solution.txt", 'a')
    best_guess = open("results/best_guess.txt", 'a')
    result.truncate(0)
    best_guess.truncate(0)

    # open file
    with open(str(file_path), "r") as input:
        cipherText = input.read()
    input.close()

    # perform brute force
    keyspace = "ABCDEFGHIJKLMNOPQRSTUVWXYZ. "
    possiblePlaneText = []
    for i in range(0, 28):
        possiblePlaneText.append(rotate(cipherText, i, keyspace))
    counter = 0

    # print every possible decryption
    for possible in possiblePlaneText:
        answer = "ROT:" +  str(counter) + " " + str(possible)
        result.write(answer)

        # check for best guess
        guess = bg.count_words(possible, counter, guess)
        
        # count main iterations
        counter += 1

    # add final best guess
    #print(guess)
    final_guess = bg.calc_best_guess(guess)
    winner = "KEY: " + str(final_guess[0]) + " " + str(final_guess[1])
    best_guess.write(winner)

    # close files
    best_guess.close()
    result.close()


