import tkinter as tk

def menu_bar(root):
    menu_bar = tk.Menu(root)
    root.config(menu = menu_bar, width = 300, height = 300 )

    menu_init = tk.Menu(menu_bar, tearoff = 0)
    menu_bar.add_cascade( label = 'Inicio', menu = menu_init )

    menu_init.add_command( label = 'Buscar cliente' )
    menu_init.add_command( label = 'Salir', command = root.destroy )


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width = 1000, height = 700 )
        self.root = root
        self.pack()
        self.config( bg = 'gray' )