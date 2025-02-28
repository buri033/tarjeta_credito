import pytest

from src.tc import TASA_USURA_EA, tarjeta_credito, get_tasa_usura_mv, compra, cuota


def test_calcular_tasa_usura_efectiva_anual():
    assert TASA_USURA_EA == 0.2489


def test_calcular_tasa_usura_mensual_vencida():
    assert get_tasa_usura_mv() == 0.018694525225513958


def test_caso_36_cuotas():
    compra1 = compra.Compra(0.031, 200000, 36)
    assert compra1.calcular_intereses() == 134726.53


def test_caso_24_cuotas():
    monto = 200000
    tasa = 0.031
    cuotas = 36
    resultado = 134726.53
    assert pytest.approx(intereses, 0.01) == 407059.97


def test_caso_tasa_cero():
    intereses = tarjeta_credito.calcular_total_intereses(480000, 0.0, 48)
    assert intereses == 0


def test_caso_tasa_usura():
    with pytest.raises(ValueError, match="La tasa de interés supera la tasa de usura"):
        tarjeta_credito.calcular_total_intereses(50000, 0.125, 60)


def test_caso_cuota_unica():
    intereses = tarjeta_credito.calcular_total_intereses(90000, 0.024, 1)
    assert intereses == 0


def test_caso_monto_invalido():
    with pytest.raises(ValueError, match="el monto debe ser superior a cero"):
        tarjeta_credito.calcular_total_intereses(0, 0.024, 60)


def test_caso_cuota_negativa():
    with pytest.raises(ValueError, match="el número de cuotas debe ser mayor a cero"):
        tarjeta_credito.calcular_total_intereses(50000, 0.01, -10)
