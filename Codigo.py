import sys
import datetime

separador=("*"*30)
menu=1
listanombreproduc=[]
listaunidadavender=[]
listadelistas=[]
listadelistas.append(listaunidadavender)
contadorp=1
contadoru=0
primer="Primer Semestre"
segundo="Segundo Semestre"
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

    for producto in listanombreproduc:
        unidadavender=int(input(f"Dime las unidades a vender de el producto {listanombreproduc[contadoru]} del {primer}"))
        preciodeventa=float(input(f"Dime el precio de Venta de el producto {listanombreproduc[contadoru]} del {primer}"))
        contadoru=contadoru+1
        unidadavender2=int(input(f"Dime las unidades a vender de el producto {listanombreproduc[contadoru]} del {segundo}"))
        preciodeventa2=float(input(f"Dime el precio de Venta de el producto {listanombreproduc[contadoru]} del {segundo}"))
        listaunidadavender.append(unidadavender,preciodeventa,unidadavender2,preciodeventa2)
        


