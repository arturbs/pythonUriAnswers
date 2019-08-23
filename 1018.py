valororiginal = int (input())
nota100= int(valororiginal / 100)
valor1= valororiginal%100
nota50=int(valor1/50)
valor2= valor1%50
nota20=int(valor2/20)
valor3= valor2%20
nota10=int(valor3/10)
valor4= valor3%10
nota5=int(valor4/5)
valor5= valor4%5
nota2=int(valor5/2)
valor6= valor5%2
nota1=int(valor6/1)

#prints das notas
print (valororiginal)
print ("%d nota(s) de R$ 100,00" %nota100)
print ("%d nota(s) de R$ 50,00" %nota50)
print ("%d nota(s) de R$ 20,00" %nota20)
print ("%d nota(s) de R$ 10,00" %nota10)
print ("%d nota(s) de R$ 5,00" %nota5)
print ("%d nota(s) de R$ 2,00" %nota2)
print ("%d nota(s) de R$ 1,00" %nota1)