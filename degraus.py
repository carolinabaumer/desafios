n = input('Quantos degraus deseja subir? ')
n = int(n)
def possibilidades(ndegraus):
    if ndegraus<=1:
        return ndegraus
    else:
        return (ndegraus-1)+(ndegraus-2)

print('Número de possibilidade: ',possibilidades(n))