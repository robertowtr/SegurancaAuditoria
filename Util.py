from collections import Counter


def scan(message):
   input = raw_input(message)
   return input


def scanFile(path):
    file = open(path, 'r')
    string = file.read()
    file.close()
    return string

def writeFile(path, message):
    file = open(path, "w")
    file.write(message)
    file.close()

def menuAlgoritmo():
    option = scan("\nEscolha o algoritmo de criptografia"
                  "\n1 - Cesar"
                  "\n2 - Transposicao"
                  "\n3 - Vigenere"
                  "\n4 - Substituicao"
                  "\n5 - Quebrar Cifra"
                  "\n6 - Ataque Dicionario"
                  "\n0 - Sair\n")
    return int(option)

def menuOperacao():
    option = scan("\n1 - Criptografar"
                  "\n2 - Descriptografar\n")
    return int(option)

def menuSubstituicao():
    option = scan("\n1 - Criptografar"
                  "\n2 - Descriptografar"
                  "\n3 - Gerar tabela\n")
    return int(option)

from string import punctuation


def unique_words(sentence):
    return set(sentence.translate(None, punctuation).lower().split())


def get_string_combination_letters(string, size):
    result = []
    limit = len(string) - size + 1
    for i in range(0, limit):
        result.append(string[i:i+size])
    return result


def get_count_list(_list):
    return Counter(_list)


def get_compared_lists(_list1, _list2):
    _list1 = sorted(zip(_list1.itervalues(), _list1.iterkeys()), reverse=True)
    _list2 = sorted(zip(_list2.itervalues(), _list2.iterkeys()), reverse=True)
    _ret = []
    for a, b in zip(_list1, _list2):
        _ret.append((a[1], b[1]))
    return _ret
