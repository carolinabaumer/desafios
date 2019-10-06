listainicial = [2,3,4,5]

def multiplicacao(lista):        
    produto = 1                 
    zeros = 0     
    listafinal = []              
    for i in lista:            
        if(i==0):
            zeros += 1
            if(zeros > 1):
                return[0 for i in lista]        
        else:
            produto *= i
    if(zeros < 1):
        return [produto//i for i in lista]
    return [produto if (i == 0) else 0 for i in lista]

print(multiplicacao(listainicial))