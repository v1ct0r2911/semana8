#11.	Ingrese un número entero y luego calcule el factorial del número ingresado
cont=1
fact=1
i=int(input("ingrese numro"))
while cont<=i:
    fact=fact*cont
    cont+=1
print(fact)    