#12.	Ingrese un número entero y luego visualice un mensaje indicando si es “primo” o “no primo”. 
cont=0
div=0
i=int(input("ingrese numro"))
while div<=i:
    div+=1
    if i % div==0:
        cont+=1
if cont==2:
    print("el numero es primo")
else:
    print(" el numero no es primo")            
