import numpy as np
import pandas as pd
from sklearn import preprocessing
infile ="/Users/josepplloo/Documents/scripts/xaa.csv"
dictfile ="/Users/josepplloo/Documents/scripts/dict.csv"
df = pd.read_csv(infile, header = 0)
a=[]
#cargo el archivo de datos
l1 = preprocessing.LabelEncoder()
l2 = preprocessing.LabelEncoder()
l3 = preprocessing.LabelEncoder()
l4 = preprocessing.LabelEncoder()
l5 = preprocessing.LabelEncoder()
l6 = preprocessing.LabelEncoder()


#Guardo los encabezados de la tabla y los transformo
a.append("PersonaID: id de la persona")
a.append(df.PersonaID.unique())
df=df.drop('PersonaID',1)

a.append("TipoEventoRIPSDesc: Evento en la Factura")
a.append(df.TipoEventoRIPSDesc.unique())
df=df.drop('TipoEventoRIPSDesc',1)

a.append("Codigo: id de la eps")
a.append(df.Codigo.unique())
df=df.drop('Codigo',1)

a.append("RegimenAdministradoraDesc: id del regimen: Contributivo-Subsidiado-Vinculado-Particular-Otro-Desplazado")
a.append(df.RegimenAdministradoraDesc.unique())
l2.fit(df.RegimenAdministradoraDesc.unique())
a.append(l2.transform(df.RegimenAdministradoraDesc.unique()))
df.RegimenAdministradoraDesc=l2.transform(df.RegimenAdministradoraDesc)

a.append("DxPrincipal: diagnostico principal")
a.append(df.DxPrincipal.unique())
l3.fit(df.DxPrincipal.unique())
a.append(l3.transform(df.DxPrincipal.unique()))
df.DxPrincipal=l3.transform(df.DxPrincipal)

a.append("DxEgreso: diagnostico de salida")
a.append(df.DxEgreso.unique())
df=df.drop('DxEgreso',1)

a.append("FinalidadProcedimientosCD: si la finalidad es diagnostica-terapeutica")
a.append(df.FinalidadProcedimientosCD.unique())

a.append("FinalidadConsultaCD: la consulta que se realiza")
a.append(df.FinalidadConsultaCD.unique())
df=df.drop('FinalidadConsultaCD',1)


a.append("TipoUsuarioCD: si el usuario es Contributivo-Subsidiado-Vinculado-Particular-Otro-Desplazado")
a.append(df.TipoUsuarioCD.unique())


a.append("CausaExternaCD:si es victima de matrato o violencia")
a.append(df.CausaExternaCD.unique())
df=df.drop('CausaExternaCD',1)

a.append("Prestador: ISP")
a.append(df.Prestador.unique())
df=df.drop('Prestador',1)

a.append("AmbitosProcedimientoCD: si es ambulatorio-hospitalario-urgencias")
a.append(df.AmbitosProcedimientoCD.unique())
l4.fit(df.AmbitosProcedimientoCD.unique())
a.append(l4.transform(df.AmbitosProcedimientoCD.unique()))
df.AmbitosProcedimientoCD=l4.transform(df.AmbitosProcedimientoCD)

a.append("CodigoProcedimiento: procedimiento medico")
a.append(df.CodigoProcedimiento.unique())
l5.fit(df.CodigoProcedimiento.unique())
a.append(l5.transform(df.CodigoProcedimiento.unique()))
df.CodigoProcedimiento=l5.transform(df.CodigoProcedimiento)

a.append("MunicipioCD: id municipo")
a.append(df.MunicipioCD.unique())
df=df.drop('MunicipioCD',1)


a.append("EstadoSalidaDesc: si sale vivo o muerto")
a.append(df.EstadoSalidaDesc.unique())
df=df.drop('EstadoSalidaDesc',1)

a.append("CostoConsulta: el costo de la consulta")
a.append(df.CostoConsulta.unique())
df=df.drop('CostoConsulta',1)

a.append("CostoProcedimiento: costo del procedimiento")
a.append(df.CostoProcedimiento.unique())
df=df.drop('CostoProcedimiento',1)

a.append("NetoAPagarConsulta: total a pagar")
a.append(df.NetoAPagarConsulta.unique())
df=df.drop('NetoAPagarConsulta',1)

a.append("NumeroDiasEstancia: numero de dias en el servicio")
a.append(df.NumeroDiasEstancia.unique())
df=df.drop('NumeroDiasEstancia',1)

a.append("fechaid: fecha")
a.append(df.fechaid.unique())
df=df.drop('fechaid',1)

a.append("Edad: edad")
a.append(df.Edad.unique())

a.append("SexoDesc: genero del usuario")
a.append(df.SexoDesc.unique())
l6.fit(df.SexoDesc.unique())
a.append(l6.transform(df.SexoDesc.unique()))
df.SexoDesc=l6.transform(df.SexoDesc)

#ahora a volcar el df en un csv y en un diccionario
np.savetxt(dictfile, a, delimiter=",",fmt='%s')

df.to_csv("/Users/josepplloo/Documents/scripts/xaa_clean.csv",index=False)

"""
PersonaID: id de la persona
TipoEventoRIPSDesc: Evento en la Factura
Codigo: id de la eps
RegimenAdministradoraDesc: id del regimen: Contributivo-Subsidiado-Vinculado-Particular-Otro-Desplazado
DxPrincipal: diagnostico principal
DxEgreso: diagnostico de salida
FinalidadProcedimientosCD: si la finalidad es diagnostica-terapeutica
FinalidadConsultaCD: la consulta que se realiza
TipoUsuarioCD: si el usuario es Contributivo-Subsidiado-Vinculado-Particular-Otro-Desplazado
CausaExternaCD:si es victima de matrato o violencia
Prestador: ISP
AmbitosProcedimientoCD: si es ambulatorio-hospitalario-urgencias
CodigoProcedimiento: procedimiento medico
MunicipioCD: id municipo
EstadoSalidaDesc: si sale vivo o muerto
CostoConsulta: el costo de la consulta
CostoProcedimiento: costo del procedimiento
NetoAPagarConsulta: total a pagar
NumeroDiasEstancia: numero de dias en el servicio
fechaid: fecha
Edad: edad
SexoDesc: genero del usuario
"""
