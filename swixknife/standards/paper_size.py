

from swixknife.sezimal import Sezimal

#
# Paper sizes in dpad (W dpad, H dpad, A ktr)
# SA0 is aprox. 1 ktr
# SA1 is aprox. 0.3 ktr
# and so on
#
# For the SA series, we start with
# W = 2 ** -1/4
# H = 2 ** 1/4
#
# For the SB series, we start with
# W = 1
# H = 2 ** 1/2
#
# For the SC and SD series, I used LibreOffice’s solver to find
# the starting value of H
#
# Those are not the paper sizes of ISO-216 converted to dpad,
# but, surprisingly, there where once a similar size set,
# in a D-series, from 1922_dec to 1925_dec:
# https://en.wikipedia.org/wiki/Paper_size#DIN_D
# https://de.wikipedia.org/wiki/Papierformat#%C3%9Cbersicht
#
# Size      Width                    Height                      Area
# SA00 : 5_014 dpad (785 mm) × 11_045 dpad (1_110 mm) = 10_000 ktr   (871_350 mm²)
# SA01 : 3_323 dpad (555 mm) ×  5_014 dpad (  785 mm) =  3_000 ktr   (435_675 mm²)
# SA02 : 2_305 dpad (392 mm) ×  3_323 dpad (  555 mm) =  1_300 ktr   (217_560 mm²)
# SA03 : 1_441 dpad (277 mm) ×  2_305 dpad (  392 mm) =    430 ktr   (108_584 mm²)
# SA04 : 1_132 dpad (196 mm) ×  1_441 dpad (  277 mm) =    213 ktr   ( 54_292 mm²)
# SA05 :   520 dpad (138 mm) ×  1_132 dpad (  196 mm) =    104 ktr   ( 27_048 mm²)
# SA10 :   344 dpad ( 98 mm) ×    520 dpad (  138 mm) =     32 ktr   ( 13_524 mm²)
# SA11 :   240 dpad ( 69 mm) ×    344 dpad (   98 mm) =     14 ktr   (  6_762 mm²)
# SA12 :   152 dpad ( 49 mm) ×    240 dpad (   69 mm) =      5 ktr   (  3_381 mm²)
# SA13 :   120 dpad ( 35 mm) ×    152 dpad (   49 mm) =      2.3 ktr (  1_715 mm²)
# SA14 :    54 dpad ( 24 mm) ×    120 dpad (   35 mm) =      1.2 ktr (    840 mm²)
# SA15 :    40 dpad ( 17 mm) ×     54 dpad (   24 mm) =      0.4 ktr (    408 mm²)
# SA20 :    25 dpad ( 12 mm) ×     40 dpad (   17 mm) =      0.2 ktr (    204 mm²)
#
#
# Size       Width                     Height                      Area
# SB00 : 10_000 dpad (933 mm) × 12_253 dpad (1_320 mm) = 12_253 ktr    (1_231_560 mm²)
# SB01 :  4_124 dpad (660 mm) × 10_000 dpad (  933 mm) =  4_124 ktr    (  615_780 mm²)
# SB02 :  3_000 dpad (467 mm) ×  4_124 dpad (  660 mm) =  2_042 ktr    (  308_220 mm²)
# SB03 :  2_042 dpad (330 mm) ×  3_000 dpad (  467 mm) =  1_021 ktr    (  154_110 mm²)
# SB04 :  1_300 dpad (233 mm) ×  2_042 dpad (  330 mm) =    310.30 ktr (   76_890 mm²)
# SB05 :  1_021 dpad (165 mm) ×  1_300 dpad (  233 mm) =    133.13 ktr (   38_445 mm²)
# SB10 :    430 dpad (117 mm) ×  1_021 dpad (  165 mm) =     44.35 ktr (   19_305 mm²)
# SB11 :    311 dpad ( 83 mm) ×    430 dpad (  117 mm) =     22.22 ktr (    9_711 mm²)
# SB12 :    213 dpad ( 58 mm) ×    311 dpad (   83 mm) =     11.11 ktr (    4_814 mm²)
# SB13 :    133 dpad ( 41 mm) ×    213 dpad (   58 mm) =      3.32 ktr (    2_378 mm²)
# SB14 :    104 dpad ( 29 mm) ×    133 dpad (   41 mm) =      1.43 ktr (    1_189 mm²)
# SB15 :     44 dpad ( 20 mm) ×    104 dpad (   29 mm) =      0.51 ktr (      580 mm²)
# SB20 :     32 dpad ( 14 mm) ×     44 dpad (   20 mm) =      0.24 ktr (      280 mm²)
#
#
# Size       Width                     Height                      Area
# SC00 : 5_301 dpad (856 mm) × 11_441 dpad (1_211 mm) = 11_050 ktr (1_036_616 mm²)
# SC01 : 3_521 dpad (606 mm) ×  5_301 dpad (  856 mm) =  3_324 ktr (  518_736 mm²)
# SC02 : 2_431 dpad (428 mm) ×  3_521 dpad (  606 mm) =  1_442 ktr (  259_368 mm²)
# SC03 : 1_541 dpad (303 mm) ×  2_431 dpad (  428 mm) =    521 ktr (  129_684 mm²)
# SC04 : 1_214 dpad (215 mm) ×  1_541 dpad (  303 mm) =    241 ktr (   65_145 mm²)
# SC05 :   551 dpad (152 mm) ×  1_214 dpad (  215 mm) =    121 ktr (   32_680 mm²)
# SC10 :   405 dpad (107 mm) ×    551 dpad (  152 mm) =     40 ktr (   16_264 mm²)
# SC11 :   253 dpad ( 76 mm) ×    405 dpad (  107 mm) =     20 ktr (    8_132 mm²)
# SC12 :   202 dpad ( 53 mm) ×    253 dpad (   76 mm) =     10 ktr (    4_028 mm²)
# SC13 :   124 dpad ( 37 mm) ×    202 dpad (   53 mm) =      3 ktr (    1_961 mm²)
# SC14 :   101 dpad ( 27 mm) ×    124 dpad (   37 mm) =      1.3 ktr (      999 mm²)
# SC15 :    42 dpad ( 19 mm) ×    101 dpad (   27 mm) =      0.4 ktr (      513 mm²)
# SC20 :    30 dpad ( 13 mm) ×     42 dpad (   19 mm) =      0.2 ktr (      247 mm²)
#
#
# Size       Width                     Height                      Area
# SD00 : 4_344 dpad (720 mm) × 10_314 dpad (1_018 mm) = 5_015 ktr (732_960 mm²)
# SD01 : 3_135 dpad (509 mm) ×  4_344 dpad (  720 mm) = 2_310 ktr (366_480 mm²)
# SD02 : 2_152 dpad (360 mm) ×  3_135 dpad (  509 mm) = 1_133 ktr (183_240 mm²)
# SD03 : 1_350 dpad (255 mm) ×  2_152 dpad (  360 mm) =   345 ktr ( 91_800 mm²)
# SD04 : 1_054 dpad (180 mm) ×  1_350 dpad (  255 mm) =   152 ktr ( 45_900 mm²)
# SD05 :   453 dpad (127 mm) ×  1_054 dpad (  180 mm) =    54 ktr ( 22_860 mm²)
# SD10 :   325 dpad ( 90 mm) ×    453 dpad (  127 mm) =    25 ktr ( 11_430 mm²)
# SD11 :   224 dpad ( 63 mm) ×    325 dpad (   90 mm) =    12 ktr (  5_670 mm²)
# SD12 :   142 dpad ( 45 mm) ×    224 dpad (   63 mm) =     4 ktr (  2_835 mm²)
# SD13 :   112 dpad ( 32 mm) ×    142 dpad (   45 mm) =     2 ktr (  1_440 mm²)
# SD14 :    51 dpad ( 22 mm) ×    112 dpad (   32 mm) =     1 ktr (    704 mm²)
# SD15 :    34 dpad ( 16 mm) ×     51 dpad (   22 mm) =     0.30 ktr (    352 mm²)
# SD20 :    24 dpad ( 12 mm) ×     34 dpad (   16 mm) =     0.13 ktr (    192 mm²)
#

SA00 = (Sezimal('5_014'), Sezimal('11_045'), Sezimal('10_000.020_2'))
SA01 = (Sezimal('3_323'),  Sezimal('5_014'),  Sezimal('3_000.241_0'))
SA02 = (Sezimal('2_305'),  Sezimal('3_323'),  Sezimal('1_300.120_3'))
SA03 = (Sezimal('1_441'),  Sezimal('2_305'),    Sezimal('425.522_5'))
SA04 = (Sezimal('1_132'),  Sezimal('1_441'),    Sezimal('212.445_2'))
SA05 = (  Sezimal('520'),  Sezimal('1_132'),    Sezimal('104.144_0'))
SA10 = (  Sezimal('344'),    Sezimal('520'),     Sezimal('32.052_0'))
SA11 = (  Sezimal('240'),    Sezimal('344'),     Sezimal('14.024_0'))
SA12 = (  Sezimal('152'),    Sezimal('240'),      Sezimal('5.012_0'))
SA13 = (  Sezimal('120'),    Sezimal('152'),      Sezimal('2.304_0'))
SA14 = (   Sezimal('54'),    Sezimal('120'),      Sezimal('1.132_0'))
SA15 = (   Sezimal('40'),     Sezimal('54'),      Sezimal('0.344_0'))
SA20 = (   Sezimal('25'),     Sezimal('40'),      Sezimal('0.152_0'))

SB00 = (Sezimal('10_000'), Sezimal('12_253'), Sezimal('12_253.000_0'))
SB01 = ( Sezimal('4_124'), Sezimal('10_000'),  Sezimal('4_124.000_0'))
SB02 = ( Sezimal('3_000'),  Sezimal('4_124'),  Sezimal('2_042.000_0'))
SB03 = ( Sezimal('2_042'),  Sezimal('3_000'),  Sezimal('1_021.000_0'))
SB04 = ( Sezimal('1_300'),  Sezimal('2_042'),   Sezimal('310.300_0'))
SB05 = ( Sezimal('1_021'),  Sezimal('1_300'),   Sezimal('133.130_0'))
SB10 = (   Sezimal('430'),  Sezimal('1_021'),    Sezimal('44.343_0'))
SB11 = (   Sezimal('311'),    Sezimal('430'),    Sezimal('22.213_0'))
SB12 = (   Sezimal('213'),    Sezimal('311'),    Sezimal('11.104_3'))
SB13 = (   Sezimal('133'),    Sezimal('213'),     Sezimal('3.321_3'))
SB14 = (   Sezimal('104'),    Sezimal('133'),     Sezimal('1.432_0'))
SB15 = (    Sezimal('44'),    Sezimal('104'),     Sezimal('0.510_4'))
SB20 = (    Sezimal('32'),     Sezimal('44'),     Sezimal('0.233_2'))

SC00 = (Sezimal('5_301'), Sezimal('11_441'), Sezimal('11_050.114_1'))
SC01 = (Sezimal('3_521'),  Sezimal('5_301'),  Sezimal('3_323.322_1'))
SC02 = (Sezimal('2_431'),  Sezimal('3_521'),  Sezimal('1_442.035_1'))
SC03 = (Sezimal('1_541'),  Sezimal('2_431'),    Sezimal('521.141_1'))
SC04 = (Sezimal('1_214'),  Sezimal('1_541'),    Sezimal('240.445_4'))
SC05 = (  Sezimal('551'),  Sezimal('1_214'),    Sezimal('120.303_4'))
SC10 = (  Sezimal('405'),    Sezimal('551'),     Sezimal('40.131_5'))
SC11 = (  Sezimal('253'),    Sezimal('405'),     Sezimal('20.023_3'))
SC12 = (  Sezimal('202'),    Sezimal('253'),      Sezimal('5.555_0'))
SC13 = (  Sezimal('124'),    Sezimal('202'),      Sezimal('2.545_2'))
SC14 = (  Sezimal('101'),    Sezimal('124'),      Sezimal('1.252_4'))
SC15 = (   Sezimal('42'),    Sezimal('101'),      Sezimal('0.424_2'))
SC20 = (   Sezimal('30'),     Sezimal('42'),      Sezimal('0.210_0'))

SD00 = (Sezimal('4_344'), Sezimal('10_314'), Sezimal('5_015.014_4'))
SD01 = (Sezimal('3_135'),  Sezimal('4_344'), Sezimal('2_305.305_2'))
SD02 = (Sezimal('2_152'),  Sezimal('3_135'), Sezimal('1_132.432_4'))
SD03 = (Sezimal('1_350'),  Sezimal('2_152'),   Sezimal('344.324_0'))
SD04 = (Sezimal('1_054'),  Sezimal('1_350'),   Sezimal('152.142_0'))
SD05 = (  Sezimal('453'),  Sezimal('1_054'),    Sezimal('54.051_0'))
SD10 = (  Sezimal('325'),    Sezimal('453'),    Sezimal('25.023_3'))
SD11 = (  Sezimal('224'),    Sezimal('325'),    Sezimal('12.253_2'))
SD12 = (  Sezimal('142'),    Sezimal('224'),     Sezimal('4.113_2'))
SD13 = (  Sezimal('112'),    Sezimal('142'),     Sezimal('2.034_4'))
SD14 = (   Sezimal('51'),    Sezimal('112'),     Sezimal('1.015_2'))
SD15 = (   Sezimal('34'),     Sezimal('51'),     Sezimal('0.305_4'))
SD20 = (   Sezimal('24'),     Sezimal('34'),     Sezimal('0.134_4'))


PAPER_SIZES = [
    SA00, SA01, SA02, SA03, SA04, SA05,
    SA10, SA11, SA12, SA13, SA14, SA15, SA20,

    SB00, SB01, SB02, SB03, SB04, SB05,
    SB10, SB11, SB12, SB13, SB14, SB15, SB20,

    SC00, SC01, SC02, SC03, SC04, SC05,
    SC10, SC11, SC12, SC13, SC14, SC15, SC20,

    SD00, SD01, SD02, SD03, SD04, SD05,
    SD10, SD11, SD12, SD13, SD14, SD15, SD20,
]


def _calc_paper_size_series(initial_height, series_name):
    height = initial_height

    for i in SezimalRange(0, 21):
        height_dpad = height
        width_dpad = round(height_dpad / SQRT_2, 0)
        area_ketra = round(height_dpad / 100 * width_dpad / 100, 4)

        height_mm = round(sdu(height_dpad, 'dpad', 'mm').decimal, 0)
        width_mm = round(sdu(width_dpad, 'dpad', 'mm').decimal, 0)
        area_m2 = round(height_mm * width_mm, 0)

        print(f'S{series_name}{str(i).zfill(2)} : {width_dpad.formatted_number} dpad ({width_mm} mm) × {height_dpad.formatted_number} dpad ({height_mm} mm) = {area_ketra.formatted_number} ktr ({area_m2} mm²)')
        print(f"S{series_name}{str(i).zfill(2)} = (Sezimal('{width_dpad.formatted_number}'), Sezimal('{height_dpad.formatted_number}'), Sezimal('{area_ketra.formatted_number}'))")

        height = width_dpad


if __name__ == '__main__':
    from swixknife import SezimalInteger as SI
    from swixknife import SezimalRange
    from swixknife.units import sezimal_to_decimal_unit as sdu
    from swixknife.constants import SQRT_2

    _calc_paper_size_series(Sezimal('11_045'), 'A')
    _calc_paper_size_series(Sezimal('12_253'), 'B')
    _calc_paper_size_series(Sezimal('11_441'), 'C')
    _calc_paper_size_series(Sezimal('10_314'), 'D')
