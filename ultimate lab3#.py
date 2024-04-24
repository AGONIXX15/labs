#se importa la libreria de tkinter para darle una interfaz grafica al programa
import tkinter as tk
from tkinter import messagebox
global victorias1
global victorias2
global empates
victorias1=0
victorias2=0
empates=0
turno=0
#se crea la funcion ventana_juego_jugador_jugador para crear la ventana de juego jugador jugador
def ventana_juego_jugador_jugador(ventana_nombre):
    ventana_nombre = tk.Tk()
    #se crea un titulo para la ventana
    ventana_nombre.title("Juego")
    ventana_nombre.geometry("1000x600")
    ventana_nombre.config(bg="black")
    def datos(nombre1, nombre2,entrada1, entrada2,partidas_entrada ,ventana_juego):
        global victorias1
        global victorias2
        global empates
        global turno
        victorias1=0
        victorias2=0
        empates=0
        lista_nombres = []
        lista_datos = []
        turno=0
        global partidas_int
        partidas_int = int(partidas_entrada.get())
        if nombre1.get() == "" or nombre2.get() == "":
            messagebox.showerror("Error", "Debe ingresar los nombres de los jugadores")
        elif  entrada1.get() == "" or entrada2.get() == "":
            messagebox.showerror("Error", "Debe ingresar los caracteres que va a usar")
        elif entrada1.get() == entrada2.get():
            messagebox.showerror("Error", "Los caracteres deben ser diferentes")
        elif partidas_int <=0:
            messagebox.showerror("Error", "El numero de partidas debe ser mayor a 0")
        else:
           lista_nombres.append(nombre1.get())
           lista_nombres.append(nombre2.get())
           lista_datos.append(entrada1.get())
           lista_datos.append(entrada2.get())
           ventana_nombre.destroy()
           ventana_juego_jugador(lista_nombres,lista_datos)
    # se cre la funcion de reiniciar dentro del juego
    def reiniciar(ventana_juego):
        ventana_juego.destroy()
        ventana_juego_jugador_jugador(ventana_nombre)
    #  se crea lo que va a leer el programa
    
    # las entradas mientras juega el usuario
    def entradas_juego(ventana_juego,boton,lista_nombres,lista_datos,partidas_int,x,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,y):
        global aux,turno
        global turno_label
        aux-=1
        if y%2==0:    
         if x%2==0:
             boton.config(text=lista_datos[1])
             condiciones(lista_datos,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,lista_nombres,ventana_juego)
             turno=0
             turno_label.config(text=f"Turno del jugador {lista_nombres[turno]}")
         else:
             boton.config(text=lista_datos[0]) 
             condiciones(lista_datos,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,lista_nombres,ventana_juego)
             boton.config(state="disabled")
             turno=1
             turno_label.config(text=f"Turno del jugador {lista_nombres[turno]}")
        else:
            if x%2==0:
             boton.config(text=lista_datos[0])
             condiciones(lista_datos,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,lista_nombres,ventana_juego)
             turno=1
             turno_label.config(text=f"Turno del jugador {lista_nombres[turno]}")
            else:
             boton.config(text=lista_datos[1]) 
             condiciones(lista_datos,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,lista_nombres,ventana_juego)
             turno=0
             turno_label.config(text=f"Turno del jugador {lista_nombres[turno]}")
        boton.config(state="disabled")
        
    
    def tabla_victorias(lista_nombres,lista_datos):
        tabla=tk.Tk()
        tabla.title("Tabla de victorias")
        tabla.geometry("500x500")
        titulo= tk.Label(tabla, text="Tabla de victorias", bg="black", fg="white", font=("Arial", 20))
        titulo.grid(row=0, column=0, columnspan=2, padx=100, pady=20)
        jugador1=tk.Label(tabla, text=f"Jugador {lista_nombres[0]}", bg="black", fg="white", font=("Arial", 12))
        jugador1.grid(row=1, column=0, padx=0, pady=10)
        jugador2=tk.Label(tabla, text=f"Jugador {lista_nombres[1]}", bg="black", fg="white", font=("Arial", 12))
        jugador2.grid(row=1, column=1, padx=0, pady=10)
        victorias1_=tk.Label(tabla, text=f"Victorias de {lista_nombres[0]}: {victorias1}", bg="black", fg="white", font=("Arial", 12))
        victorias1_.grid(row=2, column=0, padx=0, pady=10)
        victorias2_=tk.Label(tabla, text=f"Victorias de {lista_nombres[1]}: {victorias2}", bg="black", fg="white", font=("Arial", 12))
        victorias2_.grid(row=2, column=1, padx=0, pady=10)
        empates_=tk.Label(tabla, text=f"Empates: {empates}", bg="black", fg="white", font=("Arial", 12))
        empates_.grid(row=3, column=0, columnspan=2, padx=0, pady=10)
        tabla.after(3000,tabla.destroy)
        tabla.mainloop()
        ventana_juego_jugador(lista_nombres,lista_datos)
    #se crea las condiciones de paradas,victoria y empate
    def condiciones(lista_datos,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,lista_nombres,ventana_juego):
        global partidas_int
        global victorias1
        global victorias2
        global empates
        global turno
        if boton1["text"]==boton2["text"]==boton3["text"]==lista_datos[0]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[0]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias1+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        elif boton4["text"]==boton5["text"]==boton6["text"]==lista_datos[0]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[0]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias1+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        elif boton7["text"]==boton8["text"]==boton9["text"]==lista_datos[0]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[0]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias1+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        #vertical
        elif boton1["text"]==boton4["text"]==boton7["text"]==lista_datos[0]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[0]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias1+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        elif boton2["text"]==boton5["text"]==boton8["text"]==lista_datos[0]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[0]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias1+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        elif boton3["text"]==boton6["text"]==boton9["text"]==lista_datos[0]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[0]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias1+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        #diagonal
        elif boton1["text"]==boton5["text"]==boton9["text"]==lista_datos[0]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[0]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias1+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        elif boton3["text"]==boton5["text"]==boton7["text"]==lista_datos[0]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[0]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias1+=1
            tabla_victorias(lista_nombres,lista_datos)
        #horizontal
        elif boton1["text"]==boton2["text"]==boton3["text"]==lista_datos[1]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[1]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias2  +=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        elif boton4["text"]==boton5["text"]==boton6["text"]==lista_datos[1]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[1]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias2+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        elif boton7["text"]==boton8["text"]==boton9["text"]==lista_datos[1]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[1]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias2+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        #vertical
        elif boton1["text"]==boton4["text"]==boton7["text"]==lista_datos[1]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[1]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias2+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        elif boton2["text"]==boton5["text"]==boton8["text"]==lista_datos[1]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[1]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias2+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        elif boton3["text"]==boton6["text"]==boton9["text"]==lista_datos[1]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[1]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias2+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        #diagonal
        elif boton1["text"]==boton5["text"]==boton9["text"]==lista_datos[1]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[1]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias2+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        elif boton3["text"]==boton5["text"]==boton7["text"]==lista_datos[1]:
            messagebox.showinfo("Victoria", f"El jugador {lista_nombres[1]} ha ganado")
            ventana_juego.destroy()
            partidas_int-=1
            victorias2+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
        elif boton1["text"]!= "" and boton2["text"]!= "" and boton3["text"]!= "" and boton4["text"]!= "" and boton5["text"]!= "" and boton6["text"]!= "" and boton7["text"]!= "" and boton8["text"]!= "" and boton9["text"]!= "":
            messagebox.showinfo("Empate", "No hay ganador")
            ventana_juego.destroy()
            partidas_int-=1
            empates+=1
            turno+=1
            tabla_victorias(lista_nombres,lista_datos)
            
    #tabla de victorias,derrotas y empates
    #se crea la ventana donde se va a jugar
    def ventana_juego_jugador(lista_nombres,lista_datos):
        global partidas_int
        global turno_label
        global turno
        if partidas_int%2==0:
            turno=0
        else:
            turno=1
        while partidas_int!=0:
         ventana_juego = tk.Tk()
         ventana_juego.title("Juego")
         ventana_juego.geometry("1500x1000")
         ventana_juego.config(bg="black")
         global aux
         aux=9
         while aux !=0:
          titulo= tk.Label(ventana_juego, text=f"{lista_nombres[0]} vs {lista_nombres[1]}" ,bg="black", fg="white", font=("Arial", 20))
          titulo.grid(row=0, column=0, padx=80, pady=20)
          games=tk.Label(ventana_juego, text=f"Partidas restantes: {partidas_int}", bg="black", fg="white", font=("Arial", 20))
          games.grid(row=0, column=2, pady=20)
          turno_label=tk.Label(ventana_juego, text=f"Turno del jugador {lista_nombres[turno%2]}", bg="black", fg="white", font=("Arial", 20))
          turno_label.grid(row=0, column=1, pady=20)
          retry=tk.Button(ventana_juego, text="Reiniciar", bg="red", fg="white", font=("Arial bold", 12), width=20, height=2, command=lambda:reiniciar(ventana_juego))
          retry.grid(row=2, column=5, pady=20)
          salir=tk.Button(ventana_juego, text="salir", bg="red", fg="white", font=("Arial bold", 12), width=20, height=2, command=ventana_juego.destroy)
          salir.grid(row=3, column=5, pady=20)
          boton1=tk.Button(ventana_juego, text="", bg="white", fg="black", font=("Arial bold", 25), width=20, height=2, command=lambda:entradas_juego(ventana_juego,boton1,lista_nombres,lista_datos,partidas_int,aux,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,partidas_int))
          boton2=tk.Button(ventana_juego, text="", bg="white", fg="black", font=("Arial bold", 25), width=20, height=2, command=lambda:entradas_juego(ventana_juego,boton2,lista_nombres,lista_datos,partidas_int,aux,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,partidas_int))
          boton3=tk.Button(ventana_juego, text="", bg="white", fg="black", font=("Arial bold", 25), width=20, height=2, command=lambda:entradas_juego(ventana_juego,boton3,lista_nombres,lista_datos,partidas_int,aux,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,partidas_int))
          boton4=tk.Button(ventana_juego, text="", bg="white", fg="black", font=("Arial bold", 25), width=20, height=2, command=lambda:entradas_juego(ventana_juego,boton4,lista_nombres,lista_datos,partidas_int,aux,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,partidas_int))
          boton5=tk.Button(ventana_juego, text="", bg="white", fg="black", font=("Arial bold", 25), width=20, height=2, command=lambda:entradas_juego(ventana_juego,boton5,lista_nombres,lista_datos,partidas_int,aux,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,partidas_int))
          boton6=tk.Button(ventana_juego, text="", bg="white", fg="black", font=("Arial bold", 25), width=20, height=2, command=lambda:entradas_juego(ventana_juego,boton6,lista_nombres,lista_datos,partidas_int,aux,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,partidas_int))
          boton7=tk.Button(ventana_juego, text="", bg="white", fg="black", font=("Arial bold", 25), width=20, height=2, command=lambda:entradas_juego(ventana_juego,boton7,lista_nombres,lista_datos,partidas_int,aux,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,partidas_int))
          boton8=tk.Button(ventana_juego, text="", bg="white", fg="black", font=("Arial bold", 25), width=20, height=2, command=lambda:entradas_juego(ventana_juego,boton8,lista_nombres,lista_datos,partidas_int,aux,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,partidas_int))
          boton9=tk.Button(ventana_juego, text="", bg="white", fg="black", font=("Arial bold", 25), width=20, height=2, command=lambda:entradas_juego(ventana_juego,boton9,lista_nombres,lista_datos,partidas_int,aux,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,partidas_int))
          #se le da una posicion a los botones
          boton1.grid(row=1, column=0, padx=0, pady=10)
          boton2.grid(row=1, column=1, padx=0, pady=10)
          boton3.grid(row=1, column=2, padx=0, pady=10)
          boton4.grid(row=2, column=0, padx=0, pady=10)
          boton5.grid(row=2, column=1, padx=0, pady=10)
          boton6.grid(row=2, column=2, padx=0, pady=10)
          boton7.grid(row=3, column=0, padx=0, pady=10)
          boton8.grid(row=3, column=1, padx=0, pady=10)
          boton9.grid(row=3, column=2, padx=0, pady=10)
          ventana_juego.mainloop()
        if victorias1 > victorias2:
         ganador = lista_nombres[0]
        elif victorias2 > victorias1:
         ganador = lista_nombres[1]
        else:
         ganador = "Ninguno, es un empate"
        messagebox.showinfo("Fin del juego", f"El ganador definitivo es: {ganador}")
        
    #se crea un titulo para la ventana
    titulo= tk.Label(ventana_nombre, text="Juego", bg="black", fg="white", font=("Arial", 20))
    #se le da una posicion al titulo
    titulo.grid(row=0, column=0, padx=80, pady=20)
    subtitulo=tk.Label(ventana_nombre, text="Ingrese los nombres de los jugadores", bg="black", fg="white", font=("Arial", 12))
    jugador1=tk.Label(ventana_nombre, text="Jugador 1", bg="black", fg="white", font=("Arial", 12))
    nombre1=tk.Entry(ventana_nombre, bg="white", fg="black", font=("Arial bold", 18))
    jugador2=tk.Label(ventana_nombre, text="Jugador 2", bg="black", fg="white", font=("Arial", 12))
    nombre2=tk.Entry(ventana_nombre, bg="white", fg="black", font=("Arial bold", 18))
    enviar=tk.Button(ventana_nombre, text="Enviar", bg="red", fg="white", font=("Arial", 12), width=20, height=2, command=lambda: datos(nombre1, nombre2,entrada1, entrada2,partidas_entrada ,ventana_juego_jugador))
    figura1=tk.Label(ventana_nombre, text="escoja el caracter que va a usar", bg="black", fg="white", font=("Arial", 12))
    entrada1=tk.Entry(ventana_nombre, bg="white", fg="black", font=("Arial bold", 18))
    figura2=tk.Label(ventana_nombre, text="escoja el caracter que va a usar", bg="black", fg="white", font=("Arial", 12))
    entrada2=tk.Entry(ventana_nombre, bg="white", fg="black", font=("Arial bold", 18), width=20)
    partidas=tk.Label(ventana_nombre, text="Ingrese el numero de partidas", bg="black", fg="white", font=("Arial", 12))
    partidas_entrada=tk.Entry(ventana_nombre, bg="white", fg="black", font=("Arial bold", 18))
    #se le da una posicion a los labels y a los entrys
    subtitulo.grid(row=1, column=0, columnspan=2, padx=0, pady=10)
    jugador1.grid(row=2, column=0, padx=0, pady=10) 
    nombre1.grid(row=2, column=1, padx=5, pady=10)
    jugador2.grid(row=3, column=0, padx=0, pady=10)
    nombre2.grid(row=3, column=1, padx=5, pady=10)
    enviar.grid(row=4, column=3, padx=0, pady=10)
    figura1.grid(row=2, column=2, padx=0, pady=10)
    entrada1.grid(row=2, column=3, padx=0, pady=10,)
    figura2.grid(row=3, column=2, padx=0, pady=10)
    entrada2.grid(row=3, column=3, padx=0, pady=10, )
    partidas.grid(row=4, column=0, padx=0, pady=10)
    partidas_entrada.grid(row=4, column=1, padx=0, pady=10)
  

    ventana_nombre.mainloop()
    
# se crea la funcion click para que al dar click en el boton de jugador vs jugador se abra la ventana de juego jugador jugador

def click(ventana):
    ventana_menu.destroy()
    ventana_juego_jugador_jugador(ventana)
    pass


#se crea la ventana de menu:
ventana_menu = tk.Tk()
ventana_menu.title("Menu")
ventana_menu.geometry("500x500")
#se le da un color de fondo a la ventana


ventana_menu.config(bg="black")
#se crea un titulo para la ventana
titulo= tk.Label(ventana_menu, text="Bienvenido a la aplicacion", bg="black", fg="white", font=("Arial", 20))
#se le da una posicion al titulo
titulo.grid(row=0, column=0, columnspan=1, padx=100, pady=20)
#se crean los botones para las opciones
opcion2= tk.Button(ventana_menu, text="Jugador vs jugador", bg="red", fg="white", font=("Arial", 12), width=20, height=2,command=lambda:click(ventana_juego_jugador_jugador))
opcion3= tk.Button(ventana_menu, text="Salir", bg="red", fg="white", font=("Arial", 12), width=20, height=2, command=ventana_menu.quit)
#se le da una posicion a los botones
opcion2.grid(row=2, column=0, padx=10, pady=10)
opcion3.grid(row=3, column=0, padx=10, pady=10)
ventana_menu.mainloop()

