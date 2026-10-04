"""Calcula el promedio de tres números ingresados por el usuario."""


def main():
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    numero3 = float(input("Ingresa el tercer número: "))

    promedio = (numero1 + numero2 + numero3) / 3

    print(f"El promedio es: {promedio:.2f}")


if __name__ == "__main__":
    main()