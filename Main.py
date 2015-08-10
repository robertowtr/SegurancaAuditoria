import Util
import Cesar
import Vigenere
import Transposicao
import Substituicao

fileName = "./entrada.txt"

option = Util.menuAlgoritmo()

while option != 5:
    fileName = Util.readInput()
    if option == 1:
        Cesar.start(fileName)
    elif option == 2:
        Transposicao.start(fileName)
    elif option == 3:
        Vigenere.cript(fileName)
    elif option == 4:
        Substituicao.start(fileName)

    option = Util.menuAlgoritmo()
