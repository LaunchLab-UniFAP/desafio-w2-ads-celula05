# LaunchLab UniFAP - Desenvolvimento Exclusivo ADS

# Capacidade fisica da carga do veiculo, em m³.
LIMITE_MAXIMO_M3 = 50.0

# Trava de seguranca: mesmo que as duas paradas de negocio falhem, o laco
# nunca roda para sempre (evita o "codigo cego" / loop infinito).
MAX_LEITURAS = 1000


def processar_motor_coleta():
    volume_acumulado = 0.0
    limite_atingido = False
    leituras = 0

    print("--- MOTOR OPERACIONAL DE COLETA (ADS) ---")

    while leituras < MAX_LEITURAS:
        leituras += 1

        # O try cobre apenas a leitura e a conversao: e' onde o erro acontece.
        try:
            entrada = input("Digite o volume da cacamba (m³) ou -1 para encerrar: ")
            volume = float(entrada)
        except ValueError:
            # Texto, simbolo ou linha vazia: avisa e continua o turno.
            print("Erro: Entrada Invalida")
            continue
        except EOFError:
            # Fim da entrada (arquivo/pipe acabou): encerra sem quebrar.
            break

        # Parada 1: fim programado do turno.
        if volume == -1:
            break

        # Volume negativo nao existe na operacao: rejeita sem somar.
        if volume < 0:
            print("Erro: Entrada Invalida")
            continue

        volume_acumulado += volume

        # Parada 2: saturacao fisica da carga do veiculo.
        if volume_acumulado >= LIMITE_MAXIMO_M3:
            limite_atingido = True
            break

    # A apresentacao fica fora do laco: o laco decide, o final comunica.
    print(f"Volume Total: {volume_acumulado:g} m³")
    if limite_atingido:
        print("Status: Capacidade Maxima Atingida")


if __name__ == "__main__":
    processar_motor_coleta()
