TASA_USURA_EA = 0.2489


def get_tasa_usura_mv():
    return (1+TASA_USURA_EA)**(1/12)-1