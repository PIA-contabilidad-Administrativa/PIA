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
lista_nombre_material=[]
lista_total_materiales=[]
lista_req=[]
lista_total_total_materiales=[]
listamat1=[]
listamat2=[]
compras_totales=[]
listareu=[]
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
contador11=0
contador12=0
contador13=0
contador14=0
contador15=0
contador16=0
contador17=0
contador18=0
contador19=0
contador20=0
contador21=0
contador22=1
contador23=0
contador24=0
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
        archivoA.write("-"*15+"Respuestas del Presupuesto de Ventas"+"-"*15 +"\n" )
        archivoA.write("\n" )
        archivoA.write("-"*30 +"\n" )

        for nombre in listanombreproduc:
            texto1=str(nombre)
            archivoA.write(texto1+":" +"\n" )

            archivoA.write("\n" )
            archivoA.write("PRIMER SEMESTRE:" +"\n" )

            texto2=str(listaunidadavender[contador3])
            archivoA.write("UNIDADES A VENDER: "+texto2+"\n" )

            texto3=str(listaprecioventa[contador3])
            archivoA.write("PRECIO DE VENTA: "+texto3+"\n" )

            texto4=str(listaimportedeventa1[contador4])
            archivoA.write("IMPORTE DE VENTA: "+texto4+"\n" )

            contador3=contador3+1
            archivoA.write("\n" )
            archivoA.write("SEGUNDO SEMESTRE: "+"\n" )

            texto5=str(listaunidadavender[contador3])
            archivoA.write("UNIDADES A VENDER: "+texto5+"\n" )


            texto6=str(listaprecioventa[contador3])
            archivoA.write("PRECIO DE VENTA: "+texto6+"\n" )

            texto7=str(listaimportedeventa2[contador4])
            archivoA.write("IMPORTE DE VENTA: "+texto7+"\n" )
            archivoA.write("-"*30 +"\n" )

            
            contador3=contador3+1
            contador4=contador4+1
        totalventasS1=(sum(listaimportedeventa1))
        totalventasS2=(sum(listaimportedeventa2))
        VENTASTOTALES=(totalventasS1+totalventasS2)
        archivoA.write("\n" )
        archivoA.write("Totales Primer Semestre: "+str(totalventasS1)+"\n" )
        archivoA.write("Totales Segundo Semestre: "+str(totalventasS2)+"\n" )
        archivoA.write("Total de Ventas por Semestre: "+str(VENTASTOTALES)+"\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        # FINAL TABLA 1
        #TABLA 2
        print(separador)
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
        archivoA.write("Saldo de Clientes "+str(año)+": "+str(saldoCliente)+"\n" )

        archivoA.write("Ventas "+str(año2)+": "+str(VENTASTOTALES)+"\n" )

        archivoA.write("Total de Clientes "+str(año2)+": "+str(totalCliente)+"\n" )

        
        archivoA.write("\n" )
        archivoA.write("Entradas de Efectivo: "+"\n" )

        archivoA.write("Por cobranza del "+str(año)+": "+str(saldoCliente)+"\n" )

        archivoA.write("Por cobranza del "+str(año2)+": "+str(cobranza)+"\n" )
        archivoA.write("\n" )
        archivoA.write("Total de Entradas del "+str(año2)+": "+str(totalEntradas)+"\n" )

        
        archivoA.write("Saldo de Clientes del "+str(año2)+": "+str(SALDODECLIENTES)+"\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        #FINAL TABLA 2

         #TABLA 3
        #PRESUPUESTO DE PRODUCCION
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

        #TABLA 4
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("\n" )
        archivoA.write("-"*15+"PRESUPUESTO DE REQUERIMIENTO DE MATERIALES" +"-"*15 +"\n" )

        x=lista_unidad_producir[contador12]
        contador12=contador12+1
        y=lista_unidad_producir[contador12]
        suma=(x+y)

        cuantos=int(input("Cuantos materiales tienes :"))
        for material in range(cuantos):
            material=input("Dime el nombre del material : ")
            lista_nombre_material.append(material)
        print(separador)

        

        for producto in listanombreproduc:
            archivoA.write("\n" )
            archivoA.write(producto+":"+"\n" )
            archivoA.write("PRIMER SEMESTRE:"+"\n" )
            archivoA.write("\n" )
            archivoA.write("Unidades a producir:"+str(lista_unidad_producir[contador21])+"\n" )
            archivoA.write("\n" )
            contador13=0
            contador16=0
            for material in lista_nombre_material:
                
                archivoA.write("MATERIAL "+str(lista_nombre_material[contador13])+":"+"\n" )
                

                for req in range(1):
                    print(producto)
                    print("")
                    requerimientoM=float(input(f"Dime el requerimiento de Material {material}: "))
                    lista_req.append(requerimientoM)
                print(separador)
                
                x=(lista_unidad_producir[contador21]*lista_req[contador15])
                lista_total_materiales.append(x)
                archivoA.write("Requerimiento de material:"+str(lista_req[contador14])+"\n" )
                archivoA.write("TOTAL DE MATERIAL "+str(lista_nombre_material[contador16])+":"+str(lista_total_materiales[contador17])+"\n" )
                archivoA.write("\n" )
                listamat1.append(x)
               
                contador13=contador13+1
                contador14=contador14+1
                contador15=contador15+1
                contador16=contador16+1
                contador17=contador17+1
            contador21=contador21+2
                
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()

        contador25=1
        contador14=0
        contador15=0
        contador17=0
        lista_total_materiales=[]
        archivoA=open("./respuestas.txt" , 'a')
        for producto in listanombreproduc:
            archivoA.write("\n" )
            archivoA.write(producto+":"+"\n" )
            archivoA.write("SEGUNDO SEMESTRE:"+"\n" )
            archivoA.write("\n" )
            archivoA.write("Unidades a producir:"+str(lista_unidad_producir[contador25])+"\n" )
            archivoA.write("\n" )
            contador13=0
            contador16=0
            for material in lista_nombre_material:
                
                archivoA.write("MATERIAL "+str(lista_nombre_material[contador13])+":"+"\n" )
                
                
                x=(lista_unidad_producir[contador25]*lista_req[contador15])
                lista_total_materiales.append(x)
                archivoA.write("Requerimiento de material:"+str(lista_req[contador14])+"\n" )
                archivoA.write("TOTAL DE MATERIAL "+str(lista_nombre_material[contador16])+":"+str(lista_total_materiales[contador17])+"\n" )
                archivoA.write("\n" )
                listamat2.append(x)
               
                contador13=contador13+1
                contador14=contador14+1
                contador15=contador15+1
                contador16=contador16+1
                contador17=contador17+1
            contador25=contador25+2
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )

        archivoA.write("TOTAL DE REQUERIMIENTOS:" +"\n" )
        archivoA.write("\n" )
        listaMateriales=[]
        materialA1=sum(listamat1[0::3])
        listaMateriales.append(materialA1)

        materialB1=sum(listamat1[1::3])
        listaMateriales.append(materialB1)

        materialC1=sum(listamat1[2::3])
        listaMateriales.append(materialC1)

        materialA2=sum(listamat2[0::3])
        listaMateriales.append(materialA2)

        materialB2=sum(listamat2[1::3])
        listaMateriales.append(materialB2)

        materialC2=sum(listamat2[2::3])
        listaMateriales.append(materialC2)

        archivoA.write("PRIMER SEMESTRE :" +"\n" )
        
        archivoA.write("MATERIAL A  :" +str(materialA1)+"\n" )
        archivoA.write("MATERIAL B  :" +str(materialB1)+"\n" )
        archivoA.write("MATERIAL C  :" +str(materialC1)+"\n" )
        archivoA.write("\n" )

        archivoA.write("SEGUNDO SEMESTRE :" +"\n" )
        archivoA.write("MATERIAL A  :" +str(materialA2)+"\n" )
        archivoA.write("MATERIAL B  :" +str(materialB2)+"\n" )
        archivoA.write("MATERIAL C  :" +str(materialC2)+"\n" )
        archivoA.write("\n" )

        archivoA.write("FINALES :" +"\n" )
        materialAT=(materialA1+materialA2)
        materialBT=(materialB1+materialB2)
        materialCT=(materialC1+materialC2)

        archivoA.write("MATERIAL TOTAL A :" +str(materialAT)+"\n" )
        archivoA.write("MATERIAL TOTAL B  :" +str(materialBT)+"\n" )
        archivoA.write("MATERIAL TOTAL C  :" +str(materialCT)+"\n" )

        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n" )
        archivoA.close()
    # FIN TABLA 4

        #TABLA 5 
        #semestre 1
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("-"*15+"PRESUPUESTO DE COMPRAS DE MATERIALES" +"-"*15 +"\n" )
        archivoA.write("\n" )
        archivoA.write("PRIMER SEMESTRE:"+"\n")
        print("PRIMER SEMESTRE : ")
        print("")
        for material in lista_nombre_material:

            archivoA.write("MATERIAL "+material+" :"+"\n" )
            archivoA.write("Requerimiento de Materiales: "+str(listaMateriales[contador23])+"\n")
            inventarioFinal=int(input(f"Dime el inventario Final {material} :  "))
            print(separador)
            listareu.append(inventarioFinal)

            archivoA.write("Inventario Final: "+str(inventarioFinal)+"\n")
            total_materiales=(listaMateriales[contador23]+inventarioFinal)
            archivoA.write("Total de Materiales: "+str(total_materiales)+"\n")

            inventarioInicial=int(input(f"Dime el inventario Inicial {material} :"))
            print(separador)
            archivoA.write("Inventario Inicial: "+str(inventarioInicial)+"\n")

            material_comprar=(total_materiales-inventarioInicial)
            archivoA.write("Material a Comprar : "+str(material_comprar)+"\n")

            precio_compra=int(input(f"Dime el precio de compra {material} : "))
            print(separador)
            archivoA.write("Precio de Compra : "+str(precio_compra)+"\n")

            total_material=(material_comprar * precio_compra)
            compras_totales.append(total_material)
            archivoA.write("TOTAL DE MATERIAL"+material+"en $ : "+str(total_material)+"\n")
            archivoA.write("\n" )
            contador23=contador23+1
        
        archivoA.write("COMPRAS TOTALES : "+str(sum(compras_totales))+"\n")
        archivoA.write("\n" )
        

        # semestre 2
        archivoA.write("SEGUNDO SEMESTRE:"+"\n")
        archivoA.write("\n" )
        print("SEGUNDO SEMESTRE : ")
        print("")
        for material in lista_nombre_material:
            
            archivoA.write("MATERIAL "+material+" :"+"\n" )
            archivoA.write("Requerimiento de Materiales: "+str(listaMateriales[contador23])+"\n")
            print(separador)
            inventarioFinal=int(input(f"Dime el inventario Final {material} :  "))

            archivoA.write("Inventario Final: "+str(inventarioFinal)+"\n")
            total_materiales=(listaMateriales[contador23]+inventarioFinal)
            archivoA.write("Total de Materiales: "+str(total_materiales)+"\n")

            inventarioInicial=(listareu[contador24])
            contador24=contador24+1
            archivoA.write("Inventario Inicial: "+str(inventarioInicial)+"\n")

            material_comprar=(total_materiales-inventarioInicial)
            archivoA.write("Material a Comprar : "+str(material_comprar)+"\n")

            precio_compra=int(input(f"Dime el precio de compra {material} : "))
            print(separador)
            archivoA.write("Precio de Compra : "+str(precio_compra)+"\n")

            total_material=(material_comprar*precio_compra)
            compras_totales.append(total_material)
            archivoA.write("TOTAL DE MATERIA "+material+" en $ : "+str(total_material)+"\n")
            archivoA.write("\n" )
            contador23=contador23+1
        
        archivoA.write("COMPRAS TOTALES : "+str(sum(compras_totales[3::1]))+"\n")
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n" )
        archivoA.close()

    

        
      


except:
    print("Intenta respetar lo que se te pide :)")










