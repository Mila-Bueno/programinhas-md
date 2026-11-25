
# Soma dos numeros impares
#O programa trabalha a propriedade que diz: A soma dos primeiros n números ímpares é sempre igual a n²
#Ex.: n = 3. 
# 1 + 3 + 5 = 9. 
# 3² = 9.

print("=== SOMA DOS NUMEROS IMPARES ===")


n = int(input("Quantos numeros impares deseja somar? "))

if n < 1:
    print("Digite uma quantidade maior ou igual a 1.")

else:
    
    soma = 0
    impares = []

    for numero in range(1, 2 * n, 2):
        soma += numero
        impares.append(numero)

    
    quadrado = n ** 2

    
    expressao = " + ".join(str(numero) for numero in impares)

    
    print("\n=== RESULTADOS ===")

    print("Soma dos impares:", expressao, "=", soma)

    print("Formula matematica: n²")
    print("Substituindo n =", n, ":", n, "^ 2 =", quadrado)

    if soma == quadrado:
        print("A propriedade foi confirmada!")
    else:
        print("Os resultados sao diferentes!")
