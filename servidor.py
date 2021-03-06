import pandas as pd
import time
import requests

def general():
    descarga()
    dataSinModificacion(url, ruta)
    dataSinModificacion2(url, ruta)
    lecturaFuente()
    modificacionArchivo1()
    modificacionArchivo2()
    modificacionArchivo3()
    modificacionArchivo4()
    modificacionArchivo5()
    modificacionArchivo6()
    modificacionArchivo7()
    descargaArchivoModificado()

def dataSinModificacion(url, ruta):
    try:
        dfDato = pd.read_csv(url, encoding = "ISO-8859-1", sep=";")
        dfDato.to_excel(ruta, index=False)
    except Exception as e: 
        print (f"Hubo un error en: {url}")
        print ("Código error: "+str(e))

def dataSinModificacion2(url, ruta):
    try:
        dfDato = pd.read_excel(url)
        dfDato.to_excel(ruta, index=False)
    except:
        print (f"Hubo un error en: {url}")
        print ("Código error: "+str(e))

def lecturaFuente():
    fuente = pd.read_excel(r"C:\Users\gusti\grafico_prueba\Descargas_1.xlsx")
    for i in range (len(fuente)):
    dataSinModificacion(fuente["URL"][i],fuente["ruta"][i])

def modificacionArchivo1():
    dfDato7 = pd.read_csv(r"http://www.cplt.cl/transparencia_activa/datoabierto/archivos/TA_Otras_transferencias.csv", encoding = "ISO-8859-1", sep=";")
    dfDato13 = pd.read_csv(r"http://www.cplt.cl/transparencia_activa/datoabierto/archivos/TA_PersonalPlanta.csv", encoding = "ISO-8859-1", sep=";")
    dfDato14 = pd.read_csv(r"http://www.cplt.cl/transparencia_activa/datoabierto/archivos/TA_PersonalContrata.csv", encoding = "ISO-8859-1", sep=";")
    dfDato15 = pd.read_csv(r"http://www.cplt.cl/transparencia_activa/datoabierto/archivos/TA_PersonalCodigotrabajo.csv", encoding = "ISO-8859-1", sep=";")
    dfDato16 = pd.read_csv(r"http://www.cplt.cl/transparencia_activa/datoabierto/archivos/TA_PersonalContratohonorarios.csv", encoding = "ISO-8859-1", sep=";")  
    dfDato17 = pd.read_csv(r"http://www.cplt.cl/transparencia_activa/datoabierto/archivos/TA_Otras_compras.csv", encoding = "ISO-8859-1", sep=";")
    dfDato19 = pd.read_csv(r"http://www.cplt.cl/transparencia_activa/datoabierto/archivos/TA_Nomina_beneficiarios.csv", encoding = "ISO-8859-1", sep=";")
    dfDato48 = pd.read_csv(r"http://www.cplt.cl/transparencia_activa/datoabierto/archivos/solicitudes_por_estado_360.csv", encoding = "ISO-8859-1", sep=";")
    
    return dfDato7, dfDato13, dfDato14, dfDato15, dfDato16, dfDato17, dfDato19, dfDato48

def modificacionArchivo2():
    dfDato7 = modificacionArchivo1()
    dfDato13 = modificacionArchivo1()
    dfDato14 = modificacionArchivo1()
    dfDato15 = modificacionArchivo1()
    dfDato16 = modificacionArchivo1()
    dfDato17 = modificacionArchivo1()
    dfDato19 = modificacionArchivo1()
    dfDato48 = modificacionArchivo1()
    dfDato7["Año"] = dfDato7["fecha"].apply(lambda x: str(x)[0:4])
    dfDato13["Año"] = dfDato13["fecha"].apply(lambda x: str(x)[0:4])
    dfDato14["Año"] = dfDato14["fecha"].apply(lambda x: str(x)[0:4])
    dfDato15["Año"] = dfDato15["fecha"].apply(lambda x: str(x)[0:4])
    dfDato16["Año"] = dfDato16["fecha"].apply(lambda x: str(x)[0:4])
    dfDato17["Año"] = dfDato17["fecha"].apply(lambda x: str(x)[0:4])
    dfDato19["Año"] = dfDato19["fecha"].apply(lambda x: str(x)[0:4])
    dfDato48["Año"] = dfDato48["fecha_ingreso"].apply(lambda x: str(x)[3:7])
    
    return dfDato7, dfDato13, dfDato14, dfDato15, dfDato16, dfDato17, dfDato19, dfDato48    

def modificacionArchivo3():
    dfDato7 = modificacionArchivo2()
    dfDato13 = modificacionArchivo2()
    dfDato14 = modificacionArchivo2()
    dfDato15 = modificacionArchivo2()
    dfDato16 = modificacionArchivo2()
    dfDato17 = modificacionArchivo2()
    dfDato19 = modificacionArchivo2()
    del dfDato7['fecha_publicacion_ta']
    del dfDato7['anyo']
    del dfDato7['fecha']
    del dfDato13['fecha_publicacion_ta']
    del dfDato13['anyo']
    del dfDato13['fecha']
    del dfDato14['fecha_publicacion_ta']
    del dfDato14['anyo']
    del dfDato14['fecha']
    del dfDato15['fecha_publicacion_ta']
    del dfDato15['anyo']
    del dfDato15['fecha']
    del dfDato16['fecha_publicacion_ta']
    del dfDato16['anyo']
    del dfDato16['fecha']
    del dfDato17['fecha_publicacion_ta']
    del dfDato17['anyo']
    del dfDato17['fecha']
    del dfDato19['fecha_publicacion_ta']
    del dfDato19['anyo']
    del dfDato19['fecha']
    
    return dfDato7, dfDato13, dfDato14, dfDato15, dfDato16, dfDato17, dfDato19

def modificacionArchivo4():
    dfDato7 = modificacionArchivo3()
    dfDato13 = modificacionArchivo3()
    dfDato14 = modificacionArchivo3()
    dfDato15 = modificacionArchivo3()
    dfDato16 = modificacionArchivo3()
    dfDato17 = modificacionArchivo3()
    dfDato19 = modificacionArchivo3()
    dfGroup7 = dfDato7.groupby(['organismo_nombre', 'organismo_codigo',  'Mes', 'denominacion', 
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año']).sum()
    dfGroup13 = dfDato13.groupby(['organismo_nombre', 'organismo_codigo',  'Mes', 'denominacion', 
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año']).sum()
    dfGroup14 = dfDato14.groupby(['organismo_nombre', 'organismo_codigo',  'Mes', 'denominacion', 
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año']).sum()
    dfGroup15 = dfDato15.groupby(['organismo_nombre', 'organismo_codigo',  'Mes', 'denominacion', 
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año']).sum()
    dfGroup16 = dfDato16.groupby(['organismo_nombre', 'organismo_codigo',  'Mes', 'denominacion', 
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año']).sum()
    dfGroup17 = dfDato17.groupby(['organismo_nombre', 'organismo_codigo',  'Mes', 'denominacion', 
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año']).sum()
    dfGroup19 = dfDato19.groupby(['organismo_nombre', 'organismo_codigo',  'Mes', 'denominacion', 
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año']).sum()
    
    return dfGroup7, dfGroup13, dfGroup14, dfGroup15, dfGroup16, dfGroup17, dfGroup19

def modificacionArchivo5():
    dfGroup7 = modificacionArchivo4()
    dfGroup13 = modificacionArchivo4()
    dfGroup14 = modificacionArchivo4()
    dfGroup15 = modificacionArchivo4()
    dfGroup16 = modificacionArchivo4()
    dfGroup17 = modificacionArchivo4()
    dfGroup19 = modificacionArchivo4()
    dfGroup7 = dfGroup7.reset_index()
    dfGroup13 = dfGroup13.reset_index()
    dfGroup14 = dfGroup14.reset_index()
    dfGroup15 = dfGroup15.reset_index()
    dfGroup16 = dfGroup16.reset_index()
    dfGroup17 = dfGroup17.reset_index()
    dfGroup19 = dfGroup17.reset_index()
    
    return dfGroup7, dfGroup13, dfGroup14, dfGroup15, dfGroup16, dfGroup17, dfGroup19

def modificacionArchivo6():
    dfGroup7 = modificacionArchivo5()
    dfGroup13 = modificacionArchivo5()
    dfGroup14 = modificacionArchivo5()
    dfGroup15 = modificacionArchivo5()
    dfGroup16 = modificacionArchivo5()
    dfGroup17 = modificacionArchivo5()
    dfGroup19 = modificacionArchivo5()
    dfPivot7 = dfGroup7.pivot( index=[ 'organismo_nombre', 'organismo_codigo', 'denominacion',
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año'], columns=['Mes'], values='monto')
    dfPivot13 = dfGroup13.pivot( index=[ 'organismo_nombre', 'organismo_codigo', 'denominacion',
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año'], columns=['Mes'], values='monto')
    dfPivot14 = dfGroup14.pivot( index=[ 'organismo_nombre', 'organismo_codigo', 'denominacion',
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año'], columns=['Mes'], values='monto')
    dfPivot15 = dfGroup15.pivot( index=[ 'organismo_nombre', 'organismo_codigo', 'denominacion',
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año'], columns=['Mes'], values='monto')
    dfPivot16 = dfGroup16.pivot( index=[ 'organismo_nombre', 'organismo_codigo', 'denominacion',
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año'], columns=['Mes'], values='monto')
    dfPivot17 = dfGroup17.pivot( index=[ 'organismo_nombre', 'organismo_codigo', 'denominacion',
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año'], columns=['Mes'], values='monto')
    dfPivot19 = dfGroup19.pivot( index=[ 'organismo_nombre', 'organismo_codigo', 'denominacion',
           'Tipo Unidad monetaria', 'imputacion_presupuestaria', 'objeto_transferencia', 'razon_social',
           'Nombre persona', 'apellido_paterno', 'apellido_materno', 'activado', 'Año'], columns=['Mes'], values='monto')
    
    return dfPivot7, dfPivot13, dfPivot14, dfPivot15, dfPivot16, dfPivot17, dfPivot19

def modificacionArchivo7():
    dfPivot7 = modificacionArchivo6()
    dfPivot13 = modificacionArchivo6()
    dfPivot14 = modificacionArchivo6()
    dfPivot15 = modificacionArchivo6()
    dfPivot16 = modificacionArchivo6()
    dfPivot17 = modificacionArchivo6()
    dfPivot19 = modificacionArchivo6()
    dfPivot7 = dfPivot7.reset_index()
    dfPivot13 = dfPivot13.reset_index()
    dfPivot14 = dfPivot14.reset_index()
    dfPivot15 = dfPivot15.reset_index()
    dfPivot16 = dfPivot16.reset_index()
    dfPivot17 = dfPivot17.reset_index()
    dfPivot19 = dfPivot19.reset_index()
    
    return dfPivot7, dfPivot13, dfPivot14, dfPivot15, dfPivot16, dfPivot17, dfPivot19

def descargaArchivoModificado():
    dfPivot7 = modificacionArchivo7()
    dfPivot13 = modificacionArchivo7()
    dfPivot14 = modificacionArchivo7()
    dfPivot15 = modificacionArchivo7()
    dfPivot16 = modificacionArchivo7()
    dfPivot17 = modificacionArchivo7()
    dfPivot19 = modificacionArchivo7()
    dfDato48 = modificacionArchivo2()
    for i in dfPivot7['Año'].unique():
        dfAuxiliar = dfPivot7[dfPivot7['Año']== i]
        dfAuxiliar.to_excel(f'TA/TA_Otras_transferencias_{str(i)}.xlsx', index = False)
    for i in dfPivot13['Año'].unique():
        dfAuxiliar = dfPivot13[dfPivot13['Año']== i]
        dfAuxiliar.to_excel(f'TA/TA_PersonalPlanta_{str(i)}.xlsx', index = False)
    for i in dfPivot14['Año'].unique():
        dfAuxiliar = dfPivot14[dfPivot14['Año']== i]
        dfAuxiliar.to_excel(f'TA/TA_PersonalContrata_{str(i)}.xlsx', index = False)
    for i in dfPivot15['Año'].unique():
        dfAuxiliar = dfPivot15[dfPivot15['Año']== i]
        dfAuxiliar.to_excel(f'TA/TA_PersonalCodigotrabajo_{str(i)}.xlsx', index = False)    
    for i in dfPivot16['Año'].unique():
        dfAuxiliar = dfPivot16[dfPivot16['Año']== i]
        dfAuxiliar.to_excel(f'TA/TA_PersonalContratohonorarios_{str(i)}.xlsx', index = False)
    for i in dfPivot17['Año'].unique():
        dfAuxiliar = dfPivot17[dfPivot17['Año']== i]
        dfAuxiliar.to_excel(f'TA/TA_Otras_compras_{str(i)}.xlsx', index = False)  
    for i in dfPivot19['Año'].unique():
        dfAuxiliar = dfPivot19[dfPivot19['Año']== i]
        dfAuxiliar.to_excel(f'TA/TA_Nomina_beneficiarios_{str(i)}.xlsx', index = False)
    for i in dfDato48['Año'].unique():
        dfAuxiliar = dfDato48[dfDato48['Año']== i]
        dfAuxiliar.to_excel(f'TA/solicitudes_por_estado_360_{str(i)}.xlsx', index = False)




if __name__ == '__main__':
    general()