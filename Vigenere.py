import Util


def start(fileName):
    option = Util.menuOperacao()
    if option == 1:
        cript(fileName)
    elif option == 2:
        decript(fileName)


def buildKey(key, length):
    output = key
    while (len(output) < length):
        output = output + key
    return output


def cript(fileName):
    key = Util.scan("Key: ")
    inputFile = Util.scanFile(fileName)
    key = buildKey(key, len(inputFile))

    outputText = ""
    for i in range(len(inputFile)):
        asciiCode = ord(inputFile[i]) + ord(key[i])

        if asciiCode > 255:
            asciiCode = asciiCode - 255

        outputText = outputText + chr(asciiCode)
        Util.writeFile("./saida.txt", outputText)


def decript(fileName):
    key = Util.scan("Key: ")
    inputFile = Util.scanFile(fileName)
    key = buildKey(key, len(inputFile))

    outputText = ""
    for i in range(len(inputFile)):
        asciiCode = ord(inputFile[i]) - ord(key[i])

        if asciiCode < 0:
            asciiCode = asciiCode + 255

        outputText = outputText + chr(asciiCode)
        Util.writeFile("./saida.txt", outputText)
