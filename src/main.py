from tc import get_tasa_usura_mv 
from tc import TASA_USURA_EA
 
tasa_usura = get_tasa_usura_mv()
print("usura efectiva anual", TASA_USURA_EA*100, "%" )
print("usura mensual vencido", tasa_usura*100, "%" )