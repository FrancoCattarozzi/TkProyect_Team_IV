import tkinter as tk
import time as t

dict_ejercicios = {}
tiempo_descanso = 0
rutina = {}
descansos_intermedios = {}

#----------------------------VENTANA PRINCIPAL---------------------------------

ventana = tk.Tk()
ventana.title('App de rutinas')
ventana.geometry("600x400")

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Menu', menu=menu_principal)

submenu_ejercicios = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label='Ejercicios', menu=submenu_ejercicios)
submenu_rutinas = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label='Rutinas', menu=submenu_rutinas)

tk.Label(ventana, text='BIENVENIDO A LA APP DE RUTINAS', font=('Verdana', 10, 'bold'), pady=20).pack()
tk.Label(ventana, text='Aquí podrás generar tu propia rutina para ejercitarte', font=('Verdana', 10)).pack()

listbox_principal = tk.Listbox(ventana, font=('Verdana', 10))
listbox_principal.pack(pady=10)

def actualizar_listbox_principal():
    listbox_principal.delete(0, tk.END)
    for ejercicio, duracion in dict_ejercicios.items():
        listbox_principal.insert(tk.END, f"{ejercicio} - {duracion} segundos")

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

    def agregar_ejercicio():
        ejercicio = entry_ejercicio.get()
        duracion = entry_duracion.get()
        if ejercicio and duracion.isdigit():
            dict_ejercicios[ejercicio] = int(duracion)
            entry_ejercicio.delete(0, tk.END)
            entry_duracion.delete(0, tk.END)
            actualizar_listbox_principal()

    tk.Button(ventana_agregar, text='Agregar ejercicio', font=('Verdana', 10), command=agregar_ejercicio).pack(pady=5)

#----------------------------VENTANA ELIMINAR EJERCICIO---------------------------------

def abrir_ventana_eliminar():
    ventana_eliminar = tk.Toplevel(ventana)
    ventana_eliminar.title('Eliminar ejercicios')
    ventana_eliminar.geometry('600x400')

    tk.Label(ventana_eliminar, text='Seleccione el ejercicio a eliminar:', font=('Verdana', 10)).pack(pady=10)
    listbox_ejercicios = tk.Listbox(ventana_eliminar, font=('Verdana', 10))
    listbox_ejercicios.pack(pady=5)

    for ejercicio in dict_ejercicios:
        listbox_ejercicios.insert(tk.END, ejercicio)

    def eliminar_ejercicio():
        seleccion = listbox_ejercicios.curselection()
        if seleccion:
            ejercicio = listbox_ejercicios.get(seleccion)
            if ejercicio in dict_ejercicios:
                del dict_ejercicios[ejercicio]
                listbox_ejercicios.delete(seleccion)
                actualizar_listbox_principal()

    tk.Button(ventana_eliminar, text='Eliminar', font=('Verdana', 10), command=eliminar_ejercicio).pack(pady=5)

#----------------------------VENTANA DEFINIR DESCANSO GENERAL---------------------------------

def abrir_ventana_descanso():
    ventana_descanso = tk.Toplevel(ventana)
    ventana_descanso.title('Definir descanso')
    ventana_descanso.geometry('600x400')

    tk.Label(ventana_descanso, text='Ingrese el tiempo de descanso general (en segundos):', font=('Verdana', 10)).pack(pady=10)
    entry_descanso = tk.Entry(ventana_descanso, font=('Verdana', 10))
    entry_descanso.pack(pady=5)

    def definir_descanso():
        global tiempo_descanso
        valor = entry_descanso.get()
        if valor.isdigit():
            tiempo_descanso = int(valor)
            ventana_descanso.destroy()

    tk.Button(ventana_descanso, text='Guardar', font=('Verdana', 10), command=definir_descanso).pack(pady=5)

#----------------------------VENTANA DEFINIR RUTINA---------------------------------

def abrir_ventana_rutinas():
    ventana_rutinas = tk.Toplevel(ventana)
    ventana_rutinas.title('Definir rutina')
    ventana_rutinas.geometry('600x400')

    tk.Label(ventana_rutinas, text='Seleccione los ejercicios para la rutina:', font=('Verdana', 10)).pack(pady=10)
    listbox_rutina = tk.Listbox(ventana_rutinas, font=('Verdana', 10), selectmode=tk.MULTIPLE)
    listbox_rutina.pack(pady=5)

    for ejercicio in dict_ejercicios:
        listbox_rutina.insert(tk.END, ejercicio)

    def definir_rutina():
        seleccionados = listbox_rutina.curselection()
        rutina.clear()
        descansos_intermedios.clear()

        for i in seleccionados:
            ejercicio = listbox_rutina.get(i)
            rutina[ejercicio] = dict_ejercicios[ejercicio]

            ventana_input = tk.Toplevel(ventana_rutinas)
            ventana_input.title(f'Descanso tras "{ejercicio}"')
            ventana_input.geometry('400x200')

            tk.Label(ventana_input, text=f'Descanso después de "{ejercicio}" (segundos):', font=('Verdana', 10)).pack(pady=10)
            entry = tk.Entry(ventana_input, font=('Verdana', 10))
            entry.pack(pady=5)

            def guardar():
                valor = entry.get()
                if valor.isdigit():
                    descansos_intermedios[ejercicio] = int(valor)
                    ventana_input.destroy()
                else:
                    entry.delete(0, tk.END)
                    entry.insert(0, "Solo números")

            tk.Button(ventana_input, text='Guardar', command=guardar).pack(pady=10)
            ventana_input.wait_window()

        ventana_rutinas.destroy()

    tk.Button(ventana_rutinas, text='Guardar rutina', font=('Verdana', 10), command=definir_rutina).pack(pady=5)

#----------------------------VENTANA INICIAR RUTINA---------------------------------

def abrir_ventana_iniciar():
    ventana_iniciar = tk.Toplevel(ventana)
    ventana_iniciar.title('Iniciar rutina')
    ventana_iniciar.geometry('600x400')

    tk.Label(ventana_iniciar, text='Iniciar rutina', font=('Verdana', 10)).pack(pady=10)

    temporizador = tk.Label(ventana_iniciar, font=('Arial', 60), bg='blue', fg='white')
    temporizador.pack(anchor='center')

    def cuenta_regresiva(segundos, texto, callback):
        if segundos >= 0:
            minutos = segundos // 60
            segs = segundos % 60
            temporizador.config(text=f"{texto}\n{minutos:02d}:{segs:02d}")
            ventana_iniciar.after(1000, lambda: cuenta_regresiva(segundos - 1, texto, callback))
        else:
            callback()

    def iniciar_rutina():
        ejercicios = list(rutina.items())
        if not ejercicios:
            temporizador.config(text="Sin rutina")
            return

        def ejecutar_ejercicio(idx):
            if idx < len(ejercicios):
                ejercicio, duracion = ejercicios[idx]
                cuenta_regresiva(duracion, ejercicio, lambda: ejecutar_descanso(idx))
            else:
                temporizador.config(text="¡Rutina terminada!")

        def ejecutar_descanso(idx):
            ejercicio_actual = ejercicios[idx][0]
            descanso = descansos_intermedios.get(ejercicio_actual, tiempo_descanso)
            if descanso > 0:
                cuenta_regresiva(descanso, "Descanso", lambda: ejecutar_ejercicio(idx + 1))
            else:
                ejecutar_ejercicio(idx + 1)

        ejecutar_ejercicio(0)

    tk.Button(ventana_iniciar, text='Iniciar', font=('Verdana', 10), command=iniciar_rutina).pack(pady=5)

#----------------------------ASOCIAR FUNCIONES AL MENÚ---------------------------------

submenu_ejercicios.add_command(label='Agregar ejercicios', command=abrir_ventana_agregar)
submenu_ejercicios.add_command(label='Eliminar ejercicios', command=abrir_ventana_eliminar)
submenu_rutinas.add_command(label='Definir descanso general', command=abrir_ventana_descanso)
submenu_rutinas.add_command(label='Definir rutina (con descansos)', command=abrir_ventana_rutinas)
menu_principal.add_command(label='Iniciar rutina', command=abrir_ventana_iniciar)  # ✔️ Esta línea debe estar
menu_principal.add_command(label='Salir', command=ventana.quit)

ventana.mainloop()
