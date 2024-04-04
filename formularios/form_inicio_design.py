import tkinter as tk
from config import COLOR_MENU_LATERAL, COLOR_MENU_CURSOSR_ENCIMA, COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL


class FormularioInicioDesign():
    def __init__(self, panel_principal,logo):
        # Crear paneles: barra superior
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)

        # Primer Label con texto
        self.labelTitulo = tk.Label(
            self.barra_superior, text="Libro digital")
        self.labelTitulo.config(fg="#FFFFFF", font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL, pady=20)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        self.barra_inferior.config(bg=COLOR_CUERPO_PRINCIPAL)




