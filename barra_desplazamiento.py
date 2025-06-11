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

# Centrar la ventana en la pantalla
ventana.update_idletasks()
ancho_ventana = 400
alto_ventana = 200
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

ventana.mainloop ()