import tkinter as tk
from tkinter import font
from config import COLOR_MENU_LATERAL, COLOR_MENU_CURSOSR_ENCIMA, COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_LETRA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from formularios.form_info_design import FormularioInfoDesign
from formularios.form_sitio_construccion import FormularioSitioConstruccionDesign
from formularios.form_graficas_design import FormularioGraficasDesign
from util.util_tooltip import CreateToolTip
from formularios.form_temario_pdf import FormularioTemarioPDF
from formularios.form_inicio_design import FormularioInicioDesign

class FormMainDesign(tk.Tk):
    # Constructor
    def __init__(self):
        super().__init__()
        self.perfil = util_img.leer_imagen("./imagenes/logofes_0.png", (100, 100))
        self.img_sitio_construccion = util_img.leer_imagen("./imagenes/sitio_construccion.png", (400, 400))
        self.iconMenuBar = util_img.leer_imagen("./imagenes/menu_icon_white.png", (30, 30))
        self.iconHome = util_img.leer_imagen("./imagenes/home_icon.png", (30, 30))
        self.iconPerson = util_img.leer_imagen("./imagenes/book_icon.png", (30, 30))
        self.iconGraficas = util_img.leer_imagen("./imagenes/grafic_icon.png", (30, 30))
        self.iconInfo = util_img.leer_imagen("./imagenes/info_icon.png", (30, 30))
        self.iconSetting = util_img.leer_imagen("./imagenes/settings_icon.png", (30, 30))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

    def config_window(self):
        # Configuracion de la ventana
        self.title("Algebra Lineal")
        self.iconbitmap("./imagenes/logo_algebra_icon.ico")
        w, h = 1280, 720
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        self.barra_superior = tk.Frame(self, height=35, bg=COLOR_BARRA_SUPERIOR)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=250)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)
        # Etiqueta de titulo
        self.labelTitulo = tk.Label(self.barra_superior, text="Algebra")
        self.labelTitulo.config(fg=COLOR_LETRA, font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Boton
        self.btnMenuLateral = tk.Button(self.barra_superior, image=self.iconMenuBar, command=self.toggle_panel, bd=0,
                                        bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.btnMenuLateral.pack(side=tk.LEFT)
        CreateToolTip(self.btnMenuLateral,"Mostrar/Ocutar barra lateral")
        # Etiqueta de info
        self.labelTitulo = tk.Label(self.barra_superior, text="Libro digital de Algebra Lineal")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        ancho_menu = 200
        alto_menu = 40
        font_awesome = font.Font(family='FontAwesome', size=15)

        # Etiqueta logo
        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botones del menú lateral

        self.buttonDashBoard = tk.Button(self.menu_lateral)
        self.buttonProfile = tk.Button(self.menu_lateral)
        self.buttonPicture = tk.Button(self.menu_lateral)
        self.buttonInfo = tk.Button(self.menu_lateral)
        self.buttonSettings = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Inicio", "\u1F4B", self.buttonDashBoard, self.iconHome, self.abrir_panel_inicio),
            ("Temario", "\uf007", self.buttonProfile, self.iconPerson, self.abrir_panel_temario),
            ("Graficas", "\uf03e", self.buttonPicture, self.iconGraficas, self.abrir_panel_graficas),
            ("Información", "\u2699", self.buttonInfo, self.iconInfo, self.abrir_panel_info),
            ("Configuración", "\uf0ad", self.buttonSettings, self.iconSetting, self.abrir_panel_construccion)
        ]
        for text, icon, button, icono, comando in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu, icono, comando)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, icono, comando):
        button.config(text=f"{text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white",
                      width=ancho_menu, height=alto_menu,
                      image=icono, compound=tk.LEFT, padx=10,
                      command=comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOSR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self.perfil,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def abrir_panel_info(self):
        FormularioInfoDesign()

    def abrir_panel_construccion(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioSitioConstruccionDesign(self.cuerpo_principal, self.img_sitio_construccion)

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()

    def abrir_panel_graficas(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioGraficasDesign(self.cuerpo_principal)

    def abrir_panel_temario(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioTemarioPDF(self.cuerpo_principal)

    def abrir_panel_inicio(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioInicioDesign(self.cuerpo_principal,self.perfil)

