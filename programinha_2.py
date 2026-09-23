# Programa Gerador de Tabela-Verdade

valores = [True, False]

print("p | q | r | p OR (q AND r)")
print("-------------------------")

for p in valores:
    for q in valores:
        for r in valores:
            resultado = p or (q and r)

            p_txt = "V" if p else "F"
            q_txt = "V" if q else "F"
            r_txt = "V" if r else "F"
            resultado_txt = "V" if resultado else "F"

            print(p_txt, "|", q_txt, "|", r_txt, "|", resultado_txt)
