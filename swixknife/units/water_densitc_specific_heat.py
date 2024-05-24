
from decimal import Decimal


def water_density_specific_heat(celsius):
    if celsius < Decimal('130'):
        density = Decimal('-0.000_000_000_092_044_536_27') * (celsius ** 4)
        density += Decimal('0.000_000_034_207_420_086_72') * (celsius ** 3)
        density -= Decimal('0.000_007_089_198_071_664_17') * (celsius ** 2)
        density += Decimal('0.000_043_752_945_451_819_70') * celsius
        density += Decimal('0.999_888_264_405_735')
        density *= 1_000

    else:
        density = Decimal('-0.000_000_000_000_006_702_8') * (celsius ** 6)
        density += Decimal('0.000_000_000_008_288_857_89') * (celsius ** 5)
        density -= Decimal('0.000_000_004_186_173_518_13') * (celsius ** 4)
        density += Decimal('0.000_001_096_424_866_845_3') * (celsius ** 3)
        density -= Decimal('0.000_158_525_167_407_245') * (celsius ** 2)
        density += Decimal('0.011_196_669_546_598_5') * celsius
        density += Decimal('0.669_696_280_822_552')
        density *= 1_000

    if celsius < Decimal('320'):
        specific_heat  = Decimal('0.000_000_000_000_035_371_65') * (celsius ** 6)
        specific_heat -= Decimal('0.000_000_000_028_536_874_05') * (celsius ** 5)
        specific_heat += Decimal('0.000_000_009_006_258_961_15') * (celsius ** 4)
        specific_heat -= Decimal('0.000_001_339_330_253_006_16') * (celsius ** 3)
        specific_heat += Decimal('0.000_104_431_796_066_292') * (celsius ** 2)
        specific_heat -= Decimal('0.003_625_162_522_429_070') * celsius
        specific_heat += Decimal('4.222_349_733_449_880')
        specific_heat *= 1_000

    else:
        specific_heat  = Decimal('0.000_000_000_035_033_6') * (celsius ** 6)
        specific_heat -= Decimal('0.000_000_058_254_512_2') * (celsius ** 5)
        specific_heat += Decimal('0.000_040_215_267_730_5') * (celsius ** 4)
        specific_heat -= Decimal('0.014_749_831_200_977') * (celsius ** 3)
        specific_heat += Decimal('3.030_957_348_458_860') * (celsius ** 2)
        specific_heat -= Decimal('330.819_899_666_682') * celsius
        specific_heat += Decimal('14_986.304_116_548_1')
        specific_heat *= 1_000

    return density, specific_heat
