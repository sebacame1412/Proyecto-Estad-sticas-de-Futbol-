'''
Documentación del programa:

Autor: Sebastian Cameroni

Version: 1.0

'''

import csv

#Función para las victorias de local y de visitante.
def victorias (pais, condicion):

    try:
        csvfile = open('partidos.csv', errors="ignore")
    except:
        print("Archivo no encontrado")

    data = list(csv.DictReader(csvfile))
    csvfile.close
    
    contador = 0
    #Bucle para encontrar victorias de local.
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
        except:
            print("Datos no encontrados")                
        print("El país", pais, "acumula", contador, "victorias de local")
    
    #Bucle para encontrar victorias de visitante.
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
        
        print("El país", pais, "acumula", contador, "victorias de visitante")
                    
    
    if condicion < 1 or condicion > 2: #Condicional por si se ingresa opción erronea.
        print('¡Ingrese una opción valida! Vuelva a ingresar una opción del inicio...')
        
          
    
#Función para las derrotas de local y de visitante.
def derrotas (pais, condicion):
    
    try:
        csvfile = open('partidos.csv', errors="ignore")
    except:
        print("Archivo no encontrado")

    data = list(csv.DictReader(csvfile))
    csvfile.close
    
    contador = 0
    
    #Bucle para encontrar derrotas de local.
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
                                if gol_local < gol_visitante:
                                    contador = contador + 1      
                else:
                    continue
        except:
            print("Datos no encontrados")

        print("El país", pais, "acumula", contador, "derrotas de local")                     
                
    #Bucle para encontrar derrotas de visitante.
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
                                if gol_visitante < gol_local:
                                    contador = contador + 1      
                else:
                    continue
        except:
            print("Datos no encontrados")
    
        print("El país", pais, "acumula", contador, "derrotas de visitante")       
    
    if condicion < 1 or condicion > 2: #Condicional por si se ingresa opción erronea.
        print('¡Ingrese una opción valida! Vuelva a ingresar una opción del inicio...')
       



#Función para el resultado de los últimos 10 partidos.
def ultimos_partidos (pais):
    try:
        csvfile = open('partidos.csv', errors="ignore")
    except:
        print("Archivo no encontrado")

    data = list(csv.DictReader(csvfile))
    csvfile.close
       
    ultima_fecha = '0'
    archivo = [] 
    
    #Bucle para encontrar los ultimos 10 partidos del país seleccionado.
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
    
 #Función para ver el ultimo adversario de local y visitante.       
def ultimo_adversario (pais, condicion):
    
    try:
        csvfile = open('partidos.csv', errors="ignore")
    except:
        print("Archivo no encontrado")

    data = list(csv.DictReader(csvfile))
    csvfile.close
    
    #Bucle para encontrar el último adversario de local.
    if condicion == 1:
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
    
    #Bucle para encontrar el último adversario de visitante.
    if condicion == 2:
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
    
    if condicion < 1 or condicion > 2: #Condicional por si se ingresa opción erronea.
        print('¡Ingrese una opción valida! Vuelva a ingresar una opción del inicio...')    



#Función para ver el historial vs otro equipo.
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

    #Bucle para encontrar todos los partidos del país seleccionado y el adversario.
    for i in range(len(data)):
        try:
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
        except:
            print("Dato no encontrado")     
    
                                                                                                                                        
    print("El país", pais, "acumula", victorias, "victorias", derrotas, "derrotas y", empates, "empates contra el pais", adversario)

#Función para ver todos los partidos de un país.
#(esta opción no esta en el readme original, solo la agregue para tener una opcíon más) 
def historial_completo(pais):   
    try:
        csvfile = open('partidos.csv', errors="ignore")
    except:
        print("Archivo no encontrado")

    data = list(csv.DictReader(csvfile))
    csvfile.close
    
    print("HISTORIAL COMPLETO...")
    
    ultima_fecha = '0'

    #Bucle para mostral todos los partidos de un país
    for i in range(len(data)):
        try:
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
        except:
            print('Dato no encontrado')        
    
      


if __name__ == '__main__':
    
        print("¡Bienvenido al programa Estadística de Futbol!")
    
        print("En este programa usted podrá elegir las siguientes opciones:")
    
        print(""" 
    1- Determinar cuántas veces ganó un país de local o de visitante.
    2- Determinar cuántas veces perdió un país de local o de visitante.
    3- Determinar cómo le fue al país en los últimos 10(diez) partidos.
    4- Contra quien jugó el último partido de local o de visitante.
    5- Como le fue al país históricamente jugando contra otro país indicado. 
    6- Historial completo de un equipo (todos los partidos jugados) 
    7- Para finalizar el programa.
    """)
        print('* Ingresar el nombre del país con la primer letra en mayúscula')
        print('* El país a ingresar debe estar escrito exactamente como figura en el archivo csv.')

while True: 
    opcion = int(input('Ingrese una opción del menú:'))
    
    pais = str(input('Ingrese el pais que quiere consultar:'))

    
    if  opcion > 7 or opcion < 1: 
        print('Ingrese una opción valida')
    
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
    
    if opcion == 7:
        print("Fin del programa") #Finalizar programa.
        break
       
    

            



   
    
     