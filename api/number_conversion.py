
__all__ = ('number_decimal_to_sezimal',)

from main import app

from swixknife.localization import sezimal_locale, SezimalLocale
from decimal import Decimal
from swixknife import Sezimal, Dozenal
from swixknife.base import sezimal_format, decimal_format, dozenal_format, niftimal_format
from swixknife import sezimal_context, validate_clean_decimal, niftimal_to_sezimal


@app.route('/api/number/<string:base_from>-to-<string:base_to>/<string:number>')
@app.route('/api/number/<string:locale>/<string:base_from>-to-<string:base_to>/<string:number>')
def number_decimal_to_sezimal(base_from: str = 'decimal', base_to: str = 'sezimal', number: str = '0', locale: str = None):
    if base_from == 'decimal':
        number = Sezimal(Decimal(validate_clean_decimal(number)))

    elif base_from == 'sezimal':
        number = Sezimal(number)

    elif base_from == 'dozenal':
        number = Sezimal(Dozenal(number))

    elif base_from == 'niftimal' or base_from == 'niftimal-alpha':
        number = Sezimal(niftimal_to_sezimal(number))

    if not locale:
        if base_to == 'decimal':
            if number._fraction:
                number = decimal_format(
                    number,
                    decimal_places=sezimal_context.decimal_precision,
                    recurring_digits_notation=6,
                    group_separator='',
                    fraction_group_separator='',
                )
            else:
                number = decimal_format(
                    number,
                    decimal_places=0,
                    group_separator='',
                    fraction_group_separator='',
                )

        elif base_to == 'sezimal':
            if number._fraction:
                number = sezimal_format(
                    number,
                    sezimal_places=sezimal_context.sezimal_precision,
                    recurring_digits_notation=10,
                    group_separator='',
                    fraction_group_separator='',
                )
            else:
                number = sezimal_format(
                    number,
                    sezimal_places=0,
                    group_separator='',
                    fraction_group_separator='',
                )

        elif base_to == 'dozenal':
            if number._fraction:
                number = dozenal_format(
                    number,
                    dozenal_places=sezimal_context.dozenal_precision,
                    recurring_digits_notation=6,
                    group_separator='',
                    fraction_group_separator='',
                )
            else:
                number = dozenal_format(
                    number,
                    dozenal_places=0,
                    group_separator='',
                    fraction_group_separator='',
                )

        elif base_to == 'niftimal' or base_to == 'niftimal-alpha':
            if number._fraction:
                number = niftimal_format(
                    number,
                    niftimal_places=sezimal_context.niftimal_precision,
                    recurring_digits_notation=10,
                    group_separator='',
                    fraction_group_separator='',
                    regularized_digits=base_to == 'niftimal',
                )
            else:
                number = niftimal_format(
                    number,
                    niftimal_places=0,
                    group_separator='',
                    fraction_group_separator='',
                    regularized_digits=base_to == 'niftimal',
                )

    else:
        locale = sezimal_locale(locale or 'iso')

        if base_to == 'decimal':
            if number._fraction:
                number = locale.format_decimal_number(
                    number,
                    decimal_places=sezimal_context.decimal_precision,
                    use_fraction_group_separator=True,
                    recurring_digits_notation=10,
                )
            else:
                number = locale.format_decimal_number(number, decimal_places=0)

        elif base_to == 'sezimal':
            if number._fraction:
                number = locale.format_number(
                    number,
                    sezimal_places=sezimal_context.sezimal_precision,
                    use_fraction_group_separator=True,
                    recurring_digits_notation=10,
                )
            else:
                number = locale.format_number(number, sezimal_places=0)

        elif base_to == 'dozenal':
            if number._fraction:
                number = locale.format_dozenal_number(
                    number,
                    dozenal_places=sezimal_context.dozenal_precision,
                    use_fraction_group_separator=True,
                    recurring_digits_notation=10,
                )
            else:
                number = locale.format_dozenal_number(number, dozenal_places=0)

        elif base_to == 'niftimal' or base_to == 'niftimal-alpha':
            if number._fraction:
                number = locale.format_niftimal_number(
                    number,
                    niftimal_places=sezimal_context.niftimal_precision,
                    use_fraction_group_separator=True,
                    recurring_digits_notation=10,
                    regularized_digits=base_to == 'niftimal',
                )
            else:
                number = locale.format_niftimal_number(
                    number,
                    niftimal_places=0,
                    regularized_digits=base_to == 'niftimal',
                )

    return number
