import calculadoraimaginario as ca
import unittest

class TestCalculadoraImaginario(unittest.TestCase):
    
    def test_sumai(self):
        # Ejemplo 1
        a = (3, 4)
        b = (1, 2)
        resultado = ca.sumai(a, b)
        self.assertEqual(resultado, (4, 6))
        
        # Ejemplo 2
        a = (-1, -1)
        b = (2, 3)
        resultado = ca.sumai(a, b)
        self.assertEqual(resultado, (1, 2))
    
    def test_resta(self):
        # Ejemplo 1
        a = (3, 4)
        b = (1, 2)
        resultado = ca.resta(a, b)
        self.assertEqual(resultado, (2, 2))
        
        # Ejemplo 2
        a = (2, 3)
        b = (-1, -1)
        resultado = ca.resta(a, b)
        self.assertEqual(resultado, (3, 4))
    
    def test_multiplicacion(self):
        # Ejemplo 1
        a = (3, 4)
        b = (1, 2)
        resultado = ca.multiplicacion(a, b)
        self.assertEqual(resultado, (-5, 10))
        
        # Ejemplo 2
        a = (2, 3)
        b = (4, -5)
        resultado = ca.multiplicacion(a, b)
        self.assertEqual(resultado, (23, 2))
    
    def test_division(self):
        # Ejemplo 1
        a = (3, 4)
        b = (1, 2)
        resultado = ca.division(a, b)
        self.assertAlmostEqual(resultado[0], 2.2, places=1)  # Resultado esperado 2.2
        self.assertAlmostEqual(resultado[1], -0.4, places=1)  # Resultado esperado -0.4
        
        # Ejemplo 2
        a = (5, 6)
        b = (1, -1)
        resultado = ca.division(a, b)
        self.assertAlmostEqual(resultado[0], -0.5, places=1)  # Resultado esperado -0.5
        self.assertAlmostEqual(resultado[1], 5.5, places=1)  # Resultado esperado 5.5
    
    def test_modulo(self):
        # Ejemplo 1
        a = (3, 4)
        resultado = ca.modulo(a)
        self.assertEqual(resultado, 5)
        
        # Ejemplo 2
        a = (5, 12)
        resultado = ca.modulo(a)
        self.assertEqual(resultado, 13)
    
    def test_conjugado(self):
        # Ejemplo 1
        a = (3, 4)
        resultado = ca.conjugado(a)
        self.assertEqual(resultado, (3, -4))
        
        # Ejemplo 2
        a = (-2, -3)
        resultado = ca.conjugado(a)
        self.assertEqual(resultado, (-2, 3))
    
    def test_conversionCartPolar(self):
        # Ejemplo 1
        a = (3, 4)
        resultado = ca.conversionCartPolar(a)
        self.assertAlmostEqual(resultado[0], 5)
        self.assertAlmostEqual(resultado[1], 0.93, places=2)  # Aproximado a 0.93 radianes
        
        # Ejemplo 2
        a = (1, 1)
        resultado = ca.conversionCartPolar(a)
        self.assertAlmostEqual(resultado[0], 1.41, places=2)  # Aproximado a 1.41
        self.assertAlmostEqual(resultado[1], 0.79, places=2)  # Aproximado a 0.79 radianes
    
    def test_conversionPolarCart(self):
        # Ejemplo 1
        polar = (5, 0.93)
        resultado = ca.conversionPolarCart(polar)
        self.assertAlmostEqual(resultado[0], 3, places=1)  # Aproximado a 3
        self.assertAlmostEqual(resultado[1], 4, places=1)  # Aproximado a 4
        
        # Ejemplo 2
        polar = (1.41, 0.79)
        resultado = ca.conversionPolarCart(polar)
        self.assertAlmostEqual(resultado[0], 1, places=1)  # Aproximado a 1
        self.assertAlmostEqual(resultado[1], 1, places=1)  # Aproximado a 1
    
    def test_fase(self):
        # Ejemplo 1
        a = (3, 4)
        resultado = ca.fase(a)
        self.assertAlmostEqual(resultado, 0.93, places=2)  # Aproximado a 0.93 radianes
        
        # Ejemplo 2
        a = (1, 1)
        resultado = ca.fase(a)
        self.assertAlmostEqual(resultado, 0.79, places=2)  # Aproximado a 0.79 radianes

if __name__ == '__main__':
    unittest.main()
