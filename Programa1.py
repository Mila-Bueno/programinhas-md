#Programa para calcular o  valor lógico de:
#p or (q and r)

p = input("Digite o valor de 'p'(true/false):").strip().lower()=="true"
q = input("Digite o valor de 'q'(true/false):").strip().lower()=="true"
r = input("Digite o valor de 'r'(true/false):").strip().lower()=="true"

if p or (q and r):
   print("verdadeiro")
else:
   print("false")