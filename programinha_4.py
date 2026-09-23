#Programa que calcula cardinalidade de um conjunto
print("Ao digitar números, coloque um espaço entre eles")
print("Exemplo: 10 22 1 2")
A = set(input("Digite números para elementos de um conjunto:").split())

print("Conjunto:", sorted(A))
print("Cardinalidade:", len(A))
