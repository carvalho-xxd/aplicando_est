def calcular_pontos(direita, planograma):
    pontos = 0
    if direita == 's':
        pontos += 3
    if planograma == 's':
        pontos += 2
    return pontos

def calcular_bonus(pontos_totais):
    if pontos_totais >= 90:
        return 30
    elif pontos_totais >= 80:
        return 20
    elif pontos_totais >= 70:
        return 10
    else:
        return 0

produtos = ["Ox", "Neutrox", "Francis", "Minuano", "Matinset"]
pontos_totais = 0

print("Sistema de Pontuação - Verificação de Bônus\n")

for produto in produtos:
    print(f"--- {produto} ---")

    while True:
        direita = input("Está ao lado direito da concorrência? (s/n): ").strip().lower()
        if direita == 's':
            print("3pts")
            break
        elif direita == 'n':
            print("0pts")
            break
        else:
            print("Digite apenas 's' ou 'n'.")

    while True:
        planograma = input("Está no planograma da empresa? (s/n): ").strip().lower()
        if planograma in ['s', 'n']:
            break
        else:
            print("Digite apenas 's' ou 'n'.")

    pontos = calcular_pontos(direita, planograma)
    print(f"Pontos para {produto}: {pontos}\n")
    pontos_totais += pontos

print(f"Pontuação total da loja: {pontos_totais}")
bonus = calcular_bonus(pontos_totais)
print(f"Bônus do promotor: {bonus}%")