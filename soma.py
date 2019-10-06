num = [10,15,3,7,9,13,12,6, 0]
print('A lista é: ', num)
k = input('Insira um número para k: ')
k = int(k)

def soma(lista,constante):
     #import random
     lista.sort() 
     if  len(lista)<2:
         return False;
     for i in lista:
        if constante>i and constante-i in lista:
             return True
        if constante==1 and constante-i!=0:
             return True
     else:
        print(constante-i)
        return False

            
print(soma(num, k))



