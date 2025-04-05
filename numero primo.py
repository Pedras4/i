a= int(input("Entre com o numero: "))
b=0
for x in range (1,a+1):
    if a % x == 0:
        b+=1
        print(x, end=" ")

if b>2:
    print()
    print("O numero",a,"foi divisivel",b,"Vezes")
    print(a, "não é um numero primo")
else:
    print()
    print("O numero", a, "foi divisivel", b, "Vezes")
    print(a, "é um numero primo")