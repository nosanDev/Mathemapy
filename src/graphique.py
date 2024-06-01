import matplotlib.pyplot as plt
import numpy as np

def Graphique(m, c):
    # Définir les valeurs de x
    x = np.linspace(-10, 10, 100)

    # Calculer les valeurs de y pour la fonction affine
    y = m * x + c

    # Tracer le graphique
    plt.plot(x, y, label=f'y = {m}x + {c}')
    plt.title('Graphique d\'une fonction affine')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()
