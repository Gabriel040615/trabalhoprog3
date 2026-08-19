"""Suíte final: cada caso representa uma regra ou um limite do domínio."""

import pytest

from src.loja import calcular_desconto


@pytest.mark.parametrize(
    ("valor", "cliente_vip", "esperado"),
    [
        (100, True, 80),
        (100, False, 100),
        (500, False, 450),
        (1000, False, 900),
    ],
    ids=["vip", "comum_abaixo_do_limite", "limite_500", "comum_acima_do_limite"],
)
def test_calcular_desconto(valor, cliente_vip, esperado):
    """Valida os caminhos de desconto e o valor de fronteira."""
    assert calcular_desconto(valor, cliente_vip) == esperado


def test_valor_negativo_e_invalido():
    """Valida o caminho excepcional da regra de negócio."""
    with pytest.raises(ValueError, match="não pode ser negativo"):
        calcular_desconto(-1, False)
