import numpy as np

arregloA = np.random.randint(500, size=(100))
obj = [f"{i} es numero par" if i%2==0 else f"{i} es impar" for i  in arregloA]
print(arregloA)
print(obj)
print("El numero mayor es: ", arregloA.max())
print("El numero menor es: ", arregloA.min())
#print("La copia del arreglo: ", arregloA.  )
