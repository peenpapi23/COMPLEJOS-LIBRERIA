# Calculadora de Números Complejos

Este proyecto implementa una calculadora básica para operaciones con números complejos en Python. La calculadora soporta operaciones como suma, resta, multiplicación, división, módulo, conjugado, conversión entre coordenadas cartesianas y polares, y cálculo de la fase. Además, se incluyen pruebas unitarias para garantizar la correcta funcionalidad de las operaciones implementadas.

## Archivos

- **calculadoraimaginario.py**: Contiene las implementaciones de las operaciones básicas para números complejos.
- **test_calculadoraimaginario.py**: Contiene las pruebas unitarias para verificar la funcionalidad de cada operación en `calculadoraimaginario.py`.

## Funciones Implementadas

### calculadoraimaginario.py

- `sumai(a, b)`: Suma de dos números complejos.
- `resta(a, b)`: Resta de dos números complejos.
- `multiplicacion(a, b)`: Multiplicación de dos números complejos.
- `division(a, b)`: División de dos números complejos.
- `modulo(a)`: Cálculo del módulo de un número complejo.
- `conjugado(a)`: Obtención del conjugado de un número complejo.
- `conversionCartPolar(a)`: Conversión de un número complejo de coordenadas cartesianas a polares.
- `conversionPolarCart(a)`: Conversión de un número complejo de coordenadas polares a cartesianas.
- `fase(a)`: Cálculo de la fase de un número complejo.

## Pruebas Unitarias

### test_calculadoraimaginario.py

Se incluyen pruebas unitarias para cada una de las funciones mencionadas anteriormente. Las pruebas se realizan utilizando el módulo `unittest` de Python y cubren casos básicos y algunos casos límite para asegurar que las funciones se comportan correctamente.

Las pruebas se pueden ejecutar utilizando el siguiente comando:

```bash
python -m unittest test_calculadoraimaginario.py
