tempoEmSegundos = int (input())

segundos = 0
minutos = 0
horas = 0

segundos = tempoEmSegundos % 60
temporario = tempoEmSegundos / 60
minutos = temporario % 60
horas = temporario / 60 

print ("%d:%d:%d"  %(horas, minutos, segundos))