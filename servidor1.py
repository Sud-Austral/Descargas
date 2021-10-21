import pandas as pd
import time
import requests

def general():
    lecturaArchivos()
    

def lecturaArchivos():
    dfConsolidado = pd.read_excel(r"Consolidado.xlsx"), usecols = ""

    return dfConsolidado




if __name__ == '__main__':
    general()
    #import os
    #print(os.getcwd())
    #print("Aqui estamos comenzando")
    #f = open ('Test/HolaMundo.txt','w')
    #f.write('hola mundo')
    #f.close()
    #print("Aqui terminamos")