'''
import pandas as pd
import time
import requests

def general():
    lecturaArchivos()
    modificacionArchivo1()
    modificacionArchivo2()
    modificacionArchivo3()
    modificacionArchivo4()
    modificacionArchivo5()
    modificacionArchivo6()
    modificacionArchivo7()
    modificacionArchivo8()
    modificacionArchivo9()
    descargas()

def lecturaArchivos():
    df1996 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_1996.xlsx")
    df1997 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_1997.xlsx")
    df1998 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_1998.xlsx")
    df1999 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_1999.xlsx")
    df2000 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2000.xlsx")
    df2001 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2001.xlsx")
    df2002 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2002.xlsx")
    df2003 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2003.xlsx")
    df2004 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2004.xlsx")
    df2005 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2005.xlsx")
    df2006 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2006.xlsx")
    df2007 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2007.xlsx")
    df2008 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2008.xlsx")
    df2009 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2009.xlsx")
    df2010 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2010.xlsx")
    df2011 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2011.xlsx")
    df2012 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2012.xlsx")
    df2013 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2013.xlsx")
    df2014 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2014.xlsx")
    df2015 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2015.xlsx")
    df2016 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2016.xlsx")
    df2017 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2017.xlsx")
    df2018 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2018.xlsx")
    df2019 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2019.xlsx")
    df2020 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2020.xlsx")
    df2021 = pd.read_excel(r"C:\Carteras históricas de Inversión de los Fondos de Pensiones\cartera_mensual_2021.xlsx")

def modificacionArchivo1():
    df1996["Año"] = "1996"
    df1997["Año"] = "1997"
    df1998["Año"] = "1998"
    df1999["Año"] = "1999"
    df2000["Año"] = "2000"
    df2001["Año"] = "2001"
    df2002["Año"] = "2002"
    df2003["Año"] = "2003"
    df2004["Año"] = "2004"
    df2005["Año"] = "2005"
    df2006["Año"] = "2006"
    df2007["Año"] = "2007"
    df2008["Año"] = "2008"
    df2009["Año"] = "2009"
    df2010["Año"] = "2010"
    df2011["Año"] = "2011"
    df2012["Año"] = "2012"
    df2013["Año"] = "2013"
    df2014["Año"] = "2014"
    df2015["Año"] = "2015"
    df2016["Año"] = "2016"
    df2017["Año"] = "2017"
    df2018["Año"] = "2018"
    df2019["Año"] = "2019"
    df2020["Año"] = "2020"
    df2021["Año"] = "2021"

def modificacionArchivo2():
    dfFinal = pd.concat([df1996,df1997,df1998,df1999,df2000,df2001,df2002,df2003,df2004,df2005,df2006,df2007,df2008,df2009,df2010,df2011,df2012,df2013,df2014,df2015,df2016,df2017,df2018,df2019,df2020,df2021])

def modificacionArchivo3():
    dfFinal["Mes"] = dfFinal["fecha"].apply(lambda x: str(x)[4:6])

def modificacionArchivo4():
    del dfFinal['nemotecnico_del_instrumento']
    del dfFinal['unidades']
    del dfFinal['inversion']
    del dfFinal['moneda_contrato_forward']
    del dfFinal['precio_ejercicio_forward']
    del dfFinal['plazo_economico']
    del dfFinal['tasa_pactada_del_fondo_swap']
    del dfFinal['tasa_pactada_de_la_contraparte_s']
    del dfFinal['fecha']

def modificacionArchivo5():
    dfFinal["grupo_economico"] =dfFinal["grupo_economico"].fillna("")
    dfFinal["nacionalidad_del_emisor"] =dfFinal["nacionalidad_del_emisor"].fillna("")

def modificacionArchivo6():
    dfGroup = dfFinal.groupby(['afp', 'tipo_de_fondo', 'tipo_de_instrumento',
       'nombre_del_emisor', 'nacionalidad_del_emisor',
       'unidad_de_reajuste_de_moneda', 'grupo_economico',
       'moneda_objeto_forward', 'Año', 'Mes']).mean()
    dfGroup = dfGroup.reset_index()

def modificacionArchivo7():
    dfpivot = dfGroup.pivot( index=[ 'afp', 'tipo_de_fondo', 'tipo_de_instrumento',
       'nombre_del_emisor', 'nacionalidad_del_emisor',
       'unidad_de_reajuste_de_moneda', 'grupo_economico',
       'moneda_objeto_forward', 'Año'],columns=['Mes'], values='precio')
    dfpivot = dfpivot.reset_index()

def modificacionArchivo8():
    dfpivot["Enero"] = dfpivot["01"]
    dfpivot["Febrero"] = dfpivot["02"]
    dfpivot["Marzo"] = dfpivot["03"]
    dfpivot["Abril"] = dfpivot["04"]
    dfpivot["Mayo"] = dfpivot["05"]
    dfpivot["Junio"] = dfpivot["06"]
    dfpivot["Julio"] = dfpivot["07"]
    dfpivot["Agosto"] = dfpivot["08"]
    dfpivot["Septiembre"] = dfpivot["09"]
    dfpivot["Octubre"] = dfpivot["10"]
    dfpivot["Noviembre"] = dfpivot["11"]
    dfpivot["Diciembre"] = dfpivot["12"]

def modificacionArchivo9():
    dfpivot.to_excel("Consolidado.xlsx", index=False)

def descargas():
    lecturaArchivos()
    modificacionArchivo1()
    modificacionArchivo2()
    modificacionArchivo3()
    modificacionArchivo4()
    modificacionArchivo5()
    modificacionArchivo6()
    modificacionArchivo7()
    modificacionArchivo8()
    modificacionArchivo9()

'''

if __name__ == '__main__':
    #general()
    import os
    print(os.getcwd())
    print("Aqui estamos comenzando")
    f = open ('Test/HolaMundo.txt','w')
    f.write('hola mundo')
    f.close()
    print("Aqui terminamos")