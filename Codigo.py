import sys
import datetime

separador=("*"*30)
menu=1
listanombreproduc=[]
listaunidadavender=[]
listaprecioventa=[]
listatotal=[]
listaimportedeventa1=[]
listaimportedeventa2=[]
contadorp=1
contadoru=0
contador3=0
contador4=0
primer="Primer Semestre"
segundo="Segundo Semestre"
while menu==1:
    print(separador+" Bienvenido al Programa "+separador)
    print("")
    print("-"*15+" Este programa realiza el Presupuesto Maestro "+"-"*15)
    print("")
    #Preguntar datos y agregar a variables
    año=input("Dime el año 1 : ")
    año2=input("Dime el año 2: ")
    productocon=int(input("Dime cuantos productos son :"))
    for producto in range(productocon):
        nombre=input(f"Dime el nombre del Producto{contadorp} :")
        listanombreproduc.append(nombre)
        contadorp=contadorp+1
    print(separador)

    for producto in listanombreproduc:
        unidadavender=int(input(f"Dime las unidades a vender de el producto {listanombreproduc[contadoru]} del {primer} : "))
        listaunidadavender.append(unidadavender)

        preciodeventa=float(input(f"Dime el precio de Venta de el producto {listanombreproduc[contadoru]} del {primer} : "))
        listaprecioventa.append(preciodeventa)
        print(separador)
        listaimportedeventa1.append(unidadavender*preciodeventa)

        unidadavender2=int(input(f"Dime las unidades a vender de el producto {listanombreproduc[contadoru]} del {segundo} : "))
        listaunidadavender.append(unidadavender2)

        preciodeventa2=float(input(f"Dime el precio de Venta de el producto {listanombreproduc[contadoru]} del {segundo} : "))
        listaprecioventa.append(preciodeventa2)
        print(separador)
        listaimportedeventa2.append(unidadavender2*preciodeventa2)
        
        contadoru=contadoru+1
        
    print(separador+"Respuestas del Presupuesto de Ventas"+separador)

    for nombre in listanombreproduc:
        print(nombre+":")
        print("PRIMER SEMESTRE")
        print(f"UNIDADES A VENDER: {listaunidadavender[contador3]}")
        print(f"PRECIO DE VENTA:{listaprecioventa[contador3]}")
        print(f"IMPORTE DE VENTA: {listaimportedeventa1[contador4]}")
        contador3=contador3+1
        print("SEGUNDO SEMESTRE")
        print(f"UNIDADES A VENDER: {listaunidadavender[contador3]}")
        print(f"PRECIO DE VENTA:{listaprecioventa[contador3]}")
        print(f"IMPORTE DE VENTA: {listaimportedeventa2[contador4]}")
        print(separador)
        contador3=contador3+1
        contador4=contador4+1
    totalventasS1=(sum(listaimportedeventa1))
    totalventasS2=(sum(listaimportedeventa2))
    VENTASTOTALES=(totalventasS1+totalventasS2)
    print(separador)
    print("Total PrimerS\t", end="")
    print("Total SegundoS\t", end="")
    print("Ventas Totales")
    print(f"{totalventasS1}\t",end="")
    print(f"{totalventasS2}\t",end="")
    print(VENTASTOTALES)
    print(separador*2)

    saldoCliente=float(input("Dime el saldo de Clientes del Balance General : "))
    totalCliente=(saldoCliente+VENTASTOTALES)

    porcentaje=float(input("Cuanto porcentaje del total de Ventas se va aplicar por cobranza ejemplo(.80) : "))
    cobranza=(VENTASTOTALES*porcentaje)
    totalEntradas=(cobranza+saldoCliente)
    SALDODECLIENTES=(totalCliente-totalEntradas)

    print(separador+"Determinacion de saldo de clientes y flujo de entradas"+separador)
    print(f"Saldo de Clientes {año} : {saldoCliente}")
    print(f"Ventas {año2}: {VENTASTOTALES}")
    print(f"Total de Clientes {año2}: {totalCliente}")
    print("")
    print("Entradas de Efectivo: ")
    print(f"Por cobranza del {año}: {saldoCliente}")
    print(f"Por cobranza del {año2}: {cobranza}")
    print(f"Total de Entradas del {año2} : {totalEntradas}")
    print(f"Saldo de Clientes del {año2} : {SALDODECLIENTES}")










