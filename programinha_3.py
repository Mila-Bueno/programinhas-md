# Programa para operações com conjuntos
print("Digite números para elementos, dando espaço entre eles.")
print("Exemplo: 1 2 3 10 11 ")
A = set(input("Digite os elementos do conjunto A: ").split())
B = set(input("Digite os elementos do conjunto B: ").split())

print("Conjunto A:", sorted(A))
print("Conjunto B:", sorted(B))

print("União:", sorted(A | B))
print("Interseção:", sorted(A & B))
print("A - B:", sorted(A - B))
print("B - A:", sorted(B - A))
