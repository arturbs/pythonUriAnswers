numeros = input()
numeros.split()

a = int(numeros[0])
b = int(numeros[2])
c = int(numeros[4])


if a < b :
    if b < c : 
        maior = c
    
    else: 
        maior = b
    

else:
    if  a < c: 
        maior = c
    
    else: 
        maior = a
    
print ("%d eh o maior" %maior)