def duplicate_nums(lista_numeros):
    lista_duplicados=[]
    lista_j = lista_numeros.copy()

    for numero_i in lista_numeros:
        lista_j.remove(numero_i)
        for numero_j in lista_j:
            if numero_i == numero_j:
                lista_duplicados.append(numero_i)
    return lista_duplicados

print(duplicate_nums([1,2,1,3,4,5]))
