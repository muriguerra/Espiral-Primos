import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def primos():

    plt.rcParams["figure.figsize"] = [5, 5]
    plt.rcParams["figure.autolayout"] = True

    plt.xlim(-5, 5)
    plt.ylim(-5, 5)

    x = [0]
    y = [0]
    final = 1601
    num_primos = [2]
    passo = 0
    virou = 0
    caso = 0
    tamanho_passo = 1

    plt.ion()

    figure, ax = plt.subplots(figsize=(6.5, 6.5))
    ax.set_ylim(-25, 25)
    ax.set_xlim(-25, 25)
    line, = ax.plot(x, y, " ")


    for i in range(1,   final):
        
        if (passo % tamanho_passo == 0): #checa se passo é do tamanho do passo para poder virar e mudar o caso
            caso = (caso + 1) % 4        #aumenta caso(esquerda, direita, cima ou baixo)
            virou += 1                   #avisa que virou
            
            if (virou % 2 ==0):     # Tamanho do passo aumenta a cada 2 curvas 1, 1, 2, 2, 3, 3, ...
                tamanho_passo += 1

        passo += 1

        line.set_xdata(x)
        line.set_ydata(y)

        p = 0
        while i % num_primos[p] != 0 and i != 1:
            
            if p == len(num_primos) - 1:
                num_primos.append(i)
            p += 1

        print(num_primos)

        if (i in num_primos):
            ax.plot(x[i-1], y[i-1], marker="o", markersize="5", markeredgecolor="darkred", markerfacecolor="darkred")
        elif (i == 1):
            ax.plot(x[i - 1], y[i - 1], marker="o", markersize="6", markeredgecolor="black",
                    markerfacecolor="black")
        else:
            ax.plot(x[i - 1], y[i - 1], marker="o", markersize="4", markeredgecolor="lightblue", markerfacecolor="lightblue")

        figure.canvas.draw()

        figure.canvas.flush_events()

        if (caso == 1):
            direita(x, y)

        if (caso == 2):
            cima(x, y)

        if (caso == 3):
            esquerda(x, y)

        if (caso == 0):
            baixo(x, y)

        if (i == final - 1):
            plt.savefig('primo.png')
            print(len(num_primos))
            wait = input()

def cima(x, y):
    x.append(x[-1])
    y.append(y[-1] + 1)
    print("cima", x, y)

def direita(x, y):
    x.append(x[-1] + 1)
    y.append(y[-1])
    print("direita", x, y)

def esquerda(x, y):
    x.append(x[-1] - 1)
    y.append(y[-1])
    print("esquerda", x, y)

def baixo(x, y):
    x.append(x[-1])
    y.append(y[-1] - 1)
    print("baixo", x, y)

if __name__ == "__main__":
    primos()

