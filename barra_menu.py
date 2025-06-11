import tkinter as tk
ventana = tk.Tk()

ventana.title('Menú desplegable')
ventana.geometry('400x200')

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)

barra_menu.add_cascade(label =
'Principal', menu=menu_principal)

submenu = tk.Menu(menu_principal)

menu_principal.add_cascade(label =
'Opciones', menu=submenu)

submenu.add_command(label = 'Opción 1')
submenu.add_command(label = 'Opción 2')

ventana.mainloop()# ...existing code...

# Centrar la ventana en la pantalla
ventana.update_idletasks()
ancho_ventana = 400
alto_ventana = 200
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

ventana.mainloop()