import Util

def start(fileName):
    option = Util.menuOperacao()
    if option == 1:
        cript(fileName)
    elif option == 2:
        decript(fileName)

def cript(fileName):
    key = int(Util.scan("Key: "))
    inputFile = Util.scanFile(fileName)
    outputText = ""

    for i in range(len(inputFile)):
        asciiCode = ord(inputFile[i]) + key
        if asciiCode > 255:
            asciiCode = asciiCode - 255

        outputText = outputText + chr(asciiCode)

    Util.writeFile("./saida.txt", outputText)

def decript(fileName):
    key = int(Util.scan("Key: "))
    inputFile = Util.scanFile(fileName)
    outputText = ""

    for i in range(len(inputFile)):
        asciiCode = ord(inputFile[i]) - key
        if asciiCode < 0:
            asciiCode = asciiCode + 255

        outputText = outputText + chr(asciiCode)

    Util.writeFile("./saida.txt", outputText)