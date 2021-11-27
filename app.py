import tkinter as tk
from client.interface_client import Frame, menu_bar

def main ():
    root = tk.Tk()
    root.title('Lubricentro-PitMar')
    root.maxsize(1000, 400)

    menu_bar(root)

    app = Frame(root = root)
    #finaly of aplication
    root.mainloop()

if __name__ =='__main__':
    main()