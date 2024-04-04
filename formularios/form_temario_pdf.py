import tkinter as tk
from PIL import Image, ImageTk
from config import COLOR_CUERPO_PRINCIPAL


class FormularioTemarioPDF():
    def __init__(self, panel_principal):
        # Crear paneles: barra superior
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)

        # Primer Label con texto
        self.labelTitulo = tk.Label(
            self.barra_superior, text="Temario Álgebra lineal")
        self.labelTitulo.config(fg="#FFFFFF", font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL, pady=5)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        # Crear un Canvas para contener el Frame con la imagen
        self.canvas = tk.Canvas(self.barra_inferior, bg=COLOR_CUERPO_PRINCIPAL)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Agregar un Scrollbar
        scrollbar = tk.Scrollbar(self.barra_inferior, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(yscrollcommand=scrollbar.set)

        # Crear un Frame dentro del Canvas
        self.frame_imagenes = tk.Frame(self.canvas, bg=COLOR_CUERPO_PRINCIPAL)
        self.canvas.create_window((0, 0), window=self.frame_imagenes, anchor=tk.NW)

        # Agregar imagenes
        for i in range(8):
            image_path = f'./recursos/temario/temario_{i + 1}.jpg'
            image = Image.open(image_path)
            # Ajustar el tamaño de la imagen
            width, height = 1050, 1150
            image = image.resize((width, height), Image.ADAPTIVE)
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(self.frame_imagenes, image=photo, bg='white')
            image_label.image = photo  # Guardar una referencia para evitar que la imagen sea eliminada por el recolector de basura
            image_label.pack()


        self.frame_imagenes.bind("<Configure>", self.on_frame_configure)


        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_frame_configure(self, event):

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mousewheel(self, event):

        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
