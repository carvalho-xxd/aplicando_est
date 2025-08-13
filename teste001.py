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

produtos = ['produto1','produto2', 'produto3', 'produto4', 'produto5','produto6','produto7','produto8','produto9']
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

valor_unitario_ponto_extra = 5

while True:
    ponto_extra = input("A loja possui ponto extra? (s/n): ").strip().lower()
    if ponto_extra in ['s', 'n']:
        break
    else:
        print("Digite apenas 's' ou 'n'.")

if ponto_extra == 's':
    while True:
        try:
            pontos_extra = int(input("Quantos pontos extras a loja possui? "))
            if pontos_extra >= 0:
                break
            else:
                print("Digite um número inteiro maior ou igual a zero.")
        except ValueError:
            print("Por favor, digite um número válido.")

    pontos_adicionados = pontos_extra * valor_unitario_ponto_extra
    pontos_totais += pontos_adicionados
    print(f"Pontos extras adicionados: {pontos_adicionados}")
else:
    print("Nenhum ponto extra adicionado.")

print(f"\nPontuação total da loja (com ponto extra): {pontos_totais}")
bonus = calcular_bonus(pontos_totais)
print(f"Bônus do promotor: {bonus}%")