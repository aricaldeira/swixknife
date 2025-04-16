#
# This file is intended to be run from the terminal;
# it creates/overwrite the conversion_factor.py file,
# containing the dictionaries with the conversion factors
# between all related units
#

from swixknife import sezimal
from swixknife import sezimal_context
from swixknife import Sezimal, SezimalInteger, SezimalFraction
from swixknife import SezimalRange
from swixknife.constants import TAU, PI, TWO_TAU
from decimal import Decimal

sezimal_context.ultra_precision = 300
sezimal_context.use_ultra_precision()

#
# Time fraction:
# 1 day in seconds ÷ 10¹²
# 1 day in seconds ÷ 6⁸_dec
#
TIME = SezimalFraction('41 / 2_130')

#
# Gravity
#
GRAVITY = SezimalFraction('5_324_444_301_513 / 322_545_201_312')

#
# Density of water at 293.149_986_919_793_dec K
#
# from iapws.iapws95 import IAPWS95
# water = IAPWS95(T=293.149_986_919_793, P=0.101325)
# print(water.rho)
# 998.207_153_168_156_9
#
DENSITY = SezimalFraction('3_023_235_045_222_024_505 / 355_321_023_311_132')

#
# Specific heat of water at 293.149_986_919_793_dec K
#
# from iapws.iapws95 import IAPWS95
# water = IAPWS95(T=293.149_986_919_793, P=0.101325)
# print(water.cp * 1000)
# 4184.050_933_649_753
#
# This exact value gives a conversion between K and gkt
#      273.15_dec K = 240_234_312 (4_499_396_dec) gtk
# exactly, and the conversion between gkt and tap
#      tap = (gtk - 240_234_312) / 100_000
#
SPECIFIC_HEAT = SezimalFraction('323_245_314_040_541_203_352_340_150_141 / 10_212_445_512_343_411_332_414_300')

#
# Vacuum resistance/impedance in ohms, converted to
# fraction form:
# https://en.wikipedia.org/wiki/Impedance_of_free_space
#
IMPEDANCE_FREE_SPACE = SezimalFraction('111_133_351_303_201 / 40_450_211_224')

#
# Elementary charge in coulombos, converted to
# fraction form:
# https://en.wikipedia.org/wiki/Elementary_charge
#
ELEMENTARY_CHARGE_IN_COULOMBS = SezimalFraction('211_254_034_113 / 252_412_511_453_013_134_321_101_511_222_244_052')

#
# Luminous efficacy, converted to
# fraction form:
# https://en.wikipedia.org/wiki/Luminous_efficiency_function
#
LUMINOUS_EFICACY = SezimalFraction('151_435_021_012 / 33_233_341')


ONE_TO_ONE = SezimalFraction('1 / 1')


def calculate_conversions():
    unit_conversion = {}

    #
    # Time
    #
    # Ananta
    # https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%A8%E0%A4%A8%E0%A5%8D%E0%A4%A4#Sanskrit
    #
    ANUGA_TO_SECOND = TIME
    ANANTA_TO_SECOND_SQUARED = ANUGA_TO_SECOND ** 2
    DAY_TO_SECOND = TIME * 100_000_000

    for unit, factor in (
        #
        # Shadarenium - shadara years
        #
        ('xad', SezimalFraction('1_205 / 2_143_240') / 1_000_000),
        #
        # Nifardenium - nif arda years
        #
        ('nrd', SezimalFraction('1_205 / 2_143_240') / 100_000),
        #
        # Sezardenium - six arda years
        #
        ('srd', SezimalFraction('1_205 / 2_143_240') / 10_000),
        #
        # Ardenium - arda years
        #
        ('ard', SezimalFraction('1_205 / 2_143_240') / 1000),
        #
        # Nifenium - nif years
        #
        ('nif', SezimalFraction('1_205 / 2_143_240') / 100),
        #
        # Sezenium - six years
        #
        ('sez', SezimalFraction('1_205 / 2_143_240') / 10),
        #
        # Varsha (year) is the Symmetry454 mean year:
        # 1405 + 155⁄1205 din
        # 2143240⁄1205 din
        # 1405 din 12 uta 42 pox 01 agm 41 ang 53 + 223⁄1205 bod
        #
        ('vrx', SezimalFraction('1_205 / 2_143_240')),
        #
        # Masa (month) is Varsha / 20 (20 months in the mean year)
        #
        ('mas', SezimalFraction('1_205 / 105_142')),
        #
        # Saptaha (week) is the same, 11 days
        #
        ('spt', SezimalFraction('1 / 11')),
        ('din', 1),
        ('uta', 100),
        ('pox', 10_000),
        ('agm', 1_000_000),
        ('ang', 100_000_000),
        ('bod', 10_000_000_000),
    ):
        unit_conversion[unit] = {
            's': DAY_TO_SECOND / factor,
            'prefixed': ('s', 'min', 'h', 'day', 'week', 'month', 'year'),
            'comparable': ('ang', 'vrx', 'mas', 'spt', 'din', 'uta', 'pox', 'agm', 'bod'),
            'ang': factor * 100_000_000,
            #
            # Non S.I. units
            #
            'min': DAY_TO_SECOND / 140 / factor,
            'h': DAY_TO_SECOND / 140 / 140 / factor,
            'day': DAY_TO_SECOND / 140 / 140 / 40 / factor,
            'week': DAY_TO_SECOND / 140 / 140 / 40 / 11 / factor,
            #
            # This is the Gregorian Calendar mean year and month;
            # The Gregorian Calendar has a cycle of 114_144 years
            # comprising 210_141_213 days; and that many days
            # divided into 114_144 × 20 = 2_323_320 months
            #
            'month': SezimalFraction('2_323_320 / 210_141_213') / factor,
            'year': SezimalFraction('114_144 / 210_141_213') / factor,
            'decade': SezimalFraction('114_144 / 210_141_213') / factor / 14,
            'century': SezimalFraction('114_144 / 210_141_213') / factor / 244,
            'millenium': SezimalFraction('114_144 / 210_141_213') / factor / 4344,
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Frequency (avriti)
    #
    # Avriti
    # https://en.wiktionary.org/wiki/%E0%A4%86%E0%A4%B5%E0%A5%83%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%BF#Sanskrit
    #
    # Bramsha (decay)
    # https://en.wiktionary.org/wiki/%E0%A4%AD%E0%A5%8D%E0%A4%B0%E0%A4%82%E0%A4%B6#Sanskrit
    #
    AVRITI_TO_HERTZ = ANUGA_TO_SECOND.reciprocal

    for unit in ('avt', 'brx'):
        unit_conversion[unit] = {
            'Hz': AVRITI_TO_HERTZ,
            'Bq': AVRITI_TO_HERTZ,
            's-1': AVRITI_TO_HERTZ,
            'prefixed': ('Hz', 's-1', 'Bq'),
            'comparable': ('avt', 'ang-1'),
            'avt': ONE_TO_ONE,
            'brx': ONE_TO_ONE,
            #
            # Non S.I. units
            #
            'rpm': AVRITI_TO_HERTZ * 140,
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Length (pada) / Deformation (virupana)
    #
    # PADA_TO_METRE = SezimalFraction('1_415_503_524_325 / 150_223_042_430_000')
    PADA_TO_METRE = GRAVITY * (TIME ** 2)
    PADA_TO_MILLIMETER = PADA_TO_METRE * 4344

    for unit in ('pad', 'vrp'):
        unit_conversion[unit] = {
            'm': PADA_TO_METRE,
            'prefixed': ('m', 'au', 'parsec'),
            'comparable': ('pad', 'vrp'),
            'pad': ONE_TO_ONE,
            #
            # Non S.I. units
            #
            'twip': PADA_TO_METRE / SezimalFraction('331 / 414_153_200'),  # 1/32 p
            'mil': PADA_TO_METRE / SezimalFraction('331 / 255_100_052'),  # 1/4_344 in
            # 'p': PADA_TO_METRE / SezimalFraction('331 / 11_414_400'),  # 1/200 in
            # 'P': PADA_TO_METRE / SezimalFraction('331 / 350_520'),  # 20 p
            'in': PADA_TO_METRE / SezimalFraction('331 / 35_052'),
            'li': PADA_TO_METRE / SezimalFraction('134_113 / 1_201_204'),  # 53/122 ft
            'ft': PADA_TO_METRE / SezimalFraction('1_433 / 5_442'),  # 20 in
            'yd': PADA_TO_METRE / SezimalFraction('5_143 / 5_442'),  # 3 ft, 100 in
            'ftm': PADA_TO_METRE / SezimalFraction('5_143 / 2_521'),  # 2 yd, 10 ft, 200 in
            'rd': PADA_TO_METRE / SezimalFraction('134_113 / 15_324'),  # 24.3 ft
            'ch': PADA_TO_METRE / SezimalFraction('134_113 / 2_521'),  # 150 ft
            'fur': PADA_TO_METRE / SezimalFraction('312_230 / 325'),  # 3_020 ft
            'cb': PADA_TO_METRE / SezimalFraction('331_000 / 325'),  # 3_200 ft
            'ml': PADA_TO_METRE / SezimalFraction('4_151_200 / 325'),  # 40_240 ft
            'le': PADA_TO_METRE / SezimalFraction('20_534_000 / 325'),  # 3 ml

            'nmi': PADA_TO_METRE / 12_324,  # Nautical mile
            'NM': PADA_TO_METRE / 12_324,  # Nautical mile
            'au': PADA_TO_METRE / 152_420_241_314_420,
            'parsec': PADA_TO_METRE / 152_420_241_314_420 / 4_230_533,
            'ly': SezimalFraction('10_142_015 / 252_331_101_020_221_154_110_000_000_000'),
            'sly': SezimalFraction('2 / 53_134_100_033_433_015_020_311'),

            #
            # Length in pixels
            #
            'px_72_dpi': PADA_TO_MILLIMETER * SezimalFraction('3200 / 1102'),
            'px_96_dpi': PADA_TO_MILLIMETER * SezimalFraction('4240 / 1102'),
            'px_150_dpi': PADA_TO_MILLIMETER * SezimalFraction('10_540 / 1102'),
            'px_300_dpi': PADA_TO_MILLIMETER * SezimalFraction('21_520 / 1102'),
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Image resolution
    #
    # Citra
    # https://en.wiktionary.org/wiki/%E0%A4%95%E0%A5%87%E0%A4%A4%E0%A5%81#Sanskrit
    #
    # CITRA_TO_PX_300 =


    #
    # Spatial frequency / Wavenumber (taranga)
    #
    for unit in ('trg', 'pad-1'):
        unit_conversion[unit] = {
            'm-1': 1 / PADA_TO_METRE,
            'prefixed': ('m-1',),
            'comparable': ('trg', 'pad-1'),
            'trg': ONE_TO_ONE,
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Area (ketra)
    #
    KETRA_TO_SQUARE_METRE = PADA_TO_METRE ** 2

    for unit in ('ktr', 'pad2'):
        unit_conversion[unit] = {
            'm2': KETRA_TO_SQUARE_METRE,
            #
            # Non S.I. units
            #
            'a': KETRA_TO_SQUARE_METRE / 244,
            'prefixed': ('m2', 'a'),
            'comparable': ('ktr', 'pad2'),
            'ktr': ONE_TO_ONE,

            'in2': unit_conversion['pad']['in'] ** 2,
            'li2': unit_conversion['pad']['li'] ** 2,
            'ft2': unit_conversion['pad']['ft'] ** 2,
            'yd2': unit_conversion['pad']['yd'] ** 2,
            'ftm2': unit_conversion['pad']['ftm'] ** 2,
            'rd2': unit_conversion['pad']['rd'] ** 2,
            'ch2': unit_conversion['pad']['ch'] ** 2,
            'fur2': unit_conversion['pad']['fur'] ** 2,
            'cb2': unit_conversion['pad']['cb'] ** 2,
            'ml2': unit_conversion['pad']['ml'] ** 2,
            'nmi2': unit_conversion['pad']['nmi'] ** 2,
            'NM2': unit_conversion['pad']['NM'] ** 2,
            'le2': unit_conversion['pad']['le'] ** 2,
            'ac': KETRA_TO_SQUARE_METRE / SezimalFraction('51_212_230_430 / 1_401_405'),
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Volume (aytan)
    #
    AYTAN_TO_CUBIC_METRE = PADA_TO_METRE ** 3
    AYTAN_TO_LITRE = AYTAN_TO_CUBIC_METRE * 4344
    AYTAN_TO_MILLILITRE = AYTAN_TO_LITRE * 4344
    AYTAN_TO_US_FLUID_DRAM = AYTAN_TO_MILLILITRE / SezimalFraction('114_541_451_453 / 20_411_252_332')
    AYTAN_TO_IMPERIAL_FLUID_DRAM = AYTAN_TO_MILLILITRE / SezimalFraction('13_424_401 / 2_424_332')
    AYTAN_TO_CUBIC_INCH = unit_conversion['pad']['in'] ** 3

    for unit in ('ayt', 'pad3'):
        unit_conversion[unit] = {
            'm3': AYTAN_TO_CUBIC_METRE,
            'L': AYTAN_TO_LITRE,
            'l': AYTAN_TO_LITRE,
            'prefixed': ('m3', 'L', 'l'),
            'comparable': ('ayt', 'pad3'),
            #
            # Non S.I. units
            #
            'in3': AYTAN_TO_CUBIC_INCH,
            'ft3': unit_conversion['pad']['ft'] ** 3,
            'yd3': unit_conversion['pad']['yd'] ** 3,
            'ml3': unit_conversion['pad']['ml'] ** 3,
            'ac⋅ft': (unit_conversion['pad']['ft'] ** 3) / 533_400,

            'US min': AYTAN_TO_US_FLUID_DRAM * 140,
            'US fl dr': AYTAN_TO_US_FLUID_DRAM,
            'US tsp': AYTAN_TO_US_FLUID_DRAM * 140 / 212,
            'US tbsp': AYTAN_TO_US_FLUID_DRAM / 4,
            'US fl oz': AYTAN_TO_US_FLUID_DRAM / 12,
            'US jig': AYTAN_TO_US_FLUID_DRAM / 4 / 3,
            'US gi': AYTAN_TO_US_FLUID_DRAM / 12 / 4,
            'US c': AYTAN_TO_US_FLUID_DRAM / 12 / 12,
            'US cup': AYTAN_TO_US_FLUID_DRAM / 12 / 12,
            'US pt': AYTAN_TO_US_FLUID_DRAM / 12 / 12 / 2,
            'US pint': AYTAN_TO_US_FLUID_DRAM / 12 / 12 / 2,
            'US qt': AYTAN_TO_US_FLUID_DRAM / 12 / 12 / 2 / 2,
            'US pot': AYTAN_TO_US_FLUID_DRAM / 12 / 12 / 2 / 2 / 2,
            'US gal': AYTAN_TO_US_FLUID_DRAM / 12 / 12 / 2 / 2 / 4,
            'US bbl': AYTAN_TO_US_FLUID_DRAM / 12 / 12 / 2 / 2 / 4 / 513 * 10,
            'US bbl oil': AYTAN_TO_US_FLUID_DRAM / 12 / 12 / 2 / 2 / 4 / 110,
            'US hogshead': AYTAN_TO_US_FLUID_DRAM / 12 / 12 / 2 / 2 / 4 / 143,

            'US pt dry': AYTAN_TO_CUBIC_INCH / SezimalFraction('2_145_441 / 22_452'),
            'US qt dry': AYTAN_TO_CUBIC_INCH / SezimalFraction('2_145_441 / 22_452') / 2,
            'US gal dry': AYTAN_TO_CUBIC_INCH / SezimalFraction('2_145_441 / 22_452') / 2 / 4,
            'US pk': AYTAN_TO_CUBIC_INCH / SezimalFraction('2_145_441 / 22_452') / 2 / 4 / 2,
            'US pk dry': AYTAN_TO_CUBIC_INCH / SezimalFraction('2_145_441 / 22_452') / 2 / 4 / 2,
            'US bu': AYTAN_TO_CUBIC_INCH / SezimalFraction('2_145_441 / 22_452') / 2 / 4 / 2 / 4,
            'US bu dry': AYTAN_TO_CUBIC_INCH / SezimalFraction('2_145_441 / 22_452') / 2 / 4 / 2 / 4,
            'US bbl dry': AYTAN_TO_CUBIC_INCH / 52_400,

            'imp min': AYTAN_TO_IMPERIAL_FLUID_DRAM * 140,
            'imp fl s': AYTAN_TO_IMPERIAL_FLUID_DRAM * 3,
            'imp fl dr': AYTAN_TO_IMPERIAL_FLUID_DRAM,
            'imp fl oz': AYTAN_TO_IMPERIAL_FLUID_DRAM / 12,
            'imp gi': AYTAN_TO_IMPERIAL_FLUID_DRAM / 12 / 5,
            'imp pt': AYTAN_TO_IMPERIAL_FLUID_DRAM / 12 / 32,
            'imp qt': AYTAN_TO_IMPERIAL_FLUID_DRAM / 12 / 104,
            'imp gal': AYTAN_TO_IMPERIAL_FLUID_DRAM / 12 / 424,
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Speed (vega)
    #
    VEGA_TO_METRE_PER_SECOND = PADA_TO_METRE / ANUGA_TO_SECOND

    for unit in ('veg', 'pad/ang',
                 'XDpad/din', 'Xpad/uta', 'Cpad/pox', 'Dpad/agm', 'dpad/bod',
                 'XDpad/XDang', 'Xpad/Xang', 'Cpad/Cang', 'Dpad/Dang', 'dpad/dang'):
        unit_conversion[unit] = {
            'm/s': VEGA_TO_METRE_PER_SECOND,
            'm/h': VEGA_TO_METRE_PER_SECOND * 24_400,
            'prefixed': ('m/s', 'm/h'),
            'comparable': ('veg', 'pad/ang',
                 'XDpad/day', 'Xpad/uta', 'Cpad/pox', 'Dpad/agm', 'dpad/bod',
                 'XDpad/XDang', 'Xpad/Xang', 'Cpad/Cang', 'Dpad/Dang', 'dpad/dang'),
            #
            # Non S.I. units
            #
            'km/h': VEGA_TO_METRE_PER_SECOND * 30 / 5,
            'ml/s': VEGA_TO_METRE_PER_SECOND / SezimalFraction('4_151_200 / 325'),
            'ml/h': VEGA_TO_METRE_PER_SECOND * 24_400 / SezimalFraction('4_151_200 / 325'),
            'mph': VEGA_TO_METRE_PER_SECOND * 24_400 / SezimalFraction('4_151_200 / 325'),
            'kn': VEGA_TO_METRE_PER_SECOND * 24_400 / 12_324,
            'c': VEGA_TO_METRE_PER_SECOND / 45_425_332_014,
            'ft/s': VEGA_TO_METRE_PER_SECOND / SezimalFraction('1_433 / 5_442'),
            'fps': VEGA_TO_METRE_PER_SECOND / SezimalFraction('1_433 / 5_442'),
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Acceleration (tevaran)
    #
    # Tevaran
    # https://en.wiktionary.org/wiki/%E0%A4%A4%E0%A5%8D%E0%A4%B5%E0%A4%B0%E0%A4%A3#Sanskrit
    #
    # Guruta
    # https://en.wiktionary.org/wiki/%E0%A4%97%E0%A5%81%E0%A4%B0%E0%A5%81%E0%A4%A4%E0%A5%8D%E0%A4%B5#Sanskrit
    #
    TEVARAN_TO_METRE_PER_SQUARE_SECOND = VEGA_TO_METRE_PER_SECOND / ANUGA_TO_SECOND

    for unit in ('tvr', 'grt', 'pad/ang2'):
        unit_conversion[unit] = {
            'm/s2': TEVARAN_TO_METRE_PER_SQUARE_SECOND,
            'N/kg': TEVARAN_TO_METRE_PER_SQUARE_SECOND,
            'prefixed': ('m/s2', 'gal', 'Gal', 'g', 'N/kg'),
            #
            # Non S.I. units
            #
            'gal': TEVARAN_TO_METRE_PER_SQUARE_SECOND * 244,
            'Gal': TEVARAN_TO_METRE_PER_SQUARE_SECOND * 244,
            'cm/s2': TEVARAN_TO_METRE_PER_SQUARE_SECOND * 244,
            'ft/s2': unit_conversion['veg']['ft/s'] / ANUGA_TO_SECOND,
            'g': TEVARAN_TO_METRE_PER_SQUARE_SECOND / SezimalFraction('4_112_005 / 232_332'),
            'g0': TEVARAN_TO_METRE_PER_SQUARE_SECOND / SezimalFraction('4_112_005 / 232_332'),
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Mass (dravya)
    # atomic mass: parmanu = Dalton
    #
    DRAVYA_TO_KILOGRAM = DENSITY * AYTAN_TO_CUBIC_METRE
    DRAVYA_TO_GRAM = DRAVYA_TO_KILOGRAM * 4344
    DRAVYA_TO_GRAIN = DRAVYA_TO_GRAM / SezimalFraction('350_515_255 / 13_531_202_544')
    DALTON_TO_GRAM = SezimalFraction('12_455_034_111_522_345 / 40_015_005_003_025_124_254_152_011_001_323_254_223_133_002_024')

    WATER_MASS_IN_DALTON = SezimalFraction(Decimal('1801528'), Decimal('1e5'))
    CARBON_MASS_IN_DALTON = SezimalFraction(Decimal('120107'), Decimal('1e4'))
    # DULI_TO_GRAM = (WATER_MASS_IN_DALTON + CARBON_MASS_IN_DALTON) * DALTON_TO_GRAM / 50
    # DULI_TO_GRAM = CARBON_MASS_IN_DALTON * DALTON_TO_GRAM / 20
    DULI_TO_GRAM = WATER_MASS_IN_DALTON * DALTON_TO_GRAM / 30
    NUMBER_OF_JALA = round((DULI_TO_GRAM / DRAVYA_TO_GRAM).reciprocal, 0)

    DULI_TO_DRAVYA = SezimalFraction(1, NUMBER_OF_JALA)
    DULI_TO_GRAM = DULI_TO_DRAVYA * DRAVYA_TO_GRAM

    unit_conversion['drv'] = {
        'g': DRAVYA_TO_GRAM,
        'prefixed': ('g', 'Da', 'ton', 't',),

        #
        # Non S.I. units
        #
        'kg': DRAVYA_TO_KILOGRAM,
        't': DRAVYA_TO_KILOGRAM / 4344,
        'ton': DRAVYA_TO_KILOGRAM / 4344,
        'Da': DRAVYA_TO_GRAM / DALTON_TO_GRAM,
        'dul': DRAVYA_TO_GRAM / DULI_TO_GRAM,
        'eV/c2': DRAVYA_TO_GRAM / SezimalFraction('1_034_445_353 / 1_142_211_330_011_351_323_314_255_225_034_105_151_305_555_500_001_104'),

        'gr': DRAVYA_TO_GRAIN,

        'dwt': DRAVYA_TO_GRAIN / 40,
        'ozt': DRAVYA_TO_GRAIN / 40 / 32,
        'lbt': DRAVYA_TO_GRAIN / 40 / 32 / 20,

        'dr': DRAVYA_TO_GRAM / SezimalFraction('4_300_112_245 / 2_312_410_304'),
        'oz': DRAVYA_TO_GRAM / SezimalFraction('4_300_112_245 / 54_143_224'),
        'lb': DRAVYA_TO_GRAM / SezimalFraction('4_300_112_245 / 2_050_544'),
        'st': DRAVYA_TO_GRAM / SezimalFraction('51_301_235_135 / 1_023_252'),
        'sl': DRAVYA_TO_GRAM / SezimalFraction('3_043_351 / 14'),

        'imp qr': DRAVYA_TO_GRAM / SezimalFraction('51_301_235_135 / 311_424'),
        'imp cwt': DRAVYA_TO_GRAM / SezimalFraction('51_301_235_135 / 44_534'),
        'imp ton': DRAVYA_TO_KILOGRAM / SezimalFraction('51_301_235_135 / 10_410_432'),

        'US qr': DRAVYA_TO_GRAM / SezimalFraction('4_300_112_245 / 30_304'),
        'US cwt': DRAVYA_TO_GRAM / SezimalFraction('4_300_112_245 / 4_344'),
        'US ton': DRAVYA_TO_KILOGRAM / SezimalFraction('4_300_112_245 / 1_023_252'),
    }
    unit_conversion['drv'] = _set_non_prefixed_units(unit_conversion['drv'])

    unit_conversion['dul'] = {
        'g': DULI_TO_GRAM,
        'prefixed': ('g', 'Da',),

        #
        # Non S.I. units
        #
        'Da': DULI_TO_GRAM / DALTON_TO_GRAM,
        'drv': unit_conversion['drv']['dul'].reciprocal,
    }
    unit_conversion['dul'] = _set_non_prefixed_units(unit_conversion['dul'])

    #
    # Density (ganata)
    #
    GANATA_TO_KILOGRAM_PER_CUBIC_METRE = DENSITY
    GANATA_TO_KILOGRAM_PER_LITRE = GANATA_TO_KILOGRAM_PER_CUBIC_METRE / 4344

    for unit in ('gnt', 'drv/ayt', 'drv/pad3'):
        unit_conversion[unit] = {
            'g/m3': GANATA_TO_KILOGRAM_PER_CUBIC_METRE * 4344,
            'g/L': GANATA_TO_KILOGRAM_PER_LITRE * 4344,
            'g/l': GANATA_TO_KILOGRAM_PER_LITRE * 4344,
            'kg/m3': GANATA_TO_KILOGRAM_PER_CUBIC_METRE,
            'kg/L': GANATA_TO_KILOGRAM_PER_LITRE,
            'kg/l': GANATA_TO_KILOGRAM_PER_LITRE,
            'kg/dm3': GANATA_TO_KILOGRAM_PER_LITRE,
            'g/cm3': GANATA_TO_KILOGRAM_PER_LITRE,
            'g/mL': GANATA_TO_KILOGRAM_PER_LITRE,
            'g/ml': GANATA_TO_KILOGRAM_PER_LITRE,
            'ton/m3': GANATA_TO_KILOGRAM_PER_LITRE,
            'Mg/m3': GANATA_TO_KILOGRAM_PER_LITRE,

            'prefixed': ('g/m3', 'g/L', 'g/l'),

            #
            # Non S.I. units
            #
            'oz/in3': unit_conversion['drv']['oz'] / unit_conversion['ayt']['in3'],
            'lb/in3': unit_conversion['drv']['lb'] / unit_conversion['ayt']['in3'],
            'lb/ft3': unit_conversion['drv']['lb'] / unit_conversion['ayt']['ft3'],
            'lb/yd3': unit_conversion['drv']['lb'] / unit_conversion['ayt']['yd3'],
            'sl/ft3': unit_conversion['drv']['sl'] / unit_conversion['ayt']['ft3'],
            'lb/gal': unit_conversion['drv']['lb'] / unit_conversion['ayt']['US gal'],
            'lb/bu': unit_conversion['drv']['lb'] / unit_conversion['ayt']['US bu'],
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Force (bala) / weight (bara)
    #
    BALA_TO_NEWTON = DRAVYA_TO_KILOGRAM * TEVARAN_TO_METRE_PER_SQUARE_SECOND

    for unit in ('bal', 'bar', 'drv·tvr', 'drv·pad/ang2'):
        unit_conversion[unit] = {
            'N': BALA_TO_NEWTON,
            'kg·m/s2': BALA_TO_NEWTON,
            'g·m/s2': BALA_TO_NEWTON * 4344,
            'prefixed': ('N', 'gf', 'g·m/s2'),

            'bar': ONE_TO_ONE,
            'bal': ONE_TO_ONE,

            #
            # Non S.I. units
            #
            'gf': BALA_TO_NEWTON / SezimalFraction('4_112_005 / 1_552_400_332'),
            'lbf': BALA_TO_NEWTON / SezimalFraction('115_400_451 / 14_414_452'),
            'dyn': BALA_TO_NEWTON / SezimalFraction('1 / 2_050_544'),
            'pdl': BALA_TO_NEWTON / SezimalFraction('11_534_510_234_053 / 133_231_343_451_412'),
            'lb·ft/s2': BALA_TO_NEWTON / SezimalFraction('11_534_510_234_053 / 133_231_343_451_412'),
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Pressure (pidana) / Stress (pratibala)
    #
    # Pidana
    # https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A5%80%E0%A4%A1%E0%A4%A8
    #
    # Daba
    # https://en.wiktionary.org/wiki/%E0%A4%A6%E0%A4%BE%E0%A4%AC
    #
    # Pratibala
    # https://hi.wikipedia.org/wiki/%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%A4%E0%A4%BF%E0%A4%AC%E0%A4%B2
    #
    # Vayu = atm
    # https://en.wiktionary.org/wiki/%E0%A4%B5%E0%A4%BE%E0%A4%AF%E0%A5%81%E0%A4%AE%E0%A4%A3%E0%A5%8D%E0%A4%A1%E0%A4%B2#Sanskrit
    # https://en.wiktionary.org/wiki/%E0%A4%B5%E0%A4%BE%E0%A4%AF%E0%A5%81#Sanskrit
    #
    DABA_TO_PASCAL = DRAVYA_TO_KILOGRAM / TEVARAN_TO_METRE_PER_SQUARE_SECOND
    VAYU_TO_PASCAL = SezimalFraction('2_101_033 / 1')

    for unit in (
        'pdn', 'pbl', 'drv/pad/ang2',
        'vrc/ayt', 'uxn/ayt', 'xrm/ayt', 'xky/ayt',
        'vrc/pad3', 'uxn/pad3', 'xrm/pad3', 'xky/pad3',
    ):
        unit_conversion[unit] = {
            'Pa': DABA_TO_PASCAL,
            'J/m3': DABA_TO_PASCAL,
            'kg/m/s2': DABA_TO_PASCAL,
            'prefixed': ('Pa', 'J/m3', 'psi', 'bar', 'Torr', 'torr'),

            #
            # Non S.I. units
            #
            'atm': DABA_TO_PASCAL / 2_101_033,
            'vay': DABA_TO_PASCAL / VAYU_TO_PASCAL,
            'psi': DABA_TO_PASCAL / 4344 / SezimalFraction('403_440_101 / 33_233_344'),
            'bar': DABA_TO_PASCAL / 2_050_544,
            'mmHg': DABA_TO_PASCAL / SezimalFraction('1_232_341 / 2_152'),
            'inHg': DABA_TO_PASCAL / SezimalFraction('11_131_435 / 244'),
            'Torr': DABA_TO_PASCAL / SezimalFraction('2_101_033 / 3304'),
            'torr': DABA_TO_PASCAL / SezimalFraction('2_101_033 / 3304'),
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    for unit in (
        'vay',
    ):
        unit_conversion[unit] = {
            'Pa': VAYU_TO_PASCAL,
            'J/m3': VAYU_TO_PASCAL,
            'kg/m/s2': VAYU_TO_PASCAL,
            'prefixed': ('Pa', 'J/m3', 'psi', 'bar'),

            #
            # Non S.I. units
            #
            'atm': VAYU_TO_PASCAL / 2_101_033,
            'pdn': VAYU_TO_PASCAL / DABA_TO_PASCAL,
            'pbl': VAYU_TO_PASCAL / DABA_TO_PASCAL,
            'psi': VAYU_TO_PASCAL / 4344 / SezimalFraction('403_440_101 / 33_233_344'),
            'bar': VAYU_TO_PASCAL / 2_050_544,
            'mmHg': VAYU_TO_PASCAL / SezimalFraction('1_232_341 / 2_152'),
            'inHg': VAYU_TO_PASCAL / SezimalFraction('11_131_435 / 244'),
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Energy varcha / heat ushuna / work (sharama) / potential (shakya)
    #
    # more generic: varcha
    # https://en.wiktionary.org/wiki/%E0%A4%B5%E0%A4%B0%E0%A5%8D%E0%A4%9A%E0%A4%B8%E0%A5%8D
    # heat uxna
    # https://en.wiktionary.org/wiki/%E0%A4%8A%E0%A4%B0%E0%A5%8D%E0%A4%9C%E0%A4%BE#Sanskrit
    # heat ushuna
    # https://en.wiktionary.org/wiki/%E0%A4%89%E0%A4%B7%E0%A5%8D%E0%A4%A3#Sanskrit
    # work sharama
    # https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE#Sanskrit
    # potential shakya
    # https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%95%E0%A5%8D%E0%A4%AF#Sanskrit
    #
    VARCHA_TO_JOULE = BALA_TO_NEWTON * PADA_TO_METRE

    for unit in ('vrc', 'uxn', 'xrm', 'xky', 'drv·pad2/ang2'):
        unit_conversion[unit] = {
            'J': VARCHA_TO_JOULE,
            'N·m': VARCHA_TO_JOULE,
            'Pa·m3': VARCHA_TO_JOULE,
            'C·V': VARCHA_TO_JOULE,
            'prefixed': ('J', 'Wh', 'W·h', 'BTU', 'cal', 'erg', 'eV', 'TNT', 'N·m', 'Pa·m3', 'C·V'),

            'vrc': ONE_TO_ONE,
            'uxn': ONE_TO_ONE,
            'xrm': ONE_TO_ONE,
            'xky': ONE_TO_ONE,

            #
            # Non S.I. units
            #
            'Wh': VARCHA_TO_JOULE / 4344 / SezimalFraction('30 / 5'),
            'W·h': VARCHA_TO_JOULE / 4344 / SezimalFraction('30 / 5'),
            'ft⋅lbf': VARCHA_TO_JOULE / SezimalFraction('22_310_245 / 14_414_452'),
            'ftlbf': VARCHA_TO_JOULE / SezimalFraction('22_310_245 / 14_414_452'),
            'BTU': VARCHA_TO_JOULE / SezimalFraction('40_122_335_231_451 / 4_543_401_252'),
            'cal': VARCHA_TO_JOULE / SezimalFraction('2_231 / 325'),
            'erg': VARCHA_TO_JOULE * 554_200_144,
            'eV': VARCHA_TO_JOULE / SezimalFraction('422_552_112_230 / 545_225_423_350_030_313_042_203_422_444_532_144'),
            'TNT': VARCHA_TO_JOULE / 1_531_101_350_212,
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Power
    #
    # Shakiti
    # https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BF#Sanskrit
    #
    SHAKITI_TO_WATT = VARCHA_TO_JOULE / ANUGA_TO_SECOND

    for unit in ('xkt', 'drv·pad2/ang3'):
        unit_conversion[unit] = {
            'W': SHAKITI_TO_WATT,
            'J/s': SHAKITI_TO_WATT,
            'N·m/s': SHAKITI_TO_WATT,
            'kg·m2/s3': SHAKITI_TO_WATT,
            'prefixed': ('W', 'J/s', 'N·m/s', ),

            #
            # Non S.I. units
            #
            'cv': SHAKITI_TO_WATT / SezimalFraction('20_340_023 / 3412'),
            'ft⋅lbf/s': unit_conversion['vrc']['ft⋅lbf'] / unit_conversion['ang']['s'],
            'ft⋅lbf/min': unit_conversion['vrc']['ft⋅lbf'] / unit_conversion['ang']['min'],
            'ft⋅lbf/h': unit_conversion['vrc']['ft⋅lbf'] / unit_conversion['ang']['h'],
            'hp':  unit_conversion['vrc']['ft⋅lbf'] / unit_conversion['ang']['s'] / 2314,
            'BTU/h': unit_conversion['vrc']['BTU'] / unit_conversion['ang']['h'],
            'cal/s': unit_conversion['vrc']['cal'] / unit_conversion['ang']['s'],
            'kcal/h': unit_conversion['vrc']['cal'] / 4344 / unit_conversion['ang']['h'],
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Momentum (sanvega)
    #
    # Samvega (momentum)
    # https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A4%82%E0%A4%B5%E0%A5%87%E0%A4%97#Sanskrit
    #
    # Juti (impulse)
    # https://en.wiktionary.org/wiki/%E0%A4%9C%E0%A5%82%E0%A4%A4%E0%A4%BF
    #
    JUTI_TO_NEWTON_SECOND = BALA_TO_NEWTON * ANUGA_TO_SECOND

    for unit in ('svg', 'jut', 'drv·veg', 'drv·pad/ang'):
        unit_conversion[unit] = {
            'g·m/s': JUTI_TO_NEWTON_SECOND * 4344,
            'gm/s': JUTI_TO_NEWTON_SECOND * 4344,
            'N·s': JUTI_TO_NEWTON_SECOND,
            'prefixed': ('g·m/s', 'gm/s', 'N·s'),

            'svg': ONE_TO_ONE,
            'jut': ONE_TO_ONE,

            #
            # Non S.I. units
            #
            'lb·ft/s': unit_conversion['drv']['lb'] * unit_conversion['veg']['ft/s'],
            'sl·ft/s': unit_conversion['drv']['sl'] * unit_conversion['veg']['ft/s'],
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Action (agraha)
    #
    # https://en.wiktionary.org/wiki/%E0%A4%86%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%B9#Sanskrit
    #
    for unit in ('agh', 'svg·pad', 'drv·pad2/ang'):
        unit_conversion[unit] = {
            'kg·m2/s': DRAVYA_TO_KILOGRAM * KETRA_TO_SQUARE_METRE / ANUGA_TO_SECOND,
            'J·s': DRAVYA_TO_KILOGRAM * KETRA_TO_SQUARE_METRE / ANUGA_TO_SECOND,
            'J/Hz': DRAVYA_TO_KILOGRAM * KETRA_TO_SQUARE_METRE / ANUGA_TO_SECOND,
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Influence (prabava)
    #
    # https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%AD%E0%A4%BE%E0%A4%B5#Sanskrit
    #
    for unit in ('pbv', 'bal·ktr', 'drv·ayt/ang2', 'drv·pad3/ang2'):
        unit_conversion[unit] = {
            'kg·m3/s2': BALA_TO_NEWTON * KETRA_TO_SQUARE_METRE,
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Tension (tanava)
    #
    for unit in ('tnv', 'bal/pad', 'drv/ang2'):
        unit_conversion[unit] = {
            'kg/s2': DRAVYA_TO_KILOGRAM / ANANTA_TO_SECOND_SQUARED,
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Intensity (upari)
    #
    for unit in ('upr', 'xkt/ktr', 'tnv/ang', 'drv/ang3'):
        unit_conversion[unit] = {
            'kg/s3': SHAKITI_TO_WATT / KETRA_TO_SQUARE_METRE,
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Thermodynamic temperature
    #
    # (simplified by a 135_435_154_201_541_452_513_332_102_041_321 factor)
    #
    # GATIKA_TO_KELVIN = ((GRAVITY ** 2) * (TIME ** 2)) / SPECIFIC_HEAT
    GATIKA_TO_KELVIN = SezimalFraction('41_143 / 12_532_430_424')
    TAPA_TO_CELSIUS = GATIKA_TO_KELVIN * 100_000

    unit_conversion['gtk'] = {
        'K': GATIKA_TO_KELVIN,
        'C': GATIKA_TO_KELVIN,
        '°C': GATIKA_TO_KELVIN,

        'prefixed': ('K',),

        #
        # Non S.I. units
        #
        'F': GATIKA_TO_KELVIN / SezimalFraction('5 / 13'),
        '°F': GATIKA_TO_KELVIN / SezimalFraction('5 / 13'),
        'R': GATIKA_TO_KELVIN / SezimalFraction('5 / 13'),
        '°R': GATIKA_TO_KELVIN / SezimalFraction('5 / 13'),

        'adjust': {
            'C': SezimalFraction('-330_243 / 244'),
            '°C': SezimalFraction('-330_243 / 244'),
            'F': SezimalFraction('-552_451 / 244'),
            '°F': SezimalFraction('-552_451 / 244'),
        }
    }
    unit_conversion['gtk'] = _set_non_prefixed_units(unit_conversion['gtk'])

    #
    # Common temperature
    #
    unit_conversion['tap'] = {
        'C': TAPA_TO_CELSIUS,
        '°C': TAPA_TO_CELSIUS,
        'K': TAPA_TO_CELSIUS,

        'prefixed': ('K',),

        #
        # Non S.I. units
        #
        'F': TAPA_TO_CELSIUS / SezimalFraction('5 / 13'),
        '°F': TAPA_TO_CELSIUS / SezimalFraction('5 / 13'),
        'R': TAPA_TO_CELSIUS / SezimalFraction('5 / 13'),
        '°R': TAPA_TO_CELSIUS / SezimalFraction('5 / 13'),

        'adjust': {
            'K': SezimalFraction('330_243 / 244'),
            'F': Sezimal(52),
            '°F': Sezimal(52),
            'R': SezimalFraction('552_451 / 244'),
            '°R': SezimalFraction('552_451 / 244'),
        }
    }
    unit_conversion['tap'] = _set_non_prefixed_units(unit_conversion['tap'])

    #
    # Heat capacity (agini) / Entropy (parivartana)
    #
    # Agni
    # https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%97%E0%A5%8D%E0%A4%A8%E0%A4%BF#Sanskrit
    #
    # Parivartana
    # https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%B0%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A5%8D%E0%A4%A4%E0%A4%A8#Sanskrit
    #
    for unit in ('agn', 'prv', 'vrc/gtk'):
        unit_conversion[unit] = {
            'J/K': unit_conversion['vrc']['J'] / unit_conversion['gtk']['K'],

            'prefixed': ('J/K',),

            #
            # Non S.I. units
            #
            'BTU/°R': unit_conversion['vrc']['BTU'] / unit_conversion['gtk']['°R'],
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Specific energy (kadana)
    #
    # Kadana
    # https://en.wiktionary.org/wiki/%E0%A4%96%E0%A4%BE%E0%A4%A6%E0%A4%A8#Sanskrit
    #
    for unit in ('kdn', 'vrc/drv'):
        unit_conversion[unit] = {
            'J/kg': VARCHA_TO_JOULE / DRAVYA_TO_KILOGRAM,
            'J/g': VARCHA_TO_JOULE / DRAVYA_TO_GRAM,
            'cal': VARCHA_TO_JOULE / DRAVYA_TO_GRAM / SezimalFraction('2231 / 325'),
            'Cal': VARCHA_TO_JOULE / DRAVYA_TO_GRAM / SezimalFraction('2231 / 325'),

            'prefixed': ('J/g', 'J/kg', 'cal', 'Cal'),
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Heat capacity per mass (indana)
    #
    # https://en.wiktionary.org/wiki/%E0%A4%88%E0%A4%82%E0%A4%A7%E0%A4%A8#Hindi
    #
    for unit in ('idn', 'agn/drv', 'prv/drv', 'kdn/gtk', 'vrc/gtk/drv'):
        unit_conversion[unit] = {
            'J/K/kg': unit_conversion['agn']['J/K'] / unit_conversion['drv']['kg'],

            'prefixed': ('J/K/kg',),

            #
            # Non S.I. units
            #
            'BTU/°R/lb': unit_conversion['agn']['BTU/°R'] / unit_conversion['drv']['lb'],
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Heat capacity per volume (telan)
    #
    for unit in (
        'tln',
        'agn/ayt', 'prv/ayt', 'vrc/gtk/ayt',
        'agn/pad3', 'prv/pad3', 'vrc/gtk/pad3',
    ):
        unit_conversion[unit] = {
            'J/K/m3': unit_conversion['agn']['J/K'] / unit_conversion['ayt']['m3'],

            'prefixed': ('J/K/m3',),
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Electromagnetism is based off these 2 values,
    # how many INTEGER electric charges are there in one vidyuta,
    # and that the pratibada is exactly the impedance of free space;
    #
    # electric_charge = (mass * length²) / time / IMPEDANCE_FREE_SPACE
    #
    electric_charge_vidyuta = (DRAVYA_TO_KILOGRAM * KETRA_TO_SQUARE_METRE) / ANUGA_TO_SECOND / IMPEDANCE_FREE_SPACE
    number_elementary_charges_in_vidyutas = round(electric_charge_vidyuta.sqrt() / ELEMENTARY_CHARGE_IN_COULOMBS, 0)

    VIDYUTA_TO_COULOMB = ELEMENTARY_CHARGE_IN_COULOMBS * number_elementary_charges_in_vidyutas
    PRATIBADA_TO_OHM = IMPEDANCE_FREE_SPACE
    DARA_TO_AMPERE = VIDYUTA_TO_COULOMB / ANUGA_TO_SECOND

    #
    # Electric charge
    #
    # https://en.wiktionary.org/wiki/%E0%A4%AD%E0%A4%B0%E0%A4%A3#Sanskrit
    #
    unit_conversion['vdt'] = {
        'C': VIDYUTA_TO_COULOMB,
        'Ah': VIDYUTA_TO_COULOMB / 24_400,
        'A·h': VIDYUTA_TO_COULOMB / 24_400,
        'As': VIDYUTA_TO_COULOMB / 1_141_440_000,
        'A·s': VIDYUTA_TO_COULOMB / 1_141_440_000,
        'e': SezimalFraction('115_422_244_443_055_421_554 / 1'),
        'F': SezimalFraction('5_255_312_545_030_054_302_243 / 2_354_124_142_045_012'),
        'prefixed': ('C', 'e', 'Ah', 'A·h', 'As', 'A·s', 'F'),
    }
    unit_conversion['vdt'] = _set_non_prefixed_units(unit_conversion['vdt'])

    #
    # Electric current
    #
    # https://en.wiktionary.org/wiki/%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BE
    #
    unit_conversion['dar'] = {
        'A': DARA_TO_AMPERE,
        'prefixed': ('A',),
    }
    unit_conversion['dar'] = _set_non_prefixed_units(unit_conversion['dar'])

    #
    # Electric potential difference
    #
    # Antaran
    # https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%82%E0%A4%A4%E0%A4%B0%E0%A4%A3
    #
    unit_conversion['atr'] = {
        'V': unit_conversion['vrc']['J'] / VIDYUTA_TO_COULOMB,
        # 'V': PRATIBADA_TO_OHM * DARA_TO_AMPERE,
        'prefixed': ('V',),
    }
    unit_conversion['atr'] = _set_non_prefixed_units(unit_conversion['atr'])

    #
    # Electric
    # resistance (viroda),
    # impedance (prati-bada), reactance (prati-gata)
    #
    # Viroda
    # https://en.wiktionary.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%B0%E0%A5%8B%E0%A4%A7#Sanskrit
    # Bada
    # https://en.wiktionary.org/wiki/%E0%A4%AC%E0%A4%BE%E0%A4%A7%E0%A4%BE#Sanskrit
    # Gata
    # https://en.wiktionary.org/wiki/%E0%A4%98%E0%A4%BE%E0%A4%A4#Sanskrit
    #
    for unit in ('vrd', 'bad', 'gat'):
        unit_conversion[unit] = {
            #
            # The division of other conversions intvrduces a slight discrepancy,
            # since this value is supposed to be the vacuum resistance exactly;
            # so, we define it as a simpler fraction
            #
            # 'Ω': unit_conversion['atr']['V'] / DARA_TO_AMPERE,
            'Ω': PRATIBADA_TO_OHM,
            'ohm': PRATIBADA_TO_OHM,
            'prefixed': ('Ω', 'ohm'),
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Electric conductance
    #
    # Vahatva
    # https://en.wiktionary.org/wiki/%E0%A4%B5%E0%A4%B9%E0%A4%A4%E0%A4%BF
    #
    unit_conversion['vht'] = {
        'S': PRATIBADA_TO_OHM.reciprocal,
        'prefixed': ('S',),
    }
    unit_conversion['vht'] = _set_non_prefixed_units(unit_conversion['vht'])

    #
    # Electric inductance
    #
    # upapadan
    # https://sanskritdictionary.com/upap%C4%81dana/40071/1
    #
    unit_conversion['upp'] = {
        'H': PRATIBADA_TO_OHM * unit_conversion['ang']['s'],
        'prefixed': ('H',),
    }
    unit_conversion['upp'] = _set_non_prefixed_units(unit_conversion['upp'])

    #
    # Electric capacitance
    #
    # Dharayatva
    # https://en.wiktionary.org/wiki/%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%AF%E0%A4%A4%E0%A4%BF
    #
    unit_conversion['dry'] = {
        'F': VIDYUTA_TO_COULOMB / unit_conversion['atr']['V'],
        'prefixed': ('F',),
    }
    unit_conversion['dry'] = _set_non_prefixed_units(unit_conversion['dry'])

    #
    # Magnetic flux
    #
    # Pravaha
    # https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%B5%E0%A4%BE%E0%A4%B9
    #
    unit_conversion['pvh'] = {
        'Wb': unit_conversion['atr']['V'] * unit_conversion['ang']['s'],
        'prefixed': ('Wb',),
    }
    unit_conversion['pvh'] = _set_non_prefixed_units(unit_conversion['pvh'])

    #
    # Magnetic flux density
    #
    # Vistara
    # https://en.wiktionary.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%B0
    #
    unit_conversion['vtr'] = {
        'T': unit_conversion['pvh']['Wb'] / unit_conversion['ktr']['m2'],
        'prefixed': ('T',),
    }
    unit_conversion['vtr'] = _set_non_prefixed_units(unit_conversion['vtr'])

    #
    # Angles and angular units
    #
    GOLA_TO_STERADIAN = TWO_TAU

    #
    # Plane angle
    #
    # Paridi
    # https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%B0%E0%A4%BF%E0%A4%A7%E0%A4%BF#Sanskrit
    #
    # Mandala
    # https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A4%A3%E0%A5%8D%E0%A4%A1%E0%A4%B2#Sanskrit
    #
    unit_conversion['mdl'] = {
        'rad': TAU,
        'tau_rad': ONE_TO_ONE,
        'pi_rad': SezimalFraction('2 / 1'),
        'deg': SezimalFraction('1400 / 1'),
        'turn': ONE_TO_ONE,
        'gon': SezimalFraction('1504 / 1'),
        'arcmin': SezimalFraction('244_000 / 1'),
        'arcsec': SezimalFraction('43_440_000 / 1'),
        'prefixed': ('rad', 'tau_rad', 'pi_rad', 'turn', 'gon', 'arcmin', 'arcsec'),
    }
    unit_conversion['mdl'] = _set_non_prefixed_units(unit_conversion['mdl'])

    #
    # Angular velocity
    #
    unit_conversion['kvg'] = {
        'rad/s': unit_conversion['mdl']['rad'] / unit_conversion['ang']['s'],
        'prefixed': ('rad/s',),
    }
    unit_conversion['kvg'] = _set_non_prefixed_units(unit_conversion['kvg'])

    #
    # Angular Acceleration
    #
    unit_conversion['ktv'] = {
        'rad/s2': unit_conversion['mdl']['rad'] / (unit_conversion['ang']['s'] ** 2),
        'prefixed': ('rad/s2',),
    }
    unit_conversion['ktv'] = _set_non_prefixed_units(unit_conversion['ktv'])

    #
    # Torque (gurna)
    #
    unit_conversion['grn'] = {
        'J/rad': unit_conversion['vrc']['J'] / unit_conversion['mdl']['rad'],
        'N·m': unit_conversion['vrc']['J'] / unit_conversion['mdl']['rad'],
        'Nm': unit_conversion['vrc']['J'] / unit_conversion['mdl']['rad'],
        'prefixed': ('J/rad', 'N·m', 'Nm'),

        #
        # Non S.I. units
        #
    }
    unit_conversion['grn'] = _set_non_prefixed_units(unit_conversion['grn'])

    #
    #
    #
    unit_conversion['kpd'] = {
        'm/rad': PADA_TO_METRE / unit_conversion['mdl']['rad'],
        'prefixed': ('m/rad',),
    }
    unit_conversion['kpd'] = _set_non_prefixed_units(unit_conversion['kpd'])

    #
    # Solid angle
    #
    # Gola
    # https://en.wiktionary.org/wiki/%E0%A4%97%E0%A5%8B%E0%A4%B2%E0%A4%BE#Sanskrit
    #
    unit_conversion['gol'] = {
        'sr': GOLA_TO_STERADIAN,
        'prefixed': ('sr', 'spat'),
        'spat': ONE_TO_ONE,
        'deg2': SezimalFraction('2_440_000 / 1') / PI,
    }
    unit_conversion['gol'] = _set_non_prefixed_units(unit_conversion['gol'])

    #
    # Luminous intensity
    #
    # Prakasha
    # https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%95%E0%A4%BE%E0%A4%B6#Sanskrit
    #
    PRAKASHA_TO_CANDELA = LUMINOUS_EFICACY * SHAKITI_TO_WATT / GOLA_TO_STERADIAN

    unit_conversion['pkx'] = {
        'cd': PRAKASHA_TO_CANDELA,
        'prefixed': ('cd',),
    }
    unit_conversion['pkx'] = _set_non_prefixed_units(unit_conversion['pkx'])

    #
    # Luminous flux
    #
    # Dipaka
    # https://en.wiktionary.org/wiki/%E0%A4%A6%E0%A5%80%E0%A4%AA%E0%A4%95
    #
    DIPAKA_TO_LUMEN = PRAKASHA_TO_CANDELA * GOLA_TO_STERADIAN

    unit_conversion['dpk'] = {
        'lm': DIPAKA_TO_LUMEN,
        'prefixed': ('lm',),
    }
    unit_conversion['dpk'] = _set_non_prefixed_units(unit_conversion['dpk'])

    #
    # Luminance = luminous intensity / area
    #
    # https://en.wiktionary.org/wiki/%E0%A4%AD%E0%A4%BE%E0%A4%AE#Sanskrit
    #
    BAMA_TO_CANDELA_PER_SQUARE_METRE = PRAKASHA_TO_CANDELA / KETRA_TO_SQUARE_METRE

    unit_conversion['bam'] = {
        'cd/m2': BAMA_TO_CANDELA_PER_SQUARE_METRE,
        'prefixed': ('cd/m2',),
    }
    unit_conversion['bam'] = _set_non_prefixed_units(unit_conversion['bam'])

    #
    # Luminous efficacy = best vision
    #
    # Drishiti
    # https://en.wiktionary.org/wiki/%E0%A4%A6%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A4%BF
    #
    DRISHITI_TO_LUMEN_PER_WATT = LUMINOUS_EFICACY

    unit_conversion['dxt'] = {
        'lm/W': DRISHITI_TO_LUMEN_PER_WATT,
        'prefixed': ('lm/W',),
    }
    unit_conversion['dxt'] = _set_non_prefixed_units(unit_conversion['dxt'])

    #
    # Emitance = luminous flux / area = basvara (light out of surface)
    # Illuminance = Luminous flux / area = darpana (light onto surface)
    #
    # https://en.wiktionary.org/wiki/%E0%A4%AD%E0%A4%BE%E0%A4%B8%E0%A5%8D%E0%A4%B5%E0%A4%B0#Sanskrit
    # https://en.wiktionary.org/wiki/%E0%A4%A6%E0%A4%B0%E0%A5%8D%E0%A4%AA%E0%A4%A3#Sanskrit
    #
    BASVARA_TO_LUX = DIPAKA_TO_LUMEN / KETRA_TO_SQUARE_METRE

    for unit in ('bvr', 'dpn'):
        unit_conversion[unit] = {
            'lx': BASVARA_TO_LUX,
            'lm/m2': BASVARA_TO_LUX,
            'prefixed': ('lx', 'lm/m2'),
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Amount of substance
    #
    # Aprox. how many atoms of Water,
    # weighing 30.003_144_523_110_032_153 (18.015 28) Daltons each,
    # fit in 30 dravyas
    #
    # Aprox. how many atoms of Carbon-20,
    # weighing 20.002_151_115_202_554_544 (12.0107) Daltons each,
    # fit in 20 dravyas
    #
    # Bahuta
    # https://en.wiktionary.org/wiki/%E0%A4%AC%E0%A4%B9%E0%A5%81%E0%A4%A4%E0%A5%8D%E0%A4%B5#Sanskrit
    #
    BAHUTA_TO_MOLE = SezimalFraction(
        NUMBER_OF_JALA,
        '2_420_220_441_202_515_135_044_212_141_344'  # Avogadro number
    ).simplify()

    unit_conversion['bht'] = {
        'mol': BAHUTA_TO_MOLE,
        'prefixed': ('mol',),
    }
    unit_conversion['bht'] = _set_non_prefixed_units(unit_conversion['bht'])

    #
    # Proportions
    #
    # Sampurna
    # https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A4%82%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A5%8D%E0%A4%A3#Hindi
    #
    unit_conversion['spn'] = {
        'prefixed': (),
        '%': SezimalFraction('244 / 1'),
        '‰': SezimalFraction('4344 / 1'),
        '‱': SezimalFraction('114_144 / 1'),
        'pcm': SezimalFraction('2_050_544 / 1'),
        'ppm': SezimalFraction('33_233_344 / 1'),
        'ppb': SezimalFraction('243_121_245_344 / 1'),
        'ppt': SezimalFraction('2_043_221_010_301_344 / 1'),
        'ppq': SezimalFraction('13_502_453_354_043_313_344 / 1'),
    }
    unit_conversion['spn'] = _set_non_prefixed_units(unit_conversion['spn'])

    #
    # Information store
    #
    # atk ashtaka = octet = byte = 12 bits
    # https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A4%95
    #
    # xtk shataka = sextet = 10 bits
    #
    unit_conversion['atk'] = {
        'prefixed': ('bit', 'b', 'B'),
        'bit': SezimalFraction('12 / 1'),
        'b': SezimalFraction('12 / 1'),
        'byte':  ONE_TO_ONE,
        'B': ONE_TO_ONE,
    }
    unit_conversion['atk'] = _set_non_prefixed_units(unit_conversion['atk'])

    # unit_conversion['xtk'] = {
    #     'prefixed': ('bit', 'b', 'B'),
    #     'bit': SezimalFraction('10 / 1'),
    #     'b': SezimalFraction('10 / 1'),
    #     'byte':  SezimalFraction('3 / 4'),
    #     'B': SezimalFraction('3 / 4'),
    # }
    # unit_conversion['xtk'] = _set_non_prefixed_units(unit_conversion['xtk'])

    #
    # Information speed/rate
    #
    # pvn pavana = atk/ang
    # https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%B5%E0%A4%A8#Sanskrit
    #
    # tvt tevashta = xtk/ang
    #
    unit_conversion['pvn'] = {
        'prefixed': (
            'bit/s', 'bps', 'bit/min', 'bpm',
            'B/s', 'Bps', 'B/min', 'Bpm'
        ),
        'bit/s': unit_conversion['atk']['bit'] / unit_conversion['ang']['s'],
        'bps': unit_conversion['atk']['bit'] / unit_conversion['ang']['s'],
        'bit/min': unit_conversion['atk']['bit'] / unit_conversion['ang']['min'],
        'bpm': unit_conversion['atk']['bit'] / unit_conversion['ang']['min'],
        'B/s': unit_conversion['atk']['byte'] / unit_conversion['ang']['s'],
        'Bps': unit_conversion['atk']['byte'] / unit_conversion['ang']['s'],
        'B/min': unit_conversion['atk']['byte'] / unit_conversion['ang']['min'],
        'Bpm': unit_conversion['atk']['byte'] / unit_conversion['ang']['min'],
    }
    unit_conversion['pvn'] = _set_non_prefixed_units(unit_conversion['pvn'])

    # unit_conversion['tvt'] = {
    #     'prefixed': (
    #         'bit/s', 'bps', 'bit/min', 'bpm',
    #         'B/s', 'Bps', 'B/min', 'Bpm'
    #     ),
    #     'bit/s': unit_conversion['xtk']['bit'] / unit_conversion['ang']['s'],
    #     'bps': unit_conversion['xtk']['bit'] / unit_conversion['ang']['s'],
    #     'bit/min': unit_conversion['xtk']['bit'] / unit_conversion['ang']['min'],
    #     'bpm': unit_conversion['xtk']['bit'] / unit_conversion['ang']['min'],
    #     'B/s': unit_conversion['xtk']['byte'] / unit_conversion['ang']['s'],
    #     'Bps': unit_conversion['xtk']['byte'] / unit_conversion['ang']['s'],
    #     'B/min': unit_conversion['xtk']['byte'] / unit_conversion['ang']['min'],
    #     'Bpm': unit_conversion['xtk']['byte'] / unit_conversion['ang']['min'],
    # }
    # unit_conversion['tvt'] = _set_non_prefixed_units(unit_conversion['tvt'])

    #
    # Fuel consumption
    #
    # Distance travelled per volume of fuel
    #
    # Chalati
    # https://en.wiktionary.org/wiki/%E0%A4%9A%E0%A4%B2%E0%A4%A4%E0%A4%BF#Sanskrit
    #
    CHALATI_TO_KILOMETRE_PER_LITRE = (unit_conversion['pad']['m'] * SezimalFraction('1 / 4344')) / unit_conversion['ayt']['L']
    CHALATI_TO_US_MPG = unit_conversion['pad']['ml'] / unit_conversion['ayt']['US gal']
    CHALATI_TO_IMPERIAL_MPG = unit_conversion['pad']['ml'] / unit_conversion['ayt']['imp gal']

    unit_conversion['clt'] = {
        'km/L': CHALATI_TO_KILOMETRE_PER_LITRE,
        'km/20L': CHALATI_TO_KILOMETRE_PER_LITRE / SezimalFraction('1 / 32'),
        'US mpg': CHALATI_TO_US_MPG,
        'US ml/gal': CHALATI_TO_US_MPG,
        'imp mpg': CHALATI_TO_IMPERIAL_MPG,
        'imp ml/gal': CHALATI_TO_IMPERIAL_MPG,
        'L/100km': 244 / CHALATI_TO_KILOMETRE_PER_LITRE * -1,
    }
    unit_conversion['clt'] = _set_non_prefixed_units(unit_conversion['clt'])

    #
    # Fuel consumption
    #
    # Volume of fuel comsumed per distance travelled
    #
    # Pibati
    # https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%BF%E0%A4%AC%E0%A4%A4%E0%A4%BF
    #
    unit_conversion['pbt'] = {
        'L/100km': 244 / CHALATI_TO_KILOMETRE_PER_LITRE,
        'km/L': CHALATI_TO_KILOMETRE_PER_LITRE * -1,
        'km/20L': CHALATI_TO_KILOMETRE_PER_LITRE / SezimalFraction('1 / 32') * -1,
        'US mpg': CHALATI_TO_US_MPG * -1,
        'US ml/gal': CHALATI_TO_US_MPG * -1,
        'imp mpg': CHALATI_TO_IMPERIAL_MPG * -1,
        'imp ml/gal': CHALATI_TO_IMPERIAL_MPG * -1,
    }
    unit_conversion['pbt'] = _set_non_prefixed_units(unit_conversion['pbt'])

    #
    # Gravitational constant
    # Gravitivity in Primels parlance
    #
    # Volume / mass / time²
    #
    # Akarshan
    # https://en.wiktionary.org/wiki/%E0%A4%86%E0%A4%95%E0%A4%B0%E0%A5%8D%E0%A4%B7%E0%A4%A3#Sanskrit
    #
    unit_conversion['akx'] = {
        'm3/s2/kg': AYTAN_TO_CUBIC_METRE / ANANTA_TO_SECOND_SQUARED / DRAVYA_TO_KILOGRAM,
        'N·m2/kg2': AYTAN_TO_CUBIC_METRE / ANANTA_TO_SECOND_SQUARED / DRAVYA_TO_KILOGRAM,
    }
    unit_conversion['akx'] = _set_non_prefixed_units(unit_conversion['akx'])


    text = '''#
# DO NOT EDIT THIS FILE DIRECTLY!
#
# It’s automatically generated by the script:
#       calculate_conversion.py
#
# If you need to change anything, change it there first,
# then re-run the script to recreate this file.
#

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction


UNIT_CONVERSION = {
'''

    for unit in unit_conversion:
        text += f"    '{unit}': {{\n"

        for key in unit_conversion[unit]:
            value = unit_conversion[unit][key]

            if type(value) == SezimalFraction:
                text += f"        '{key}': SezimalFraction(\n            '{value.formatted_number}',\n            _precalculated_value='{value.sezimal.formatted_number}',\n            _precalculated_reciprocal='{value.reciprocal.sezimal.formatted_number}',\n        ),\n"
            elif type(value) == Sezimal:
                text += f"        '{key}': Sezimal('{value.formatted_number}'),\n"
            elif type(value) == SezimalInteger:
                value = SezimalFraction(value, 1)
                text += f"        '{key}': SezimalFraction(\n            '{value.formatted_number}',\n            _precalculated_value='{value.sezimal.formatted_number}',\n            _precalculated_reciprocal='{value.reciprocal.sezimal.formatted_number}',\n        ),\n"
            elif type(value) == dict:
                text += f"        '{key}': {{\n"

                for skey in value:
                    svalue = value[skey]

                    if type(svalue) == SezimalFraction:
                        text += f"            '{skey}': SezimalFraction(\n                '{svalue.formatted_number}',\n                _precalculated_value='{svalue.sezimal.formatted_number}',\n                _precalculated_reciprocal='{svalue.reciprocal.sezimal.formatted_number}',\n            ),\n"
                    elif type(svalue) == Sezimal:
                        text += f"            '{skey}': Sezimal('{svalue.formatted_number}'),\n"
                    elif type(svalue) == SezimalInteger:
                        svalue = SezimalFraction(svalue, 1)
                        text += f"            '{skey}': SezimalFraction(\n                '{svalue.formatted_number}',\n                _precalculated_value='{svalue.sezimal.formatted_number}',\n                _precalculated_reciprocal='{svalue.reciprocal.sezimal.formatted_number}',\n            ),\n"
                    else:
                        text += f"            '{skey}': {svalue}),\n"

                text += f"        }},\n"
            else:
                text += f"        '{key}': {value},\n"

        text += '    },\n'

    text += '}\n'

    #
    # Now, let’s pre-calculate de prefixes conversion
    #
    text += '''
#
# Pre-calculated sezimal exponents conversion
#
SEZIMAL_EXPONENT_FACTOR = {
'''

    for i in SezimalRange(-130, 131):
        if i == 0:
            continue

        if i < 0:
            spf = SezimalFraction(1, SezimalInteger(10) ** abs(i))
        else:
            spf = SezimalFraction(SezimalInteger(10) ** i, 1)

        line = f"""    SezimalInteger('{i}'): SezimalFraction(
            '{spf.formatted_number}',
            _precalculated_value='{spf.sezimal.formatted_number}',
            _precalculated_reciprocal='{spf.reciprocal.sezimal.formatted_number}',
        ),
"""
        text += line

    text += '''}

#
# Pre-calculated sezimal exponents conversion
#
DECIMAL_EXPONENT_FACTOR = {
'''

    for i in SezimalRange(-102, 103):
        if i == 0:
            continue

        if i < 0:
            dpf = SezimalFraction(1, SezimalInteger(14) ** abs(i))
        else:
            dpf = SezimalFraction(SezimalInteger(14) ** i, 1)

        line = f"""    SezimalInteger('{i}'): SezimalFraction(
            '{dpf.formatted_number}',
            _precalculated_value='{dpf.sezimal.formatted_number}',
            _precalculated_reciprocal='{dpf.reciprocal.sezimal.formatted_number}',
        ),
"""
        text += line

    text += '}\n'


    open('conversion_factor.py', 'w').write(text)


def _set_non_prefixed_units(unit_conversion):
    non_prefixed = []

    if 'prefixed' not in unit_conversion:
        unit_conversion['prefixed'] = []

    for unit in unit_conversion:
        if unit not in unit_conversion['prefixed']:
            non_prefixed.append(unit)

    unit_conversion['non_prefixed'] = tuple(non_prefixed)

    return unit_conversion


if __name__ == '__main__':
    calculate_conversions()
