import argparse


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
                        '.' : 0.000001,
                        ' ': 0}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()

    print(args.file.readlines())


    analysisTable = {}
