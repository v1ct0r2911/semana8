#3.	Elabore un algoritmo que imprima el factorial de un número.

contador=1
factorial=1
i= int(input("ingrese numero: "))
while contador<=i:
    factorial=factorial*contador
    contador+=1
print(factorial)    