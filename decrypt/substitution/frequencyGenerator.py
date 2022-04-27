
import os
import glob
from collections import OrderedDict

symbolSet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .'
path = 'unencryptedBooks/'

encryptedCharacterFrequancyDictionary = {} 
letterCountTotal = 0
# For loop to loop through all files in unEncryptedBooks
for infile in glob.glob( os.path.join(path, '*.*') ):
    masterStringOriginal = ""
    with open(str(infile), "r") as input:
        masterStringOriginal = input.read()
        # print(masterStringOriginal)

    # Loop through masterStringOriginal and store all uppercase variants into dictionary.
    for keys in masterStringOriginal:
        letterCountTotal+= 1
        if keys.upper() in symbolSet:
            encryptedCharacterFrequancyDictionary[keys.upper()] = encryptedCharacterFrequancyDictionary.get(keys.upper(), 0) + 1

    input.close()


for k, v in encryptedCharacterFrequancyDictionary.items():
    encryptedCharacterFrequancyDictionary[k] = (v/(letterCountTotal * 1.0))

encryptedCharacterFrequancySorted = OrderedDict(sorted(encryptedCharacterFrequancyDictionary.items(), key=lambda x: x[1], reverse=True))


print(encryptedCharacterFrequancySorted)
print(letterCountTotal)

# OrderedDict([(' ', 26749108), ('E', 14963342), ('T', 11004714), ('A', 9637706), ('O', 9299702), ('N', 8296209), ('I', 8250878), ('H', 7850330), ('S', 7600680), ('R', 6993983), ('D', 5279818), ('L', 4854018), ('U', 3454043), ('M', 3130459), ('C', 2870764), ('W', 2753967), ('F', 2706148), ('Y', 2435757), ('G', 2397394), ('P', 2011450), ('B', 1808052), ('.', 1412530), ('V', 1211719), ('K', 925755), ('J', 190643), ('X', 182038), ('Q', 125763), ('Z', 75821)])
# 156971314

# OrderedDict([(' ', 0.17040761982791328), ('E', 0.09532532804051064), ('T', 0.07010652914582852), ('A', 0.06139788063441961), ('O', 0.05924459548067489), ('N', 0.05285175226347408), ('I', 0.05256296701446992), ('H', 0.05001123963324917), ('S', 0.04842082165407623), ('R', 0.04455580336162568), ('D', 0.03363555967939467), ('L', 0.030922962140713176), ('U', 0.022004294364255623), ('M', 0.01994287312903554), ('C', 0.018288462565841806), ('W', 0.01754439667874603), ('F', 0.01723976139997146), ('Y', 0.015517210998182764), ('G', 0.015272816025480937), ('P', 0.012814124751481663), ('B', 0.011518359335387866), ('.', 0.008998650543245118), ('V', 0.007719365845405358), ('K', 0.005897606233964506), ('J', 0.0012145085311574828), ('X', 0.0011596895978076606), ('Q', 0.0008011846037040883), ('Z', 0.00048302456078057674)])


