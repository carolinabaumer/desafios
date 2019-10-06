num = [10,15,3,7,9,13,12,6, 0]
print('A lista é: ', num)
k = input('Insira um número para k: ')
k = int(k)

def soma(lista,constante): 
     if  len(lista)<2:
         return False;
     for i in lista:
        if constante>i and constante-i in lista:
             return True
        if constante==i and constante-i!=0:
             return True
     else:
        return False

            
print(soma(num, k))



