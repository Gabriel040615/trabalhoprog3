"""Código de apoio: todo o fluxo pode executar e a regra ainda estar errada."""


def desconto_vip_com_bug(valor: float) -> float:
    """BUG intencional: a regra correta seria 20%, mas calcula 15%."""
    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")
    return valor * 0.85
