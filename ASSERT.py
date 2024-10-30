import unittest
import sys
sys.path.append('C:/Users/andre/OneDrive - Estudiantes ITCR/Documentos/Semestre I ATI 2024/Taller Programación/LAB9')
from LaboratorioRecursividad import *

class TestLabRecursividad(unittest.TestCase):
    def testSumarDigitosMultiplos(self):
        self.assertTrue(sumarDigitosMultiplos(6,3) == 6)
        self.assertTrue(sumarDigitosMultiplos(1002,7) == 0)
        self.assertTrue(sumarDigitosMultiplos(666,3) == 18)
        self.assertTrue(sumarDigitosMultiplos(1234,2) == 6)
    
    def testFormarNumero(self):
        self.assertTrue(formarNumero(-2556) == 26)
        self.assertTrue(formarNumero(2552180) == 2280)
        self.assertTrue(formarNumero(125) == 2)
        self.assertTrue(formarNumero(135) == 0)

    def testlevar(self):
        self.assertTrue(elevar(5,0) == 1)
        self.assertTrue(elevar(2,4) == 16)
        self.assertTrue(elevar(0,0) == 1)
        self.assertTrue(elevar(5,3) == 125)
    
    def convertirADecimal(self):
        self.assertTrue(convertirADecimal(1010) == 10)
        self.assertTrue(convertirADecimal(101) == 5)
        self.assertTrue(convertirADecimal(10000000) == 128)
        self.assertTrue(convertirADecimal(110010) == 50)
        self.assertTrue(convertirADecimal(110101) == 53)
        
    def testsumatoriaRecursividad(self):
        self.assertTrue(sumatoriaRecursividad(10) == 55)
        self.assertTrue(sumatoriaRecursividad(1000) == 500500)
        self.assertTrue(sumatoriaRecursividad(4) == 10)
        self.assertTrue(sumatoriaRecursividad(100000) == 5000050000)

    def testEliminarRepetidos(self):
        self.assertTrue(eliminarRepetidos([1,1,3,8,4,9,4,2]) == [1, 3, 8, 9, 4, 2])
        self.assertTrue(eliminarRepetidos([1,1,1,2,2,2,4,4,4]) == [1, 2, 4])
        self.assertTrue(eliminarRepetidos(["a","b","c","a","a","a","b"]) == ['c', 'a', 'b'])
        self.assertTrue(eliminarRepetidos(["as","as"]) == ['as'])
    
    def testInterseccion(self):
        self.assertTrue(interseccion([1,2,3,4,5,7,8,9],[2,4,6,8]) == [2, 4, 8])
        self.assertTrue(interseccion(["a","b","c","d","e","f","g"],["a","c","d","e"]) == ['a', 'c', 'd', 'e'])
        self.assertTrue(interseccion([45,44,43,42,41,40],[44,42]) == [44,42])

    def testDiferencia(self):
        self.assertTrue(diferencia([1,2,3,4,5,7,8,9],[2,4,6,8]) == [1, 3, 5, 7, 9])
        self.assertTrue(diferencia(["a","b","c","d","e","f","g"],["a","c","d","e"]) == ['b', 'f', 'g'])
        self.assertTrue(diferencia([45,44,43,42,41,40],[44,42]) == [45, 43, 41, 40])

    def testSumaSucesiva(self):
        self.assertTrue(sumaSucesiva([1,1,3,8,4,9,4,2]) == [1, 2, 5, 13, 17, 26, 30, 32])
        self.assertTrue(sumaSucesiva([1,1,1,2,2,2,4,4,4]) == [1, 2, 3, 5, 7, 9, 13, 17, 21])
        self.assertTrue(sumaSucesiva([1,2,3]) == [1,3,6])

    def testEliminarCaracter(self):
        self.assertTrue(eliminarCaracter("aaaaabbbbcccc", "a") == "bbbbcccc")
        self.assertTrue(eliminarCaracter("andrey figueroa calderon"," ") == "andreyfigueroacalderon")
        self.assertTrue(eliminarCaracter("Mariangel","a") == "Mringel")

    def testPrimosLista(self):
        self.assertTrue(primosLista([1,2,3,4,5,6,7,8,9]) == [2, 3, 5, 7])
        self.assertTrue(primosLista([2,17,15,7,9]) == [2, 17, 7])
        self.assertTrue(primosLista([41,42,43,44,45,46,47,48,49,50]) == [41, 43, 47])
    
    def testProductoCartesiano(self):
        self.assertTrue(productoCartesiano([1,2],["x","y","z"]) == [[1, 'x'], [1, 'y'], [1, 'z'], [2, 'x'], [2, 'y'], [2, 'z']])
        self.assertTrue(productoCartesiano([2,2],[1,2,4,5]) == [[2, 1], [2, 2], [2, 4], [2, 5], [2, 1], [2, 2], [2, 4], [2, 5]])
        self.assertTrue(productoCartesiano(["a"],[1,2,3]) == [['a', 1], ['a', 2], ['a', 3]])

    def testSucesionULAM(self):
        self.assertTrue(sucesionULAM(10) == [10, 5, 16, 8, 4, 2, 1])
        self.assertTrue(sucesionULAM(25) == [25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        self.assertTrue(sucesionULAM(45) == [45, 136, 68, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        self.assertTrue(sucesionULAM(8) == [8, 4, 2, 1])

    def testContarCarateresCadena(self):
        self.assertTrue(contarCarateresCadena("Andrey") == [['A', 1], ['n', 1], ['d', 1], ['r', 1], ['e', 1], ['y', 1]])
        self.assertTrue(contarCarateresCadena("Mariangel") == [['M', 1], ['a', 2], ['r', 1], ['i', 1], ['n', 1], ['g', 1], ['e', 1], ['l', 1]])
        self.assertTrue(contarCarateresCadena("Kristel") == [['K', 1], ['r', 1], ['i', 1], ['s', 1], ['t', 1], ['e', 1], ['l', 1]])
        self.assertTrue(contarCarateresCadena("Hola a todos") == [['H', 1], ['o', 3], ['l', 1], ['a', 2], [' ', 2], ['t', 1], ['d', 1], ['s', 1]])
        
if __name__ == '__main__':
    unittest.main()