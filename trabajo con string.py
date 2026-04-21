# name= "alonso robles"
# n= "lionel"
# #  -3-2-1
# print(name(0))
# print(len(name))
# print(n.strip())
# print(name.upper())
# #name=name.lower reasisnacion el alor a la variable
# print(name.lower())
# print(name=name.replace("robles","parra"))
# print(name.split())
#Tarea clave

# clave= "Joemasho"

# code=input("ingrese la clave: ")
# if clave==code:
#     print("acceso consedido")
# else:
#     print("acceso denegado")


user=input("ingrese un nombre de usaria: ")
if len(user)>4:
    print("el usuario debe tener al menos 4 caracteres")

elif len (user)>10:
    print("error, usuario con el maximo de caracteres")
else:
    print("usuario creado correctamente")