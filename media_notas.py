def calcular_media(notas):
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")
    return sum(notas) / len(notas)

def soma (a,b):
    return a + b

def main():
    notas = []
    for i in range(1, 5):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)

    media = calcular_media(notas)
    print(f"A média das notas é: {media:.2f}")


if __name__ == "__main__":
    main()
