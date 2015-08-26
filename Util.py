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
                  "\n6 - Sair\n")
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
