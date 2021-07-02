import random
import os

while(1):
 os.system("cls")
 str(input("Presione enter para generar 1 RUT aleatorio"))
 
 a= random.randint(1,2)
 b= random.randint(0,5)
 c= random.randint(1,9)
 d= random.randint(1,9)
 e= random.randint(1,9)
 f= random.randint(1,9)
 g= random.randint(1,9)
 h= random.randint(1,9)
 print("====================")
 print("RUT: "+str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h))
 print("====================")
 print("\n")
 input("presione enter para reiniciar el programa...")