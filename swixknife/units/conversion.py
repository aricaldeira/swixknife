
__all__ = (
    'sezimal_to_decimal_unit', 'sezimal_to_sezimal_unit',
    'decimal_to_sezimal_unit', 'decimal_to_decimal_unit',
)

from typing import TypeVar

Dozenal = TypeVar('Dozenal', bound='Dozenal')
DozenalInteger = TypeVar('DozenalInteger', bound='DozenalInteger')
DozenalFraction = TypeVar('DozenalFraction', bound='DozenalFraction')


from ..base import sezimal_context
from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..exponents import sezimal_symbol_to_exponent, sezimal_exponent_to_symbol, \
    sezimal_exponent_to_factor, decimal_symbol_to_exponent, \
    decimal_exponent_to_factor, binary_symbol_to_exponent, \
    binary_exponent_to_factor
from decimal import Decimal


from .conversion_factor import UNIT_CONVERSION


def _identify_validate_sezimal_unit(sezimal_unit: str) -> (str, str, SezimalFraction):
    if not sezimal_unit:
        raise ValueError('Informing the symbol of the Shastadari is mandatory')
    elif len(sezimal_unit) < 3:
        raise ValueError(f'Invalid Shastadari unit [{sezimal_unit}]')

    sezimal_unit = sezimal_unit.replace('⁻', '-').replace('¹', '1')
    sezimal_unit = sezimal_unit.replace('²', '2').replace('³', '3')
    sezimal_unit = sezimal_unit.replace('τ\u202f', 'tau_').replace('τ ', 'tau_').replace('τ ', 'tau_')
    sezimal_unit = sezimal_unit.replace('π\u202f', 'pi_').replace('π ', 'pi_').replace('π ', 'pi_')

    #
    # Let’s convert pad² to ktr
    #
    if sezimal_unit.endswith('pad2'):
        prefix = sezimal_unit.replace('pad2', '')

        if prefix:
            exponent = sezimal_symbol_to_exponent(prefix)
            exponent *= 2
            prefix = sezimal_exponent_to_symbol(exponent)

        sezimal_unit = prefix + 'ktr'

    if sezimal_unit.endswith('pad3'):
        prefix = sezimal_unit.replace('pad3', '')

        if prefix:
            exponent = sezimal_symbol_to_exponent(prefix)
            exponent *= 3
            prefix = sezimal_exponent_to_symbol(exponent)

        sezimal_unit = prefix + 'ayt'

    if 'p/' in sezimal_unit:
        sp, su = sezimal_unit.split('p/')
        su = 'p/' + su
    else:
        su = sezimal_unit[-3:]
        sp = sezimal_unit[0:-3]

    if su not in UNIT_CONVERSION:
        raise ValueError(f'Invalid Shastadari unit [{su}]')

    try:
        se = sezimal_symbol_to_exponent(sp)
    except:
        raise ValueError(f'Invalid Shastadari prefix [{sp}]')

    spf = sezimal_exponent_to_factor(se, True)

    return sp, su, spf


def _identify_validate_decimal_unit(decimal_unit: str, sezimal_unit: str = None) -> (str, str, SezimalFraction):
    if not decimal_unit:
        raise ValueError('Informing the symbol of the decimal unit is mandatory')

    decimal_unit = decimal_unit.replace('⁻', '-').replace('¹', '1')
    decimal_unit = decimal_unit.replace('²', '2').replace('³', '3')
    decimal_unit = decimal_unit.replace('τ\u202f', 'tau_').replace('τ ', 'tau_').replace('τ ', 'tau_')
    decimal_unit = decimal_unit.replace('π\u202f', 'pi_').replace('π ', 'pi_').replace('π ', 'pi_')

    if not sezimal_unit:
        for su in UNIT_CONVERSION:
            if decimal_unit in UNIT_CONVERSION[su]:
                sezimal_unit = su
                break

    if not sezimal_unit:
        for su in UNIT_CONVERSION:
            if len(decimal_unit) >= 2 and decimal_unit[1:] in UNIT_CONVERSION[su]:
                sezimal_unit = su
                break
            #
            # Binary prefixes and “da”
            #
            elif len(decimal_unit) >= 3 and decimal_unit[2:] in UNIT_CONVERSION[su]:
                sezimal_unit = su
                break

    if not sezimal_unit:
        raise ValueError(f'Invalid decimal unit [{decimal_unit}]')

    if decimal_unit not in UNIT_CONVERSION[sezimal_unit]:
        #
        # Maybe there’s a prefix, let’s remove it
        #
        if len(decimal_unit) >= 2 and decimal_unit[1:] in UNIT_CONVERSION[sezimal_unit]:
            pass

        #
        # Binary prefixes and “da”
        #
        elif len(decimal_unit) >= 3 and decimal_unit[2:] in UNIT_CONVERSION[sezimal_unit]:
            pass

        else:
            raise ValueError(f'Invalid decimal unit [{decimal_unit}] paired with Shastadari unit [{sezimal_unit}]')

    binary_prefix = False

    #
    # Let’s see if the decimal unit uses SI prefixes
    #
    if decimal_unit in UNIT_CONVERSION[sezimal_unit]['non_prefixed']:
        du = decimal_unit
        dp = ''
    elif decimal_unit in UNIT_CONVERSION[sezimal_unit]:
        du = decimal_unit
        dp = ''
    #
    # The unit is prefixed, and the prefix is a binary prefix
    # Binary prefixes too the form [KMGTPEZYRQ]i
    #
    elif len(decimal_unit) >= 3 \
        and decimal_unit[0] in 'KMGTPEZYRQ' \
        and decimal_unit[1] == 'i':
        dp = decimal_unit[0:2]
        du = decimal_unit[2:]
        binary_prefix = True
    #
    # The unit is prefixed, and the prefix is da
    #
    elif len(decimal_unit) >= 3 and decimal_unit[0:2] == 'da':
        dp = decimal_unit[0:2]
        du = decimal_unit[2:]
    #
    # The unit is prefixed, and the prefix is a single letter
    #
    else:
        dp = decimal_unit[0]
        du = decimal_unit[1:]

    try:
        if binary_prefix:
            de = binary_symbol_to_exponent(dp)
        else:
            de = decimal_symbol_to_exponent(dp)
    except:
        if binary_prefix:
            raise ValueError(f'Invalid binary prefix [{dp}]')
        else:
            raise ValueError(f'Invalid S.I. prefix [{dp}]')

    if du[-1] == '2':
        de *= 2
    elif du[-1] == '3':
        de *= 3

    if binary_prefix:
        dpf = binary_exponent_to_factor(de, True)
    else:
        dpf = decimal_exponent_to_factor(de, True)

    if 'adjust' in UNIT_CONVERSION[sezimal_unit] \
        and du in UNIT_CONVERSION[sezimal_unit]['adjust']:
        da = UNIT_CONVERSION[sezimal_unit]['adjust'][du]
    else:
        da = SezimalInteger(0)

    return dp, du, dpf, da


def _identify_validate_prefix_unit(sezimal_unit: str, decimal_unit: str):
    sp, su, spf = _identify_validate_sezimal_unit(sezimal_unit)
    dp, du, dpf, da = _identify_validate_decimal_unit(decimal_unit, su)

    sezimal_context.use_ultra_precision()

    factor = spf * UNIT_CONVERSION[su][du] / dpf

    sezimal_context.back_to_regular_precision()

    return factor, da


def sezimal_to_decimal_unit(measure: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction, sezimal_unit: str, decimal_unit: str, return_fraction: bool = False, simplify_fraction: bool = True) -> Sezimal | SezimalInteger | SezimalFraction:
    factor, adjust = _identify_validate_prefix_unit(sezimal_unit, decimal_unit)

    sezimal_context.use_ultra_precision()
    original_fraction_simplify = sezimal_context.fractions_simplify
    sezimal_context.fractions_simplify = False

    if type(measure) in (str, int, float, Decimal):
        measure = Sezimal(measure)

    if return_fraction and type(measure) != SezimalFraction:
        measure = SezimalFraction(*measure.as_integer_ratio())

    if factor >= 0:
        measure *= factor
    else:
        measure = (1 / measure) * (factor * -1)

    if adjust:
        measure += adjust

    sezimal_context.back_to_regular_precision()
    sezimal_context.fractions_simplify = original_fraction_simplify

    if not return_fraction:
        measure = round(measure, sezimal_context.precision)
    elif type(measure) == SezimalFraction and simplify_fraction:
        measure = measure.simplify()

    return measure


def sezimal_to_sezimal_unit(measure: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction, sezimal_unit_1: str, sezimal_unit_2, return_fraction: bool = False, simplify_fraction: bool = True) -> Sezimal | SezimalInteger | SezimalFraction:
    sp_1, su_1, spf_1 = _identify_validate_sezimal_unit(sezimal_unit_1)
    sp_2, su_2, spf_2 = _identify_validate_sezimal_unit(sezimal_unit_2)

    if su_1 != su_2 \
        and (not (
            su_1 in ('tap', 'gtk')
            and su_2 in ('tap', 'gtk')
        )) \
        and (not (
            su_1 in ('vrx', 'mas', 'spt', 'din', 'uta', 'pox', 'agm', 'ang', 'bod')
            and su_2 in ('vrx', 'mas', 'spt', 'din', 'uta', 'pox', 'agm', 'ang', 'bod')
        )) \
        and (not (
            su_1 in ('clt', 'pbt')
            and su_2 in ('clt', 'pbt')
        )):
        raise ValueError(f'Invalid conversion between units [{sezimal_unit_1}] and [{sezimal_unit_2}]')

    sezimal_context.use_ultra_precision()
    original_fraction_simplify = sezimal_context.fractions_simplify
    sezimal_context.fractions_simplify = False

    if type(measure) in (str, int, float, Decimal):
        measure = Sezimal(measure)

    if return_fraction and type(measure) != SezimalFraction:
        measure = SezimalFraction(*measure.as_integer_ratio())

    measure *= spf_1

    if su_1 == 'tap' and su_2 == 'gtk':
        measure *= SezimalInteger('100_000')
        measure += SezimalInteger('240_234_312')
    elif su_1 == 'gtk' and su_2 == 'tap':
        measure -= SezimalInteger('240_234_312')
        measure /= SezimalInteger('100_000')

    if su_1 in ('vrx', 'mas', 'spt', 'din', 'uta', 'pox', 'agm', 'ang', 'bod'):
        measure /= UNIT_CONVERSION[su_1]['ang']

    if su_2 in ('vrx', 'mas', 'spt', 'din', 'uta', 'pox', 'agm', 'ang', 'bod'):
        measure *= UNIT_CONVERSION[su_2]['ang']

    #
    # Reciprocal conversion
    #
    if (su_1 == 'clt' and su_2 == 'pbt') or (su_1 == 'pbt' and su_2 == 'clt'):
        measure = 1 / measure

    measure /= spf_2

    sezimal_context.back_to_regular_precision()

    if not return_fraction:
        measure = round(measure, sezimal_context.precision)
    elif type(measure) == SezimalFraction and simplify_fraction:
        measure = measure.simplify()

    return measure


def decimal_to_sezimal_unit(measure: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction, decimal_unit: str, sezimal_unit: str, return_fraction: bool = False, simplify_fraction: bool = True) -> Sezimal | SezimalInteger | SezimalFraction:
    factor, adjust = _identify_validate_prefix_unit(sezimal_unit, decimal_unit)

    sezimal_context.use_ultra_precision()
    original_fraction_simplify = sezimal_context.fractions_simplify
    sezimal_context.fractions_simplify = False

    if type(measure) in (str, int, float, Decimal):
        measure = Sezimal(measure)

    if return_fraction and type(measure) != SezimalFraction:
        measure = SezimalFraction(*measure.as_integer_ratio())

    if adjust:
        measure -= adjust

    measure /= factor

    sezimal_context.back_to_regular_precision()
    sezimal_context.fractions_simplify = original_fraction_simplify

    if not return_fraction:
        measure = round(measure, sezimal_context.precision)
    elif type(measure) == SezimalFraction and simplify_fraction:
        measure = measure.simplify()

    return measure


def decimal_to_decimal_unit(measure: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction, decimal_unit_1: str, decimal_unit_2: str, return_fraction: bool = False, simplify_fraction: bool = True) -> Sezimal | SezimalInteger | SezimalFraction:
    sezimal_unit_1 = ''
    sezimal_unit_2 = ''

    for su in UNIT_CONVERSION:
        if decimal_unit_1 in UNIT_CONVERSION[su]:
            sezimal_unit_1 = su
            break

    if not sezimal_unit_1:
        for su in UNIT_CONVERSION:
            if decimal_unit_1[1:] in UNIT_CONVERSION[su]:
                sezimal_unit_1 = su
                break

    for su in UNIT_CONVERSION:
        if decimal_unit_2 in UNIT_CONVERSION[su]:
            sezimal_unit_2 = su
            break

    if not sezimal_unit_2:
        for su in UNIT_CONVERSION:
            if decimal_unit_2[1:] in UNIT_CONVERSION[su]:
                sezimal_unit_2 = su
                break

    measure = decimal_to_sezimal_unit(measure, decimal_unit_1, sezimal_unit_1, return_fraction=True, simplify_fraction=False)

    if sezimal_unit_1 != sezimal_unit_2:
        measure = sezimal_to_sezimal_unit(measure, sezimal_unit_1, sezimal_unit_2, return_fraction=True, simplify_fraction=False)

    measure = sezimal_to_decimal_unit(measure, sezimal_unit_2, decimal_unit_2, return_fraction=True, simplify_fraction=False)

    if not return_fraction:
        measure = round(measure, sezimal_context.precision)
    elif type(measure) == SezimalFraction and simplify_fraction:
        measure = measure.simplify()

    return measure
