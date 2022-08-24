
victorias_totales = 0
    derrotas_totales = 0
    empates = 0

    try:
        for i in range(len(data)):
                for k,v in data[i].items():
                    if v == pais and k == 'home_team': #Victoria/empates/derrota local
                        for k,v in data[i].items():
                            if k == 'date' and data[-1:-10] == v:
                                for k,v in data[i].items():
                                    if k == 'home_score':
                                        gol_local = v
                                        if k == 'away_score':
                                            gol_visitante = v
                                            if gol_local > gol_visitante:
                                                victorias_totales = victorias_totales + 1
                                            if gol_visitante > gol_local:
                                                derrotas_totales = derrotas_totales + 1 
                                            if gol_local == gol_visitante:
                                                empates = empates + 1   
                    if v == pais and k == 'away_team': #victoria/empates/derrota visitante
                        for k,v in data[i].items():
                            if k == 'date' and data[-1:-10] == v:
                                for k,v in data[i].items():
                                    if k == 'home_score':
                                     gol_local = v
                                    if k == 'away_score':
                                        gol_visitante = v
                                        if gol_visitante > gol_local:
                                            victorias_totales = victorias_totales + 1
                                        if gol_visitante > gol_local:
                                            derrotas_totales = derrotas_totales + 1
                                        if gol_local == gol_visitante:
                                            empates = empates + 1                                         
                else:
                    continue
    except:
        print("Datos no encontrados")
    print(victorias_totales, derrotas_totales, empates)    











    ultima_fecha = '0'
    archivo = []

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
                                    archivo.append(ultima_fecha, local, gol_local, gol_visitante, visitante)
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
                                        archivo.append(ultima_fecha, local, gol_local, gol_visitante, visitante)
            else:
                continue  
    print(archivo[-1:-10])