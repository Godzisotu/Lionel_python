#uso y explicacion de while

cont=1
while cont<=3:
    print("repeticion numero", cont)
    cont+=1


pin=3232

causa=int(input("ingrese su pin"))
while pin!=causa:
    print("pin incorrecto, intentalo otra ve we")
    causa=int(input("ingrese su pin: "))