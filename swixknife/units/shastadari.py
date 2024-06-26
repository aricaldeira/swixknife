
from swixknife import sezimal_context
from decimal import Decimal, getcontext
from swixknife import Sezimal, SezimalFraction, SezimalRange, SezimalInteger
from swixknife.localization import sezimal_locale
from swixknife.base import sezimal_format, decimal_format
from collections import OrderedDict

from swixknife.sezimal import _RECIPROCAL_MAP

sezimal_context.sezimal_precision = 4000

#
# Time fraction:
# 1 day in seconds ÷ 10¹²
# 1 day in seconds ÷ 6⁸_dec
#
TIME = SezimalFraction('41 / 2_130')

#
# Acceleration fraction:
# Earth’s gravity at coordinates 51.28_dec N 0 W
# The common value for g is slightly lower, but also arbitrary;
# The following fraction, when combined with the time fraction,
# gives an integer number for the speed of light
#
# https://www.wolframalpha.com/input?i=standard+gravity+at+latitude+51.28+longitude+0+
#
# The position is close to, but not exactly on, the Greenwich Prime Meridian:
# https://en.wikipedia.org/wiki/Prime_meridian_(Greenwich)
#
GRAVITY = SezimalFraction('44_220 / 2_521')

#
# First acceleration I used, gets nice SI conversion,
# but is too low to be Earth’s gravity, plus the whole
# system is not entirely coherent
#
# GRAVITY = SezimalFraction('1_043 / 41')

#
# Density of water at 1 atm and
# at the temperature of
# 293.150_547_159_702_806_710_267_922_561_179_315_dec K
#  20.000_547_159_702_806_710_267_922_561_179_315_dec °C
# as calculated by Wolfram Alpha using the link:
# https://www.wolframalpha.com/input?i=density+water+at+293.150547159702806710267922561179315+K+and+1+atm+with+15+digits+precision
# Limited to 15_dec digits precision
#
# DENSITY = SezimalFraction('13_455_001_552_110_541_335 / 2_043_221_010_301_344')
DENSITY = SezimalFraction('5_223_045_303_000_304_351 / 1_100_315_423_005_012')

#
# The same density, but with more precision
# https://www.wolframalpha.com/input?i=density+water+at+293.150547159702806710267922561179315+K+and+1+atm+with+36+digits+precision
#
# DENSITY = SezimalFraction('210_534_053_505_503_445_233_200/ 25_025_240_544_021_032_155')

#
# Specific heat of water at 1 atm and
# at the temperature of
# 293.150_547_159_702_806_710_267_922_561_179_315_dec K
#  20.000_547_159_702_806_710_267_922_561_179_315_dec °C
# as calculated by Wolfram Alpha using the link:
# https://www.wolframalpha.com/input?i=specific+heat+of+water+at+293.150547159702806710267922561179315+K+and+1+atm+with+15+digits+precision
# Limited to 15_dec digits precision
#
# SPECIFIC_HEAT = SezimalFraction('105_110_422_141_212_423_455 / 2_043_221_010_301_344')
SPECIFIC_HEAT = SezimalFraction('113_144_132_111_030_100_551 / 2_201_035_250_014_024')

#
# The same specific heat, but with more precision
# https://www.wolframalpha.com/input?i=specific+heat+of+water+at+293.150547159702806710267922561179315+K+and+1+atm+with+36+digits+precision
#
# SPECIFIC_HEAT = SezimalFraction('533_221_420_232_325_332_212_332/ 14_221_432_040_152_314_415')

#
# Vacuum resistance/impedance in ohms, converted to
# fraction form:
# https://en.wikipedia.org/wiki/Impedance_of_free_space
#
#VACUUM_RESISTANCE = SezimalFraction('424_125_300_421_243_401 / 231_513_450_033_532')
VACUUM_RESISTANCE = SezimalFraction('111_133_351_303_345 / 40_450_211_224')

#
# Elementary charge in coulombos, converted to
# fraction form:
# https://en.wikipedia.org/wiki/Elementary_charge
#
ELEMENTARY_CHARGE = SezimalFraction('211_254_034_113 / 252_412_511_453_013_134_321_101_511_222_244_052')

#
# Luminous efficacy, converted to
# fraction form:
# https://en.wikipedia.org/wiki/Luminous_efficiency_function
#
LUMINOUS_EFICACY = SezimalFraction('151_435_021_012 / 33_233_341')


class ShastadariUnits:
    def __init__(self):
        self.time = TIME  # second
        self.frequency = self.time.reciprocal  # Hertz
        self.acceleration = GRAVITY  # m/s²
        self.velocity = self.time * self.acceleration  # m/s
        self.speed = self.velocity * SezimalFraction('30 / 5')  # km/h
        self.length = self.velocity * self.time  # m
        self.area = self.length * self.length  # m²
        self.volume = self.length * self.area  # m³
        self.density = DENSITY  # kg/m³
        self.mass = self.density * self.volume  # kg
        self.mass_grams = self.mass * 4_344  # g
        self.mass_milligrams = self.mass_grams * 4_344  # mg
        self.momentum = self.mass * self.velocity  # kg·m/s
        self.action = self.momentum * self.length  # kg·m²/s
        self.force__weight = self.mass * self.acceleration  # N = kg·m/s²
        self.energy__work__potential__heat = self.force__weight * self.length  # J = kg·m²/s²
        self.influence = self.force__weight * self.area  # N·m² = kg·m³/s²
        self.power = self.energy__work__potential__heat / self.time  # W = kg·m²/s³
        self.intensity = self.power / self.area  # W/m² = kg/s³
        self.tension = self.force__weight / self.length  # N/m = kg/s²
        self.pressure = self.force__weight / self.area  # Pa = kg/m/s²
        self.atmosphere = self.pressure / 2_101_033
        self.dynamic_viscosity = self.mass / self.length / self.time  # kg/m/s
        self.kinectic_viscosity = self.area / self.time  # m³/s
        self.heatability = SPECIFIC_HEAT  # J/K/kg = m²/s²/K
        self.heat_capacity__entropy = SPECIFIC_HEAT * self.mass  # J/K = kg·m²/s²/K
        self.absolute_temperature = self.energy__work__potential__heat / self.heat_capacity__entropy
        self.absolute_temperature = SezimalFraction('41_143 / 12_523_221_412')  # K
        self.common_temperature = self.absolute_temperature * 100_000
        self.common_temperature = SezimalFraction('132_523_430 / 320_113_505')  # °C
        self.gravitivity = self.influence / self.mass / self.mass  # m³/s²/kg

        self.electric_resistance = VACUUM_RESISTANCE  # Ω = V/A = kg·m²/s³/A²

        #
        # First calculation of an integer amount of elementary charges
        # tuned so that the ohm equivalent is exactly the vacuum resistance
        #
        # breakpoint()
        # old_precision = sezimal_context.sezimal_precision
        # old_fractions_use_decimal = sezimal_context.fractions_use_decimal
        # sezimal_context.sezimal_precision = 1200
        # getcontext().prec = 216
        # sezimal_context.fractions_use_decimal = True
        #
        # vr = SezimalFraction('111_133_351_303_345 / 40_450_211_224')
        # ec = SezimalFraction('211_254_034_113 / 252_412_511_453_013_134_321_101_511_222_244_052')
        #
        # electric_charge = (self.mass * self.area) / self.time / vr
        # elementary_charges = round(electric_charge.decimal.sqrt() / ec.decimal, 0)
        # self.electric_charge = elementary_charges * ELEMENTARY_CHARGE
        # sezimal_context.sezimal_precision = old_precision
        # sezimal_context.fractions_use_decimal = old_fractions_use_decimal

        #
        # Pre-calculated elementary charge - coulomb
        #
        self.electric_charge = SezimalFraction('4_223_523_221_410_440_513_140_205_022_413 / 42_102_114_542_132_152_350_143_244_503_341_012')  # C = A·s
        self.electric_current = self.electric_charge / self.time  # A = C/s
        self.electric_potential_difference = self.energy__work__potential__heat / self.electric_charge  # V = J/C = kg·m²/s³/A
        self.electric_conductance = self.electric_current / self.electric_potential_difference  # S = 1/Ω = s³·A²/kg/m²
        self.electric_inductance = self.electric_resistance * self.time  # H = Wb/A = kg·m²/s²/A²
        self.electric_capacitance = self.electric_charge / self.electric_potential_difference  # F = C/V = s⁴·A²/kg/m²
        self.magnetic_flux = self.electric_potential_difference * self.time  # Wb = V·s = kg·m²/s²/A
        self.magnetic_flux_density = self.magnetic_flux / self.area  # T = Wb/m² = kg/s²/A

        self.luminous_energy = self.energy__work__potential__heat * LUMINOUS_EFICACY  # lm·s
        self.luminous_flux = self.luminous_energy / self.time  # lm
        self.luminous_illuminance_emitance = self.luminous_flux / self.area  # lx = lm/m²
        self.luminous_energy_density = self.luminous_energy / self.volume  # lm·s/m³
        self.luminous_exposure = self.luminous_illuminance_emitance * self.time  # lx·s = lm·s/m²
        self.luminous_eficacy = LUMINOUS_EFICACY  # lm/W = lm·s³/kg/m²
        self.luminous_intensity = self.luminous_flux  # cd
        self.luminous_luminance = self.luminous_intensity / self.area  # cd/m²

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
            'force__weight': 'N = kg·m/s²',
            'energy__work__potential__heat': 'J = kg·m²/s²',
            'influence': 'N·m² = kg·m³/s²',
            'power': 'W = kg·m²/s³',
            'intensity': 'W/m² = kg/s³',
            'tension': 'N/m = kg/s²',
            'pressure': 'Pa = kg/m/s²',
            'dynamic_viscosity': 'kg/m/s',
            'kinectic_viscosity': 'm³/s',
            'gravitivity': 'm³/s²/kg',

            'absolute_temperature': 'K',
            'common_temperature': '°C',
            'heat_capacity__entropy': 'J/K = kg·m²/s²/K',
            'heatability': 'J/K/kg = m²/s²/K',

            'electric_current': 'A = C/s',
            'electric_charge': 'C = A·s',
            'electric_potential_difference': 'V = J/C = kg·m²/s³/A',
            'electric_capacitance': 'F = C/V = s⁴·A²/kg/m²',
            'electric_resistance': 'Ω = V/A = kg·m²/s³/A²',
            'electric_conductance': 'S = 1/Ω = s³·A²/kg/m²',
            'magnetic_flux': 'Wb = V·s = kg·m²/s²/A',
            'magnetic_flux_density': 'T = Wb/m² = kg/s²/A',
            'electric_inductance': 'H = Wb/A = kg·m²/s²/A²',

            'luminous_flux': 'lm',
            'luminous_energy': 'lm·s',
            'luminous_illuminance_emitance': 'lx = lm/m²',
            'luminous_exposure': 'lx·s = lm·s/m²',
            'luminous_energy_density': 'lm·s/m³',
            'luminous_eficacy': 'lm/W = lm·s³/kg/m²',
            'luminous_intensity': 'cd',
            'luminous_luminance': 'cd/m²',
        })

        for unit, symbol in UNITS.items():
            name = unit.replace('__', '; ').replace('_', ' ').capitalize()
            value = getattr(self, unit)
            SezimalInteger(1) / value.sezimal
            # print(f'{name} [ {symbol} ]|{sezimal_format(value, sezimal_places=33, fraction_group_separator="_", recurring_digits_notation=False)}|{decimal_format(value.decimal, decimal_places=15, fraction_group_separator="_", recurring_digits_notation=False)}|{value.formatted_number}|{value.decimal_formatted_number}'.replace('_', ' '))

        print()
        print()

        for unit, symbol in UNITS.items():
            name = unit.replace('__', '; ').replace('_', ' ').capitalize()
            value = getattr(self, unit).reciprocal
            SezimalInteger(1) / value.sezimal
            # print(f'{name} [ {symbol} ]|{sezimal_format(value, sezimal_places=33, fraction_group_separator="_", recurring_digits_notation=False)}|{decimal_format(value.decimal, decimal_places=15, fraction_group_separator="_", recurring_digits_notation=False)}|{value.formatted_number}|{value.decimal_formatted_number}'.replace('_', ' '))


if __name__ == '__main__':
    su = ShastadariUnits()
    # su.report('en')

    new_map = {}

    arq = open('/home/ari/mapa.py', 'w')

    for i in _RECIPROCAL_MAP:
        val = Sezimal(i).decimal

        new_map[val] = [i, _RECIPROCAL_MAP[i]]


    for i in sorted(new_map.keys()):
        val, div = new_map[i]

        if '.' in val:
            continue

        if len(val) <= 4:
            continue

        if val.replace('0', '') == '1':
            continue

        if '_' not in div:
            div = round(Sezimal(div), 1200).formatted_number

        arq.write(f"""    '{val}': '{div}',\n""")


    # caloria = (su.energy_work_potential_heat / su.temperature) / su.mass
    # print(caloria, caloria.sezimal, caloria.decimal)
    # caloria = SPECIFIC_HEAT
    # print(caloria, caloria.sezimal, caloria.decimal)
    #
    # print((Decimal('27315') / su.temperature).decimal / 100)
