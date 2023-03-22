def box_seq(numero):
    resultado=0
    for valor in range(numero+1):
        if valor % 2 == 0 and valor!=0:
            resultado -=1
        elif valor!=0:
            resultado+=3
    return resultado

print(box_seq(0))
