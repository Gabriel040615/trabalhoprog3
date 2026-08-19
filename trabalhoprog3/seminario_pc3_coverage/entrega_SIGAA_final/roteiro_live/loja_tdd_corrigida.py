"""Versão GREEN: acrescente esta validação à versão incompleta ao vivo."""


def calcular_desconto(valor: float, cliente_vip: bool) -> float:
    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")
    if cliente_vip:
        return valor * 0.80
    if valor >= 500:
        return valor * 0.90
    return valor
