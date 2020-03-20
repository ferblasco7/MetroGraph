#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:08:09 2020

@author: f
"""

#%% Importaciones
import networkx as nx
from datos_metro import bruto
from funciones_propias_redes import crea_red
import netwulf

#%%
G=crea_red(bruto, nx)
netwulf.visualize(G,is_test=True) # Si no le digo que es un test, peta y no vuelve xD
