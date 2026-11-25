
# Sequencia de Fibonacci
#Um programa que exibe quantos termos o usuário quiser da sequência de Fibonacci

print("=== SEQUENCIA DE FIBONACCI ===")


n = int(input("Quantos termos deseja visualizar? "))

if n < 1:
    print("Digite uma quantidade maior ou igual a 1.")

else:
    
    a = 0
    b = 1

    sequencia = []

    
    contador = 0

    while contador < n:
        sequencia.append(a)

        proximo = a + b
        a = b
        b = proximo

        contador += 1

    
    print("\n=== RESULTADOS ===")

    print("Sequencia de Fibonacci:")
    print(" -> ".join(str(numero) for numero in sequencia))

    print("\nQuantidade de termos:", n)