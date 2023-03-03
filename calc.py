import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd

def simplificar():
    expr = sp.simplify(input("Digite a expressão a ser simplificada: "))
    print(expr)

def resolver_equacao():
    eq = sp.Eq(sp.sympify(input("Digite a equação a ser resolvida: ")), 0)
    solutions = sp.solve(eq)
    print(solutions)

def derivar():
    f = sp.sympify(input("Digite a função a ser derivada: "))
    df = sp.diff(f)
    print(df)

def integrar():
    g = sp.sympify(input("Digite a função a ser integrada: "))
    integral = sp.integrate(g)
    print(integral)

def multiplicar_matrizes():
    a = np.array(eval(input("Digite a primeira matriz: ")))
    b = np.array(eval(input("Digite a segunda matriz: ")))
    c = np.dot(a, b)
    print(c)

def determinante():
    a = np.array(eval(input("Digite a matriz: ")))
    det = np.linalg.det(a)
    print(det)

def resolver_sistema():
    A = np.array(eval(input("Digite a matriz dos coeficientes: ")))
    B = np.array(eval(input("Digite o vetor das constantes: ")))
    x = np.linalg.solve(A, B)
    print(x)

def autovalores_autovetores():
    a = np.array(eval(input("Digite a matriz: ")))
    w, v = np.linalg.eig(a)
    print(w)
    print(v)

def plotar_grafico():
    x = np.linspace(float(input("Digite o valor mínimo de x: ")), float(input("Digite o valor máximo de x: ")), 100)
    y = sp.sympify(input("Digite a função a ser plotada: "))
    y = np.array([y.subs('x', i) for i in x])
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico da função')
    plt.show()

def encontrar_minimo():
    def f(x):
        return sp.sympify(input("Digite a função a ser minimizada: "))

    solution = sp.optimize.minimize_scalar(f)
    print(solution.x)

def soma():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a + b
    print(resultado)

def subtracao():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a - b
    print(resultado)

def multiplicacao():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a * b
    print(resultado)

def divisao():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a / b
    print(resultado)

def raiz_quadrada():
    a = float(input("Digite o número: "))
    resultado = np.sqrt(a)
    print(resultado)

def seno():
    a = float(input("Digite o ângulo em graus: "))
    resultado = np.sin(np.deg2rad(a))
    print(resultado)

def cosseno():
    a = float(input("Digite o ângulo em graus: "))
    resultado = np.cos(np.deg2rad(a))
    print(resultado)
    
def tangente():
    a = float(input("Digite o ângulo em graus: "))
    resultado = np.tan(np.deg2rad(a))
    print(resultado)

cond = True    
while cond:
    
    print("\n\nCalculadora Científica\n")
    print("Escolha uma das opções abaixo:")
    print("1 - Simplificar uma expressão matemática")
    print("2 - Resolver uma equação")
    print("3 - Derivar uma função")
    print("4 - Integrar uma função")
    print("5 - Multiplicar duas matrizes")
    print("6 - Calcular o determinante de uma matriz")
    print("7 - Resolver um sistema linear")
    print("8 - Calcular autovalores e autovetores de uma matriz")
    print("9 - Plotar o gráfico de uma função")
    print("10 - Encontrar o mínimo de uma função")
    print("11 - Soma")
    print("12 - Subtração")
    print("13 - Multiplicação")
    print("14 - Divisão")
    print("15 - Raiz Quadrada")
    print("16 - Seno")
    print("17 - Cosseno")
    print("18 - Tangente")
    print("0 - Sair do programa")
    
    opcao = int(input("\nDigite a opção desejada: "))

    if opcao == 1:
        simplificar()
    elif opcao == 2:
        resolver_equacao()
    elif opcao == 3:
        derivar()
    elif opcao == 4:
        integrar()
    elif opcao == 5:
        multiplicar_matrizes()
    elif opcao == 6:
        determinante()
    elif opcao == 7:
        resolver_sistema()
    elif opcao == 8:
        autovalores_autovetores()
    elif opcao == 9:
        plotar_grafico()
    elif opcao == 10:
        encontrar_minimo()
    elif opcao == 11:
        soma()
    elif opcao == 12:
        subtracao()
    elif opcao == 13:
        multiplicacao()
    elif opcao == 14:
        divisao()
    elif opcao == 15:
        raiz_quadrada()
    elif opcao == 16:
        seno()
    elif opcao == 17:
        cosseno()
    elif opcao == 18:
        tangente()
    elif opcao == 0:
        cond = False
        break
    else:
        print("Opção inválida. Tente novamente.")
        cond = True
        
        
