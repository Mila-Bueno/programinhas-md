
# Soma dos numeros naturais e validação pela fórmula do Princípio de Indução Matemática.

print("=== SOMA E COMPARAÇÃO DOS NUMEROS NATURAIS ===")


n = int(input("Digite um numero natural: "))

if n < 1:
    print("Digite um numero maior ou igual a 1.")

else:
    # Metodo 1: soma por repeticao (1 + 2 + 3 +...+ n)
    soma = 0

    for numero in range(1, n + 1):
        soma += numero

    # Metodo 2: formula matematica PPIM
    formula = n * (n + 1) // 2

    
    print("\n=== RESULTADOS ===")

    print("Soma por repeticao: (1 + 2 + 3 +...+ n):", soma)
    print("Soma pela formula (n * (n + 1) // 2):", formula)

    if soma == formula:
        print("Os resultados sao iguais!")
    else:
        print("Os resultados sao diferentes!")
