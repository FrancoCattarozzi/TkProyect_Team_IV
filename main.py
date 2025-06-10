import tkinter as tk
import time as t
dict_ejercicios = {}
tiempo_descanso = 0
rutina = {}

#----------------------------VENTANA AGREGAR EJERCICIO---------------------------------

def abrir_ventana_agregar():
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title('Agregar nuevo ejercicio')
    ventana_agregar.geometry('600x400')

    tk.Label(ventana_agregar, text='Ingrese el nombre del ejercicio:', font=('Verdana', 10)).pack(pady=10)
    entry_ejercicio = tk.Entry(ventana_agregar, font=('Verdana', 10))  
    entry_ejercicio.pack(pady=5)   
    tk.Label(ventana_agregar, text='Ingrese la duración del ejercicio (en segundos):', font=('Verdana', 10)).pack(pady=10)
    entry_duracion = tk.Entry(ventana_agregar, font=('Verdana', 10))   
    entry_duracion.pack(pady=5)

    # Función para agregar el ejercicio al diccionario
    def agregar_ejercicio():
        ejercicio = entry_ejercicio.get()
        duracion = entry_duracion.get()
        if ejercicio and duracion.isdigit():
            dict_ejercicios[ejercicio] = int(duracion)
            entry_ejercicio.delete(0, tk.END)
            entry_duracion.delete(0, tk.END)

    tk.Button(ventana_agregar, text='Agregar ejercicio', font=('Verdana', 10), command=agregar_ejercicio).pack(pady=5)
       
    ventana_agregar.mainloop()

#----------------------------VENTANA ELIMINAR EJERCICIO---------------------------------

def abrir_ventana_eliminar():
    ventana_eliminar = tk.Toplevel(ventana)
    ventana_eliminar.title('Eliminar ejercicios')
    ventana_eliminar.geometry('600x400')

    tk.Label(ventana_eliminar, text='Seleccione el ejercicio a eliminar:', font=('Verdana', 10)).pack(pady=10)
    listbox_ejercicios = tk.Listbox(ventana_eliminar, font=('Verdana', 10))
    listbox_ejercicios.pack(pady=5)

    # Función para eliminar el ejercicio seleccionado del diccionario

    ventana_eliminar.mainloop()

#----------------------------VENTANA DEFINIR DESCANSO---------------------------------

def abrir_ventana_descanso():
    ventana_descanso = tk.Toplevel(ventana)
    ventana_descanso.title('Definir descanso')
    ventana_descanso.geometry('600x400')

    tk.Label(ventana_descanso, text='Ingrese el tiempo de descanso (en segundos):', font=('Verdana', 10)).pack(pady=10)
    entry_descanso = tk.Entry(ventana_descanso, font=('Verdana', 10))
    entry_descanso.pack(pady=5)

    # Función para definir el tiempo de descanso

    ventana_descanso.mainloop()

#----------------------------VENTANA DEFINIR RUTINA---------------------------------

def abrir_ventana_rutinas():
    ventana_rutinas = tk.Toplevel(ventana)
    ventana_rutinas.title('Definir rutina')
    ventana_rutinas.geometry('600x400')

    tk.Label(ventana_rutinas, text='Seleccione los ejercicios para la rutina:', font=('Verdana', 10)).pack(pady=10)
    listbox_rutina = tk.Listbox(ventana_rutinas, font=('Verdana', 10))
    listbox_rutina.pack(pady=5)

    # Función para definir la rutina con los ejercicios seleccionados y el tiempo de descanso

    ventana_rutinas.mainloop()

#----------------------------VENTANA INICIAR RUTINA---------------------------------

def abrir_ventana_iniciar():
    ventana_iniciar = tk.Toplevel(ventana)
    ventana_iniciar.title('Iniciar rutina')
    ventana_iniciar.geometry('600x400')

    tk.Label(ventana_iniciar, text='Iniciar rutina', font=('Verdana', 10)).pack(pady=10)

    #Temporizador y botones para iniciar y detener la rutina según el tiempo de los ejercicios y descanso
    tk.Button(ventana_iniciar, text='Iniciar', font=('Verdana', 10)).pack(pady=5)

    temporizador = tk.Label(ventana_iniciar, font = ('Arial', 60), bg = 'blue', fg = 'white')

    def temporizar():
        tiempo_actual = t.strftime('%H:%M:%S')
        temporizador.config(text = tiempo_actual)
        ventana.after(1000, temporizar)

    temporizador.pack(anchor = 'center')

    ventana_iniciar.mainloop()

#----------------------------VENTANA PRINCIPAL---------------------------------

ventana = tk.Tk()
ventana.title('App de rutinas')
ventana.geometry("600x400")

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label = 'Menu', menu=menu_principal)

submenu_ejercicios = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label = 'Ejercicios', menu=submenu_ejercicios)
submenu_ejercicios.add_command(label = 'Agregar ejercicios', command=(abrir_ventana_agregar))
submenu_ejercicios.add_command(label = 'Eliminar ejercicios', command=(abrir_ventana_eliminar))

submenu_rutinas = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label = 'Rutinas', menu=submenu_rutinas)
submenu_rutinas.add_command(label = 'Definir descanso', command=(abrir_ventana_descanso))
submenu_rutinas.add_command(label = 'Definir rutina', command=(abrir_ventana_rutinas))

menu_principal.add_command(label = 'Iniciar rutina', command=(abrir_ventana_iniciar))
menu_principal.add_command(label = 'Salir', command=ventana.quit)

tk.Label(ventana, text = 'BIENVENIDO A LA APP DE RUTINAS', font=('Verdana', 10, 'bold'), pady= 20).pack()
tk.Label(ventana, text = 'Aqui podrás generar tu propia rutina para ejercitarte', font=('Verdana', 10)).pack()

ventana.mainloop()