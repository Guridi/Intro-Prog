#Libreria que permite manipular el OS en donde python esta corriendo
import os 

#Input de primera y segunda variable 'a' y 'b'
a = float(input("Inserte primer numero: ")) 
b = float(input("Inserte segundo numero: "))
 
#Proceso de la operacion √({a}² + {b}²)
ar = a ** 2
br = b ** 2
sum = ar + br
squareR = (sum) ** (1/2)

#Usando la libreria antes mencionada, luego de declarar las variables 'a' y 'b', la pantalla se limpia
os.system('cls')

#Print del resultado paso por paso
print(f"Paso #1 → √({a}² + {b}²)")
print(f"Paso #2 → √({ar} + {br})")
print(f"Paso #3 → √({sum})")
print(f"Paso #4 → {squareR} ✅")