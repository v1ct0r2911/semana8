#6.	Elabore un algoritmo que calcule y visualice la suma de los todos los números impares de 3 cifras

num=99
suma=0
while num<=999:
    num+=1
    if num%2:
        print(num)
        suma+=num
print("la suma es:", suma)        