import numpy as np 
lista=[1,2,3,4]
arr= np.array(lista)
#print(arr)
#forma 2 directa
arr2 = np.array([5,6,7,8,9,10,11,12])
#print(arr2)


#funciones como arreglos 
arreglo = np.array([5,6,7,8,9,10,11,12 ])
print(arreglo.ndim)
print(len(arreglo))

print(arreglo[4:7])
print(arreglo[0:7:2])
print(arreglo[::2])

c = [i for i in range (0,5)]
print(c)

x=range(0,1000)
arreglo_automatizado = [n for n in x]
print(arreglo_automatizado.sum)