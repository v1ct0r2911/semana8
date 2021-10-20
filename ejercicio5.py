#5.	Elabore un algoritmo que imprima la tabla de multiplicar de un número ingresado por teclado. 
# Este número deberá ser positivo, en caso que ingrese un número negativo deberá emitir un mensaje 
# de error: NUMERO INCORRECTO

cont=1
i=int(input("ingrese numero:"))
if i>0:
    while cont <=12:
        tabla=cont*i
        print(cont,"x",i,"=","=",tabla)
        cont+=1
else:
    print("error")