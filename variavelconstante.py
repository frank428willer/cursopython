#variavel que não serão alterados os valores por convenção
#são declaradas com letras maiusculas 

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade = 61
local_carro = 90

velocidade_no_radar = velocidade > RADAR_1
passou_no_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_no_radar:
    print("acima de velocidade")

if passou_no_radar and velocidade_no_radar:
    print('multado por passar acima da velocidade')