"""Regras simples de desconto usadas na demonstração de coverage.py."""


def calcular_desconto(valor: float, cliente_vip: bool) -> float:
    """Calcula o valor final de uma compra conforme as regras da loja.

    Clientes VIP recebem 20% de desconto. Clientes não VIP recebem 10%
    quando a compra é de R$ 500,00 ou mais. Valores negativos são inválidos.
    """
    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")

    if cliente_vip:
        return valor * 0.80

    if valor >= 500:
        return valor * 0.90

    return valor
