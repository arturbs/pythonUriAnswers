# Programa que calcula o salario de um funcionario a partir da quantidade
# de horas e de um valor para as quanto cada hora vale. 

number = int(input())

hours = int(input())

sph = float(input())

salario = float(hours * sph)

print("NUMBER = %d" %number)

print("SALARY = U$ %0.2f" %salario)