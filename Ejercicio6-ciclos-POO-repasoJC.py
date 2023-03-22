def binary_to_decimal(lista_bits):
    longitud= len(lista_bits)
    longitud-=1
    valor_decimal=0

    for bit in lista_bits:
        valor_decimal += bit * 2 ** longitud
        longitud -= 1
    return valor_decimal

print(binary_to_decimal([1,1,1,1,1,1,1,1]))
