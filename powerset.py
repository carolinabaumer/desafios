lista = [1,2,3,4]
def powerset(lista):
    resultado = [[]]
    for i in lista:
        novalista = [sublista + [i] for sublista in resultado]
        resultado.extend(novalista)
    return resultado


print(powerset(lista))