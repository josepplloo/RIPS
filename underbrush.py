import numpy as np
import pandas as pd
infile ="/Users/josepplloo/Documents/scripts/xaa_clean.csv"
df = pd.read_csv(infile, header = 0)
df = df[df['DxPrincipal']==1333]


#df.to_csv("/Users/josepplloo/Documents/RIP2013/scripts/xaa_clean1333.csv",index=False)




#debo de filtar la data para solo un procedimiento y mirar el arbol para ese procedimiento solo
