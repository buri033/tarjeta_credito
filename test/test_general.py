import pytest

from src.tc import TASA_USURA_EA, tarjeta_credito, get_tasa_usura_mv

def test_calcular_tasa_usura_efectiva_anual():
   assert TASA_USURA_EA == 0.2489

def test_calcular_tasa_usura_mensual_vencida():
   assert get_tasa_usura_mv() == 0.018694525225513958
