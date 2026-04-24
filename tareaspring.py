# definir 2 candidatos. preguntar la cantidad de votantes
# preguntar a cada votante por quien votara mostrando
# las alternativas. contar los votos mostrar resultados 
#definir el ganador y considerar un empate



toon1=input("ingrese el toon 1 ")
toon2=input("ingrese el toon 2 ")
v1=0
v2=0
num=int(input("ingrese la acnt de votantes: "))

for i in range(num):
    voto=int(input(f"porquien votara. 1.-{toon1} 2.- {toon2}"))
    if voto==1:
        v1+=1
    elif voto==2:
        v2+=1
    else:
        print("voto no valido")
if v1>v2:
        print(f"El ganador es {toon1} con {v1} votos")
        print(f"El ganador es {toon2} con {v2} votos")