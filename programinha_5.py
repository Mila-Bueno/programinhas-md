#Programa que permite a inserção de dois conjuntos A|B pelo usuário.
#Depois o programa verifica se B é subconjunto de A.

print("Digite dois conjuntos (A e B), para verificar se B é subconjunto de A")
print("Digite números com um espeço entre eles. Exemplo: 1 2 11 42 30")
A = set(input("Digite números para o conjunto A: ").split())
B = set(input("Digite números para o conjunto B: ").split())


if B.issubset(A):
    print("B é subconjunto de A.")
else:
    print("B não é subconjunto de A.")
