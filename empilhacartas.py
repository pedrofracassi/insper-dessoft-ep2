def empilha(lista,ppartida,pchegada):
    lista[pchegada] = lista[ppartida]
    del lista[ppartida]
    return lista