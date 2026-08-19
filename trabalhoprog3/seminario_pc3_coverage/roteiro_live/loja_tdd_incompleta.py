"""Versão propositalmente incompleta para mostrar o estado RED no seminário."""


def calcular_desconto(valor: float, cliente_vip: bool) -> float:
    if cliente_vip:
        return valor * 0.80
    if valor >= 500:
        return valor * 0.90
    return valor
