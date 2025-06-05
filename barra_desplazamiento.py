import tkinter as tk
ventana = tk.Tk()

ventana.title('Barra de desplazamiento' )
ventana.geometry ('400x200' )

marco = tk.Frame(ventana)
marco.pack(padx = 10, pady = 10)

scrollbar = tk.Scrollbar (marco)
scrollbar .pack(side = tk.RIGHT, fill =
tk.Y)

lista = tk.Listbox(marco, yscrollcommand
= scrollbar .set)

for i in range(100):
    lista.insert(tk.END, f'Elemento {i+1}')

lista.pack(side = tk.LEFT, fill =
tk.BOTH)

scrollbar .config(command = lista.yview)

ventana.mainloop ()