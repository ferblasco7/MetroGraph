#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def crea_red(bruto,nx):
    """ Crea un grafo de networkx a partir del csv de la red de Metro. """

    import csv
    
    nombre_archivo = 'M4_Tramos.csv' #fuente: https://datos.crtm.es/datasets/m4-tramos/data
    csv_metro = csv.reader(open(nombre_archivo))
    
    lista_csv_metro=[]
    for fila in csv_metro:
        lista_csv_metro.append(fila)
    descripcion_columnas = lista_csv_metro.pop(0)
        
    lineas_nombre = list(set([fila[1] for fila in lista_csv_metro]))      
    
    lineas_paradas = {} #{'linea':[paradas]}
    
    for linea in lineas_nombre:
        paradas_linea = [fila[4] for fila in lista_csv_metro if fila[1]==linea]
        lineas_paradas[linea] = paradas_linea
        
    # Conectamos las paradas que están en la misma línea, secuencialmente
    G= nx.Graph()
    for linea in lineas_nombre[:]:
        paradas = lineas_paradas[linea]
        
        while len(paradas)>1:
            G.add_edge(paradas.pop(0),paradas[0],attr=linea)
    
    # Añadimos a mano las conexiones entre partes A y B de las lineas 7, 9 y 10 (elegimos [arbitrariamente] el atributo como la parte A de la linea). También añadimos PLAZA ELIPTICA como parte de la Linea 11
    G.add_edge('LAS MUSAS','ESTADIO OLIMPICO',attr='7a')
    G.add_edge('PUERTA DE ARGANDA','RIVAS URBANIZACIONES',attr='9A')
    G.add_edge('FUENCARRAL','TRES OLIVOS',attr='10a')
    G.add_edge('PLAZA ELIPTICA','ABRANTES',attr='11')

    
    return G