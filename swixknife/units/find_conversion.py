
from decimal import Decimal as D
from swixknife import Sezimal as S, SezimalFraction as SF
from swixknife.base import sezimal_format, decimal_format

from tqdm import tqdm


mass = D('3057974877246151') / D('175075132133727776')
heat = D('13888308826205568') / D('190039112087675')


for i in tqdm(range(4_184_000_000, 4_184_050_001)):
    water_entropy = D(i) / 1_000_000
    entropy = water_entropy * mass
    kelvin = heat / entropy
    congelamento = D('273.15') / kelvin
    fervura = D('373.15') / kelvin

    print(water_entropy, congelamento, fervura)

    teste = (congelamento - trunc(congelamento)) * 1_000_000

    if teste != 125_000:
        continue

    print('water_entropy', water_entropy, S(water_entropy))
    print('kelvin', kelvin, S(kelvin))

    cong_6 = S(congelamento)
    ferv_6 = S(fervura)

    print('0 °C', congelamento, cong_6)
    print('100 °C', fervura, ferv_6)

    break
