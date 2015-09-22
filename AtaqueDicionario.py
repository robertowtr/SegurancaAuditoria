import Util
import Cesar
import Transposicao
import itertools
import Vigenere

melhorIndice = 0
descrMelhorIndice = "Sem"

def startAttack(nomeArquivo):

    nomeEntrada = "./outputs/" + nomeArquivo + ".enc"
    nomeDicionario = "./inputs/dictionary.txt"

    inputFile = Util.scanFile(nomeEntrada)
    dicionario = Util.scanFile(nomeDicionario)

    tryCesar(inputFile, dicionario)
    #tryTransposicao(inputFile, dicionario)
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
    #l1 = Util.get_string_combination_letters3(input_file, 3)
    l2 = Util.get_count_list(Util.get_string_combination_letters(dicionario, 3))
    #l2 = Util.get_string_combination_letters3(dicionario, 3)
    l = Util.get_compared_lists(l1, l2)

    result = [[]]
    for i in l:
        for a, b in zip(i[0], i[1]):
            result.append((a, b))

    t = ["" for i in range(0, 256)]

    for i in range(1, len(result)):
        if t[ord(result[i][0])] == "":
            t[ord(result[i][0])] = result[i][1]

    output = ""
    for i in input_file:
        output += t[ord(i)]

    Util.writeFile("./saida.txt", output)
    return output


def try_substituicao_escuro():
    str1 = Util.scanFile("./outputs/pg74.txt.enc")
    str2 = Util.scanFile("./books/livros.txt")
    #str2 = Util.scanFile("./inputs/pg74.txt")
    '''uniqueTextWords = Util.unique_words(try_substituicao(str1, str2))
    dicionario = Util.unique_words(Util.scanFile("./inputs/dictionary.txt"))
    #print(try_substituicao(str1, str2))
    count = len(uniqueTextWords & dicionario)
    perc = count*100/len(uniqueTextWords)

    print("\nAlgoritmo de Substituicao - Livros"
            "\nTotal de palavras: " + str(len(uniqueTextWords)) +
            "\nTotal de palavras encontradas: " + str(count) +
            "\n" + str(perc) + "% de acerto")

    str2 = Util.scanFile("./inputs/pg74.txt")
    uniqueTextWords = Util.unique_words(try_substituicao(str1, str2))
    dicionario = Util.unique_words(Util.scanFile("./inputs/dictionary.txt"))
    #print(try_substituicao(str1, str2))
    count = len(uniqueTextWords & dicionario)
    perc = count*100/len(uniqueTextWords)

    print("\nAlgoritmo de Substituicao - Texto claro"
            "\nTotal de palavras: " + str(len(uniqueTextWords)) +
            "\nTotal de palavras encontradas: " + str(count) +
            "\n" + str(perc) + "% de acerto")

'''

    #str2 = Util.scanFile("./books/livros.txt")
    dicionario = Util.get_unique_words_and_patterns(Util.get_text_words_pattern(str2))
    #escape = Util.get_most_common_char(str1)
    #texto_escuro = Util.get_unique_words_and_patterns(Util.get_text_words_pattern(str1.replace(escape, " ")))

    print dicionario

    saida = []

    '''for i in range(1, len(texto_escuro)):
        for j in range(1, len(dicionario)):
            if dicionario[i][1] == texto_escuro[j][1]:
                saida.append(dicionario[i][0])
                print dicionario[i][1] + " " + dicionario[i][0]
'''
    #print saida
    #print(dicionario)
    #print texto_escuro





try_substituicao_escuro()