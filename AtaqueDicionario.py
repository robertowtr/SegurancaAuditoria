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
    tryTransposicao(inputFile, dicionario)
    #tryVigenere(inputFile, dicionario)
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


def try_substituicao(input_file, dicionario):
    l1 = Util.get_count_list(Util.get_string_combination_letters(input_file, 3))
    l2 = Util.get_count_list(Util.get_string_combination_letters(dicionario, 3))
    l = Util.get_compared_lists(l1, l2)

    print(l1)
    print(l2)
    print(l)
    result = [[]]
    for i in l:
        for a, b in zip(i[0], i[1]):
            result.append((a, b))

    tabela = [["" for i in range(0, 2)] for x in range(0, 256)]

    for i in range(1, len(result)):
        if tabela[ord(result[i][0])][0] == "":
            tabela[ord(result[i][0])][0] = result[i][0]
            tabela[ord(result[i][0])][1] = result[i][1]

    output = ""
    for i in input_file:
        output += tabela[ord(i)][1]

    Util.writeFile("./saida.txt", output)
    #print(tabela)
    return output


str1 = Util.scanFile("./outputs/pg74.txt.enc")
str2 = Util.scanFile("./books/livros.txt")
#str2 = Util.scanFile("./inputs/pg74.txt")
uniqueTextWords = Util.unique_words(try_substituicao(str1, str2))
dicionario = Util.unique_words(Util.scanFile("./inputs/dictionary.txt"))
#print(try_substituicao(str1, str2))
count = len(uniqueTextWords & dicionario)
perc = count*100/len(uniqueTextWords)

print("\nAlgoritmo de Substituicao"
        "\nTotal de palavras: " + str(len(uniqueTextWords)) +
        "\nTotal de palavras encontradas: " + str(count) +
        "\n" + str(perc) + "% de acerto")
