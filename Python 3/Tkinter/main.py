from tkinter import *
import tkinter
import random, string

def keygen():
        myrg = random.SystemRandom()
        longitud = int(entrada.get())
        alfabeto = ""
        
        if (var.get()):
                alfabeto += string.ascii_letters
        if (var1.get()):
                alfabeto += string.digits
        if (var2.get()):
                alfabeto += string.punctuation
        
        contraseña = str().join(myrg.choice(alfabeto) 
        for _ in range(longitud))
        miContraseña = Label(ventana, text = contraseña)
        miContraseña.pack()
        print(contraseña)

ventana = tkinter.Tk()
ventana.geometry("400x300")
ventana.iconbitmap('Python 3\Tkinter\Icon.ico')
ventana.title("Generador de contraseñas (PerSec)")

etiqueta = tkinter.Label(ventana, text = "Generador de contrseñas", bg = "gray")
etiqueta.pack(fill = tkinter.X)

etiqueta2 = tkinter.Label(ventana, text = "Introduce la cantidad de caracteres.", bg = "gray94")
etiqueta2.pack(fill = tkinter.X)

entrada = Entry(ventana, width = 50, bg='#000000', fg='#b7f731', relief='flat')
entrada.pack()

etiqueta3 = tkinter.Label(ventana, text = "¿Que tipo de caracteres deseas en la contraseña?", bg = "gray94")
etiqueta3.pack(fill = tkinter.X)

var = IntVar()
var1 = IntVar()
var2 = IntVar()

opcionUno = Checkbutton(ventana, text = "Alfabeto", variable = var)
opcionUno.pack()

opcionDos = Checkbutton(ventana, text = "Números", variable = var1)
opcionDos.pack()

opcionTres = Checkbutton(ventana, text = "Símbolo", variable = var2)
opcionTres.pack()


etiqueta4 = tkinter.Label(ventana, text = "Presiona el botón para generar una contraseña.", pady = 30)
etiqueta4.pack(fill = tkinter.X)

boton = tkinter.Button(ventana, text = "Generar contraseña",  bg='#000000', fg='#b7f731', relief='flat', command = keygen)
boton.pack()

ventana.mainloop()