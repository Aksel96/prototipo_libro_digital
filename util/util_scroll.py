import tkinter as tk

class ScrollableWidget(tk.Frame):
    def __init__(self, parent, widget, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # Configuración del scrollbar vertical
        scrollbar_y = tk.Scrollbar(self, orient="vertical")
        scrollbar_y.pack(side="right", fill="y")

        # Configuración del scrollbar horizontal
        scrollbar_x = tk.Scrollbar(self, orient="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")

        # Configuración del widget
        self.widget = widget(self, yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        self.widget.pack(side="left", fill="both", expand=True)
        scrollbar_y.config(command=self.widget.yview)
        scrollbar_x.config(command=self.widget.xview)

        self.pack(fill="both", expand=True)

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")

    # Creamos un Text widget y lo hacemos scrollable
    scrollable_text = ScrollableWidget(root, tk.Text)
    scrollable_text.pack(fill="both", expand=True)

    # Agregamos contenido al Text widget
    for i in range(30):
        scrollable_text.widget.insert(tk.END, f"Line {i+1}\n")

    root.mainloop()



