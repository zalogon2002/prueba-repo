def chess_board(coordenada):
    columnas= {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    fila= int(coordenada[1])
    columna= columnas[coordenada[0]]

    if fila % 2 == 0 and columna % 2 != 0:
        return "White"
    elif fila % 2 != 0 and columna % 2 == 0:
        return "White"
    else:
        return "black"
print(chess_board("a1"))
