def troca_valores(lista, indice1, indice2):
    lista[indice1], lista[indice2] = lista[indice2], lista[indice1]
    return lista

minha_lista = [1, 2, 3, 4, 5]
print(troca_valores(minha_lista, 1, 3))  # Saída: [1, 4, 3, 2, 5]
