import tkinter as tk

def main ():
    root = tk.Tk()
    root.title('Lubricentro-PitMar')
    root.maxsize(1000, 400)

    frame = tk.Frame(root)
    frame.pack()
    frame.config( width = 1000, height = 700, bg = 'gray')

    #finaly of aplication
    root.mainloop()




if __name__ =='__main__':
    main()