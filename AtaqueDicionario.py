import Util
import Cesar
import Transposicao
import Vigenere

melhorIndice = 0
descrMelhorIndice = "Sem"

def startAttack(nomeArquivo):

    nomeEntrada = "./outputs/" + nomeArquivo + ".enc"
    nomeDicionario = "./inputs/dictionary.txt"

    inputFile = Util.scanFile(nomeEntrada)
    dicionario = Util.scanFile(nomeDicionario)

    tryCesar(inputFile, dicionario)
    print(descrMelhorIndice)

def tryCesar(inputFile, dicionario):

    bestKey = 0
    bestKeyCount = 0
    wordsCount = 0
    count = 0
    for i in range(0, 256):
        uniqueTextWords = Util.unique_words(Cesar.decript2(inputFile, i))

        for word in uniqueTextWords:
            if word in dicionario:
                count += 1
        if count > bestKeyCount:
            bestKey = i
            bestKeyCount = count
            wordsCount = len(uniqueTextWords)
            count = 0

    perc = bestKeyCount*100/wordsCount
    if perc > melhorIndice:
        descrMelhorIndice = ("\nAlgoritmo de Cesar"
                              "\nChave: " + str(bestKey) +
                              "\nTotal de palavras: " + str(wordsCount) +
                              "\nTotal de palavras encontradas: " + str(bestKeyCount) +
                              "\n" + str() + "% de acerto" )
