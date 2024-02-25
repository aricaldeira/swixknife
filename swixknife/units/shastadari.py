
from decimal import Decimal
from swixknife import Sezimal, SezimalFraction, SezimalRange, SezimalInteger
from swixknife.localization import sezimal_locale
from swixknife.base import sezimal_format, decimal_format
from collections import OrderedDict


TIME = SezimalFraction('41 / 2_130')

GRAVITY = SezimalFraction('44_220 / 2_521')
# GRAVITY = SezimalFraction('235_130_000_000/ 13_531_202_544')  # Exactly the inch
# GRAVITY = SezimalFraction('1_043 / 41')

# DENSITY = SezimalFraction('210_534_053_505_503_445_233_200/ 25_025_240_544_021_032_155')
DENSITY = SezimalFraction('1_530_352_241_044_350_011 / 225_420_400_413_012')

# CALORIE = SezimalFraction('533_221_420_232_325_332_212_332/ 14_221_432_040_152_314_415')
CALORIE = SezimalFraction('14_020_313_040_133_131_521 / 304_053_500_515_144')


class ShastadariUnits:
    def __init__(self):
        self.time = TIME
        self.frequency = self.time.reciprocal
        self.acceleration = GRAVITY
        self.velocity = self.time * self.acceleration
        self.speed = self.velocity * SezimalFraction('30 / 5')
        self.length = self.velocity * self.time
        self.area = self.length * self.length
        self.volume = self.length * self.area
        self.density = DENSITY
        self.mass = self.density * self.volume
        self.mass_grams = self.mass * 4_344
        self.mass_milligrams = self.mass_grams * 4_344
        self.momentum = self.mass * self.velocity
        self.action = self.momentum * self.length
        self.force__weight = self.mass * self.acceleration
        self.energy__work__potential__heat = self.force__weight * self.length
        self.influence = self.force__weight * self.area
        self.power = self.energy__work__potential__heat / self.time
        self.intensity = self.power / self.area
        self.tension = self.force__weight / self.length
        self.pressure = self.force__weight / self.area
        self.dynamic_viscosity = self.mass / self.length / self.time
        self.kinectic_viscosity = self.area / self.time
        self.heatability = CALORIE
        self.heat_capacity__entropy = CALORIE * self.mass
        # self.absolute_temperature = self.energy__work__potential__heat / self.heat_capacity__entropy
        self.absolute_temperature = SezimalFraction('41_143 / 12_523_221_412')
        # self.common_temperature = self.absolute_temperature * 100_000
        self.common_temperature = SezimalFraction('132_523_430 / 320_113_505')
        self.gravitivity = self.influence / self.mass / self.mass

    def report(self, locale: str = None) -> str:
        # locale = sezimal_locale(locale)
        # sezimal_format = locale.format_number
        # decimal_format = locale.format_decimal_number

        text = 'Units:\n\n'

        UNITS = OrderedDict({
            'time': 's',
            'frequency': 'Hz',
            'acceleration': 'm/s²',
            'velocity': 'm/s',
            'speed': 'km/h',
            'length': 'm',
            'area': 'm²',
            'volume': 'm³',
            'density': 'kg/m³',
            'mass': 'kg',
            # 'mass_grams': 'g',
            # 'mass_milligrams': 'mg',
            'momentum': 'kg·m/s',
            'action': 'kg·m²/s',
            'force__weight': 'N',
            'energy__work__potential__heat': 'J',
            'influence': 'N·m²',
            'power': 'W',
            'intensity': 'W/m²',
            'tension': 'N/m',
            'pressure': 'Pa',
            'dynamic_viscosity': 'kg/m/s',
            'kinectic_viscosity': 'm³/s',
            'heatability': 'J/K/kg',
            'heat_capacity__entropy': 'J/K',
            'absolute_temperature': 'K',
            'common_temperature': '°C',
            'gravitivity': 'm³/s²/kg',
        })

        for unit, symbol in UNITS.items():
            name = unit.replace('__', '; ').replace('_', ' ').capitalize()
            value = getattr(self, unit)
            print(f'{name} [ {symbol} ]|{sezimal_format(value, sezimal_places=32, fraction_group_separator="_", recurring_digits_notation=False)}|{value.formatted_number}|{value.decimal_formatted_number}|{decimal_format(value.decimal, decimal_places=15, fraction_group_separator="_", recurring_digits_notation=False)}'.replace('_', ' '))

        print()
        print()

        for unit, symbol in UNITS.items():
            name = unit.replace('__', '; ').replace('_', ' ').capitalize()
            value = getattr(self, unit).reciprocal
            print(f'{name} [ {symbol} ]|{sezimal_format(value, sezimal_places=32, fraction_group_separator="_", recurring_digits_notation=False)}|{value.formatted_number}|{value.decimal_formatted_number}|{decimal_format(value.decimal, decimal_places=15, fraction_group_separator="_", recurring_digits_notation=False)}'.replace('_', ' '))


if __name__ == '__main__':
    su = ShastadariUnits()
    su.report('en')
    # caloria = (su.energy_work_potential_heat / su.temperature) / su.mass
    # print(caloria, caloria.sezimal, caloria.decimal)
    # caloria = CALORIE
    # print(caloria, caloria.sezimal, caloria.decimal)
    #
    # print((Decimal('27315') / su.temperature).decimal / 100)
