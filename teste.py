import Vigenere
import Util

inputFile = Util.scanFile("./outputs/pg174.txt.enc")
print Vigenere.decript3(inputFile, 'abcd')
