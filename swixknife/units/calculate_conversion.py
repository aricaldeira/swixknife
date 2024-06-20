
from swixknife import sezimal_context
from swixknife import Sezimal, SezimalInteger, SezimalFraction
from swixknife import SezimalRange


def calculate_conversions():
    _precision = sezimal_context.precision

    if _precision < 120:
        sezimal_context.precision = 120

    unit_conversion = {}

    #
    # Time
    #
    ANUGA_TO_SECOND = SezimalFraction('41 / 2_130')
    DAY_TO_SECOND = SezimalFraction('1_504_000 / 1')

    for unit, factor in (
        ('day', 1), ('uta', 100), ('pox', 10_000), ('agm', 1_000_000),
        ('ang', 100_000_000), ('bod', 10_000_000_000)):

        unit_conversion[unit] = {
            's': DAY_TO_SECOND / factor,
            'prefixed': ('s', 'day'),
            #
            # Non S.I. units
            #
            'min': DAY_TO_SECOND / 140 / factor,
            'h': DAY_TO_SECOND / 140 / 140 / factor,
            'day': DAY_TO_SECOND / 140 / 140 / 40 / factor,
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Frequency
    #
    AVRITA_TO_HERTZ = ANUGA_TO_SECOND.reciprocal

    unit_conversion['avt'] = {
        'Hz': AVRITA_TO_HERTZ,
        'prefixed': ('Hz',),
        #
        # Non S.I. units
        #
        'rpm': AVRITA_TO_HERTZ * 140,
    }
    unit_conversion['avt'] = _set_non_prefixed_units(unit_conversion['avt'])

    #
    # Length
    #
    PADA_TO_METER = SezimalFraction('1_415_503_524_325 / 150_223_042_430_000')

    unit_conversion['pad'] = {
        'm': PADA_TO_METER,
        'prefixed': ('m',),
        #
        # Non S.I. units
        #
        'twip': PADA_TO_METER / SezimalFraction('331 / 414_153_200'),  # 1/32 p
        'mil': PADA_TO_METER / SezimalFraction('331 / 255_100_052'),  # 1/4_344 in
        # 'p': PADA_TO_METER / SezimalFraction('331 / 11_414_400'),  # 1/200 in
        # 'P': PADA_TO_METER / SezimalFraction('331 / 350_520'),  # 20 p
        'in': PADA_TO_METER / SezimalFraction('331 / 35_052'),
        'li': PADA_TO_METER / SezimalFraction('134_113 / 1_201_204'),  # 53/122 ft
        'ft': PADA_TO_METER / SezimalFraction('1_433 / 5_442'),  # 20 in
        'yd': PADA_TO_METER / SezimalFraction('5_143 / 5_442'),  # 3 ft, 100 in
        'ftm': PADA_TO_METER / SezimalFraction('5_143 / 2_521'),  # 2 yd, 10 ft, 200 in
        'rd': PADA_TO_METER / SezimalFraction('134_113 / 15_324'),  # 24.3 ft
        'ch': PADA_TO_METER / SezimalFraction('134_113 / 2_521'),  # 150 ft
        'fur': PADA_TO_METER / SezimalFraction('312_230 / 325'),  # 3_020 ft
        'cb': PADA_TO_METER / SezimalFraction('331_000 / 325'),  # 3_200 ft
        'ml': PADA_TO_METER / SezimalFraction('4_151_200 / 325'),  # 40_240 ft
        'nmi': PADA_TO_METER / 12_324,
        'NM': PADA_TO_METER / 12_324,
        'le': PADA_TO_METER / SezimalFraction('20_534_000 / 325'),  # 3 ml
    }
    unit_conversion['pad'] = _set_non_prefixed_units(unit_conversion['pad'])

    #
    # Area
    #
    unit_conversion['kex'] = {
        'm2': unit_conversion['pad']['m'] ** 2,
        #
        # Non S.I. units
        #
        'a': (unit_conversion['pad']['m'] ** 2) / 244,
        'prefixed': ('m2', 'a'),

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
        'ac': (unit_conversion['pad']['m'] ** 2) / SezimalFraction('51_212_230_430 / 1_401_405'),
    }
    unit_conversion['kex'] = _set_non_prefixed_units(unit_conversion['kex'])

    #
    # Volume
    #
    AYTAN_TO_CUBIC_METER = unit_conversion['pad']['m'] ** 3
    AYTAN_TO_LITER = AYTAN_TO_CUBIC_METER * 4344
    AYTAN_TO_MILLILITER = AYTAN_TO_LITER * 4344
    AYTAN_TO_US_FLUID_DRAM = AYTAN_TO_MILLILITER / SezimalFraction('114_541_451_453 / 20_411_252_332')
    AYTAN_TO_UK_FLUID_DRAM = AYTAN_TO_MILLILITER / SezimalFraction('13_424_401 / 2_424_332')
    AYTAN_TO_CUBIC_INCH = unit_conversion['pad']['in'] ** 3

    unit_conversion['ayt'] = {
        'm3': AYTAN_TO_CUBIC_METER,
        'L': AYTAN_TO_LITER,
        'l': AYTAN_TO_LITER,
        'prefixed': ('m3', 'L', 'l'),
        #
        # Non S.I. units
        #
        'in3': AYTAN_TO_CUBIC_INCH,
        'ft3': unit_conversion['pad']['ft'] ** 3,
        'yd3': unit_conversion['pad']['yd'] ** 3,
        'ml3': unit_conversion['pad']['ml'] ** 3,
        'ac·ft': (unit_conversion['pad']['ft'] ** 3) / 533_400,

        'US min': AYTAN_TO_US_FLUID_DRAM * 140,
        'US fl dr': AYTAN_TO_US_FLUID_DRAM,
        'tsp': AYTAN_TO_US_FLUID_DRAM * 140 / 212,
        'tbsp': AYTAN_TO_US_FLUID_DRAM / 4,
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

        'UK min': AYTAN_TO_UK_FLUID_DRAM * 140,
        'UK fl s': AYTAN_TO_UK_FLUID_DRAM * 3,
        'UK fl dr': AYTAN_TO_UK_FLUID_DRAM,
        'UK fl oz': AYTAN_TO_UK_FLUID_DRAM / 12,
        'UK gi': AYTAN_TO_UK_FLUID_DRAM / 12 / 5,
        'UK pt': AYTAN_TO_UK_FLUID_DRAM / 12 / 32,
        'UK qt': AYTAN_TO_UK_FLUID_DRAM / 12 / 104,
        'UK gal': AYTAN_TO_UK_FLUID_DRAM / 12 / 424,
    }
    unit_conversion['ayt'] = _set_non_prefixed_units(unit_conversion['ayt'])

    #
    # Speed
    #
    VEGA_TO_METER_PER_SECOND = PADA_TO_METER / ANUGA_TO_SECOND

    for unit in ('veg', 'pad/ang',
                 'XDpad/day', 'Xpad/uta', 'Cpad/pox', 'Dpad/agm', 'dpad/bod',
                 'XDpad/XDang', 'Xpad/Xang', 'Cpad/Cang', 'Dpad/Dang', 'dpad/dang'):
        unit_conversion[unit] = {
            'm/s': VEGA_TO_METER_PER_SECOND,
            'prefixed': ('m/s',),
            #
            # Non S.I. units
            #
            'km/h': VEGA_TO_METER_PER_SECOND * 30 / 5,
            'ml/h': VEGA_TO_METER_PER_SECOND * 24_400 / SezimalFraction('4_151_200 / 325'),
            'mph': VEGA_TO_METER_PER_SECOND * 24_400 / SezimalFraction('4_151_200 / 325'),
            'kn': VEGA_TO_METER_PER_SECOND * 24_400 / 12_324,
            'c': VEGA_TO_METER_PER_SECOND / 45_425_332_014,
            'ft/s': VEGA_TO_METER_PER_SECOND / SezimalFraction('1_433 / 5_442'),
            'fps': VEGA_TO_METER_PER_SECOND / SezimalFraction('1_433 / 5_442'),
        }
        unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    #
    # Acceleration
    #
    SQUARE_ANUGA_TO_SQUARE_SECOND = ANUGA_TO_SECOND ** 2
    TEVARA_TO_METER_PER_SQUARE_SECOND = PADA_TO_METER / SQUARE_ANUGA_TO_SQUARE_SECOND

    unit_conversion['tvr'] = {
        'm/s2': TEVARA_TO_METER_PER_SQUARE_SECOND,
        'prefixed': ('m/s2',),
        #
        # Non S.I. units
        #
        'gal': TEVARA_TO_METER_PER_SQUARE_SECOND / 244,
        'Gal': TEVARA_TO_METER_PER_SQUARE_SECOND / 244,
        'cm/s2': TEVARA_TO_METER_PER_SQUARE_SECOND / 244,
        'ft/s2': TEVARA_TO_METER_PER_SQUARE_SECOND * SezimalFraction('1_433 / 5_442'),
        'g': TEVARA_TO_METER_PER_SQUARE_SECOND / SezimalFraction('4_112_005 / 232_332'),
        'g0': TEVARA_TO_METER_PER_SQUARE_SECOND / SezimalFraction('4_112_005 / 232_332'),
    }
    unit_conversion['tvr'] = _set_non_prefixed_units(unit_conversion['tvr'])

    #
    # Mass
    #
    DRAVYA_TO_GRAM = SezimalFraction('1_121_553_311_121_233_254_355_341_153_543_530_003_222_141_222_041_020_041_130_325_304 / 23_143_025_000_503_050_204_534_013_221_244_351_143_435_300_313_353_244_021_413_324')
    DRAVYA_TO_KILOGRAM = DRAVYA_TO_GRAM / 4344
    DRAVYA_TO_GRAIN = DRAVYA_TO_GRAM / SezimalFraction('350_515_255 / 13_531_202_544')

    unit_conversion['drv'] = {
        'g': DRAVYA_TO_GRAM,
        'prefixed': ('g',),

        #
        # Non S.I. units
        #
        'kg': DRAVYA_TO_KILOGRAM,
        't': DRAVYA_TO_KILOGRAM / 4344,
        'ton': DRAVYA_TO_KILOGRAM / 4344,

        'gr': DRAVYA_TO_GRAIN,

        'dwt': DRAVYA_TO_GRAIN / 40,
        'ozt': DRAVYA_TO_GRAIN / 40 / 32,
        'lbt': DRAVYA_TO_GRAIN / 40 / 32 / 20,

        'dr': DRAVYA_TO_GRAM / SezimalFraction('4_300_112_245 / 2_312_410_304'),
        'oz': DRAVYA_TO_GRAM / SezimalFraction('4_300_112_245 / 54_143_224'),
        'lb': DRAVYA_TO_GRAM / SezimalFraction('4_300_112_245 / 2_050_544'),
        'st': DRAVYA_TO_GRAM / SezimalFraction('51_301_235_135 / 1_023_252'),
        'sl': DRAVYA_TO_GRAM / SezimalFraction('3_043_351 / 14'),

        'UK qr': DRAVYA_TO_GRAM / SezimalFraction('51_301_235_135 / 311_424'),
        'UK cwt': DRAVYA_TO_GRAM / SezimalFraction('51_301_235_135 / 44_534'),
        'UK ton': DRAVYA_TO_KILOGRAM / SezimalFraction('51_301_235_135 / 10_410_432'),

        'US qr': DRAVYA_TO_GRAM / SezimalFraction('4_300_112_245 / 30_304'),
        'US cwt': DRAVYA_TO_GRAM / SezimalFraction('4_300_112_245 / 4_344'),
        'US ton': DRAVYA_TO_KILOGRAM / SezimalFraction('4_300_112_245 / 1_023_252'),
    }
    unit_conversion['drv'] = _set_non_prefixed_units(unit_conversion['drv'])

    #
    # Density
    #
    GANA_TO_KILOGRAM_PER_CUBIC_METER = DRAVYA_TO_KILOGRAM / (PADA_TO_METER ** 3)
    GANA_TO_KILOGRAM_PER_LITER = GANA_TO_KILOGRAM_PER_CUBIC_METER / 4344

    unit_conversion['gan'] = {
        'kg/m3': GANA_TO_KILOGRAM_PER_CUBIC_METER,
        'kg/L': GANA_TO_KILOGRAM_PER_LITER,
        'kg/l': GANA_TO_KILOGRAM_PER_LITER,
        'kg/dm3': GANA_TO_KILOGRAM_PER_LITER,
        'g/cm3': GANA_TO_KILOGRAM_PER_LITER,
        'g/mL': GANA_TO_KILOGRAM_PER_LITER,
        'g/ml': GANA_TO_KILOGRAM_PER_LITER,
        'ton/m3': GANA_TO_KILOGRAM_PER_LITER,
        'Mg/m3': GANA_TO_KILOGRAM_PER_LITER,

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
    unit_conversion['gan'] = _set_non_prefixed_units(unit_conversion['gan'])

    #
    # Force/weight
    #
    unit_conversion['bar'] = {
        'N': SezimalFraction('1_514_013_223_524_454_001_155_251_200_421_502_131_214_453_103_540_110_043_004_301 / 15_010_344_010_111_333_042_214_015_440_344_150_251_043_044_342_310_023_032_344_544'),
        'prefixed': ('N', 'gf'),

        #
        # Non S.I. units
        #
        'gf': SezimalFraction('1_514_013_223_524_454_001_155_251_200_421_502_131_214_453_103_540_110_043_004_301 / 15_010_344_010_111_333_042_214_015_440_344_150_251_043_044_342_310_023_032_344_544') / SezimalFraction('4_112_005 / 1_552_400_332'),
        'lbf': SezimalFraction('1_514_013_223_524_454_001_155_251_200_421_502_131_214_453_103_540_110_043_004_301 / 15_010_344_010_111_333_042_214_015_440_344_150_251_043_044_342_310_023_032_344_544') / SezimalFraction('30_530_545_233_334_201 / 4_130_442_021_003_132'),
        'dyn': SezimalFraction('1_514_013_223_524_454_001_155_251_200_421_502_131_214_453_103_540_110_043_004_301 / 15_010_344_010_111_333_042_214_015_440_344_150_251_043_044_342_310_023_032_344_544') / SezimalFraction('1 / 2_050_544'),
    }
    unit_conversion['bar'] = _set_non_prefixed_units(unit_conversion['bar'])

    #
    # Pressure
    #
    unit_conversion['dab'] = {
        'Pa': SezimalFraction('122_200_235_212_541_051_051_420_432_402_021_022_212_131 / 110_514_124_353_011_111_533_000_230_455_224_221_200'),
        'prefixed': ('Pa', 'psi', 'bar'),

        #
        # Non S.I. units
        #
        'atm': SezimalFraction('122_200_235_212_541_051_051_420_432_402_021_022_212_131 / 110_514_124_353_011_111_533_000_230_455_224_221_200') / 2_101_033,
        'psi': SezimalFraction('122_200_235_212_541_051_051_420_432_402_021_022_212_131 / 110_514_124_353_011_111_533_000_230_455_224_221_200') / 4344 / SezimalFraction('403_440_101 / 33_233_344'),
        'bar': SezimalFraction('122_200_235_212_541_051_051_420_432_402_021_022_212_131 / 110_514_124_353_011_111_533_000_230_455_224_221_200') / 2_050_544,
        'mmHg': SezimalFraction('122_200_235_212_541_051_051_420_432_402_021_022_212_131 / 110_514_124_353_011_111_533_000_230_455_224_221_200') / SezimalFraction('1_232_341 / 2_152'),
        'inHg': SezimalFraction('122_200_235_212_541_051_051_420_432_402_021_022_212_131 / 110_514_124_353_011_111_533_000_230_455_224_221_200') / SezimalFraction('11_131_435 / 244'),
    }
    unit_conversion['dab'] = _set_non_prefixed_units(unit_conversion['dab'])

    #
    # Energy/work
    #
    unit_conversion['kry'] = {
        'J': SezimalFraction('33_521_011_020_511_504_500_105_153_500_503_335_231_504_250_513_113_014_250_131 / 34_535_213_355_430_432_413_330_124_234_141_103_540_144_344_324_515_411_045_300_300'),
        'prefixed': ('J', 'Wh', 'BTU', 'cal', 'erg', 'eV', 'TNT'),

        #
        # Non S.I. units
        #
        'Wh': SezimalFraction('33_521_011_020_511_504_500_105_153_500_503_335_231_504_250_513_113_014_250_131 / 34_535_213_355_430_432_413_330_124_234_141_103_540_144_344_324_515_411_045_300_300') / 4344 / SezimalFraction('30 / 5'),
        'ft⋅lb': SezimalFraction('33_521_011_020_511_504_500_105_153_500_503_335_231_504_250_513_113_014_250_131 / 34_535_213_355_430_432_413_330_124_234_141_103_540_144_344_324_515_411_045_300_300') / SezimalFraction('22_310_245 / 14_414_452'),
        'ftlb': SezimalFraction('33_521_011_020_511_504_500_105_153_500_503_335_231_504_250_513_113_014_250_131 / 34_535_213_355_430_432_413_330_124_234_141_103_540_144_344_324_515_411_045_300_300') / SezimalFraction('22_310_245 / 14_414_452'),
        'BTU': SezimalFraction('33_521_011_020_511_504_500_105_153_500_503_335_231_504_250_513_113_014_250_131 / 34_535_213_355_430_432_413_330_124_234_141_103_540_144_344_324_515_411_045_300_300') / SezimalFraction('40_122_335_231_451 / 4_543_401_252'),
        'cal': SezimalFraction('33_521_011_020_511_504_500_105_153_500_503_335_231_504_250_513_113_014_250_131 / 34_535_213_355_430_432_413_330_124_234_141_103_540_144_344_324_515_411_045_300_300') / SezimalFraction('2_231 / 325'),
        'erg': SezimalFraction('33_521_011_020_511_504_500_105_153_500_503_335_231_504_250_513_113_014_250_131 / 34_535_213_355_430_432_413_330_124_234_141_103_540_144_344_324_515_411_045_300_300') * 554_200_144,
        'eV': SezimalFraction('33_521_011_020_511_504_500_105_153_500_503_335_231_504_250_513_113_014_250_131 / 34_535_213_355_430_432_413_330_124_234_141_103_540_144_344_324_515_411_045_300_300') / SezimalFraction('422_552_112_230 / 545_225_423_350_030_313_042_203_422_444_532_144'),
        'TNT': SezimalFraction('33_521_011_020_511_504_500_105_153_500_503_335_231_504_250_513_113_014_250_131 / 34_535_213_355_430_432_413_330_124_234_141_103_540_144_344_324_515_411_045_300_300') / 1_531_101_350_212,
    }
    unit_conversion['kry'] = _set_non_prefixed_units(unit_conversion['kry'])

    #
    # Power
    #
    unit_conversion['xat'] = {
        'W': SezimalFraction('121_132_153_514_542_401_513_232_551_044_525_041_412_401_023_245_415_205_322_023_430 / 2_353_312_241_345_501_021_435_340_022_525_025_342_351_251_450_242_104_254_225_320_300'),
        'prefixed': ('W',),

        #
        # Non S.I. units
        #
        'hp': SezimalFraction('121_132_153_514_542_401_513_232_551_044_525_041_412_401_023_245_415_205_322_023_430 / 2_353_312_241_345_501_021_435_340_022_525_025_342_351_251_450_242_104_254_225_320_300') / SezimalFraction('54_305 / 14'),
        'ftlb/s': unit_conversion['kry']['ftlb'] / unit_conversion['ang']['s'],
        'ftlb/min': unit_conversion['kry']['ftlb'] / unit_conversion['ang']['min'],
        'ftlb/h': unit_conversion['kry']['ftlb'] / unit_conversion['ang']['h'],
        'BTU/h': unit_conversion['kry']['BTU'] / unit_conversion['ang']['h'],
        'cal/s': unit_conversion['kry']['cal'] / unit_conversion['ang']['s'],
        'kcal/h': unit_conversion['kry']['cal'] / 4344 / unit_conversion['ang']['h'],
    }
    unit_conversion['xat'] = _set_non_prefixed_units(unit_conversion['xat'])

    #
    # Thermodynamic temperature
    #
    unit_conversion['gtk'] = {
        'K': SezimalFraction('10_555_444_540_024_220_300_311_044_444_024_243_143 / 2_245_430_323_350_444_405_535_225_150_451_403_235_403_344'),
        '°C': SezimalFraction('10_555_444_540_024_220_300_311_044_444_024_243_143 / 2_245_430_323_350_444_405_535_225_150_451_403_235_403_344'),

        'prefixed': ('K',),

        #
        # Non S.I. units
        #
        '°F': SezimalFraction('10_555_444_540_024_220_300_311_044_444_024_243_143 / 2_245_430_323_350_444_405_535_225_150_451_403_235_403_344') / SezimalFraction('5 / 13'),
        '°R': SezimalFraction('10_555_444_540_024_220_300_311_044_444_024_243_143 / 2_245_430_323_350_444_405_535_225_150_451_403_235_403_344') / SezimalFraction('5 / 13'),

        'adjust': {
            '°C': SezimalFraction('-41_143 / 32'),
            '°F': SezimalFraction('-552_451 / 244'),
        }
    }
    unit_conversion['gtk'] = _set_non_prefixed_units(unit_conversion['gtk'])

    #
    # Common temperature
    #
    unit_conversion['tap'] = {
        '°C': SezimalFraction('1_055_544_454_002_422_030_031_104_444_402_424_314_300_000 / 2_245_430_323_350_444_405_535_225_150_451_403_235_403_344'),
        'K': SezimalFraction('1_055_544_454_002_422_030_031_104_444_402_424_314_300_000 / 2_245_430_323_350_444_405_535_225_150_451_403_235_403_344'),

        'prefixed': ('K',),

        #
        # Non S.I. units
        #
        '°F': SezimalFraction('1_055_544_454_002_422_030_031_104_444_402_424_314_300_000 / 2_245_430_323_350_444_405_535_225_150_451_403_235_403_344') / SezimalFraction('5 / 13'),
        '°R': SezimalFraction('1_055_544_454_002_422_030_031_104_444_402_424_314_300_000 / 2_245_430_323_350_444_405_535_225_150_451_403_235_403_344') / SezimalFraction('5 / 13'),

        'adjust': {
            'K': SezimalFraction('41_143 / 32'),
            '°F': Sezimal(52),
            '°R': SezimalFraction('552_451 / 244'),
        }
    }
    unit_conversion['tap'] = _set_non_prefixed_units(unit_conversion['tap'])

    #
    # Heat capacity
    #
    unit_conversion['agn'] = {
        'J/K': unit_conversion['kry']['J'] / unit_conversion['gtk']['K'],

        'prefixed': ('J/K',),

        #
        # Non S.I. units
        #
        'BTU/°R': unit_conversion['kry']['BTU'] / unit_conversion['gtk']['°R'],
    }
    unit_conversion['agn'] = _set_non_prefixed_units(unit_conversion['agn'])

    #
    # Heat capacity per mass
    #
    unit_conversion['idn'] = {
        'J/K/kg': unit_conversion['agn']['J/K'] / unit_conversion['drv']['kg'],

        'prefixed': ('J/K/kg',),

        #
        # Non S.I. units
        #
        'BTU/°R/lb': unit_conversion['agn']['BTU/°R'] / unit_conversion['drv']['lb'],
    }
    unit_conversion['idn'] = _set_non_prefixed_units(unit_conversion['idn'])

    #
    # Heat capacity per volume
    #
    unit_conversion['tln'] = {
        'J/K/m3': unit_conversion['agn']['J/K'] / unit_conversion['ayt']['m3'],

        'prefixed': ('J/K/m3',),
    }
    unit_conversion['tln'] = _set_non_prefixed_units(unit_conversion['tln'])

    #
    # Electromagnetism is based off these 2 values, how many electric charges
    # are there in an avesha (see the “e” in avesha below), and that
    # the pratiroda is exactly the vacuum electric resistance;
    #
    AVESHA_TO_COULOMB = SezimalFraction('12_441_111_434_024_101_213_014_435_504_443 / 124_204_233_524_304_345_140_330_533_411_122_024')
    PRATIRODA_TO_OHM = SezimalFraction('111_133_351_303_345 / 40_450_211_224')

    #
    # Electric charge
    #
    unit_conversion['avx'] = {
        'C': AVESHA_TO_COULOMB,
        'Ah': AVESHA_TO_COULOMB / 24_400,
        'As': AVESHA_TO_COULOMB / 1_141_440_000,
        'e': SezimalFraction('115_422_244_443_055_421_554 / 1'),
        'F': SezimalFraction('5_255_312_545_030_054_302_243 / 2_354_124_142_045_012'),
        'prefixed': ('C', 'e', 'Ah', 'As', 'F'),
    }
    unit_conversion['avx'] = _set_non_prefixed_units(unit_conversion['avx'])

    #
    # Electric current
    #
    unit_conversion['dar'] = {
        'A': unit_conversion['avx']['C'] / unit_conversion['ang']['s'],
        'prefixed': ('A',),
    }
    unit_conversion['dar'] = _set_non_prefixed_units(unit_conversion['dar'])

    #
    # Electric potential difference
    #
    unit_conversion['vbv'] = {
        'V': unit_conversion['kry']['J'] / unit_conversion['avx']['C'],
        # 'V': PRATIRODA_TO_OHM * unit_conversion['dar']['A'],
        'prefixed': ('V',),
    }
    unit_conversion['vbv'] = _set_non_prefixed_units(unit_conversion['vbv'])

    #
    # Electric resistance
    #
    unit_conversion['ptr'] = {
        #
        # The division of other conversions introduces a slight discrepancy,
        # since this value is supposed to be the vacuum resistance exactly;
        # so, we define it as a simpler fraction
        #
        # 'Ω': unit_conversion['vbv']['V'] / unit_conversion['dar']['A'],
        'Ω': PRATIRODA_TO_OHM,
        'ohm': PRATIRODA_TO_OHM,
        'prefixed': ('Ω', 'ohm'),
    }
    unit_conversion['ptr'] = _set_non_prefixed_units(unit_conversion['ptr'])

    #
    # Electric conductance
    #
    unit_conversion['cln'] = {
        'S': PRATIRODA_TO_OHM.reciprocal,
        'prefixed': ('S',),
    }
    unit_conversion['cln'] = _set_non_prefixed_units(unit_conversion['cln'])

    #
    # Electric inductance
    #
    unit_conversion['prk'] = {
        'H': PRATIRODA_TO_OHM * unit_conversion['ang']['s'],
        'prefixed': ('H',),
    }
    unit_conversion['prk'] = _set_non_prefixed_units(unit_conversion['prk'])

    #
    # Electric capacitance
    #
    unit_conversion['sam'] = {
        'F': AVESHA_TO_COULOMB / unit_conversion['vbv']['V'],
        'prefixed': ('F',),
    }
    unit_conversion['sam'] = _set_non_prefixed_units(unit_conversion['sam'])

    #
    # Magnetic flux
    #
    unit_conversion['abv'] = {
        'Wb': unit_conversion['vbv']['V'] * unit_conversion['ang']['s'],
        'prefixed': ('Wb',),
    }
    unit_conversion['abv'] = _set_non_prefixed_units(unit_conversion['abv'])

    #
    # Magnetic flux density
    #
    unit_conversion['vtr'] = {
        'T': unit_conversion['abv']['Wb'] / unit_conversion['kex']['m2'],
        'prefixed': ('T',),
    }
    unit_conversion['vtr'] = _set_non_prefixed_units(unit_conversion['vtr'])

    #
    # Angles and angular units
    #
    TAU = SezimalFraction('10_141_100_143_234_252_214_513_232_150_255_042_205_002_433_324_012 / 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000')
    PI = TAU / 2
    GOLA = TAU * 2

    #
    # Plane angle
    #
    unit_conversion['prd'] = {
        'rad': TAU,
        'prefixed': ('rad', 'turn', 'gon', 'arcmin', 'arcsec'),
        'deg': SezimalInteger('1400'),
        'turn': SezimalInteger('1'),
        'gon': SezimalInteger('1504'),
        'arcmin': SezimalInteger('244_000'),
        'arcsec': SezimalInteger('43_440_000'),
    }
    unit_conversion['prd'] = _set_non_prefixed_units(unit_conversion['prd'])

    #
    # Proportions
    #
    # for unit, factor in (
    #     ('p/n', 2), ('p/a', 3), ('p/sa', 4), ('p/na', 5), ('p/x', 10),
    #     ('p/sx', 11), ('p/nx', 12), ('p/ax', 13), ('p/sax', 14), ('p/nax', 15),
    #     ('p/Dx', 20), ('p/Tx', 30), ('p/Cx', 40), ('p/Tx', 50), ('p/Xx', 100),
    # ):
    #     unit_conversion[unit] = {
    #         '%': SezimalFraction(244, SezimalInteger(10) ** factor),
    #         '‰': SezimalFraction(4344, SezimalInteger(10) ** factor),
    #         '‱': SezimalFraction(114_144, SezimalInteger(10) ** factor),
    #         'pcm': SezimalFraction(2_050_544, SezimalInteger(10) ** factor),
    #         'ppm': SezimalFraction(33_233_344, SezimalInteger(10) ** factor),
    #         'ppb': SezimalFraction(243_121_245_344, SezimalInteger(10) ** factor),
    #         'prefixed': (),
    #     }
    #     unit_conversion[unit] = _set_non_prefixed_units(unit_conversion[unit])

    unit_conversion['prt'] = {
        'prefixed': (),
        '%': SezimalInteger(244),
        '‰': SezimalInteger(4344),
        '‱': SezimalInteger(114_144),
        'pcm': SezimalInteger(2_050_544),
        'ppm': SezimalInteger(33_233_344),
        'ppb': SezimalInteger(243_121_245_344),
        'ppt': SezimalInteger(2_043_221_010_301_344),
        'ppq': SezimalInteger(13_502_453_354_043_313_344),
    }
    unit_conversion['prt'] = _set_non_prefixed_units(unit_conversion['prt'])

    # #
    # # Angular velocity
    # #
    # unit_conversion['prd/ang'] = {
    #     'rad/s': unit_conversion['prd']['rad'] / unit_conversion['ang']['s'],
    #     'prefixed': ('rad/s',),
    # }
    # unit_conversion['prd/ang'] = _set_non_prefixed_units(unit_conversion['prd/ang'])
    #
    # #
    # # Angular Acceleration
    # #
    # unit_conversion['prd/ang2'] = {
    #     'rad/s2': unit_conversion['prd']['rad'] / (unit_conversion['ang']['s'] ** 2),
    #     'prefixed': ('rad/s2',),
    # }
    # unit_conversion['prd/ang2'] = _set_non_prefixed_units(unit_conversion['prd/ang2'])
    #
    # unit_conversion['pad/prd'] = {
    #     'm/rad': unit_conversion['pad']['m'] / unit_conversion['rad']['prd'],
    #     'prefixed': ('m/rad',),
    # }
    # unit_conversion['pad/prd'] = _set_non_prefixed_units(unit_conversion['pad/prd'])

    #
    # Solid angle
    #
    unit_conversion['gol'] = {
        'sr': GOLA,
        'prefixed': ('sr', 'spat'),
        'spat': SezimalInteger('1'),
        'deg2': SezimalFraction('2_440_000 / 1') / PI,
    }
    unit_conversion['gol'] = _set_non_prefixed_units(unit_conversion['gol'])


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

    for i in SezimalRange(-120, 121):
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

    sezimal_context.precision = _precision


def _set_non_prefixed_units(unit_conversion):
    non_prefixed = []

    for unit in unit_conversion:
        if unit not in unit_conversion['prefixed']:
            non_prefixed.append(unit)

    unit_conversion['non_prefixed'] = tuple(non_prefixed)

    return unit_conversion


if __name__ == '__main__':
    calculate_conversions()
