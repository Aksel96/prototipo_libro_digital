import tkinter as tk
import util.util_ventana as util_ventana
from config import COLOR_CUERPO_PRINCIPAL


class FormularioInfoDesign(tk.Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.config_window()
        self.construir_widget()

    def config_window(self):
        # Configuracion de la ventana
        self.title('Informacion')
        self.iconbitmap("./imagenes/logo_algebra_icon.ico")
        w, h = 250, 100
        util_ventana.centrar_ventana(self, w, h)
        self.config(bg=COLOR_CUERPO_PRINCIPAL)

    def construir_widget(self):
        self.labelVersion = tk.Label(self, text="Version : 0.1.0")
        self.labelVersion.config(bg=COLOR_CUERPO_PRINCIPAL,fg='#FFFFFF', font=("Roboto",15), pady= 10, width=20)
        self.labelVersion.pack()

        self.labelAutor = tk.Label(self, text="Autor : Aksel Villela")
        self.labelAutor.config(bg=COLOR_CUERPO_PRINCIPAL,fg='#FFFFFF' ,font=("Roboto", 15), pady=10, width=20)
        self.labelAutor.pack()
