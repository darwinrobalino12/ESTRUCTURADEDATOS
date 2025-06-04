"""Módulo para definir figuras geométricas simples."""

import math # Necesario para usar math.pi (el valor de PI).

# --- Clase Círculo ---
class Circulo:
    """Representa un círculo."""
    def __init__(self, radio):
        # Inicializa el círculo con su radio.
        # '__radio' es una propiedad interna (encapsulada).
        self.__radio = radio

    def obtener_radio(self):
        """Devuelve el radio del círculo."""
        return self.__radio

    def calcular_area(self):
        """Calcula el área del círculo (PI * radio^2)."""
        return math.pi * self.__radio * self.__radio

    def calcular_perimetro(self):
        """Calcula el perímetro del círculo (2 * PI * radio)."""
        return 2 * math.pi * self.__radio

# --- Clase Cuadrado ---
class Cuadrado:
    """Representa un cuadrado."""
    def __init__(self, lado):
        # Inicializa el cuadrado con la longitud de su lado.
        # '__lado' es una propiedad interna (encapsulada).
        self.__lado = lado

    def obtener_lado(self):
        """Devuelve la longitud del lado del cuadrado."""
        return self.__lado

    def calcular_area(self):
        """Calcula el área del cuadrado (lado * lado)."""
        return self.__lado * self.__lado

    def calcular_perimetro(self):
        """Calcula el perímetro del cuadrado (4 * lado)."""
        return 4 * self.__lado

# --- Ejemplos de uso ---
if __name__ == "__main__":
    print("--- Probando la clase Círculo ---")
    # Crea un objeto Círculo con radio 5.
    mi_circulo = Circulo(5)
    print(f"Radio del círculo: {mi_circulo.obtener_radio()}")
    print(f"Área del círculo: {mi_circulo.calcular_area():.2f}")
    print(f"Perímetro del círculo: {mi_circulo.calcular_perimetro():.2f}")
    print("------------------------------\n")

    print("--- Probando la clase Cuadrado ---")
    # Crea un objeto Cuadrado con lado 6.
    mi_cuadrado = Cuadrado(6)
    print(f"Lado del cuadrado: {mi_cuadrado.obtener_lado()}")
    print(f"Área del cuadrado: {mi_cuadrado.calcular_area()}")
    print(f"Perímetro del cuadrado: {mi_cuadrado.calcular_perimetro()}")
    print("--------------------------------\n")

