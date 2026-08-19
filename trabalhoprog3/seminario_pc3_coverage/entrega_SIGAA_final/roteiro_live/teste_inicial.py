"""Etapa 1 do palco: execute este arquivo isoladamente, não a suíte final."""

from src.loja import calcular_desconto


def test_cliente_vip_recebe_vinte_por_cento_de_desconto():
    assert calcular_desconto(100, True) == 80
