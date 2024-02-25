
from decimal import Decimal as D
from swixknife.base import dozenal_format, decimal_format

precision = D(10) ** 9
TIMEL = D('86_400') / D(12) ** D(5)
factor_gravity = D(12) ** 0

from tqdm import tqdm

for i in tqdm(range(9_500_000_000, 10_000_000_001)):
    gravity = D(i) / precision
    accelerel = gravity / factor_gravity
    velocitel = accelerel * TIMEL
    lenghtel = velocitel * TIMEL

    light_speed = D('299_792_458') / velocitel

    if light_speed == int(light_speed):
        accelerel = decimal_format(accelerel, decimal_places=36, recurring_digits_notation=True)
        velocitel = decimal_format(velocitel, decimal_places=36, recurring_digits_notation=True)
        gravity = decimal_format(gravity, decimal_places=9, recurring_digits_notation=True)
        light_speed = decimal_format(light_speed, decimal_places=0, recurring_digits_notation=True)
        lenghtel_decimal = decimal_format(lenghtel, decimal_places=36, recurring_digits_notation=True)
        lenghtel_dozenal = dozenal_format(lenghtel, dozenal_places=30, recurring_digits_notation=True)
        print(lenghtel_dozenal, lenghtel_decimal, accelerel, gravity, velocitel, light_speed)
