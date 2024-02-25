

from swixknife.sezimal import Sezimal

#
# Paper sizes in cpad (W cpad, H cpad, A ksh)
# SA0 is aprox. 1 ksh
# SA1 is aprox. 0.3 ksh
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
# Those are not the paper sizes of ISO-216 converted to cpad,
# but, surprisingly, there where once a similar size set,
# in a D-series, from 1922_dec to 1925_dec:
# https://en.wikipedia.org/wiki/Paper_size#DIN_D
# https://de.wikipedia.org/wiki/Papierformat#%C3%9Cbersicht
#
# Size      Width                    Height                      Area
# SA00 - 5014 cpad (778.749 mm) × 1,1045 cpad (1,100.966 mm) = 1.0000 0202 ksh (0.857 932 m²)
# SA01 - 3323 cpad (550.840 mm) ×   5014 cpad   (778.749 mm) = 0.3000 2410 ksh (0.428 966 m²)
# SA02 - 2305 cpad (389.375 mm) ×   3323 cpad   (550.840 mm) = 0.1255 4454 ksh (0.214 483 m²)
# SA03 - 1441 cpad (275.063 mm) ×   2305 cpad   (389.375 mm) = 0.0425 5225 ksh (0.107 103 m²)
# SA04 - 1132 cpad (194.330 mm) ×   1441 cpad   (275.063 mm) = 0.0212 4452 ksh (0.053 453 m²)
# SA05 -  520 cpad (137.174 mm) ×   1132 cpad   (194.330 mm) = 0.0104 1440 ksh (0.026 657 m²)
# SA10 -  344 cpad  (97.165 mm) ×    520 cpad   (137.174 mm) = 0.0032 0520 ksh (0.013 329 m²)
# SA11 -  240 cpad  (68.587 mm) ×    344 cpad    (97.165 mm) = 0.0014 0240 ksh (0.006 664 m²)
# SA12 -  152 cpad  (48.583 mm) ×    240 cpad    (68.587 mm) = 0.0005 0120 ksh (0.003 332 m²)
# SA13 -  120 cpad  (34.294 mm) ×    152 cpad    (48.583 mm) = 0.0002 3040 ksh (0.001 666 m²)
# SA14 -   54 cpad  (24.291 mm) ×    120 cpad    (34.294 mm) = 0.0001 1320 ksh (0.000 833 m²)
# SA15 -   40 cpad  (17.147 mm) ×     54 cpad    (24.291 mm) = 0.0000 3440 ksh (0.000 417 m²)
# SA20 -   25 cpad  (12.146 mm) ×     40 cpad    (17.147 mm) = 0.0000 1520 ksh (0.000 208 m²)
#
# Size       Width                     Height                      Area
# SB00 - 1,0000 cpad (925.926 mm) × 1,2253 cpad (1,309.585 mm) = 1.2253 0000 ksh (1.212 579 m²)
# SB01 -   4124 cpad (654.435 mm) × 1,0000 cpad   (925.926 mm) = 0.4124 0000 ksh (0.605 958 m²)
# SB02 -   2555 cpad (462.249 mm) ×   4124 cpad   (654.435 mm) = 0.2041 1432 ksh (0.302 512 m²)
# SB03 -   2041 cpad (326.503 mm) ×   2555 cpad   (462.249 mm) = 0.1020 0515 ksh (0.150 926 m²)
# SB04 -   1255 cpad (230.767 mm) ×   2041 cpad   (326.503 mm) = 0.0305 5215 ksh (0.075 346 m²)
# SB05 -   1020 cpad (162.894 mm) ×   1255 cpad   (230.767 mm) = 0.0132 4540 ksh (0.037 591 m²)
# SB10 -    425 cpad (115.026 mm) ×   1020 cpad   (162.894 mm) = 0.0044 1540 ksh (0.018 737 m²)
# SB11 -    305 cpad  (80.733 mm) ×    425 cpad   (115.026 mm) = 0.0022 0121 ksh (0.009 286 m²)
# SB12 -    211 cpad  (56.441 mm) ×    305 cpad    (80.733 mm) = 0.0010 5155 ksh (0.004 557 m²)
# SB13 -    131 cpad  (39.295 mm) ×    211 cpad    (56.441 mm) = 0.0003 2041 ksh (0.002 218 m²)
# SB14 -    102 cpad  (27.149 mm) ×    131 cpad    (39.295 mm) = 0.0001 3402 ksh (0.001 067 m²)
# SB15 -     42 cpad  (18.576 mm) ×    102 cpad    (27.149 mm) = 0.0000 4324 ksh (0.000 504 m²)
# SB20 -     30 cpad  (12.860 mm) ×     42 cpad    (18.576 mm) = 0.0000 2100 ksh (0.000 239 m²)
#
# Size      Width                    Height                      Area
# SC00 - 5300 cpad (848.765 mm) × 1,1441 cpad (1,200.989 mm) = 1.1044 0000 ksh (1.019 357 m²)
# SC01 - 3520 cpad (600.137 mm) ×   5300 cpad   (848.765 mm) = 0.3322 0000 ksh (0.509 375 m²)
# SC02 - 2425 cpad (423.668 mm) ×   3520 cpad   (600.137 mm) = 0.1440 2040 ksh (0.254 259 m²)
# SC03 - 1535 cpad (299.354 mm) ×   2425 cpad   (423.668 mm) = 0.0515 4151 ksh (0.126 827 m²)
# SC04 - 1212 cpad (211.477 mm) ×   1535 cpad   (299.354 mm) = 0.0235 4104 ksh (0.063 306 m²)
# SC05 -  545 cpad (149.320 mm) ×   1212 cpad   (211.477 mm) = 0.0115 4224 ksh (0.031 578 m²)
# SC10 -  403 cpad (105.024 mm) ×    545 cpad   (149.320 mm) = 0.0035 4123 ksh (0.015 682 m²)
# SC11 -  251 cpad  (73.588 mm) ×    403 cpad   (105.024 mm) = 0.0015 4033 ksh (0.007 729 m²)
# SC12 -  200 cpad  (51.440 mm) ×    251 cpad    (73.588 mm) = 0.0005 4200 ksh (0.003 785 m²)
# SC13 -  122 cpad  (35.722 mm) ×    200 cpad    (51.440 mm) = 0.0002 4400 ksh (0.001 838 m²)
# SC14 -   55 cpad  (25.006 mm) ×    122 cpad    (35.722 mm) = 0.0001 2034 ksh (0.000 893 m²)
# SC15 -   40 cpad  (17.147 mm) ×     55 cpad    (25.006 mm) = 0.0000 3520 ksh (0.000 429 m²)
# SC20 -   24 cpad  (11.431 mm) ×     40 cpad    (17.147 mm) = 0.0000 1440 ksh (0.000 196 m²)
#
# Size      Width                    Height                      Area
# SD00 - 4343 cpad (713.735 mm) × 1_0314 cpad (1,010.231 mm) = 0.5013 5430 ksh (0.721 037 m²)
# SD01 - 3134 cpad (504.401 mm) ×   4343 cpad   (713.735 mm) = 0.2304 1130 ksh (0.360 009 m²)
# SD02 - 2151 cpad (356.510 mm) ×   3134 cpad   (504.401 mm) = 0.1131 4554 ksh (0.179 824 m²)
# SD03 - 1344 cpad (251.486 mm) ×   2151 cpad   (356.510 mm) = 0.0343 3104 ksh (0.089 657 m²)
# SD04 - 1052 cpad (177.183 mm) ×   1344 cpad   (251.486 mm) = 0.0151 2052 ksh (0.044 559 m²)
# SD05 -  451 cpad (125.029 mm) ×   1052 cpad   (177.183 mm) = 0.0053 2532 ksh (0.022 153 m²)
# SD10 -  323 cpad  (87.877 mm) ×    451 cpad   (125.029 mm) = 0.0024 3353 ksh (0.010 987 m²)
# SD11 -  222 cpad  (61.443 mm) ×    323 cpad    (87.877 mm) = 0.0012 0550 ksh (0.005 399 m²)
# SD12 -  140 cpad  (42.867 mm) ×    222 cpad    (61.443 mm) = 0.0003 5520 ksh (0.002 634 m²)
# SD13 -  110 cpad  (30.007 mm) ×    140 cpad    (42.867 mm) = 0.0001 5400 ksh (0.001 286 m²)
# SD14 -   45 cpad  (20.719 mm) ×    110 cpad    (30.007 mm) = 0.0000 5350 ksh (0.000 622 m²)
# SD15 -   32 cpad  (14.289 mm) ×     45 cpad    (20.719 mm) = 0.0000 2404 ksh (0.000 296 m²)
# SD20 -   22 cpad  (10.002 mm) ×     32 cpad    (14.289 mm) = 0.0000 1144 ksh (0.000 143 m²)
#

SA00 = (Sezimal('5014'), Sezimal('1_1045'), Sezimal('1.000_002_02'))
SA01 = (Sezimal('3323'),   Sezimal('5014'), Sezimal('0.300_024_10'))
SA02 = (Sezimal('2305'),   Sezimal('3323'), Sezimal('0.125_544_54'))
SA03 = (Sezimal('1441'),   Sezimal('2305'), Sezimal('0.042_552_25'))
SA04 = (Sezimal('1132'),   Sezimal('1441'), Sezimal('0.021_244_52'))
SA05 = ( Sezimal('520'),   Sezimal('1132'), Sezimal('0.010_414_40'))
SA10 = ( Sezimal('344'),    Sezimal('520'), Sezimal('0.003_205_20'))
SA11 = ( Sezimal('240'),    Sezimal('344'), Sezimal('0.001_402_40'))
SA12 = ( Sezimal('152'),    Sezimal('240'), Sezimal('0.000_501_20'))
SA13 = ( Sezimal('120'),    Sezimal('152'), Sezimal('0.000_230_40'))
SA14 = (  Sezimal('54'),    Sezimal('120'), Sezimal('0.000_113_20'))
SA15 = (  Sezimal('40'),     Sezimal('54'), Sezimal('0.000_034_40'))
SA20 = (  Sezimal('25'),     Sezimal('40'), Sezimal('0.000_015_20'))

SB00 = (Sezimal('1_0000'), Sezimal('1_2253'), Sezimal('1.225_300_00'))
SB01 = (  Sezimal('4124'), Sezimal('1_0000'), Sezimal('0.412_400_00'))
SB02 = (  Sezimal('2555'),   Sezimal('4124'), Sezimal('0.204_114_32'))
SB03 = (  Sezimal('2041'),   Sezimal('2555'), Sezimal('0.102_005_15'))
SB04 = (  Sezimal('1255'),   Sezimal('2041'), Sezimal('0.030_552_15'))
SB05 = (  Sezimal('1020'),   Sezimal('1255'), Sezimal('0.013_245_40'))
SB10 = (   Sezimal('425'),   Sezimal('1020'), Sezimal('0.004_415_40'))
SB11 = (   Sezimal('305'),    Sezimal('425'), Sezimal('0.002_201_21'))
SB12 = (   Sezimal('211'),    Sezimal('305'), Sezimal('0.001_051_55'))
SB13 = (   Sezimal('131'),    Sezimal('211'), Sezimal('0.000_320_41'))
SB14 = (   Sezimal('102'),    Sezimal('131'), Sezimal('0.000_134_02'))
SB15 = (    Sezimal('42'),    Sezimal('102'), Sezimal('0.000_043_24'))
SB20 = (    Sezimal('30'),     Sezimal('42'), Sezimal('0.000_021_00'))

SC00 = (Sezimal('5300'), Sezimal('1_1441'), Sezimal('1.1044_53'))
SC01 = (Sezimal('3520'), Sezimal('5300'), Sezimal('0.3322'))
SC02 = (Sezimal('2425'), Sezimal('3520'), Sezimal('0.1440_204'))
SC03 = (Sezimal('1535'), Sezimal('2425'), Sezimal('0.051_541_51'))
SC04 = (Sezimal('1212'), Sezimal('1535'), Sezimal('0.023_541_04'))
SC05 = (Sezimal('545'), Sezimal('1212'), Sezimal('0.011_542_24'))
SC10 = (Sezimal('403'), Sezimal('545'), Sezimal('0.003_541_23'))
SC11 = (Sezimal('251'), Sezimal('403'), Sezimal('0.001_540_33'))
SC12 = (Sezimal('200'), Sezimal('251'), Sezimal('0.0005_42'))
SC13 = (Sezimal('122'), Sezimal('200'), Sezimal('0.0002_44'))
SC14 = (Sezimal('55'), Sezimal('122'), Sezimal('0.000_120_34'))
SC15 = (Sezimal('40'), Sezimal('55'), Sezimal('0.0000_352'))
SC20 = (Sezimal('24'), Sezimal('40'), Sezimal('0.0000_144'))

SD00 = (Sezimal('4343'), Sezimal('1_0314'), Sezimal('0.501_354_30'))
SD01 = (Sezimal('3134'),   Sezimal('4343'), Sezimal('0.230_411_30'))
SD02 = (Sezimal('2151'),   Sezimal('3134'), Sezimal('0.113_145_54'))
SD03 = (Sezimal('1344'),   Sezimal('2151'), Sezimal('0.034_331_04'))
SD04 = (Sezimal('1052'),   Sezimal('1344'), Sezimal('0.015_120_52'))
SD05 = ( Sezimal('451'),   Sezimal('1052'), Sezimal('0.005_325_32'))
SD10 = ( Sezimal('323'),    Sezimal('451'), Sezimal('0.002_433_53'))
SD11 = ( Sezimal('222'),    Sezimal('323'), Sezimal('0.001_205_50'))
SD12 = ( Sezimal('140'),    Sezimal('222'), Sezimal('0.000_355_20'))
SD13 = ( Sezimal('110'),    Sezimal('140'), Sezimal('0.000_154_00'))
SD14 = (  Sezimal('45'),    Sezimal('110'), Sezimal('0.000_053_50'))
SD15 = (  Sezimal('32'),     Sezimal('45'), Sezimal('0.000_024_04'))
SD20 = (  Sezimal('22'),     Sezimal('32'), Sezimal('0.000_011_44'))

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
        height_cpad = SI(height * 1_0000)
        width_cpad = SI(height_cpad / SQRT_2)
        width = width_cpad / 1_0000
        area_keshe = height_cpad * width_cpad / 1_0000_0000

        height_mm = round((height * PADA_TO_METER).decimal * 1_000, 3)
        width_mm = round((width * PADA_TO_METER).decimal * 1_000, 3)
        area_m2 = round(height_mm / 1_000 * width_mm / 1_000, 6)

        print(f'S{series_name}{str(i).zfill(2)} - {width_cpad.formatted_number} cpad ({width_mm} mm) × {height_cpad.formatted_number} cpad ({height_mm} mm) = {area_keshe.formatted_number} ksh ({area_m2} m²)')
        print(f"S{series_name}{str(i).zfill(2)} = (Sezimal('{width_cpad.formatted_number}'), Sezimal('{height_cpad.formatted_number}'), Sezimal('{area_keshe.formatted_number}'))")

        height = width


if __name__ == '__main__':
    from swixknife import SezimalInteger as SI
    from swixknife import SezimalRange
    from swixknife.units import PADA_TO_METER
    from swixknife.constants import SQRT_2

    _calc_paper_size_series(Sezimal('1.1045'), 'A')
    _calc_paper_size_series(Sezimal('1.2253'), 'B')
    _calc_paper_size_series(Sezimal('1.1441'), 'C')
    _calc_paper_size_series(Sezimal('1.0314'), 'D')
