import numpy as np

arreglo=np.array([4,8,15,16,23,42])
contar_hasta=len(arreglo)
for i in range (contar_hasta):

    print(arreglo[i])
#print("Original", arreglo) 



#crear acceso directo a un arreglo
#arreglo_copia=arreglo[:]
#print("Copia:" , arreglo_copia)
#cambio el original
#arreglo[0]=3
#arreglo_copia[2]=100
#print("Original", arreglo)
#print("Copia", arreglo_copia)

arreglo_copia=arreglo[:].copy()
arreglo[0]=1000
print("orignal:", arreglo)
print("Copia: ", arreglo_copia)