
from swixknife import sezimal_context, \
    Sezimal, SezimalInteger, SezimalFraction, \
    Dozenal, DozenalInteger, DozenalFraction, \
    SezimalDate, SezimalTime, SezimalDateTime

from decimal import Decimal
from fractions import Fraction as DecimalFraction

import datetime


def pyspread_format_sezimal(value: Sezimal | SezimalInteger) -> str:
    if value._fraction.replace('0', '') != '':
        return sezimal_context.locale.format_number(
            value,
            sezimal_places=sezimal_context.sezimal_precision,
            recurring_digits_notation=sezimal_context.show_recurring_digits,
            minimum_size=sezimal_context.minimum_size,
            use_fraction_group_separator=True,
            sezimal_digits=sezimal_context.sezimal_digits,
            sezimal_punctuation=sezimal_context.sezimal_punctuation,
        )

    else:
        return sezimal_context.locale.format_number(
            value,
            sezimal_places=0,
            minimum_size=sezimal_context.minimum_size,
            sezimal_digits=sezimal_context.sezimal_digits,
            sezimal_punctuation=sezimal_context.sezimal_punctuation,
        )


def pyspread_format_sezimal_fraction(value: SezimalFraction) -> str:
    return sezimal_context.locale.format_number(
            value.numerator,
            sezimal_places=0,
            sezimal_digits=sezimal_context.sezimal_digits,
            sezimal_punctuation=sezimal_context.sezimal_punctuation,
        ) + ' / ' + sezimal_context.locale.format_number(
            value.denominator,
            minimum_size=sezimal_context.minimum_size,
            sezimal_places=0,
            sezimal_digits=sezimal_context.sezimal_digits,
            sezimal_punctuation=sezimal_context.sezimal_punctuation,
        )


def pyspread_format_dozenal(value: Dozenal | DozenalInteger) -> str:
    if value._fraction:
        return sezimal_context.locale.format_dozenal_number(
            value,
            dozenal_places=sezimal_context.dozenal_precision,
            recurring_digits_notation=6 if sezimal_context.show_recurring_digits else False,
            use_fraction_group_separator=True,
        )

    else:
        return sezimal_context.locale.format_dozenal_number(
            value,
            dozenal_places=0,
        )


def pyspread_format_dozenal_fraction(value: DozenalFraction) -> str:
    return sezimal_context.locale.format_dozenal_number(
            value.numerator,
            dozenal_places=0,
        ) + ' / ' + sezimal_context.locale.format_dozenal_number(
            value.denominator,
            dozenal_places=0,
        )


def pyspread_format_decimal(value: Decimal | float | int) -> str:
    if value != int(value):
        return sezimal_context.locale.format_decimal_number(
            Decimal(str(value)),
            decimal_places=sezimal_context.decimal_precision,
            recurring_digits_notation=6 if sezimal_context.show_recurring_digits else False,
            use_fraction_group_separator=True,
        )
    else:
        return sezimal_context.locale.format_decimal_number(
            value,
            decimal_places=0,
        )


def pyspread_format_decimal_fraction(value: DecimalFraction) -> str:
    return sezimal_context.locale.format_decimal_number(
            value.numerator,
            decimal_places=0,
        ) + ' / ' + sezimal_context.locale.format_decimal_number(
            value.denominator,
            decimal_places=0,
        )


def pyspread_format_sezimal_date(value: SezimalDate) -> str:
    return value.format(
        sezimal_context.locale.DATE_FORMAT,
        sezimal_context.locale,
    )


def pyspread_format_sezimal_time(value: SezimalTime) -> str:
    return value.format(
        sezimal_context.locale.TIME_FORMAT,
        sezimal_context.locale,
    )


def pyspread_format_sezimal_date_time(value: SezimalDateTime) -> str:
    return value.format(
        sezimal_context.locale.DATE_TIME_FORMAT,
        sezimal_context.locale,
    )


def pyspread_format_date(value: datetime.date) -> str:
    return SezimalDate(value).format(
        sezimal_context.locale.ISO_DATE_FORMAT,
        sezimal_context.locale,
    )


def pyspread_format_time(value: datetime.time) -> str:
    return SezimalTime(value).format(
        sezimal_context.locale.ISO_TIME_FORMAT,
        sezimal_context.locale,
    )


def pyspread_format_date_time(value: datetime.datetime) -> str:
    return SezimalDateTime(value).format(
        sezimal_context.locale.ISO_DATE_FORMAT + ' ' + sezimal_context.locale.ISO_TIME_FORMAT,
        sezimal_context.locale,
    )


swixknife_pyspread_formatting = {
    Sezimal: pyspread_format_sezimal,
    SezimalInteger: pyspread_format_sezimal,
    SezimalFraction: pyspread_format_sezimal_fraction,
    Dozenal: pyspread_format_dozenal,
    DozenalInteger: pyspread_format_dozenal,
    DozenalFraction: pyspread_format_dozenal_fraction,
    Decimal: pyspread_format_decimal,
    int: pyspread_format_decimal,
    float: pyspread_format_decimal,
    DecimalFraction: pyspread_format_decimal_fraction,
    SezimalDate: pyspread_format_sezimal_date,
    SezimalTime: pyspread_format_sezimal_time,
    SezimalDateTime: pyspread_format_sezimal_date_time,
    datetime.date: pyspread_format_date,
    datetime.time: pyspread_format_time,
    datetime.datetime: pyspread_format_date_time,
}
