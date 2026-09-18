# LaunchLab UniFAP - Desenvolvimento Exclusivo SI

# Dicionario de metadados de compliance ambiental e auditoria financeira.
# Toda regra de negocio abaixo le daqui: mudar a politica nao exige mudar codigo.
METADADOS_COMPLIANCE = {
    # --- Parametros de capacidade e ociosidade ---
    "limite_frota_m3": 50.0,          # Teto fisico da carga por viagem
    "piso_ociosidade_percentual": 0.30,  # Abaixo de 30% da frota a viagem e' deficitaria
    # --- Parametros economicos e ambientais da viagem ---
    "custo_litro_diesel_brl": 6.20,
    "consumo_medio_litros_viagem": 18.0,
    "fator_emissao_kg_co2_por_litro": 2.68,
    # --- Metadados de rastreabilidade para auditoria ---
    "versao_politica": "2024.1",
    "unidade_medida_volume": "m³",
    "area_responsavel": "Governanca de TI - Logistica Reversa",
    "indicadores_ambientais": ["Reducao CO2", "Economia Combustivel"],
}


def calcular_indice_ociosidade(volume_final):
    """Indicador dinamico: fracao da capacidade da frota que viajou vazia.

    Retorna um valor entre 0.0 (caminhao cheio) e 1.0 (caminhao vazio).
    """
    limite = METADADOS_COMPLIANCE["limite_frota_m3"]
    capacidade_ociosa = limite - volume_final

    if capacidade_ociosa <= 0:
        return 0.0
    return capacidade_ociosa / limite


def calcular_custo_ociosidade(volume_final):
    """Converte a ociosidade em desperdicio financeiro (R$) e ambiental (kg CO2)."""
    indice = calcular_indice_ociosidade(volume_final)

    litros_desperdicados = indice * METADADOS_COMPLIANCE["consumo_medio_litros_viagem"]
    custo = litros_desperdicados * METADADOS_COMPLIANCE["custo_litro_diesel_brl"]
    emissao = litros_desperdicados * METADADOS_COMPLIANCE["fator_emissao_kg_co2_por_litro"]

    return {
        "indice_ociosidade": round(indice, 4),
        "litros_desperdicados": round(litros_desperdicados, 2),
        "custo_ocioso_brl": round(custo, 2),
        "emissao_evitavel_kg_co2": round(emissao, 2),
    }


def calcular_eficiencia_financeira(volume_final):
    """Porta de entrada da regra de viabilidade economica da viagem."""
    limite = METADADOS_COMPLIANCE["limite_frota_m3"]
    piso_percentual = METADADOS_COMPLIANCE["piso_ociosidade_percentual"]

    # Piso critico derivado da politica: 50.0 m³ * 0.30 = 15.0 m³.
    piso_critico_m3 = limite * piso_percentual

    if volume_final < piso_critico_m3:
        return "Alerta: Alto Custo de Ociosidade Detectado"
    return "Eficiencia Economica Aceitavel"


if __name__ == "__main__":
    volume_exemplo = 12.5
    print(calcular_eficiencia_financeira(volume_exemplo))
    print(calcular_custo_ociosidade(volume_exemplo))
