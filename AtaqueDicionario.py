import Util
import Cesar
import Transposicao
import itertools
import Vigenere
import datetime

melhorIndice = 0
descrMelhorIndice = "Sem"

def startAttack(nomeArquivo):

    nomeEntrada = "./outputs/" + nomeArquivo + ".enc"
    nomeDicionario = "./inputs/dictionary.txt"

    inputFile = Util.scanFile(nomeEntrada)
    dicionario = Util.scanFile(nomeDicionario)

    #tryCesar(inputFile, dicionario)
    #tryTransposicao(inputFile, dicionario)
    tryVigenere(inputFile, dicionario)
    #print(descrMelhorIndice)

def tryCesar(inputFile, dicionario):

    bestKey = 0
    bestKeyCount = 0
    setDicionario = Util.unique_words(dicionario)
    perc = 0
    for i in range(0, 256):
        uniqueTextWords = Util.unique_words(Cesar.decript2(inputFile, i))
        count = len(uniqueTextWords & setDicionario)
        print("key: " + str(i) + " total: " + str(count))
        if count > bestKeyCount:
            bestKey = i
            bestKeyCount = count
            wordsCount = len(uniqueTextWords)
            perc = (bestKeyCount*100)/wordsCount
        if perc > 50:
            break

    if perc > melhorIndice:
        print("\nAlgoritmo de Cesar"
                              "\nChave: " + str(bestKey) +
                              "\nTotal de palavras: " + str(wordsCount) +
                              "\nTotal de palavras encontradas: " + str(bestKeyCount) +
                              "\n" + str(perc) + "% de acerto" )


def tryTransposicao(inputFile, dicionario):

    bestKey = 0
    bestKeyCount = 0
    setDicionario = Util.unique_words(dicionario)
    perc = 0

    for i in range(1, len(inputFile)):
        uniqueTextWords = Util.unique_words(Transposicao.decript2(inputFile, i))
        count = len(uniqueTextWords & setDicionario)
        if count > bestKeyCount:
            bestKey = i
            bestKeyCount = count
            wordsCount = len(uniqueTextWords)
            perc = (bestKeyCount*100)/wordsCount
        #if perc > 50:
         #   break


    if perc > melhorIndice:
        print("\nAlgoritmo de Transposicao"
                              "\nChave: " + str(bestKey) +
                              "\nTotal de palavras: " + str(wordsCount) +
                              "\nTotal de palavras encontradas: " + str(bestKeyCount) +
                              "\n" + str(perc) + "% de acerto" )



def tryVigenere(input_file, dicionario):
    bestKey = ''
    bestKeyCount = 0
    setDicionario = Util.unique_words(dicionario)
    perc = 0
    #list_chars = ['a','b','c','d']
    list_chars = ['1','2','3','4','5','6']

    for sizeKey in range(1, len(list_chars)+1):
        for i in itertools.product(list_chars, repeat=sizeKey):
            print(i)
            uniqueTextWords = Util.unique_words(Vigenere.decript3(input_file[0:400], i))
            #uniqueTextWords = set(Vigenere.decript3(input_file, i).split())
            count = len(uniqueTextWords & setDicionario)
            if count > bestKeyCount:
                bestKey = i
                bestKeyCount = count
                wordsCount = len(uniqueTextWords)
                perc = (bestKeyCount*100)/wordsCount

    if perc > melhorIndice:
        print("\nAlgoritmo de Transposicao"
                                  "\nChave: " + str(bestKey) +
                                  "\nTotal de palavras: " + str(wordsCount) +
                                  "\nTotal de palavras encontradas: " + str(bestKeyCount) +
                                  "\n" + str(perc) + "% de acerto" )