# -*- coding: utf-8 -*-
"""Resolvedor de Sistemas - Matemática

"""

import numpy as np

def resolver_sistema():
    n = int(input("Digite a quantidade de incógnitas: "))

    print("\nDigite os coeficientes e o termo independente(Sem variável) de cada equação.")
    print("Formato: a1 a2 ... an b")
    print("Exemplo (3 incógnitas): 2 3 -1 4 → 2x + 3y - z = 4\n")

    A = []  # matriz dos coeficientes
    B = []  # termos independentes
    for i in range(n):
        linha = list(map(float, input(f"Equação {i+1}: ").split()))
        A.append(linha[:n])
        B.append(linha[n])

    A = np.array(A)
    B = np.array(B)

    try:
        solucao = np.linalg.solve(A, B)
        print("\n=== Solução encontrada ===")
        for i, val in enumerate(solucao, start=1):
            print(f"x{i} = {val:.2f}")
    except np.linalg.LinAlgError:
        print("\nO sistema não tem solução única (pode ser impossível ou indeterminado).")


def calcular_determinante():
    n = int(input("Digite a ordem da matriz: "))

    print("\nDigite os elementos da matriz linha por linha.")
    print("Formato: a11 a12 ... a1n\n")

    M = []
    for i in range(n):
        linha = list(map(float, input(f"Linha {i+1}: ").split()))
        M.append(linha)

    M = np.array(M)

    det = np.linalg.det(M)
    print("\n=== Determinante da matriz ===")
    print(f"det = {det:.2f}")


def menu():
    while True:
        print("\n=== Resolvedor de Sistemas Lineares e Matrizes ===")
        print("1 - Resolver sistema de equações")
        print("2 - Calcular determinante de uma matriz")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            resolver_sistema()
        elif opcao == "2":
            calcular_determinante()
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()