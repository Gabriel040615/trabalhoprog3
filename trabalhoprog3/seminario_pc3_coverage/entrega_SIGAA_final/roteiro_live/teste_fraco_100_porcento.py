"""Este teste executa todas as linhas, porém não valida a regra de 20%."""

import pytest

from roteiro_live.exemplo_100_porcento_com_bug import desconto_vip_com_bug


def teste_fraco_ainda_passa_com_regra_errada():
    assert desconto_vip_com_bug(100) > 0
    with pytest.raises(ValueError):
        desconto_vip_com_bug(-1)
