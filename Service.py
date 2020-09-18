import numpy as np

def getNumber(keyLetter):
    keysAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    i = 0
    for k in keysAlphabet:
        if k == keyLetter:
            return i
        i += 1
    raise Exception("Wrong key letter [", keyLetter, "]")


def multipyMatrix(encMatrixWorker, keyMatrix, base):
    result = [[0 for j in range(1)] for i in range(2)]
    result[0][0] = (encMatrixWorker[0][0] * keyMatrix[0][0] + encMatrixWorker[1][0] * keyMatrix[0][1]) % base
    result[1][0] = (encMatrixWorker[0][0] * keyMatrix[1][0] + encMatrixWorker[1][0] * keyMatrix[1][1]) % base
    return result


def getChar(number, base):
    keysAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number > base:
        raise Exception("Wrong letter number [", number, "]")
    return keysAlphabet[number]


def encrypt(text, key):
    keysAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keysAlphabetBase = len(keysAlphabet)

    keyValidated = key.upper()
    textValidated = text.upper()
    lenText = len(text)
    result = []

    paddingZ = "Z"

    encText = [0 for e in range(lenText)]
    keyMatrix = [[0 for j in range(2)] for i in range(2)]
    encMatrixWorker = [[0 for j in range(1)] for i in range(2)]

    if len(keyValidated) != 4:
        raise Exception("Wrong key length. Key must consist of 4 letters")

    keyMatrix[0][0] = getNumber(keyValidated[0])
    keyMatrix[0][1] = getNumber(keyValidated[1])
    keyMatrix[1][0] = getNumber(keyValidated[2])
    keyMatrix[1][1] = getNumber(keyValidated[3])

    print (keyMatrix)

    # Remove all spaces
    textValidated = textValidated.replace(' ','')
    # Add padding Z if odd number
    if lenText % 2 != 0:
        textValidated = textValidated + paddingZ

    i = 0
    for c in textValidated:
        encText[i] = getNumber(c)
        i += 1
    print (encText)

    i = 0
    while i < lenText:
        encMatrixWorker[0][0] = encText[i]
        encMatrixWorker[1][0] = encText[i+1]

        encChunk = multipyMatrix(encMatrixWorker, keyMatrix, keysAlphabetBase)
        result.append(getChar(encChunk[0][0], keysAlphabetBase))
        result.append(getChar(encChunk[1][0], keysAlphabetBase))
        i +=2

    return ''.join(result)