
from decimal import Decimal
from swixknife import Dozenal, DozenalFraction
from swixknife.localization import sezimal_locale
from swixknife.base import dozenal_format, decimal_format
from collections import OrderedDict

TIME = DozenalFraction('21 / 600')
GRAVITY = DozenalFraction('42_249_605_000 / 5_159_944_12↋')
DENSITY = DozenalFraction('2↊_↋↊0_016_278_135 / 50_693_74↋_4↊8')
CALORIE = DozenalFraction('31_05↊_↊↊6_76↋_118_749_166_368 / 13_36↊_7↊4_693_430_016_929')

# GRAVITY = DozenalFraction('1_346_690 / 16↊_081')  # Primel’s original
# GRAVITY = DozenalFraction('3_670 / 441')  # Shastadari

# DENSITY = DozenalFraction('100_809 / 18↊')  # Primel’s original
# DENSITY = DozenalFraction('19_↊49_003_9↊5_307 / 31_↊29_917_168')

# CALORIE = DozenalFraction('↋_933_861_837_939 / 4_↊18_548_714')  # Primel’s original
# CALORIE = DozenalFraction('96_698_↊↊6_↊89_↋9↊.0 / 3↋_396_24↋_↊↋4')


class PrimelUnits:
    def __init__(self):
        self.time = TIME
        self.frequency = self.time.reciprocal
        self.acceleration = GRAVITY
        self.velocity = self.time * self.acceleration
        self.speed = self.velocity * DozenalFraction('16 / 5')
        self.length = self.velocity * self.time
        self.area = self.length * self.length
        self.volume = self.length * self.area
        self.density = DENSITY
        self.mass = self.density * self.volume
        self.mass_grams = self.mass * Dozenal('6↋4')
        self.mass_milligrams = self.mass_grams * Dozenal('6↋4')
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
        self.absolute_temperature = self.energy__work__potential__heat / self.heat_capacity__entropy
        self.common_temperature = self.absolute_temperature * 10_000
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
            print(f'{name} [ {symbol} ]|{dozenal_format(value, dozenal_places=Dozenal("13"), fraction_group_separator="_", recurring_digits_notation=False)}|{value.formatted_number}|{value.decimal_formatted_number}|{decimal_format(value.decimal, decimal_places=15, fraction_group_separator="_", recurring_digits_notation=False)}'.replace('_', ' '))

        print()
        print()

        for unit, symbol in UNITS.items():
            name = unit.replace('__', '; ').replace('_', ' ').capitalize()
            value = getattr(self, unit).reciprocal
            print(f'{name} [ {symbol} ]|{dozenal_format(value, dozenal_places=Dozenal("13"), fraction_group_separator="_", recurring_digits_notation=False)}|{value.formatted_number}|{value.decimal_formatted_number}|{decimal_format(value.decimal, decimal_places=15, fraction_group_separator="_", recurring_digits_notation=False)}'.replace('_', ' '))


if __name__ == '__main__':
    su = PrimelUnits()
    su.report('en')
