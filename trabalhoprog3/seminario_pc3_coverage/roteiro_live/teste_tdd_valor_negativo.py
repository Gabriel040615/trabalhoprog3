"""Etapa opcional vermelho→verde. O nome evita descoberta pela suíte final."""

import pytest

from roteiro_live.loja_tdd_incompleta import calcular_desconto


def teste_valor_negativo_deve_gerar_erro():
    with pytest.raises(ValueError, match="não pode ser negativo"):
        calcular_desconto(-1, False)
