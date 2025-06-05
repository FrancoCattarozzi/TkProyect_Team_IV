import tkinter as tk
import time

ventana = tk.Tk()
ventana.title('Reloj simple')
ventana.geometry('400x200')

reloj = tk.Label(ventana, font =
('Arial', 60), bg = 'blue', fg = 'white')

def hora():
    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text = tiempo_actual)
    ventana.after(1000, hora)

reloj.pack(anchor = 'center')

hora()

ventana.mainloop()