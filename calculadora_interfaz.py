"""CODIGO DE INTERFAZ DE UNA CALCULADORA UTILIZANDO TKINTER"""

from tkinter import *
from math import *

def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)

def resultado():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""

def clear():
    global operador
    operador=("")
    input_text.set("0")

def borrar_uno ():
    global operador
    if operador==-1:
        pass
    else:
        Salida.delete(operador, last = None)
        num=int(operador)
        num-=1


#PRIMEROS ELEMENTOS GRAFICOS: TAMAÑO DE LA CALCULADORA 
ventana = Tk ()
ventana.title ("CALCULADORA")
ventana.geometry ("482x600")
ventana.resizable (0,0)

#DEFINIMOS LAS DIMENSIONES DE LOS BOTONES 
ancho_boton = 11
alto_boton = 3

#CREAMOS BOTON DE RESULTADO
anchoRes= 24
altoRes=7
colorRes= ("green")

#DEFINIMOS EL COLOR DE LOS BOTONES
ventana.configure (background="#5D478B")
color_boton=("gray77")

#VARIABLES PARA LA FUNCION "btnClick"
input_text=StringVar()
operador=""

#DEFINIMOS LOS BOTONES 
BotonC = Button (ventana, text="C", bg=color_boton, width=ancho_boton, height=alto_boton, command=clear) .place (x=17,y=180)
BotonParen1 = Button (ventana, text="(", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("(")) .place (x=107,y=180)
BotonParen2 = Button (ventana, text=")", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(")")) .place (x=197,y=180)
BotonSqrt = Button (ventana, text="√", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("sqrt(")) .place (x=287,y=180)
BotonPi = Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("pi")) .place (x=378,y=180)
BotonSin = Button (ventana, text="sin", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("sin(")) .place (x=17,y=240)
BotonCos = Button (ventana, text="cos", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("cos(")) .place (x=107,y=240)
BotonTag = Button (ventana, text="tag", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("tan(")) .place (x=197,y=240)
BotonDiv = Button (ventana, text="/", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("/")) .place (x=287,y=240)
BotonMulti = Button (ventana, text="*", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("*")) .place (x=378,y=240)
Boton7 = Button (ventana, text="7", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(7)) .place (x=17,y=300)
Boton8 = Button (ventana, text="8", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(8)) .place (x=107,y=300)
Boton9 = Button (ventana, text="9", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(9)) .place (x=197,y=300)
BotonEqLi = Button (ventana, text="ln", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("log(")) .place (x=287,y=300)
BotonResta = Button (ventana, text="-", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("-")) .place (x=378,y=300)
Boton4 = Button (ventana, text="4", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(4)) .place (x=17,y=360)
Boton5 = Button (ventana, text="5", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(5)) .place (x=107,y=360)
Boton6 = Button (ventana, text="6", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(6)) .place (x=197,y=360)
BotonPot = Button (ventana, text="xˣ", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("**")) .place (x=287,y=360)
BotonSuma = Button (ventana, text="+", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("+")) .place (x=378,y=360)
Boton1 = Button (ventana, text="1", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(1)) .place (x=17,y=420)
BotonP = Button (ventana, text=".", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(".")) .place (x=17,y=480)
Boton0 = Button (ventana, text="0", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(0)) .place (x=107,y=480)
BotonPor = Button (ventana, text="%", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("%")) .place (x=197,y=480)
Boton2 = Button (ventana, text="2", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(2)) .place (x=107,y=420)
Boton3 = Button (ventana, text="3", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(3)) .place (x=197,y=420)
BotonResul = Button (ventana, text="=", bg=colorRes, width=anchoRes, height=altoRes, relief= "groove", command=resultado) .place (x=287,y=420)

Salida=Entry(ventana,font=('arial',20,'bold'),width=28,
textvariable=input_text,bd=20,insertwidth=4,bg="#20B2AA",justify="right")
Salida.place(x=10,y=60)

clear ()
                
                
ventana.mainloop()
