import sys
import datetime

separador=("*"*50)
menu=1
listanombreproduc=[]
listaunidadavender=[]
listaprecioventa=[]
listatotal=[]
listaimportedeventa1=[]
listaimportedeventa2=[]
lista_invfinal1=[]
lista_invfinal2=[]
lista_invinicial1=[]
lista_invinicial2=[]
lista_total_unidades1=[]
lista_total_unidades2=[]
lista_unidad_producir=[]
lista_suma_camisas_producir=[]
contadorp=1
contadoru=0
contador3=0
contador4=0
contador5=0
contador6=0
contador7=0
contador8=0
contador9=0
contador10=0
primer="Primer Semestre"
segundo="Segundo Semestre"
try:
    while menu==1:
        print(separador+" Bienvenido al Programa "+separador)
        print("")
        print("-"*15+" Este programa realiza el Presupuesto Maestro "+"-"*15)
        print("")
        #Preguntar datos y agregar a variables
        año=int(input("Dime el año 1 : "))
        año2=int(input("Dime el año 2: "))
        productocon=int(input("Dime cuantos productos son :"))
        for producto in range(productocon):
            nombre=input(f"Dime el nombre del Producto {contadorp} :")
            listanombreproduc.append(nombre)
            contadorp=contadorp+1
        print(separador)
        #TABLA 1
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
        archivoA=open("./respuestas.txt" , 'a')
        print(separador+"Respuestas del Presupuesto de Ventas"+separador)
        archivoA.write("-"*15+"Respuestas del Presupuesto de Ventas"+"-"*15 +"\n" )
        archivoA.write("\n" )
        archivoA.write("-"*30 +"\n" )

        for nombre in listanombreproduc:
            print(nombre+":")
            texto1=str(nombre)
            archivoA.write(texto1+":" +"\n" )

            print("PRIMER SEMESTRE:")
            archivoA.write("\n" )
            archivoA.write("PRIMER SEMESTRE:" +"\n" )

            print(f"UNIDADES A VENDER: {listaunidadavender[contador3]}")
            texto2=str(listaunidadavender[contador3])
            archivoA.write("UNIDADES A VENDER: "+texto2+"\n" )

            print(f"PRECIO DE VENTA:{listaprecioventa[contador3]}")
            texto3=str(listaprecioventa[contador3])
            archivoA.write("PRECIO DE VENTA: "+texto3+"\n" )

            print(f"IMPORTE DE VENTA: {listaimportedeventa1[contador4]}")
            texto4=str(listaimportedeventa1[contador4])
            archivoA.write("IMPORTE DE VENTA: "+texto4+"\n" )

            contador3=contador3+1
            print("SEGUNDO SEMESTRE:")
            archivoA.write("\n" )
            archivoA.write("SEGUNDO SEMESTRE: "+"\n" )

            print(f"UNIDADES A VENDER: {listaunidadavender[contador3]}")
            texto5=str(listaunidadavender[contador3])
            archivoA.write("UNIDADES A VENDER: "+texto5+"\n" )


            print(f"PRECIO DE VENTA: {listaprecioventa[contador3]}")
            texto6=str(listaprecioventa[contador3])
            archivoA.write("PRECIO DE VENTA: "+texto6+"\n" )

            print(f"IMPORTE DE VENTA: {listaimportedeventa2[contador4]}")
            texto7=str(listaimportedeventa2[contador4])
            archivoA.write("IMPORTE DE VENTA: "+texto7+"\n" )
            archivoA.write("-"*30 +"\n" )

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
        archivoA.write("\n" )
        archivoA.write("Totales Primer Semestre: "+str(totalventasS1)+"\n" )
        archivoA.write("Totales Segundo Semestre: "+str(totalventasS2)+"\n" )
        archivoA.write("Total de Ventas por Semestre: "+str(VENTASTOTALES)+"\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        # FINAL TABLA 1
        #TABLA 2
        saldoCliente=float(input("Dime el saldo de Clientes del Balance General : "))
        totalCliente=(saldoCliente+VENTASTOTALES)

        porcentaje=float(input("Cuanto porcentaje del total de Ventas se va aplicar por cobranza ejemplo(.80) : "))
        cobranza=(VENTASTOTALES*porcentaje)
        totalEntradas=(cobranza+saldoCliente)
        SALDODECLIENTES=(totalCliente-totalEntradas)
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("\n" )
        archivoA.write("-"*15+"Determinacion de saldo de clientes y flujo de entradas"+"-"*15 +"\n" )
        print("")
        print(separador+"Determinacion de saldo de clientes y flujo de entradas"+separador)
        print(f"Saldo de Clientes {año} : {saldoCliente}")
        archivoA.write("Saldo de Clientes "+str(año)+": "+str(saldoCliente)+"\n" )

        print(f"Ventas {año2}: {VENTASTOTALES}")
        archivoA.write("Ventas "+str(año2)+": "+str(VENTASTOTALES)+"\n" )

        print(f"Total de Clientes {año2}: {totalCliente}")
        archivoA.write("Total de Clientes "+str(año2)+": "+str(totalCliente)+"\n" )

        print("")
        archivoA.write("\n" )
        print("Entradas de Efectivo: ")
        archivoA.write("Entradas de Efectivo: "+"\n" )

        print(f"Por cobranza del {año}: {saldoCliente}")
        archivoA.write("Por cobranza del "+str(año)+": "+str(saldoCliente)+"\n" )

        print(f"Por cobranza del {año2}: {cobranza}")
        archivoA.write("Por cobranza del "+str(año2)+": "+str(cobranza)+"\n" )
        archivoA.write("\n" )
        print(f"Total de Entradas del {año2} : {totalEntradas}")
        archivoA.write("Total de Entradas del "+str(año2)+": "+str(totalEntradas)+"\n" )

        print(f"Saldo de Clientes del {año2} : {SALDODECLIENTES}")
        archivoA.write("Saldo de Clientes del "+str(año2)+": "+str(SALDODECLIENTES)+"\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        #FINAL TABLA 2

         #TABLA 3
        #PRESUPUESTO DE PRODUCCION
        print("")
        print(separador+"PRESUPUESTO DE PRODUCCION"+separador)
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("\n" )
        archivoA.write("-"*15+"PRESUPUESTO DE PRODUCCION"+"-"*15 +"\n" )
        for producto in listanombreproduc:
            archivoA.write("\n" )
            archivoA.write("PRIMER SEMESTRE :"+"\n" )
            archivoA.write(producto+":"+"\n")
            inv_final_1=float(input(f"Dime le inventario final de {listanombreproduc[contador5]} del primer semestre: "))
            lista_invfinal1.append(inv_final_1)
            archivoA.write("Inventario final de "+str(listanombreproduc[contador5])+" del primer semestre"+": "+str(inv_final_1)+"\n" )
            
            total_unidades1 = listaunidadavender[contador6] + lista_invfinal1[contador7]
            lista_total_unidades1.append(total_unidades1)
            archivoA.write("Total de unidades : "+str(total_unidades1)+"\n" )

            inv_inicial_1=float(input(f"Dime el inventario inicial de {listanombreproduc[contador5]} del primer semestre: "))
            lista_invinicial1.append(inv_inicial_1)
            archivoA.write("Inventario inicial : "+str(inv_inicial_1)+"\n" )

            lista_unidad_producir.append(total_unidades1-inv_inicial_1)
            archivoA.write("Unidades a Producir: "+str(lista_unidad_producir[contador8])+"\n" )
            contador8=contador8+1


            print("")
            archivoA.write("\n" )
            archivoA.write("SEGUNDO SEMESTRE :"+"\n" )
        
            inv_final_2=float(input(f"Dime le inventario final de {listanombreproduc[contador5]} del segundo semestre: "))
            lista_invfinal2.append(inv_final_2)
            archivoA.write("Inventario final de "+str(listanombreproduc[contador5])+" del segundo semestre"+": "+str(inv_final_2)+"\n" )
            
            contador6=contador6+1
            
            total_unidades2 = listaunidadavender[contador6] + lista_invfinal2[contador7]
            lista_total_unidades2.append(total_unidades2)
            archivoA.write("Total de unidades : "+str(total_unidades2)+"\n" )
            

            inv_inicial_2= float(input(f"Dime el inventario inicial de {listanombreproduc[contador5]} del segundo semestre: "))
            lista_invinicial2.append(inv_inicial_2)
            archivoA.write("Inventario inicial : "+str(inv_inicial_2)+"\n" )
            print(separador)

            lista_unidad_producir.append(total_unidades2-inv_inicial_2)
            archivoA.write("Unidades a Producir: "+str(lista_unidad_producir[contador8])+"\n" )

            
            x=lista_unidad_producir[contador9]
            contador9=contador9+1
            y=lista_unidad_producir[contador9]
            total=(x+y)
            lista_suma_camisas_producir.append(total)
            archivoA.write("\n" )
            archivoA.write("TOTAL "+str(año2)+" primer semestre y segundo: "+str(lista_suma_camisas_producir[contador10])+"\n" )
            archivoA.write("--------------------------------" +"\n" )


            contador5=contador5+1
            contador6=contador6+1
            contador7=contador7+1
            contador8=contador8+1
            contador9=contador9+1
            contador10=contador10+1
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        


except:
    print("Intenta respetar lo que se te pide :)")









