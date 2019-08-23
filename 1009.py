NAME= str(input())
FIXSAL= float(input())
SALES= float(input())

ENDSAL= ((SALES/100) * 15)

print("TOTAL = R$ %0.2f"%(ENDSAL + FIXSAL))