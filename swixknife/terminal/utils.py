
from .. import Sezimal, SezimalInteger, SezimalDateTime, \
    sezimal_locale, SezimalLocale, \
    sezimal_exponent_to_symbol, decimal_exponent_to_symbol

from decimal import Decimal


def sezimal_format(value: Sezimal | SezimalInteger, unit: str, locale: SezimalLocale, sezimal_places: SezimalInteger = 0, use_prefixes: bool = True, dedicated_digits: bool = False) -> str:
    sezimal_places = SezimalInteger(sezimal_places)

    if len(str(value)) <= 4:
        power = 0
    else:
        power = (len(str(value)) // 4) * 4

        if len(str(value)) == power:
            power -= 4

    if (not use_prefixes) or (power == 0) or (not unit):
        return locale.format_number(value, sezimal_places=0, suffix=unit, dedicated_digits=dedicated_digits)

    value = value / (Sezimal(10) ** Sezimal(Decimal(power)))
    unit = sezimal_exponent_to_symbol(Decimal(power)) + unit
    return locale.format_number(value, sezimal_places, suffix=unit, dedicated_digits=dedicated_digits)


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
