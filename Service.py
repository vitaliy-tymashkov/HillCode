import re

KEYS_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY_BASE = len(KEYS_ALPHABET)
KEY_LENGTH = 4
PADDING_Z = "Z"

############################################
def getNumber(letter):
    i = 0
    for k in KEYS_ALPHABET:
        if k == letter:
            return i
        i += 1
    raise Exception("Wrong letter [", letter, "]")

############################################
def multipyMatrix(encMatrixWorker, keyMatrix, base):
    result = [[0 for j in range(1)] for i in range(2)]
    result[0][0] = (encMatrixWorker[0][0] * keyMatrix[0][0] + encMatrixWorker[1][0] * keyMatrix[0][1]) % base
    result[1][0] = (encMatrixWorker[0][0] * keyMatrix[1][0] + encMatrixWorker[1][0] * keyMatrix[1][1]) % base
    return result

############################################
def getChar(number, base):
    keysAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number > base:
        raise Exception("Wrong letter number [", number, "]")
    return keysAlphabet[number]

############################################
def fillKeyMatrix(keyMatrix, keyValidated):
    keyMatrix[0][0] = getNumber(keyValidated[0])
    keyMatrix[0][1] = getNumber(keyValidated[1])
    keyMatrix[1][0] = getNumber(keyValidated[2])
    keyMatrix[1][1] = getNumber(keyValidated[3])
    return keyMatrix

############################################
def checkKeyLength(keyValidated):
    if len(keyValidated) != KEY_LENGTH:
        raise Exception("Wrong key length. Key must consist of " + KEY_LENGTH + " letters")

############################################
def validatePlainText(textValidated):
    # Remove all not alphabet symbols
    reg = re.compile('[^a-zA-Z]')
    textValidated = reg.sub('', textValidated)
    # Add padding Z if odd number
    if len(textValidated) % 2 != 0:
        textValidated = textValidated + PADDING_Z
    return textValidated

############################################
def fillEncNumbersArray(encNumbersArray, textValidated):
    i = 0
    for c in textValidated:
        encNumbersArray[i] = getNumber(c)
        i += 1
    return encNumbersArray

############################################
def encodeChunks(result, encNumbersArray, keyMatrix):
    encMatrixChunk = [[0 for j in range(1)] for i in range(2)]
    i = 0
    while i < len(encNumbersArray):
        encMatrixChunk[0][0] = encNumbersArray[i]
        encMatrixChunk[1][0] = encNumbersArray[i+1]

        encChunk = multipyMatrix(encMatrixChunk, keyMatrix, KEY_BASE)
        result.append(getChar(encChunk[0][0], KEY_BASE))
        result.append(getChar(encChunk[1][0], KEY_BASE))
        i +=2
    return result

############################################
def encrypt(text, key):
    result = []
    keyValidated = key.upper()
    textValidated = text.upper()
    keyMatrix = [[0 for j in range(2)] for i in range(2)]

    checkKeyLength(keyValidated)
    keyMatrix = fillKeyMatrix(keyMatrix, keyValidated)
    textValidated = validatePlainText(textValidated)

    encNumbersArray = [0 for e in range(len(textValidated))]
    encNumbersArray = fillEncNumbersArray(encNumbersArray, textValidated)
    result = encodeChunks(result, encNumbersArray, keyMatrix)
    return ''.join(result)