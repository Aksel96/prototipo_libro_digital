import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class FormularioGraficasDesign():
    def __init__(self, panel_principal):
        figura = Figure(figsize=(8, 6), dpi=100)
        ax1 = figura.add_subplot(211)
        ax2 = figura.add_subplot(212)

        figura.subplots_adjust(hspace=0.4)

        self.grafico1(ax1)
        self.grafico2(ax2)

        # Agregar los gráficos a la ventana de Tkinter
        canvas = FigureCanvasTkAgg(figura, master=panel_principal)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def grafico1(self, ax):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]

        ax.bar(x, y, label='Grafico 1 - Grafico de Barras')
        ax.set_xlabel('Eje x')
        ax.set_ylabel('Eje y')
        ax.legend()

        for i,v in enumerate(y):
            ax.text(x[i] - 0.1, v + 0.1, str(v), color='black')

        ax.grid(axis='y', linestyle='--', alpha=0.7)

    def grafico2(self, ax):
        # Función para graficar el segundo conjunto de datos
        x = [1, 2, 3, 4, 5]
        y = [1, 2, 1, 2, 1]
        ax.plot(x, y, label='Gráfico 2', color='red')
        ax.set_title('Gráfico 2', )
        ax.set_xlabel('Eje X', fontsize=12)
        ax.set_ylabel('Eje Y', fontsize=12)
        ax.plot(x, y, label='Gráfico 2', color='red', linestyle='--', marker='o')
        ax.annotate('Punto importante', xy=(3, 1), xytext=(3.5, 1.5),
                    arrowprops=dict(facecolor='black', shrink=0.05))
        ax.set_xlim(0, 6)  # Establece los límites del eje x
        ax.set_ylim(0, 3)  # Establece los límites del eje y
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()