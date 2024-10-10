
from .. import Sezimal, SezimalInteger, SezimalDateTime, \
    sezimal_locale, SezimalLocale, \
    sezimal_exponent_to_symbol, decimal_exponent_to_symbol

from decimal import Decimal


def sezimal_format(value: Sezimal | SezimalInteger, unit: str, locale: SezimalLocale, sezimal_places: SezimalInteger = 0, use_prefixes: bool | int = True, sezimal_digits: bool = False, sezimal_punctuation: bool = False) -> str:
    sezimal_places = SezimalInteger(sezimal_places)

    if type(use_prefixes) == int and use_prefixes > 0:
        if len(str(value)) <= use_prefixes:
            power = 0
        else:
            power = (len(str(value)) // use_prefixes) * use_prefixes

            if len(str(value)) == power:
                power -= use_prefixes

    else:
        power = len(str(value)) - 1

    if (not use_prefixes) or (power == 0) or (not unit):
        return locale.format_number(value, sezimal_places=0, suffix=unit, sezimal_digits=sezimal_digits)

    value = value / (Sezimal(10) ** Sezimal(Decimal(power)))
    unit = sezimal_exponent_to_symbol(Decimal(power)) + unit
    # power = Sezimal(Decimal(power)).formatted_number
    # power = power.replace('0', '⁰').replace('1', '¹').replace('2', '²')
    # power = power.replace('3', '³').replace('4', '⁴').replace('5', '⁵')
    # unit = power + unit
    # unit = Sezimal(Decimal(power)).formatted_number + '↑' + unit
    return locale.format_number(value, sezimal_places, suffix=unit, sezimal_digits=sezimal_digits, sezimal_punctuation=sezimal_punctuation)


def decimal_format(value: Sezimal | SezimalInteger, unit: str, locale: SezimalLocale, decimal_places: SezimalInteger = 0, use_prefixes: bool = True) -> str:
    decimal_places = SezimalInteger(decimal_places)

    if len(str(value.decimal)) <= 3:
        power = 0
    else:
        power = (len(str(value.decimal)) // 3) * 3

        if len(str(value.decimal)) == power:
            power -= 3

    if (not use_prefixes) or (power == 0) or (not unit):
        return locale.format_decimal_number(value, decimal_places=0, suffix=unit)

    value = value / (Sezimal(14) ** Sezimal(Decimal(power)))
    unit = decimal_exponent_to_symbol(Decimal(power)) + unit
    return locale.format_decimal_number(value, decimal_places, suffix=unit)


def dozenal_format(value: Sezimal | SezimalInteger, unit: str, locale: SezimalLocale, dozenal_places: SezimalInteger = 0, use_prefixes: bool = True) -> str:
    dozenal_places = SezimalInteger(dozenal_places)

    if len(str(value)) <= 4:
        power = 0
    else:
        power = (len(str(value)) // 4) * 4

        if len(str(value)) == power:
            power -= 4

    if (not use_prefixes) or (power == 0) or (not unit):
        return locale.format_dozenal_number(value, dozenal_places=0, suffix=unit)

    value = value / (Sezimal(20) ** Sezimal(Decimal(power)))
    unit = Sezimal(Decimal(power)).dozenal_formatted_number + '↑' + unit
    return locale.format_dozenal_number(value, dozenal_places, suffix=unit)
