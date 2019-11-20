import os
import random
os.system("cls")


tamaño = int(input("Ingrese el tamaño de la matriz de 2 a 5: "))
while True:
    if(tamaño>=2 and tamaño<=5):
        break
    else:
        tamaño = int(input("INgrese tamaño valido (2 a 5): "))  

matriz = []
for i in range(0,tamaño):
    matriz.append([])

for i in range(0,tamaño):
    matriz[0].append(random.randint(1,100))

for i in range(0,tamaño):
    matriz[1].append(random.randint(1,100))

for i in range(0,tamaño):
    matriz[2].append(random.randint(1,100))

for i in range(0,tamaño):
    matriz[3].append(random.randint(1,100))

for i in range(0,tamaño):
    matriz[4].append(random.randint(1,100))
        
print(f"matriz{matriz[0]}\n{matriz[1]}\n{matriz[2]}\n{matriz[3]}\n{matriz[4]}\n")