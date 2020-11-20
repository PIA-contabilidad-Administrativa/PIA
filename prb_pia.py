lista_importeMOD_1=[]
lista_total_horas_1=[]
lista_importeMOD_2=[]
lista_total_horas_2=[]

camisas=["CL","CE","CR"]
contador=0
contador2=0
materiales= 3
for valor in range(materiales):
    u_producir= int(input(f"Cuantas unidades se producieron primer semestre de {camisas[contador]} : "))
        
    h_requeridas= float(input("Cuantas horas se ocuparon: "))
    
    cuota_hora= float(input("Cuota por hora: "))
    
    total_horas= (u_producir*h_requeridas)
        
    lista_total_horas_1.append(total_horas)
    
    importe_MOD= (total_horas*cuota_hora)
    
    lista_importeMOD_1.append(importe_MOD)
    
    T_horas_semestre_1= sum(lista_total_horas_1)
    
    Total_MOD1= sum(lista_importeMOD_1)
    
    
    contador= contador +1

print(T_horas_semestre_1)
print(Total_MOD1)

for valor in range(materiales):
    u_producir2= int(input(f"Cuantas unidades se producieron segundo semestre de {camisas[contador2]} : "))
    
    h_requeridas2= float(input("Cuantas horas se ocuparon: "))
    
    cuota_hora2= float(input("Cuota por hora: "))
    
    total_horas2= (u_producir2*h_requeridas2)
        
    lista_total_horas_2.append(total_horas2)
    
    importe_MOD2= (total_horas2*cuota_hora2)
    
    lista_importeMOD_2.append(importe_MOD2)
    
    T_horas_semestre_2= sum(lista_total_horas_2)
    
    Total_MOD2= sum(lista_importeMOD_2)
    
    
    contador2= contador2 +1

print(T_horas_semestre_2)
print(Total_MOD2)

print(f"El total de horas requeridas  por semestre es de {T_horas_semestre_1 + T_horas_semestre_2}")

print(f"El total de M.O.D  por semestre es de {Total_MOD1 + Total_MOD2}")
