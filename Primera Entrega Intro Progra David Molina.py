#Primer Ejercicio del Portafolio
#Invertir el orden de un numero dado

num1 = int(input("Ingrese un digito para imprimirlo de manera invertida: "))
resultado = 0
agregarCero = ""
while num1 > 0:
    if resultado == 0 and num1 % 10 == 0:
        agregarCero += "0"
    resultado = resultado *10 + num1 % 10
    num1 = num1 // 10
print(agregarCero + str(resultado))

#Segundo Ejercicio del Portafolio
numero = int(input("Ingrese un digito para verificar si cumple los requisitos Armstrong: "))
potencia = 0
numOriginal, producto = numero, numero
while producto > 0:
    producto = producto // 10
    potencia += 1
producto = 0
while numero > 0:
    producto += (numero % 10) ** potencia
    numero = numero // 10
if producto == numOriginal:
    print(numOriginal, " si cumple con las propiedades armstrong")
else:
    print(numOriginal, " no cumple con las propiedades armstrong")