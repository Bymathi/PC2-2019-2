import os
os.system ("cls")

personas = 0
mascu = 0
femen = 0
lista =[[],[],[]]

while True:
    if personas<5:
        nombre =  input("Ingrese su nombre: ")
        while True:
            sexo = input("Ingrese su sexo(m/f): ")
            if (sexo=="m"):
                mascu+=1
                break
            elif (sexo=="f"):
                femen+=1
                break
            else:
                print("Ingrese una opcion valida")

        edad = int(input("Ingrese su edad: "))
        if edad>=5 and edad<=17:
            lista[0].append(nombre)
            lista[1].append(sexo)
            lista[2].append(edad)
            personas +=1
            print("persona registrada")
        else:
            print("Persona no apta")
    elif personas==4:
        break

promedio = (lista[2][0]+lista[2][1]+lista[2][2]+lista[2][3]+lista[2][4])/5

print("***********Resumen*********")

for i in range(0,4):
    print(f"nombre: {lista[0][i]}, sexo: {lista[1][i+1]}, edad:{lista[2][i+2]} ")

print(f"Hombres: {mascu} y Mujeres{femen}")
print(f"El promedio de edades es: {promedio}")

