"""Calcula el área de un rectángulo."""


def main():
    base = float(input("Ingresa la base del rectángulo: "))
    altura = float(input("Ingresa la altura del rectángulo: "))

    area = base * altura

    print(f"El área del rectángulo es: {area:.2f}")


if __name__ == "__main__":
        main()