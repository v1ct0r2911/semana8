suma=0
num=0
num=int(input("ingrese numero"))
for i in range(1,num):
    if num%i==0:
        print(i)
if suma==num:
    print(" no perfecto")
else:
    print("perfecto")            