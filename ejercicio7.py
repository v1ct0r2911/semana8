#7.	Elabore un algoritmo que calcule y visualice los divisores de un número entero.

div=1
num=int(input("ingrese numero"))
while div<=num:
    rest=num%div
    if rest==0:
       print(div)
    div+=1