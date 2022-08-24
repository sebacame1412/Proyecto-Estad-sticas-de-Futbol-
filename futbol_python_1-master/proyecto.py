'''
Documentación del programa

Autor: Sebastian Cameroni

Version: 1.0

Objetivo:

'''
from ast import Continue
import csv


def victorias (pais, condicion):

    try:
        csvfile = open('partidos.csv', errors="ignore")
    except:
        print("Archivo no encontrado")

    data = list(csv.DictReader(csvfile))
    csvfile.close
    
    contador = 0

    if condicion == 1:
        try:
            for i in range(len(data)):
                for k,v in data[i].items():
                    if v == pais and k == 'home_team':
                        for k,v in data[i].items():
                            if k == 'home_score':
                                gol_local = v
                            if k == 'away_score':
                                gol_visitante = v
                                if gol_local > gol_visitante:
                                    contador = contador + 1      
                else:
                    continue
        except:
            print("Datos no encontrados")

        print("El país", pais, "acumula", contador, "víctorias de local")         

    if condicion == 2:
        try:        
            for i in range(len(data)):
                for k,v in data[i].items():
                    if v == pais and k == 'away_team':
                        for k,v in data[i].items():
                            if k == 'home_score':
                                gol_local = v
                            if k == 'away_score':
                                gol_visitante = v
                                if gol_visitante > gol_local:
                                    contador = contador + 1      
                else:
                    continue
        except:
            print("Datos no encontrados")
        
        print("El país", pais, "acumula", contador, "víctorias de visitante")            
    
    if condicion != 1 or condicion != 2:
        print('Ingrese una opción valida')
        
          
        
    
    

def derrotas (pais, condicion):
    
    try:
        csvfile = open('partidos.csv', errors="ignore")
    except:
        print("Archivo no encontrado")

    data = list(csv.DictReader(csvfile))
    csvfile.close
    
    contador = 0

    while condicion == 1:
        try:
            for i in range(len(data)):
                for k,v in data[i].items():
                    if v == pais and k == 'home_team':
                        for k,v in data[i].items():
                            if k == 'home_score':
                                gol_local = v
                            if k == 'away_score':
                                gol_visitante = v
                                if gol_local < gol_visitante:
                                    contador = contador + 1      
                else:
                    continue
        except:
            print("Datos no encontrados")

        print("El país", pais, "acumula", contador, "derrotas de local")                  
    
        break   
                
    
    while condicion == 2:
        try:        
            for i in range(len(data)):
                for k,v in data[i].items():
                    if v == pais and k == 'away_team':
                        for k,v in data[i].items():
                            if k == 'home_score':
                                gol_local = v
                            if k == 'away_score':
                                gol_visitante = v
                                if gol_visitante < gol_local:
                                    contador = contador + 1      
                else:
                    continue
        except:
            print("Datos no encontrados")
    
        print("El país", pais, "acumula", contador, "derrotas de visitante")      
        break 
    
    if condicion != 1 or condicion != 2:
        print('Ingrese una opción valida')
       




def ultimos_partidos (pais):
    try:
        csvfile = open('partidos.csv', errors="ignore")
    except:
        print("Archivo no encontrado")

    data = list(csv.DictReader(csvfile))
    csvfile.close
       
    ultima_fecha = '0'
    archivo = [] 
    

    try:
        for i in range(len(data)):
            for k,v in data[i].items(): 
                if v == pais and k == 'home_team':
                    for k, v in data[i].items():
                        if k == 'date':
                            fecha = v
                            if fecha > ultima_fecha:
                                ultima_fecha = v
                                for k, v in data[i].items():
                                    if k == 'date':
                                        ultima_fecha = v
                                    if k == 'home_team':
                                        local = v
                                    if k == 'away_team':
                                        visitante = v
                                    if k == 'home_score':
                                        gol_local = v
                                    if k == 'away_score':
                                        gol_visitante = v
                                        archivo.append({'Fecha': ultima_fecha, 'Local': local, 'Gol Local': gol_local, 'Gol visitante': gol_visitante, 'Visitante': visitante})
                if v == pais and k == 'away_team':
                    for k, v in data[i].items():
                        for k, v in data[i].items():
                            if k == 'date':
                                fecha = v
                                if fecha > ultima_fecha:
                                    ultima_fecha = v
                                    for k, v in data[i].items():
                                        if k == 'date':
                                            ultima_fecha = v
                                        if k == 'home_team':
                                            local = v
                                        if k == 'away_team':
                                            visitante = v
                                        if k == 'home_score':
                                            gol_local = v
                                        if k == 'away_score':
                                            gol_visitante = v
                                            archivo.append({'Fecha' :ultima_fecha, 'Local': local, 'Gol Local': gol_local, 'Gol visitante': gol_visitante, 'Visitante': visitante})
    except:
        print('Dato no encontrado')
    print('Los últimos 10(diez) partidos de', pais,'son:')    
    print(archivo[-10])
    print(archivo[-9])
    print(archivo[-8])
    print(archivo[-7])
    print(archivo[-6])
    print(archivo[-5])
    print(archivo[-4])
    print(archivo[-3])
    print(archivo[-2])
    print(archivo[-1])
    
        

def ultimo_adversario (pais, condicion):
    
    try:
        csvfile = open('partidos.csv', errors="ignore")
    except:
        print("Archivo no encontrado")

    data = list(csv.DictReader(csvfile))
    csvfile.close
    
    
    while condicion == 1:
        try:        
            for i in range(len(data)):
                for k,v in data[i].items():
                    if v == pais and k == 'home_team':
                        for k,v in data[i].items():
                            if k == 'date':
                                for k,v in data[i].items():
                                    if v == v[-1]:
                                        for k,v in data[i].items():
                                            if k == 'away_team':
                                                adversario = v
                                        
                else:
                    continue
        except:
            print("Datos no encontrados")
        print("El último partido de", pais, "en condición de local fue contra", adversario)
        break
    
    while condicion == 2:
        try:        
            for i in range(len(data)):
                for k,v in data[i].items():
                    if v == pais and k == 'away_team':
                        for k,v in data[i].items():
                            if k == 'date':
                                for k,v in data[i].items():
                                    if v == v[-1]:
                                        for k,v in data[i].items():
                                            if k == 'home_team':
                                                adversario = v
                                        
                else:
                    continue
        except:
            print("Datos no encontrados")
        print("El último partido de", pais, "en condición de visitante fue contra", adversario)
        break




def historial_adversario (pais, adversario): 

    try:
        csvfile = open('partidos.csv', errors="ignore")
    except:
        print("Archivo no encontrado")

    data = list(csv.DictReader(csvfile))
    csvfile.close
    
    victorias = 0
    derrotas = 0
    empates = 0

    
    for i in range(len(data)):
        for k,v in data[i].items():
            if v == pais and k == 'home_team': 
                for k,v in data[i].items():
                    if k == 'home_score':
                        gol_pais = v 
                        for k,v in data[i].items():
                            if v == adversario and k == 'away_team': 
                                for k,v in data[i].items():
                                    if k == 'away_score':
                                        gol_adversario = v
                                        if gol_pais > gol_adversario:
                                            victorias = victorias + 1
                                        if gol_adversario > gol_pais:                        
                                            derrotas = derrotas + 1   
                                        if  gol_pais == gol_adversario:
                                            empates = empates + 1
                                            break                                                                       
            if v == pais and k == 'away_team': 
                for k,v in data[i].items():
                    if k == 'away_score':
                        gol_pais = v
                        for k,v in data[i].items():
                            if v == adversario and k == 'home_team': 
                                for k,v in data[i].items():
                                    if k == 'home_score':
                                        gol_adversario = v
                                        if gol_pais > gol_adversario:
                                            victorias = victorias + 1
                                        if gol_adversario > gol_pais:                        
                                            derrotas = derrotas + 1   
                                        if  gol_pais == gol_adversario:
                                            empates = empates + 1
                                            break                                                                                             
                            
        else:                                               
            continue 
    
                                                                                                                                        
    print("El país", pais, "acumula", victorias, "víctorias", derrotas, "derrotas y", empates, "empates contra el pais", adversario)



def historial_completo(pais):   
    try:
        csvfile = open('partidos.csv', errors="ignore")
    except:
        print("Archivo no encontrado")

    data = list(csv.DictReader(csvfile))
    csvfile.close
    
    print("HISTORIAL COMPLETO...")
    ultima_fecha = '0'
    

    for i in range(len(data)):
        for k,v in data[i].items(): 
            if v == pais and k == 'home_team':
                for k, v in data[i].items():
                    if k == 'date':
                        fecha = v
                        if fecha > ultima_fecha:
                            ultima_fecha = v
                            for k, v in data[i].items():
                                if k == 'date':
                                    ultima_fecha = v
                                if k == 'home_team':
                                    local = v
                                if k == 'away_team':
                                    visitante = v
                                if k == 'home_score':
                                    gol_local = v
                                if k == 'away_score':
                                    gol_visitante = v
                                    print(ultima_fecha, local, gol_local, gol_visitante, visitante)
            if v == pais and k == 'away_team':
                for k, v in data[i].items():
                    for k, v in data[i].items():
                        if k == 'date':
                            fecha = v
                            if fecha > ultima_fecha:
                                ultima_fecha = v
                                for k, v in data[i].items():
                                    if k == 'date':
                                        ultima_fecha = v
                                    if k == 'home_team':
                                        local = v
                                    if k == 'away_team':
                                        visitante = v
                                    if k == 'home_score':
                                        gol_local = v
                                    if k == 'away_score':
                                        gol_visitante = v
                                        print(ultima_fecha, local, gol_local, gol_visitante, visitante)
            else:
                continue  
    
      


if __name__ == '__main__':
    
        print("Bienvenido al programa Estadística de Futbol")
    
        print("En este programa usted podrá elegir las siguientes opciones:")
    
        print(""" 
    1- Determinar cuántas veces ganó un país de local o de visitante.
    2- Determinar cuántas veces perdió un país de local o de visitante.
    3- Determinar cómo le fue al país en los últimos 10(diez) partidos jugados.
    4- Contra quien jugó el último partido de local o de visitante.
    5- Como le fue al país históricamente jugando contra otro país indicado. 
    6- Historial completo de un equipo (todos los partidos jugados) 
        """)
        print('Recuerde ingresar el nombre del país con la primer letra en mayúscula')
        print('El país a ingresar de estar escrito exactamente como figura en el archivo csv')

  
opcion = int(input('Ingrese la opcion deseada:'))

pais = str(input('Ingrese el pais que quiere consultar:'))
#    print('Ingrese un país valido') 
#   print('''Recuerde ingresar el nombre del país con la primer letra en mayuscula 
#        y con el nombre que figura en el archivo CSV''')   

    
        
if opcion == 1:
           
    condicion = int(input(("Ingrese la opción 1(uno) para local o 2(dos) para visitante: ")))
    victorias(pais, condicion)
        

if opcion == 2:       

    condicion = int(input(("Ingrese la opción 1(uno) para local o 2(dos) para visitante: ")))
    derrotas(pais, condicion)

if opcion == 3:
    
        ultimos_partidos(pais)

        
if opcion == 4:
   
    condicion = int(input(("Ingrese la opción 1(uno) para local o 2(dos) para visitante: ")))
    ultimo_adversario(pais,condicion)


if opcion == 5:
    
        adversario = str(input("Ingrese el país adversario:"))
        historial_adversario (pais, adversario)

if opcion == 6:
        historial_completo(pais)
        print("Estos son todos los partidos de", pais)
    
else:
    
    print('Ingrese una opcion valida')
        
            



   
    
     