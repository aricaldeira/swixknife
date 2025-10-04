
import math
import matplotlib as mpl
import numpy as np


def colour_fader(c1, c2, mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1 = np.array(mpl.colors.to_rgb(c1))
    c2 = np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex(((1 - mix) * c1) + (mix * c2))


# from flask import Response, request
# from main import app, sitemapper, sezimal_render_template
# from locale_detection import browser_preferred_locale
# from today import _prepare_locale_from_cookie

from pydreamplet.shapes import ring, arc, star, polygon
from pydreamplet.core import TextOnPath
from swixknife.date_time.seasons_colors import weekly_season_colors
from swixknife.date_time import SezimalDateTime
from swixknife import SezimalInteger as SI, SezimalRange as SR
from swixknife.dozenal import DozenalInteger
from swixknife.base import default_to_sezimal_digits
from decimal import Decimal as D


# FONT_FAMILY = """'Andika', 'Sezimal QP', 'Sezimal Symbols', 'Noto Sans Hebrew', 'Noto Sans Arabic UI', 'Noto Sans Devanagari UI', 'Noto Sans Bengali UI', 'Inter Alia', 'Noto Sans Shavian', 'Noto Sans Symbols', 'Noto Sans Symbols2', sans-serif"""


# @app.route('/watchface.svg')
def watchface(locale, today) -> str:
    # today = today.from_days(today.as_days - 22 - 400)

    #
    # Let's bring the colours first
    #
    if locale.calendar_displayed == 'DCC':
        colours = weekly_season_colors(
            today.dcc_year,
            locale.DEFAULT_HEMISPHERE,
            locale.DEFAULT_TIME_ZONE,
            calendar='DCC',
        )
        gray = weekly_season_colors(
            today.dcc_year,
            locale.DEFAULT_HEMISPHERE,
            locale.DEFAULT_TIME_ZONE,
            gray_scale=True,
            calendar='DCC',
        )
        weeks = today.dcc_total_weeks_in_year + 1

    else:
        colours = weekly_season_colors(
            today.year,
            locale.DEFAULT_HEMISPHERE,
            locale.DEFAULT_TIME_ZONE,
            calendar='SYM'
        )
        gray = weekly_season_colors(
            today.year,
            locale.DEFAULT_HEMISPHERE,
            locale.DEFAULT_TIME_ZONE,
            gray_scale=True,
            calendar='SYM'
        )

        if today.is_leap or locale.calendar_displayed == 'ISO':
            weeks = SI(125)
        else:
            weeks = SI(124)

    # elif locale.calendar_displayed == 'ISO':
    #     colours = weekly_season_colors(
    #         today.year,
    #         locale.DEFAULT_HEMISPHERE,
    #         locale.DEFAULT_TIME_ZONE,
    #         calendar='ISO',
    #     )
    #
    #     if today.is_leap:
    #         weeks = SI(125)
    #     else:
    #         weeks = SI(124)

    wf = '<svg class="watchface" id="watchface" viewBox="0 0 216 216" onclick="watchface_toggle()">\n'

    wf += _weeks_display(locale, today, weeks, colours, gray)
    wf += _shastadari_logo(locale, gray, today)
    wf += _date_display(locale, colours, gray, today)
    wf += _time_display(locale, colours, gray, today)

    wf += '</svg>'

    return wf


def _angle_zero(locale):
    #
    # Weeks colors start at the same place as
    #
    if 'NT' in locale.DEFAULT_TIME_ZONE:
        angle = D(150)
    elif 'MT' in locale.DEFAULT_TIME_ZONE:
        angle = D(180)
    elif locale.HOUR_FORMAT == '12h':
        angle = D(270)
    else:
        angle = D(90)

    return angle


def _weeks_display(locale, today, weeks, colours, gray):
    wf = '    <g id="weeks_calendar">'

    arch = round(D(360) / weeks.decimal, 3)

    if locale.calendar_displayed == 'DCC' and weeks == 141:
        arch_offset = arch / 2
    elif weeks == 125:
        arch_offset = arch / 2
    else:
        arch_offset = D(0)

    angle = _angle_zero(locale)

    gweeks = '    <g id="weeks_background">\n'
    gtext = '    <g id="weeks_text">\n'
    gdays = '    <g id="days_background">\n'
    gdaystext = '    <g id="days_text">\n'

    for i in SR(weeks):
        week_wedge = ring(
            inner_radius=0,
            outer_radius=108,
            x=108,
            y=108,
            start_angle=angle + arch_offset,
            end_angle=angle + arch_offset + arch + (D('0.25') if i + 1 < weeks else 0),
            without_inner=True,
        )
        week_line = ring(
            inner_radius=93,
            outer_radius=93.5,
            x=108,
            y=108,
            start_angle=angle + arch_offset,
            end_angle=angle + arch_offset + arch,
        )

        if locale.calendar_displayed == 'DCC':
            month_line = ring(
                inner_radius=100,
                outer_radius=100.5,
                x=108,
                y=108,
                start_angle=angle + arch_offset,
                end_angle=angle + arch_offset + arch * D('6'),
            )
        else:
            if i in (0, 13, 21, 34, 42, 55, 103) or (i == 120 and not today.is_leap):
                month_line = ring(
                    inner_radius=100,
                    outer_radius=100.5,
                    x=108,
                    y=108,
                    start_angle=angle + arch_offset,
                    end_angle=angle + arch_offset + arch * D('4'),
                )

            else:
                month_line = ring(
                    inner_radius=100,
                    outer_radius=100.5,
                    x=108,
                    y=108,
                    start_angle=angle + arch_offset,
                    end_angle=angle + arch_offset + arch * D('5'),
                )

        leap_week_line = ring(
            inner_radius=100,
            outer_radius=100.5,
            x=108,
            y=108,
            start_angle=angle + arch_offset,
            end_angle=angle + arch_offset + arch,
        )

        week_style = ''

        if locale.calendar_displayed == 'DCC':
            if i == today.dcc_week_in_year:
                shade = '300'
                text_shade = '900'
            elif i in today.list_dcc_seasons_weeks():
                shade = '900'
                text_shade = '100'
            else:
                shade = '600'
                text_shade = '100'
        else:
            if i + 1 == today.week_in_year:
                shade = '300'
                text_shade = '900'
            elif i + 1 in today.list_seasons_weeks():
                shade = '900'
                text_shade = '100'
            else:
                shade = '600'
                text_shade = '100'

        gweeks += f'''        <path id="week_{str(i).zfill(3)}" style="fill:{colours[SI(i + 1)][shade]};" d="{week_wedge}" />\n'''

        gtext += f'''        <path id="week_line_{str(i).zfill(3)}" style="fill:none;" d="{week_line}" />\n'''

        if locale.calendar_displayed == 'DCC':
            gweeks, gtext, gdays, gdaystext = _dcc_display(locale, gweeks, gtext, gdays, gdaystext, i, colours, angle, week_wedge, month_line, week_line, leap_week_line, arch_offset, arch, today, gray, text_shade)

        else:
            gweeks, gtext, gdays, gdaystext = _sym_display(locale, gweeks, gtext, gdays, gdaystext, i, colours, angle, week_wedge, month_line, week_line, weeks, arch_offset, arch, today, gray, text_shade)

        angle += arch

    gtext += '    </g>\n'
    gweeks += '    </g>\n'
    gdaystext += '    </g>\n'
    gdays += '    </g>\n'

    wf += gweeks
    wf += gtext
    wf += f'''        <circle id="base" style="fill:#000000;" cx="108" cy="108" r="90" />\n'''
    wf += gdays
    wf += gdaystext
    wf += f'''        <circle id="base" style="fill:#000000;" cx="108" cy="108" r="81" />\n'''

    wf += '    </g>'
    return wf


def _dcc_display(locale, gweeks, gtext, gdays, gdaystext, i, colours, angle, week_wedge, month_line, week_line, leap_week_line, arch_offset, arch, today, gray, text_shade):
    week_number = str(i % 10)

    if 'c' in locale.format_token:
        week_number = locale.ADC_WEEK_ICON[int(week_number)]
    elif '!' in locale.format_token:
        week_number = default_to_sezimal_digits(week_number)

    if i == today.dcc_week_in_year:
        week_style = f'font-weight:bold;stroke:{colours[SI(i + 1)][text_shade]};stroke-width:0.25;'
    else:
        week_style = ''

    gtext += f'''<text style="font-size:6px;fill:{colours[SI(i + 1)][text_shade]};text-anchor:middle;text-align:center;{week_style}"><textPath href="#week_line_{str(i).zfill(3)}"  startOffset="25%">{week_number}</textPath></text>\n'''

    #
    # Separators between months
    #
    if i % 10 == 0 and i // 10 != 14:
        week_wedge = ring(
            inner_radius=0,
            outer_radius=108,
            x=108,
            y=108,
            start_angle=angle + arch_offset - D('0.25'),
            end_angle=angle + arch_offset + D('0.25'),
            without_inner=True,
        )
        gweeks += f'''        <path id="month_separator_{str(i).zfill(3)}" style="fill:#000000;" d="{week_wedge}" />\n'''

        gtext += f'''        <path id="month_line_{str(i).zfill(3)}" style="fill:none;" d="{month_line}" />\n'''

        month_number = i // 10

        if month_number == today.dcc_month:
            month_shade = '50'
            month_style = f'font-weight:bold;stroke:{colours[SI(i + 1)][month_shade]};stroke-width:0.25;'
        else:
            month_shade = text_shade
            month_style = ''

        if locale.base == 14:
            month_number = month_number.decimal
        elif locale.base == 20:
            month_number = month_number.dozenal
        elif '!' in locale.format_token:
            month_number = default_to_sezimal_digits(str(month_number))

        if 'c' in locale.format_token:
            gtext += f'''<text style="font-size:7px;fill:{colours[SI(i + 1)][month_shade]};text-anchor:middle;text-align:center;{month_style}">
<textPath href="#month_line_{str(i).zfill(3)}" startOffset="25%">{locale.ADC_MONTH_ICON[int(i // 10)]} • {locale.ADC_MONTH_NAME[int(i // 10)]}</textPath>
</text>\n'''
        else:
            gtext += f'''<text style="font-size:6px;fill:{colours[SI(i + 1)][month_shade]};text-align:center;text-anchor:middle;{month_style}"><textPath href="#month_line_{str(i).zfill(3)}" startOffset="25%">{month_number} • {locale.DCC_MONTH_NAME[int(i // 10)]}</textPath></text>\n'''

    elif i // 10 == 14:
        week_wedge = ring(
            inner_radius=0,
            outer_radius=108,
            x=108,
            y=108,
            start_angle=angle + arch_offset - D('0.25'),
            end_angle=angle + arch_offset + D('0.25'),
            without_inner=True,
        )
        gweeks += f'''        <path id="month_separator_{str(i).zfill(3)}" style="fill:#000000;" d="{week_wedge}" />\n'''
        week_wedge = ring(
            inner_radius=0,
            outer_radius=108,
            x=108,
            y=108,
            start_angle=angle + arch_offset - D('0.25') + arch,
            end_angle=angle + arch_offset + D('0.25') + arch,
            without_inner=True,
        )
        gweeks += f'''        <path id="month_separator_{str(i).zfill(3)}_2" style="fill:#000000;" d="{week_wedge}" />\n'''

        gtext += f'''        <path id="month_line_{str(i).zfill(3)}" style="fill:none;" d="{leap_week_line}" />\n'''

        month_number = str(i // 10)

        if month_number == today.dcc_month:
            month_shade = '50'
            month_style = f'font-weight:bold;stroke:{colours[SI(i + 1)][month_shade]};stroke-width:0.25;'
        else:
            month_shade = text_shade
            month_style = ''

        if '!' in locale.format_token:
            month_number = default_to_sezimal_digits(month_number)

        if 'c' in locale.format_token:
            gtext += f'''<text style="font-size:8px;fill:{colours[SI(i + 1)][month_shade]};text-anchor:middle;text-align:center;{month_style}">
<textPath href="#month_line_{str(i).zfill(3)}" startOffset="25%">{locale.ADC_MONTH_ICON[int(i // 10)]}</textPath>
</text>\n'''
        else:
            gtext += f'''<text style="font-size:6px;fill:{colours[SI(i + 1)][month_shade]};text-align:center;text-anchor:middle;{month_style}"><textPath href="#month_line_{str(i).zfill(3)}" startOffset="25%">{month_number}</textPath></text>\n'''

    if (today.dcc_month * 10) <= i < ((today.dcc_month * 10) + 10):
        for day in SR((i * 10), (i * 10) + 10):
            day = day % 100
            day_in_week = int(day % 10)

            day_colours = gray
            day_style = ''

            if i == today.dcc_week_in_year:
                if day == today.dcc_day:
                    back_shade = '600'
                    shade = '100'
                    day_colours = colours
                    day_style = f'font-weight:bold;stroke:{day_colours[SI(i + 1)][shade]};stroke-width:0.25;'
                else:
                    back_shade = '800' if day % 2 == 0 else '900'
                    shade = '600' if day % 2 == 0 else '700'
            else:
                back_shade = '800' if day % 2 == 0 else '900'
                shade = '600' if day % 2 == 0 else '700'

            day_degrees = 10

            day_colour = day_colours[i + 1][back_shade]
            text_colour = day_colours[i + 1][shade]

            day_angle = _angle_zero(locale) + day.decimal * day_degrees

            day_wedge = ring(
                inner_radius=0,
                outer_radius=90.25,
                x=108,
                y=108,
                start_angle=day_angle,
                end_angle=day_angle + D('0.1') + day_degrees,
                without_inner=True,
            )
            day_line = ring(
                inner_radius=83,
                outer_radius=83.1,
                x=108,
                y=108,
                start_angle=day_angle,
                end_angle=day_angle + day_degrees,
            )

            if 'c' in locale.format_token:
                day_number = locale.ADC_WEEKDAY_ICON[int(day % 10)]
            elif '!' in locale.format_token:
                day_number = default_to_sezimal_digits(str(day))
            elif locale.base == 10:
                day_number = day
            else:
                day_number = str(day).zfill(2)[1]
                # day_number = day_number[0] + '‐' + day_number[1]

            gdays += f'''        <path id="day_{str((i * 100) + day).zfill(4)}" style="fill:{day_colour};" d="{day_wedge}" />\n'''
            gdaystext += f'''        <path id="day_line_{str((i * 100) + day).zfill(4)}" style="fill:none;" d="{day_line}" />\n'''
            gdaystext += f'''<text style="font-size:6px;fill:{text_colour};text-anchor:middle;text-align:center;{day_style}"><textPath href="#day_line_{str((i * 100) + day).zfill(4)}"  startOffset="25%">{day_number}</textPath></text>\n'''

    return gweeks, gtext, gdays, gdaystext


def _sym_display(locale, gweeks, gtext, gdays, gdaystext, i, colours, angle, week_wedge, month_line, week_line, weeks, arch_offset, arch, today, gray, text_shade):

    if i + 1 == today.week_in_year:
        week_style = f'font-weight:bold;stroke:{colours[SI(i + 1)][text_shade]};stroke-width:0.25;'
    else:
        week_style = ''

    week_text = i + 1

    if '!' in locale.format_token:
        week_text = default_to_sezimal_digits(str(week_text))
    elif locale.base == 14:
        week_text = week_text.decimal
    elif locale.base == 20:
        week_text = week_text.dozenal

    gtext += f'''<text style="font-size:5px;fill:{colours[SI(i + 1)][text_shade]};text-anchor:middle;text-align:center;{week_style}"><textPath href="#week_line_{str(i).zfill(3)}"  startOffset="25%">{week_text}</textPath></text>\n'''

    if i <= 3:
        month = SI(1)
    elif i <= 12:
        month = SI(2)
    elif i <= 20:
        month = SI(3)
    elif i <= 24:
        month = SI(4)
    elif i <= 33:
        month = SI(5)
    elif i <= 41:
        month = SI(10)
    elif i <= 45:
        month = SI(11)
    elif i <= 54:
        month = SI(12)
    elif i <= 102:
        month = SI(13)
    elif i <= 110:
        month = SI(14)
    elif i <= 111:
        month = SI(15)
    else:
        month = SI(20)

    #
    # Separators between months
    #
    if i in (0, 4, 13, 21, 25, 34, 42, 50, 55, 103, 111, 120):
        week_wedge = ring(
            inner_radius=0,
            outer_radius=108,
            x=108,
            y=108,
            start_angle=angle + arch_offset - D('0.25'),
            end_angle=angle + arch_offset + D('0.25'),
            without_inner=True,
        )
        gweeks += f'''        <path id="month_separator_{str(i).zfill(3)}" style="fill:#000000;" d="{week_wedge}" />\n'''

        gtext += f'''        <path id="month_line_{str(i).zfill(3)}" style="fill:none;" d="{month_line}" />\n'''

        if month == today.month:
            month_shade = '50'
            month_style = f'font-weight:bold;stroke:{colours[SI(i + 1)][month_shade]};stroke-width:0.25;'
        else:
            month_shade = text_shade
            month_style = ''

        if locale.base == 10:
            if '!' in locale.format_token:
                gtext += f'''<text style="font-size:6px;fill:{colours[SI(i + 1)][month_shade]};text-align:center;text-anchor:middle;{month_style}"><textPath href="#month_line_{str(i).zfill(3)}"  startOffset="25%">{default_to_sezimal_digits(str(month))} • {locale.MONTH_NAME[int(month - 1)]}</textPath></text>\n'''
            else:
                gtext += f'''<text style="font-size:6px;fill:{colours[SI(i + 1)][month_shade]};text-align:center;text-anchor:middle;{month_style}"><textPath href="#month_line_{str(i).zfill(3)}"  startOffset="25%">{month} • {locale.MONTH_NAME[int(month - 1)]}</textPath></text>\n'''
        elif locale.base == 14:
            gtext += f'''<text style="font-size:6px;fill:{colours[SI(i + 1)][month_shade]};text-align:center;text-anchor:middle;{month_style}"><textPath href="#month_line_{str(i).zfill(3)}"  startOffset="25%">{month.decimal} • {locale.MONTH_NAME[int(month - 1)]}</textPath></text>\n'''
        elif locale.base == 20:
            gtext += f'''<text style="font-size:6px;fill:{colours[SI(i + 1)][month_shade]};text-align:center;text-anchor:middle;{month_style}"><textPath href="#month_line_{str(i).zfill(3)}"  startOffset="25%">{month.dozenal} • {locale.MONTH_NAME[int(month - 1)]}</textPath></text>\n'''

    if i + 1 == weeks:
        week_wedge = ring(
            inner_radius=0,
            outer_radius=108,
            x=108,
            y=108,
            start_angle=angle + arch_offset + arch - D('0.25'),
            end_angle=angle + arch_offset + arch + D('0.25'),
            without_inner=True,
        )
        gweeks += f'''        <path id="month_separator_{str(i).zfill(3)}" style="fill:#000000;" d="{week_wedge}" />\n'''

    if locale.calendar_displayed == 'SYM':
        gdays, gdaystext = _sym_days_display(today, locale, i, gray, colours, gdays, gdaystext)
    else:
        gdays, gdaystext = _iso_days_display(today, locale, i, gray, colours, gdays, gdaystext)

    return gweeks, gtext, gdays, gdaystext


def _sym_days_display(today, locale, i, gray, colours, gdays, gdaystext):
    draw_days = False

    if (today.month == 1 and 1 <= (i + 1) <= 4):
        draw_days = 44
        week_in_month = i + 1
    elif (today.month == 2 and 5 <= (i + 1) <= 13):
        draw_days = 55
        week_in_month = i + 1 - 4
    elif (today.month == 3 and 14 <= (i + 1) <= 21):
        draw_days = 44
        week_in_month = i + 1 - 13

    elif (today.month == 4 and 22 <= (i + 1) <= 25):
        draw_days = 44
        week_in_month = i + 1 - 21
    elif (today.month == 5 and 30 <= (i + 1) <= 34):
        draw_days = 55
        week_in_month = i + 1 - 25
    elif (today.month == 10 and 35 <= (i + 1) <= 42):
        draw_days = 44
        week_in_month = i + 1 - 34

    elif (today.month == 11 and 43 <= (i + 1) <= 50):
        draw_days = 44
        week_in_month = i + 1 - 42
    elif (today.month == 12 and 51 <= (i + 1) <= 55):
        draw_days = 55
        week_in_month = i + 1 - 50
    elif (today.month == 13 and 100 <= (i + 1) <= 103):
        draw_days = 44
        week_in_month = i + 1 - 55

    elif (today.month == 14 and 104 <= (i + 1) <= 111):
        draw_days = 44
        week_in_month = i + 1 - 103
    elif (today.month == 15 and 112 <= (i + 1) <= 120):
        draw_days = 55
        week_in_month = i + 1 - 111
    elif (today.month == 20 and 121 <= (i + 1)):
        if today.is_long_year:
            draw_days = 55
        else:
            draw_days = 44
        week_in_month = i + 1 - 120

    if not draw_days:
        return gdays, gdaystext

    for day in SR(1, 12):
        day_in_week = int(day)
        day += (week_in_month - 1) * 11

        day_colours = gray
        day_style = ''

        if i + 1 == today.week_in_year:
            if day == today.day:
                back_shade = '600'
                shade = '100'
                day_colours = colours
                day_style = f'font-weight:bold;stroke:{day_colours[SI(i + 1)][shade]};stroke-width:0.25;'
            else:
                back_shade = '800' if day % 2 == 0 else '900'
                shade = '600' if day % 2 == 0 else '700'
        else:
            back_shade = '800' if day % 2 == 0 else '900'
            shade = '600' if day % 2 == 0 else '700'

        if draw_days == 44:
            day_degrees = D(360) / 28
        else:
            day_degrees = D(360) / 35

        day_colour = day_colours[i + 1][back_shade]
        text_colour = day_colours[i + 1][shade]

        day_angle = _angle_zero(locale) + ((day.decimal - 1) * day_degrees)

        day_wedge = ring(
            inner_radius=0,
            outer_radius=90.25,
            x=108,
            y=108,
            start_angle=day_angle,
            end_angle=day_angle + D('0.1') + day_degrees,
            without_inner=True,
        )
        day_line = ring(
            inner_radius=83,
            outer_radius=83.1,
            x=108,
            y=108,
            start_angle=day_angle,
            end_angle=day_angle + day_degrees,
        )

        day_number = str(day)

        if '!' in locale.format_token:
            day_number = default_to_sezimal_digits(day_number)
        elif locale.base == 14:
            day_number = day.decimal
        elif locale.base == 20:
            day_number = day.dozenal

        gdays += f'''        <path id="day_{str((i * 100) + day).zfill(4)}" style="fill:{day_colour};" d="{day_wedge}" />\n'''
        gdaystext += f'''        <path id="day_line_{str((i * 100) + day).zfill(4)}" style="fill:none;" d="{day_line}" />\n'''
        gdaystext += f'''<text style="font-size:6px;fill:{text_colour};text-anchor:middle;text-align:center;{day_style}"><textPath href="#day_line_{str((i * 100) + day).zfill(4)}"  startOffset="25%">{day_number}</textPath></text>\n'''

    return gdays, gdaystext


def _iso_days_display(today, locale, i, gray, colours, gdays, gdaystext):
    if 'day_01' in gdays:
        return gdays, gdaystext

    if (i + 1).decimal != today.gregorian_week_in_year:
        return gdays, gdaystext

    if today.gregorian_month in (1, 3, 5, 7, 8, 10, 12):
        draw_days = 51
    elif today.gregorian_month in (4, 6, 9, 11):
        draw_days = 50
    elif today.gregorian_is_leap:
        draw_days = 45
    else:
        draw_days = 44

    for day in SR(1, SI(draw_days) + 1):
        day_colours = gray
        day_style = ''

        if day.decimal == today.gregorian_day:
            back_shade = '600'
            shade = '100'
            day_colours = colours
            day_style = f'font-weight:bold;stroke:{day_colours[SI(i + 1)][shade]};stroke-width:0.25;'
        else:
            back_shade = '800' if day % 2 == 0 else '900'
            shade = '600' if day % 2 == 0 else '700'

        day_degrees = D(360) / SI(draw_days).decimal

        day_colour = day_colours[i + 1][back_shade]
        text_colour = day_colours[i + 1][shade]

        day_angle = _angle_zero(locale) + ((day.decimal - 1) * day_degrees)

        day_wedge = ring(
            inner_radius=0,
            outer_radius=90.25,
            x=108,
            y=108,
            start_angle=day_angle,
            end_angle=day_angle + D('0.1') + day_degrees,
            without_inner=True,
        )
        day_line = ring(
            inner_radius=83,
            outer_radius=83.1,
            x=108,
            y=108,
            start_angle=day_angle,
            end_angle=day_angle + day_degrees,
        )

        day_number = str(day)

        if '!' in locale.format_token:
            day_number = default_to_sezimal_digits(day_number)
        elif locale.base == 14:
            day_number = day.decimal
        elif locale.base == 20:
            day_number = day.dozenal

        gdays += f'''        <path id="day_{str((i * 100) + day).zfill(4)}" style="fill:{day_colour};" d="{day_wedge}" />\n'''
        gdaystext += f'''        <path id="day_line_{str((i * 100) + day).zfill(4)}" style="fill:none;" d="{day_line}" />\n'''
        gdaystext += f'''<text style="font-size:6px;fill:{text_colour};text-anchor:middle;text-align:center;{day_style}"><textPath href="#day_line_{str((i * 100) + day).zfill(4)}"  startOffset="25%">{day_number}</textPath></text>\n'''

    return gdays, gdaystext


def _shastadari_logo(locale, colours, today):
    # if locale.calendar_displayed == 'DCC':
    #     back_colour = colours[today.dcc_week_in_year]['900']
    #     front_colour = colours[today.dcc_week_in_year]['700']
    # else:
    #     back_colour = colours[today.week_in_year]['900']
    #     front_colour = colours[today.week_in_year]['700']

    back_colour = '#222222aa'
    front_colour = '#000000'

    #
    # Shastadari Symbol
    #
    shastadari_size = 60
    shastadari_size_hexagon = shastadari_size / 3 * 2
    shastadari_thickness = shastadari_size / 9

    xl = '''    <g id="shastadari_logo">'''

    circle = ring(
        inner_radius=0,
        outer_radius=shastadari_size_hexagon - 3,
        x=108,
        y=108,
        start_angle=0,
        end_angle=0,
    )
    xl += f'''        <path id="shastadari_base" style="fill:none;" d="{circle}" />\n'''

    # if 'pt' in locale.LANG:
    #     name = 'Xastadári'
    # elif 'bz' in locale.LANG:
    #     name = 'Xastadari'
    # elif 'eo' in locale.LANG:
    #     name = 'Ŝastadari’'
    # elif 'es' in locale.LANG:
    #     name = 'Llastadari'
    # elif 'it' in locale.LANG:
    #     name = 'Sciastadari'
    # elif 'fr' in locale.LANG:
    #     name = 'Chastadari'
    # elif 'de' in locale.LANG:
    #     name = 'Schastadari'
    # else:
    #     name = 'Shastadari'
    # name = 'षष्टाधारी'

    # name = "[swɪksˈnaɪf]"
    name = "swixknife"

    xl += f'''<text style="font-size:{shastadari_size / 8}px;fill:{back_colour};text-anchor:middle;text-align:center;font-weight:bold;"><textPath href="#shastadari_base" startOffset="75%">{name}</textPath></text>\n'''

    # circle = ring(
    #     inner_radius=shastadari_size - shastadari_thickness,
    #     outer_radius=shastadari_size,
    #     x=108,
    #     y=108,
    #     start_angle=0,
    #     end_angle=0,
    # )
    # xl += f'''        <path id="shastadari_circle" style="fill:{front_colour};" d="{circle}" />\n'''

    # hexagon = polygon(
    #     x=108,
    #     y=108,
    #     radius=shastadari_size_hexagon,
    #     n=6,
    # )
    # xl += f'''        <path id="shastadari_hexagon_outer" style="fill:{front_colour};" d="{hexagon}" />\n'''
    hexagon = polygon(
        x=108,
        y=108,
        radius=shastadari_size_hexagon - shastadari_thickness,
        n=6,
    )
    xl += f'''        <path id="shastadari_hexagon_inner" style="fill:{back_colour};" d="{hexagon}" />\n'''

    tripod = star(
        x=108,
        y=108,
        n=3,
        outer_radius=shastadari_size_hexagon - shastadari_thickness,
        inner_radius=shastadari_thickness,
        angle=150,
    )
    xl += f'''        <path id="shastadari_halves" style="fill:{front_colour};" d="{tripod}" />\n'''

    triangle = polygon(
        x=108,
        y=108,
        radius=shastadari_size_hexagon / 2,
        n=3,
        angle=180,
    )
    xl += f'''        <path id="shastadari_triangle" style="fill:{front_colour};" d="{triangle}" />\n'''
    triangle = polygon(
        x=108,
        y=108,
        radius=(shastadari_size_hexagon / 2) - (shastadari_thickness * 1.5),
        n=3,
        angle=180,
    )
    xl += f'''        <path id="shastadari_triangle_inner" style="fill:{back_colour};" d="{triangle}" />\n'''

    xl += '    </g>'
    return xl


DAY_COLOURS = [
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#15111d', '#2b213b', '#403258', '#554375', '#6a5492',
    '#9575cd', '#9a73cc', '#a071cc', '#a56fcb', '#aa6eca', '#af6cc9',
    '#ba68c8', '#c06abc', '#c66bb0', '#cc6da4', '#d36e97', '#d9708b',
    '#e57373', '#e97d6e', '#ec8668', '#f09063', '#f49a5d', '#f8a458',
    '#ffb74d', '#ffbf53', '#ffc859', '#ffd05f', '#ffd864', '#ffe06a',
    '#fff176', '#e6ea88', '#cde49b', '#b4ddad', '#9ad7c0', '#81d0d2',
    '#4FC3F7', '#4FC3F7', '#4FC3F7', '#4FC3F7', '#4FC3F7', '#4FC3F7',
    '#4fc3f7', '#4fc3f7', '#4ec3f7', '#4ec3f7', '#4dc2f7', '#4dc2f7',
    '#4cc2f7', '#4cc2f7', '#4bc2f7', '#4bc2f7', '#4ac1f7', '#4ac1f7',
    '#49c1f7', '#49c1f7', '#48c1f7', '#48c1f7', '#47c0f7', '#47c0f7',
    '#46c0f7', '#46c0f7', '#45c0f7', '#45c0f7', '#44bff7', '#44bff7',
    '#43bff7', '#43bff7', '#42bff7', '#42bff7', '#42bef7', '#41bef7',
    '#41bef7', '#40bef7', '#40bef7', '#3fbef7', '#3fbdf7', '#3ebdf7',
    '#3ebdf7', '#3dbdf7', '#3dbdf7', '#3cbdf7', '#3cbcf6', '#3bbcf6',
    '#3bbcf6', '#3abcf6', '#3abcf6', '#39bcf6', '#39bbf6', '#38bbf6',
    '#38bbf6', '#37bbf6', '#37bbf6', '#36bbf6', '#36baf6', '#36baf6',
    '#35baf6', '#35baf6', '#34baf6', '#34baf6', '#33b9f6', '#33b9f6',
    '#32b9f6', '#32b9f6', '#31b9f6', '#31b9f6', '#30b8f6', '#30b8f6',
    '#2fb8f6', '#2fb8f6', '#2eb8f6', '#2eb8f6', '#2db7f6', '#2db7f6',
    '#2cb7f6', '#2cb7f6', '#2bb7f6', '#2bb7f6', '#2ab6f6', '#2ab6f6',
    '#29b6f6', '#29b6f6', '#2ab6f6', '#2ab6f6', '#2bb7f6', '#2bb7f6',
    '#2cb7f6', '#2cb7f6', '#2db7f6', '#2db8f6', '#2eb8f6', '#2eb8f6',
    '#2fb8f6', '#2fb8f6', '#30b8f6', '#30b9f6', '#31b9f6', '#31b9f6',
    '#32b9f6', '#32b9f6', '#33b9f6', '#33baf6', '#34baf6', '#34baf6',
    '#35baf6', '#35baf6', '#36baf6', '#36baf6', '#37bbf6', '#37bbf6',
    '#38bbf6', '#38bbf6', '#39bbf6', '#39bbf6', '#3abcf6', '#3abcf6',
    '#3bbcf6', '#3bbcf6', '#3cbcf6', '#3cbcf6', '#3cbdf7', '#3dbdf7',
    '#3dbdf7', '#3ebdf7', '#3ebdf7', '#3fbef7', '#3fbef7', '#40bef7',
    '#40bef7', '#41bef7', '#41bef7', '#42bef7', '#42bff7', '#43bff7',
    '#43bff7', '#44bff7', '#44bff7', '#45c0f7', '#45c0f7', '#46c0f7',
    '#46c0f7', '#47c0f7', '#47c0f7', '#48c0f7', '#48c1f7', '#49c1f7',
    '#49c1f7', '#4ac1f7', '#4ac1f7', '#4bc2f7', '#4bc2f7', '#4cc2f7',
    '#4cc2f7', '#4dc2f7', '#4dc2f7', '#4ec2f7', '#4ec3f7', '#4FC3F7',
    '#4FC3F7', '#4FC3F7', '#4FC3F7', '#4FC3F7', '#4FC3F7', '#4fc3f7',
    '#68cae5', '#81d0d2', '#9ad7c0', '#b4ddad', '#cde49b', '#fff176',
    '#ffe970', '#ffe06a', '#ffd864', '#ffd05f', '#ffc859', '#ffb74d',
    '#fbad52', '#f8a458', '#f49a5d', '#f09063', '#ec8668', '#e57373',
    '#df717f', '#d9708b', '#d36e97', '#cc6da4', '#c66bb0', '#ba68c8',
    '#b56ac9', '#af6cc9', '#aa6eca', '#a56fcb', '#a071cc', '#9575cd',
    '#8064b0', '#6a5492', '#554375', '#403258', '#2b213b', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
    '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',
]


def _time_display(locale, colours, gray, today):
    if locale.calendar_displayed == 'DCC':
        time_colours = gray[today.dcc_week_in_year]
        pointer_colours = colours[today.dcc_week_in_year]
    else:
        time_colours = gray[today.week_in_year]
        pointer_colours = colours[today.week_in_year]

    time_display_colour = time_colours['500']

    display = '    <g id="watchface_time_display">\n'

    size = 81

    # display += f'''        <circle id="number_base" style="fill:none;" cx="108" cy="108" r="66" />\n'''

    # for i in range(360):
    #     if DAY_COLOURS[i] == '#000000':
    #         continue
    #
    #     time_wedge = ring(
    #         inner_radius=0,
    #         outer_radius=90,
    #         x=108,
    #         y=108,
    #         start_angle=90 + i,
    #         end_angle=90 + i + 1.25,
    #         without_inner=True,
    #     )
    #     display += f'''        <path id="time_{str(i).zfill(3)}" style="fill:{DAY_COLOURS[i]};" d="{time_wedge}" />\n'''

    if 'NT' in locale.DEFAULT_TIME_ZONE:
        zero_position = 150
        hand_initial_angle = 0
    elif 'MT' in locale.DEFAULT_TIME_ZONE:
        zero_position = 180
        hand_initial_angle = 30
    elif locale.HOUR_FORMAT == '12h':
        zero_position = 270
        hand_initial_angle = 0
    else:
        zero_position = 90
        hand_initial_angle = 180

    if locale.base == 10:
        shape_vertices = 3

        for i in range(36):
            if i % 6 == 0:
                angle = zero_position + ((i / 6) * 60) - 1
                tick = ring(inner_radius=size * 13 / 15, outer_radius=size, x=108, y=108, start_angle=angle, end_angle=angle + 2)

                angle = ((i / 36) * 360) + zero_position

                if angle > 360:
                    angle -= 360

                if True:
                    cx = 108 + (size * 32 / 45) * math.cos(angle / 360 * math.pi * 2)
                    cy = 108 + (size / 15) + (size * 32 / 45) * math.sin(angle / 360 * math.pi * 2)

                    if '!' in locale.format_token:
                        display += f'''<text x="{cx}" y="{cy}" style="font-size:{size / 5}px;fill:{time_display_colour};text-anchor:middle;text-align:center;font-weight:bold;">{default_to_sezimal_digits(str(SI(D(i))))}</text>\n'''
                    else:
                        display += f'''<text x="{cx}" y="{cy}" style="font-size:{size / 5}px;fill:{time_display_colour};text-anchor:middle;text-align:center;font-weight:bold;">{SI(D(i))}</text>\n'''
                else:
                    cx = 108 + (size * 4 / 5) * math.cos(angle / 360 * math.pi * 2)
                    cy = 108 + (size * 4 / 5) * math.sin(angle / 360 * math.pi * 2)
                    display += f'''        <circle style="fill:{time_display_colour};" cx="{cx}" cy="{cy}" r="2" />\n'''

            else:
                angle = zero_position + (i * 10) - 0.5

                if i % 3 == 0:
                    tick = ring(inner_radius=size * 13 / 15, outer_radius=size, x=108, y=108, start_angle=angle, end_angle=angle + 1)
                else:
                    tick = ring(inner_radius=size * 14 / 15, outer_radius=size, x=108, y=108, start_angle=angle, end_angle=angle + 1)

            display += f'''        <path id="tick_{str(SI(D(i))).zfill(2)}" style="fill:{time_display_colour};" d="{tick}" />\n'''

    elif locale.base == 14:
        shape_vertices = 3

        if locale.HOUR_FORMAT == '24h':
            for i in range(24):
                angle = zero_position + (i * 15) - 0.5
                tick = ring(inner_radius=size * 13 / 15, outer_radius=size, x=108, y=108, start_angle=angle, end_angle=angle + 1)

                angle = ((i / 24) * 360) + zero_position

                if angle > 360:
                    angle -= 360

                if True:
                    cx = 108 + (size * 11 / 15) * math.cos(angle / 360 * math.pi * 2)
                    cy = 108 + (size / 18) + (size * 11 / 15) * math.sin(angle / 360 * math.pi * 2)
                    display += f'''<text x="{cx}" y="{cy}" style="font-size:{size * 13 / 90}px;fill:{time_display_colour};text-anchor:middle;text-align:center;font-weight:normal;">{i}</text>\n'''
                else:
                    cx = 108 + (size * 4 / 5) * math.cos(angle / 360 * math.pi * 2)
                    cy = 108 + (size * 4 / 5) * math.sin(angle / 360 * math.pi * 2)
                    display += f'''        <circle style="fill:{time_display_colour};" cx="{cx}" cy="{cy}" r="2" />\n'''

                display += f'''        <path id="tick_{str(SI(D(i))).zfill(2)}" style="fill:{time_display_colour};" d="{tick}" />\n'''

            for i in range(120):
                if i % 5 == 0:
                    continue

                angle = zero_position + (i * 6) - 0.2
                tick = ring(inner_radius=size * 18 / 19, outer_radius=size, x=108, y=108, start_angle=angle, end_angle=angle + 0.4)

                display += f'''        <path id="tick_{str(SI(D(i))).zfill(2)}" style="fill:{time_display_colour};" d="{tick}" />\n'''

        else:
            for i in range(60):
                if i % 5 == 0:
                    angle = zero_position + ((i / 5) * 30) - 1
                    tick = ring(inner_radius=size * 13 / 15, outer_radius=size, x=108, y=108, start_angle=angle, end_angle=angle + 2)

                    angle = ((i / 60) * 360) + zero_position

                    if angle > 360:
                        angle -= 360

                    if True:
                        cx = 108 + (size * 11 / 15) * math.cos(angle / 360 * math.pi * 2)
                        cy = 108 + (size / 15) + (size * 11 / 15) * math.sin(angle / 360 * math.pi * 2)
                        display += f'''<text x="{cx}" y="{cy}" style="font-size:{size * 8 / 45}px;fill:{time_display_colour};text-anchor:middle;text-align:center;font-weight:bold;">{(i // 5) if i != 0 else '12'}</text>\n'''
                    else:
                        cx = 108 + (size * 4 / 5) * math.cos(angle / 360 * math.pi * 2)
                        cy = 108 + (size * 4 / 5) * math.sin(angle / 360 * math.pi * 2)
                        display += f'''        <circle style="fill:{time_display_colour};" cx="{cx}" cy="{cy}" r="2" />\n'''

                else:
                    angle = zero_position + (i * 6) - 0.5
                    tick = ring(inner_radius=size * 14 / 15, outer_radius=size, x=108, y=108, start_angle=angle, end_angle=angle + 1)

                display += f'''        <path id="tick_{str(SI(D(i))).zfill(2)}" style="fill:{time_display_colour};" d="{tick}" />\n'''

    elif locale.base == 20:
        shape_vertices = 3

        for i in range(0, 144):
            if i % 12 == 0:
                angle = zero_position + 2 + ((i - 1) * 2.5)
                tick = ring(inner_radius=size * 13 / 15, outer_radius=size, x=108, y=108, start_angle=angle, end_angle=angle + 1)

                display += f'''        <path id="tick_{str(i).zfill(3)}" style="fill:{time_display_colour};" d="{tick}" />\n'''

                angle = ((i / 144) * 360) + zero_position

                if angle > 360:
                    angle -= 360

                if True:
                    cx = 108 + (size * 11 / 15) * math.cos(angle / 360 * math.pi * 2)
                    cy = 108 + (size / 15) + (size * 11 / 15) * math.sin(angle / 360 * math.pi * 2)
                    display += f'''<text x="{cx}" y="{cy}" style="font-size:{size / 5}px;fill:{time_display_colour};text-anchor:middle;text-align:center;font-weight:bold;">{DozenalInteger(D(i // 12))}</text>\n'''
                else:
                    cx = 108 + (size * 4 / 5) * math.cos(angle / 360 * math.pi * 2)
                    cy = 108 + (size * 4 / 5) * math.sin(angle / 360 * math.pi * 2)
                    display += f'''        <circle style="fill:{time_display_colour};" cx="{cx}" cy="{cy}" r="2" />\n'''

            else:
                angle = zero_position + 2 + ((i - 1) * 2.5)

                if i % 6 == 0:
                    tick = ring(inner_radius=size * 13 / 15, outer_radius=size, x=108, y=108, start_angle=angle, end_angle=angle + 0.5)
                elif i % 3 == 0:
                    tick = ring(inner_radius=size * 9 / 10, outer_radius=size, x=108, y=108, start_angle=angle, end_angle=angle + 0.5)
                else:
                    tick = ring(inner_radius=size * 14 / 15, outer_radius=size, x=108, y=108, start_angle=angle, end_angle=angle + 0.5)

                display += f'''        <path id="tick_{str(i).zfill(3)}" style="fill:{time_display_colour};" d="{tick}" />\n'''

    #
    # Hands
    #
    # agrima_hand_colour = pointer_colours['800'] + 'dd'
    # posha_hand_colour = pointer_colours['500'] + 'dd'
    # uta_hand_colour = pointer_colours['200'] + 'dd'
    anuga_hand_colour = '#d50000'
    agrima_hand_colour = '#d50000dd'
    posha_hand_colour = '#ffffffdd'

    if locale.base == 14 and locale.HOUR_FORMAT == '12h':
        uta_hand_colour = '#ffffffdd'
    else:
        uta_hand_colour = '#FFA726dd'
        sun_colour = '#FFA726dd'

    display += f'    <g id="hand_uta" cx="108" cy="108" transform-box="fill-box" transform-origin="center">'
    display += f'''        <circle id="hand_uta_base" style="fill:none;" cx="108" cy="108" r="{size * 2 / 3}"  />\n'''

    cx = 108 + (size * 2 / 3) * math.cos(zero_position / 360 * math.pi * 2)
    cy = 108 + (size * 2 / 3) * math.sin(zero_position / 360 * math.pi * 2)
    triangle = polygon(
        x=cx,
        y=cy,
        radius=size / 6,
        n=shape_vertices,
        angle=hand_initial_angle,
    )
    display += f'''        <path id="hand_uta_pointer" style="fill:{uta_hand_colour};" d="{triangle}" />\n'''
    # display += '''        <animateTransform id="animate_uta_pointer" attributeType="xml" attributeName="transform" type="rotate" from="0" to="360" begin="0" dur="86400s" repeatCount="indefinite" />\n'''

    if locale.base != 14 or locale.HOUR_FORMAT == '24h':
        # triangle = polygon(
        #     x=cx,
        #     y=cy,
        #     radius=size / 6,
        #     n=shape_vertices,
        #     angle=hand_initial_angle,
        # )
        # display += f'''        <path id="hand_uta_pointer_2" style="fill:{sun_colour};" d="{triangle}" />\n'''
        # triangle = polygon(
        #     x=cx,
        #     y=cy,
        #     radius=size / 7,
        #     n=shape_vertices,
        #     angle=hand_initial_angle + 40,
        # )
        # display += f'''        <path id="hand_uta_pointer_3" style="fill:{sun_colour};" d="{triangle}" />\n'''
        # triangle = polygon(
        #     x=cx,
        #     y=cy,
        #     radius=size / 6.5,
        #     n=shape_vertices,
        #     angle=hand_initial_angle + 80,
        # )
        # display += f'''        <path id="hand_uta_pointer_4" style="fill:{sun_colour};" d="{triangle}" />\n'''

        display += f'''        <circle id="hand_uta_sun" style="fill:#FDD835;" cx="{cx}" cy="{cy}" r="{size / 18}"  />\n'''
        display += f'''        <circle id="hand_uta_sun" style="fill:{uta_hand_colour};" cx="{cx}" cy="{cy}" r="{size / 54}"  />\n'''

    display += '    </g>'

    display += '    <g id="hand_posha" transform-origin="center">'
    display += f'''        <circle id="hand_posha_base" style="fill:none;" cx="108" cy="108" r="{size * 2 / 3}" />\n'''

    cx = 108 + (size * 2 / 3) * math.cos(zero_position / 360 * math.pi * 2)
    cy = 108 + (size * 2 / 3) * math.sin(zero_position / 360 * math.pi * 2)
    triangle = polygon(
        x=cx,
        y=cy,
        radius=size / 8,
        n=shape_vertices,
        angle=hand_initial_angle,
    )
    display += f'''        <path id="hand_posha_pointer" style="fill:{posha_hand_colour};" d="{triangle}" />\n'''
    # display += '''        <animateTransform id="animate_posha_pointer" attributeType="xml" attributeName="transform" type="rotate" from="0" to="360" begin="0" dur="2400s" repeatCount="indefinite" />\n'''
    display += '    </g>'

    display += '    <g id="hand_agrima" transform-origin="center">'
    display += f'''        <circle id="hand_agrima_base" style="fill:none;" cx="108" cy="108" r="{size * 2 / 3}" />\n'''

    cx = 108 + (size * 2 / 3) * math.cos(zero_position / 360 * math.pi * 2)
    cy = 108 + (size * 2 / 3) * math.sin(zero_position / 360 * math.pi * 2)
    triangle = polygon(
        x=cx,
        y=cy,
        radius=size / 10,
        n=shape_vertices,
        angle=hand_initial_angle,
    )

    if locale.base == 20:
        display += f'''        <path id="hand_agrima_pointer" style="fill:{posha_hand_colour};" d="{triangle}" />\n'''
    else:
        display += f'''        <path id="hand_agrima_pointer" style="fill:{agrima_hand_colour};" d="{triangle}" />\n'''
    # display += '''        <animateTransform id="animate_agrima_pointer" attributeType="xml" attributeName="transform" type="rotate" from="0" to="360" begin="0" dur="60606ms" repeatCount="indefinite" />\n'''
    display += '    </g>'

    if locale.base == 20:
        display += '    <g id="hand_dozenal" transform-origin="center">'
        display += f'''        <circle id="hand_dozenal_base" style="fill:none;" cx="108" cy="108" r="{size * 2 / 3}" />\n'''

        cx = 108 + (size * 2 / 3) * math.cos(zero_position / 360 * math.pi * 2)
        cy = 108 + (size * 2 / 3) * math.sin(zero_position / 360 * math.pi * 2)
        triangle = polygon(
            x=cx,
            y=cy,
            radius=size / 12,
            n=shape_vertices,
            angle=hand_initial_angle,
        )
        display += f'''        <path id="hand_dozenal_pointer" style="fill:{agrima_hand_colour};" d="{triangle}" />\n'''
        # display += '''        <animateTransform id="animate_agrima_pointer" attributeType="xml" attributeName="transform" type="rotate" from="0" to="360" begin="0" dur="60606ms" repeatCount="indefinite" />\n'''
        display += '    </g>'

    display += '    </g>\n'

    return display


def _date_display(locale, colours, gray, today):
    size = 60

    if locale.calendar_displayed == 'DCC':
        # time_colours = gray[today.dcc_week_in_year]
        date_colours = colours[today.dcc_week_in_year]
    else:
        # time_colours = gray[today.week_in_year]
        date_colours = colours[today.week_in_year]

    display = '    <g id="watchface_date_display">\n'
    opening = f'''        <text x="108" y="108" style="font-size:{size / 6}px;font-weight:bold;fill:#ffffff88;text-anchor:middle;text-align:center;alignment-baseline:middle;">'''
    display += opening

    if locale.calendar_displayed == 'DCC':
        if 'c' in locale.format_token:
            # display += f'''            <tspan x="108" dy="-1.5em">{today.format(locale.ADC_DATE_FORMAT, locale)}</tspan>'''
            if '!' in locale.format_token:
                display += f'''            <tspan x="108" dy="-1.5em">{today.format('&!>Y', locale)}</tspan>'''
                display += '        </text>' + opening
                display += f'''            <tspan x="108" dy="-0.25em">{today.format('&!-m &iM &cM', locale)}</tspan>'''
                display += '        </text>' + opening
                display += f'''            <tspan x="108" dy="+1em">{today.format('&!-wM &iW &cW', locale)}</tspan>'''
                display += '        </text>' + opening
                display += f'''            <tspan x="108" dy="+2.25em">{today.format('&!-dW &iD &cD', locale)}</tspan>'''
            else:
                display += f'''            <tspan x="108" dy="-1.5em">{today.format('&>Y', locale)}</tspan>'''
                display += '        </text>' + opening
                display += f'''            <tspan x="108" dy="-0.25em">{today.format('&-m &iM &cM', locale)}</tspan>'''
                display += '        </text>' + opening
                display += f'''            <tspan x="108" dy="+1em">{today.format('&-wM &iW &cW', locale)}</tspan>'''
                display += '        </text>' + opening
                display += f'''            <tspan x="108" dy="+2.25em">{today.format('&-dW &iD &cD', locale)}</tspan>'''
        else:
            display += f'''            <tspan x="108" dy="0.5em">{today.format(locale.DCC_DATE_FORMAT, locale)}</tspan>'''

            # display += '        </text>' + opening
            # display += f'''            <tspan x="108" dy="1em">{today.format('&D', locale)}</tspan>'''

    elif locale.calendar_displayed == 'SYM':
        display += f'''            <tspan x="108" dy="-0.125em">{today.format(locale.DATE_FORMAT, locale)}</tspan>'''
        display += '        </text>' + opening
        display += f'''            <tspan x="108" dy="1.125em">{today.format('#W', locale)}</tspan>'''

    else:
        display += f'''            <tspan x="108">{today.format(locale.ISO_DATE_FORMAT, locale)}</tspan>'''
        display += '        </text>' + opening
        display += f'''            <tspan x="108" dy="1em">{today.format('#W', locale)}</tspan>'''

    display += '        </text>\n'
    display += '    </g>\n'

    return display
