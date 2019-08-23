LINHA1= input().split(" ")

A, B, C = LINHA1
PI = 3.14159

TRIANGULO= (float(A) * float(C)) / 2
CIRCULO= PI * (float(C)) ** 2
TRAPEZIO= ((float(A) + float(B)) * float(C)) / 2
QUADRADO= float(B) ** 2
RETANGULO= float(A) * float(B)

print ("TRIANGULO: %0.3f"%TRIANGULO)
print ("CIRCULO: %0.3f"%CIRCULO)
print ("TRAPEZIO: %0.3f"%TRAPEZIO)
print ("QUADRADO: %0.3f"%QUADRADO)
print ("RETANGULO: %0.3f"%RETANGULO)