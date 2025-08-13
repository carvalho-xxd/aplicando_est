valor_unitario_pe = 3

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

    pontos_adicionados = pontos_extra * valor_unitario_pe
    pontos_totais += pontos_adicionados
    print(f"Pontos extras adicionados: {pontos_adicionados}")
else:
    print("Nenhum ponto extra adicionado.")
