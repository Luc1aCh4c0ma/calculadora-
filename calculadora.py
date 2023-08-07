""" codigo de una calculadora donde se puede resolver las siguientes operaciones: suma, resta, division, multiplicacion, potencia, radicacion,
 fracciones, calculos de trigonometria, ecuaciones lineales de primer grado"""

import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(num):
    return math.sqrt(num)

def seno(angulo):
    return math.sin(math.radians(angulo))

def coseno(angulo):
    return math.cos(math.radians(angulo))

def tangente(angulo):
    return math.tan(math.radians(angulo))

def ecuacion_lineal_primer_grado(a, b):
    if a == 0:
        raise ValueError("El coeficiente 'a' debe ser diferente de cero para una ecuación de primer grado.")
    return -b / a



# Uso de las funciones

# Suma
resultado_suma = suma(5, 3)
print("Suma:", resultado_suma)

# Resta
resultado_resta = resta(10, 4)
print("Resta:", resultado_resta)

# Multiplicación
resultado_multiplicacion = multiplicacion(6, 7)
print("Multiplicación:", resultado_multiplicacion)

# División
try:
    resultado_division = division(15, 3)
    print("División:", resultado_division)
except ValueError as e:
    print(str(e))  # error si se intenta dividir entre cero.

# Potencia
resultado_potencia = potencia(2, 3)
print("Potencia:", resultado_potencia)

# Raíz cuadrada
resultado_raiz_cuadrada = raiz_cuadrada(25)
print("Raíz cuadrada:", resultado_raiz_cuadrada)

# Trigonometría
angulo = 30
resultado_seno = seno(angulo)
print(f"Seno de {angulo} grados:", resultado_seno)

resultado_coseno = coseno(angulo)
print(f"Coseno de {angulo} grados:", resultado_coseno)

resultado_tangente = tangente(angulo)
print(f"Tangente de {angulo} grados:", resultado_tangente)

# Ecuación lineal de primer grado (ax + b = 0)
a = 2
b = -4
resultado_ecuacion_lineal = ecuacion_lineal_primer_grado(a, b)
print(f"Solución de la ecuación {a}x + {b} = 0:", resultado_ecuacion_lineal)
