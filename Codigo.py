import sys
import datetime

separador=("*"*30)
menu=1
listanombreproduc=[]
listaunidadavender=[]
contadorp=1
while menu==1:
    print(separador+" Bienvenido al Programa "+separador)
    print("")
    print("-"*15+" Este programa realiza el Presupuesto Maestro "+"-"*15)
    print("")
    #Preguntar datos y agregar a variables
    productocon=int(input("Dime cuantos productos son :"))
    for producto in range(productocon):
        nombre=input(f"Dime el nombre del Producto{contadorp} :")
        listanombreproduc.append(nombre)
        contadorp=contadorp+1

