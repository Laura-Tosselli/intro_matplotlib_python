# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
from tkinter import Y
from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    # Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función y = tanh(x) --> tangente hiperbólica
    y = np.tanh(x)

    # Alumno: Graficar la función utilizando "scatter"
    # utilizando "x" e "y" ya disponible
    fig1 = plt.figure()
    fig1.suptitle('Funcion Tangente Hiperbólica', fontsize=14, label='y = tanh(x)')
    ax = fig1.add_subplot()

    # Colocar la leyenda y el label con el nombre de la función
    ax.plot(x,y, label='y = tanh(x)')
    ax.legend()
    ax.grid()

    # Elegir un marker a elección
    ax.scatter(x, y, c='darkblue',marker="d")

    # Crear acá su gráfico
    plt.show()
    print("terminamos")
