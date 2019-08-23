linha1= input().split(" ")
linha2= input().split(" ")

cod1, qtd1, val1 = linha1
cod2, qtd2, val2 = linha2

TOTAL= (int(qtd1) * float(val1) + int(qtd2) * float(val2))

print ("VALOR A PAGAR: R$ %0.2f" %TOTAL)