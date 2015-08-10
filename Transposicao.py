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

    lines = key
    columns = int(len(inputFile) / key)

    if (len(inputFile) / key) != 0 and lines != len(inputFile):
        columns += 1

    matrix = [['a' for i in xrange(0, lines)] for i in xrange(0, columns)]

    idxLinhas = [i for i in xrange(0, lines)]
    idxColunas = [i for i in xrange(0, columns)]

    idx = 0
    for i in idxColunas:
        for j in idxLinhas:
            if idx < len(inputFile):
                matrix[i][j] = inputFile[idx]
                idx += 1
            else:
                matrix[i][j] = '\0'

    for j in idxLinhas:
        for i in idxColunas:
            if matrix[i][j] != '\0':
                outputText += matrix[i][j]

    Util.writeFile("./saida.txt", outputText)

def decript(fileName):
    key = int(Util.scan("Key: "))
    inputFile = Util.scanFile(fileName)
    outputText = ""

    lines = key
    columns = int(len(inputFile) / key)

    if (len(inputFile) / key) != 0 and lines != len(inputFile):
        columns += 1

    matrix = [['a' for i in xrange(0, lines)] for i in xrange(0, columns)]

    idxLinhas = [i for i in xrange(0, lines)]
    idxColunas = [i for i in xrange(0, columns)]

    idx = 0

    for j in idxLinhas:
        for i in idxColunas:
            if idx < len(inputFile):
                matrix[i][j] = inputFile[idx]
                idx += 1
            else:
                matrix[i][j] = '\0'

    print(matrix)

    for j in idxLinhas:
        for i in idxColunas:
            print(matrix[i][j])
            if matrix[i][j] != '\0':
                outputText += matrix[i][j]

    Util.writeFile("./saida.txt", outputText)