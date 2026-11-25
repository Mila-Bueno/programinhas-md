
# Verificador de propriedades de uma relação

print("=== VERIFICADOR DE RELACOES ===")


elementos = input("Digite os elementos do conjunto separados por virgula: ex.: 1,2,3\n")
A = [x.strip() for x in elementos.split(",")]


entrada = input("Digite os pares ordenados: ex.: 1,2; 2,3 \n")

R = set()

if entrada.strip():
    pares = entrada.split(";")

    for par in pares:
        x, y = par.split(",")
        R.add((x.strip(), y.strip()))


if any(x not in A or y not in A for x, y in R):
    print("Erro: existem elementos fora do conjunto!")
else:
    
    reflexiva = all((x, x) in R for x in A)

    
    simetrica = all((y, x) in R for x, y in R)

    
    transitiva = True

    for x, y in R:
        for z, w in R:
            if y == z and (x, w) not in R:
                transitiva = False


    print("\n=== SEU CONJUNTO É: ===")
    print("Reflexiva:", "Sim" if reflexiva else "Não")
    print("Simetrica:", "Sim" if simetrica else "Não")
    print("Transitiva:", "Sim" if transitiva else "Não")
