
# Calculadora de Fecho Transitivo que verifica se a relação é transitiva ou o cojunto que falta para se tornar transitiva

print("=== CALCULADORA DE FECHO TRANSITIVO ===")


elementos = input("Digite os elementos do conjunto (separados por virgula): ")
A = [x.strip() for x in elementos.split(",")]


entrada = input("Digite os pares ordenados (ex: 1,2; 2,3): ")

R = set()

if entrada.strip():
    pares = entrada.split(";")

    for par in pares:
        x, y = par.split(",")
        R.add((x.strip(), y.strip()))

# Verifica se os elementos pertencem ao conjunto
if any(x not in A or y not in A for x, y in R):
    print("Erro: existem elementos fora do conjunto!")

else:
    
    fecho = R.copy()

    
    mudou = True

    while mudou:
        mudou = False

        for x, y in list(fecho):
            for z, w in list(fecho):

                if y == z and (x, w) not in fecho:
                    fecho.add((x, w))
                    mudou = True

    
    print("\nRelacao original:", sorted(R))
    print("Fecho transitivo:", sorted(fecho))

    if fecho == R:
        print("A relacao ja era transitiva!")
    else:
        print("Novos pares adicionados:")
        print(sorted(fecho - R))
