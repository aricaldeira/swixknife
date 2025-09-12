
import math

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


FONT_FAMILY = """'Andika', 'Sezimal QP', 'Sezimal Symbols', 'Noto Sans Hebrew', 'Noto Sans Arabic UI', 'Noto Sans Devanagari UI', 'Noto Sans Bengali UI', 'Inter Alia', 'Noto Sans Shavian', 'Noto Sans Symbols', 'Noto Sans Symbols2', sans-serif"""


# @app.route('/watchface.svg')
def watchface(locale, today) -> str:
    # if 'sezimal' in request.cookies:
    #     locale = _prepare_locale_from_cookie()
    # else:
    #     locale = sezimal_locale(browser_preferred_locale())

    # locale.calendar_displayed = 'DCC'
    # locale.DEFAULT_HEMISPHERE = 'S'
    # locale.format_token = 'c'

    today = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

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

        if today.is_leap:
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

    arch = round(D(360) / weeks.decimal, 3)
    angle = D(270)

    # wf = '<svg width="172" height="172" id="watchface" viewBox="0 0 216 216">\n'
    wf = '<svg width="50%" id="watchface" viewBox="0 0 216 216" onclick="watchface_toggle()">\n'
    gweeks = '    <g id="weeks_background">\n'
    gtext = '    <g id="weeks_text">\n'

    for i in SR(weeks):
        week_wedge = ring(
            inner_radius=0,
            outer_radius=108,
            x=108,
            y=108,
            start_angle=angle,
            end_angle=angle + arch + (D('0.25') if i + 1 < weeks else 0),
            without_inner=True,
        )
        week_line = ring(
            inner_radius=93,
            outer_radius=93.5,
            x=108,
            y=108,
            start_angle=angle,
            end_angle=angle + arch,
        )

        if locale.calendar_displayed == 'DCC':
            month_line = ring(
                inner_radius=100,
                outer_radius=100.5,
                x=108,
                y=108,
                start_angle=angle,
                end_angle=angle + arch * D('6'),
            )
        else:
            if i in (0, 13, 21, 34, 42, 55, 103) or (i == 120 and not today.is_leap):
                month_line = ring(
                    inner_radius=100,
                    outer_radius=100.5,
                    x=108,
                    y=108,
                    start_angle=angle,
                    end_angle=angle + arch * D('4'),
                )

            else:
                month_line = ring(
                    inner_radius=100,
                    outer_radius=100.5,
                    x=108,
                    y=108,
                    start_angle=angle,
                    end_angle=angle + arch * D('5'),
                )

        leap_week_line = ring(
            inner_radius=100,
            outer_radius=100.5,
            x=108,
            y=108,
            start_angle=angle,
            end_angle=angle + arch,
        )

        if locale.calendar_displayed == 'DCC':
            if i == today.dcc_week_in_year:
                shade = '50'
            elif i < today.dcc_week_in_year:
                shade = '900'
            else:
                shade = '400'
        else:
            if i + 1 == today.week_in_year:
                shade = '50'
            elif (i + 1) < today.week_in_year:
                shade = '900'
            else:
                shade = '400'

        gweeks += f'''        <path id="week_{str(i).zfill(3)}" style="fill:{colours[SI(i + 1)][shade]};" d="{week_wedge}" />\n'''

        gtext += f'''        <path id="week_line_{str(i).zfill(3)}" style="fill:none;" d="{week_line}" />\n'''

        if locale.calendar_displayed == 'DCC':
            gweeks, gtext = _dcc_display(locale, gweeks, gtext, i, colours, angle, week_wedge, month_line, week_line, leap_week_line, arch)

        else:
            gweeks, gtext = _sym_display(locale, gweeks, gtext, i, colours, angle, week_wedge, month_line, week_line, weeks, arch)

        angle += arch

    gtext += '    </g>\n'
    gweeks += '    </g>\n'

    wf += '    <g id="weeks_calendar">'
    wf += gweeks
    wf += gtext
    wf += '    </g>'

    wf += _time_display(locale, colours, gray, today)
    wf += _shastadari_logo(locale, gray, today)
    wf += '</svg>'

    return wf

#     text = f'''<html>
# <head>
#     <style>
#         html {{
#             background-color: #000;
#         }};
#     </style>
# </head>
# <body>
# {wf}
# </body>
# <script>
# </script>
# </html>'''
    # return Response(wf, mimetype='image/svg+xml')


def _dcc_display(locale, gweeks, gtext, i, colours, angle, week_wedge, month_line, week_line, leap_week_line, arch):
    if 'c' in locale.format_token:
        gtext += f'''<text style="font-family:{FONT_FAMILY};font-size:6px;fill:{colours[SI(i + 1)]['900']};text-anchor:middle;text-align:center;"><textPath href="#week_line_{str(i).zfill(3)}"  startOffset="25%" textLength="50%">{locale.ADC_WEEK_ICON[int(i % 10)]}</textPath></text>\n'''
    else:
        gtext += f'''<text style="font-family:{FONT_FAMILY};font-size:6px;fill:{colours[SI(i + 1)]['900']};text-anchor:middle;text-align:center;"><textPath href="#week_line_{str(i).zfill(3)}"  startOffset="25%" textLength="50%">{i % 10}</textPath></text>\n'''

    #
    # Separators between months
    #
    if i % 10 == 0 and i // 10 != 14:
        week_wedge = ring(
            inner_radius=0,
            outer_radius=108,
            x=108,
            y=108,
            start_angle=angle - D('0.25'),
            end_angle=angle + D('0.25'),
            without_inner=True,
        )
        gweeks += f'''        <path id="month_separator_{str(i).zfill(3)}" style="fill:#000000;" d="{week_wedge}" />\n'''

        gtext += f'''        <path id="month_line_{str(i).zfill(3)}" style="fill:none;" d="{month_line}" />\n'''

        if 'c' in locale.format_token:
            gtext += f'''<text style="font-family:{FONT_FAMILY};font-size:8px;fill:{colours[SI(i + 1)]['900']};text-anchor:middle;text-align:center;">
<textPath href="#month_line_{str(i).zfill(3)}" startOffset="25%" textLength="50%">{locale.ADC_MONTH_ICON[int(i // 10)]} • {locale.ADC_MONTH_NAME[int(i // 10)]}</textPath>
</text>\n'''
        else:
            gtext += f'''<text style="font-family:{FONT_FAMILY};font-size:6px;fill:{colours[SI(i + 1)]['900']};text-align:center;text-anchor:middle;"><textPath href="#month_line_{str(i).zfill(3)}"  startOffset="25%" textLength="50%">{i // 10} • {locale.DCC_MONTH_NAME[int(i // 10)]}</textPath></text>\n'''

    elif i // 10 == 14:
        week_wedge = ring(
            inner_radius=0,
            outer_radius=108,
            x=108,
            y=108,
            start_angle=angle - D('0.25'),
            end_angle=angle + D('0.25'),
            without_inner=True,
        )
        gweeks += f'''        <path id="month_separator_{str(i).zfill(3)}" style="fill:#000000;" d="{week_wedge}" />\n'''
        week_wedge = ring(
            inner_radius=0,
            outer_radius=108,
            x=108,
            y=108,
            start_angle=angle - D('0.25') + arch,
            end_angle=angle + D('0.25') + arch,
            without_inner=True,
        )
        gweeks += f'''        <path id="month_separator_{str(i).zfill(3)}_2" style="fill:#000000;" d="{week_wedge}" />\n'''

        gtext += f'''        <path id="month_line_{str(i).zfill(3)}" style="fill:none;" d="{leap_week_line}" />\n'''

        if 'c' in locale.format_token:
            gtext += f'''<text style="font-family:{FONT_FAMILY};font-size:8px;fill:{colours[SI(i + 1)]['900']};text-anchor:middle;text-align:center;">
<textPath href="#month_line_{str(i).zfill(3)}" startOffset="25%" textLength="50%">{locale.ADC_MONTH_ICON[int(i // 10)]}</textPath>
</text>\n'''
        else:
            gtext += f'''<text style="font-family:{FONT_FAMILY};font-size:6px;fill:{colours[SI(i + 1)]['900']};text-align:center;text-anchor:middle;"><textPath href="#month_line_{str(i).zfill(3)}" startOffset="25%" textLength="50%">{i // 10}</textPath></text>\n'''

    return gweeks, gtext


def _sym_display(locale, gweeks, gtext, i, colours, angle, week_wedge, month_line, week_line, weeks, arch):
    if locale.base == 10:
        gtext += f'''<text style="font-family:{FONT_FAMILY};font-size:5px;fill:{colours[SI(i + 1)]['900']};text-anchor:middle;text-align:center;"><textPath href="#week_line_{str(i).zfill(3)}"  startOffset="25%" textLength="50%">{(i + 1)}</textPath></text>\n'''
    elif locale.base == 14:
        gtext += f'''<text style="font-family:{FONT_FAMILY};font-size:5px;fill:{colours[SI(i + 1)]['900']};text-anchor:middle;text-align:center;"><textPath href="#week_line_{str(i).zfill(3)}"  startOffset="25%" textLength="50%">{(i + 1).decimal}</textPath></text>\n'''
    elif locale.base == 20:
        gtext += f'''<text style="font-family:{FONT_FAMILY};font-size:5px;fill:{colours[SI(i + 1)]['900']};text-anchor:middle;text-align:center;"><textPath href="#week_line_{str(i).zfill(3)}"  startOffset="25%" textLength="50%">{(i + 1).dozenal}</textPath></text>\n'''

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
            start_angle=angle - D('0.25'),
            end_angle=angle + D('0.25'),
            without_inner=True,
        )
        gweeks += f'''        <path id="month_separator_{str(i).zfill(3)}" style="fill:#000000;" d="{week_wedge}" />\n'''

        gtext += f'''        <path id="month_line_{str(i).zfill(3)}" style="fill:none;" d="{month_line}" />\n'''

        if locale.base == 10:
            gtext += f'''<text style="font-family:{FONT_FAMILY};font-size:6px;fill:{colours[SI(i + 1)]['900']};text-align:center;text-anchor:middle;"><textPath href="#month_line_{str(i).zfill(3)}"  startOffset="25%" textLength="50%">{month} • {locale.MONTH_NAME[int(month - 1)]}</textPath></text>\n'''
        elif locale.base == 14:
            gtext += f'''<text style="font-family:{FONT_FAMILY};font-size:6px;fill:{colours[SI(i + 1)]['900']};text-align:center;text-anchor:middle;"><textPath href="#month_line_{str(i).zfill(3)}"  startOffset="25%" textLength="50%">{month.decimal} • {locale.MONTH_NAME[int(month - 1)]}</textPath></text>\n'''
        elif locale.base == 20:
            gtext += f'''<text style="font-family:{FONT_FAMILY};font-size:6px;fill:{colours[SI(i + 1)]['900']};text-align:center;text-anchor:middle;"><textPath href="#month_line_{str(i).zfill(3)}"  startOffset="25%" textLength="50%">{month.dozenal} • {locale.MONTH_NAME[int(month - 1)]}</textPath></text>\n'''

    if i + 1 == weeks:
        week_wedge = ring(
            inner_radius=0,
            outer_radius=108,
            x=108,
            y=108,
            start_angle=angle + arch - D('0.25'),
            end_angle=angle + arch + D('0.25'),
            without_inner=True,
        )
        gweeks += f'''        <path id="month_separator_{str(i).zfill(3)}" style="fill:#000000;" d="{week_wedge}" />\n'''

    return gweeks, gtext


def _shastadari_logo(locale, colours, today):
    if locale.calendar_displayed == 'DCC':
        back_colour = colours[today.dcc_week_in_year]['900']
        front_colour = colours[today.dcc_week_in_year]['700']
    else:
        back_colour = colours[today.week_in_year]['900']
        front_colour = colours[today.week_in_year]['700']

    #
    # Shastadari Symbol
    #
    shastadari_size = 36
    shastadari_size_hexagon = shastadari_size / 3 * 2
    shastadari_thickness = shastadari_size / 9

    xl = '''    <g id="shastadari_logo">'''

    circle = ring(
        inner_radius=0,
        outer_radius=shastadari_size,
        x=108,
        y=108,
        start_angle=0,
        end_angle=0,
    )
    xl += f'''        <path id="shastadari_base" style="fill:{back_colour};" d="{circle}" />\n'''

    circle = ring(
        inner_radius=shastadari_size - shastadari_thickness,
        outer_radius=shastadari_size,
        x=108,
        y=108,
        start_angle=0,
        end_angle=0,
    )
    xl += f'''        <path id="shastadari_circle" style="fill:{front_colour};" d="{circle}" />\n'''

    hexagon = polygon(
        x=108,
        y=108,
        radius=shastadari_size_hexagon,
        n=6,
    )
    xl += f'''        <path id="shastadari_hexagon_outer" style="fill:{front_colour};" d="{hexagon}" />\n'''
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

    time_display_colour = time_colours['600']
    agrima_hand_colour = pointer_colours['200']
    posha_hand_colour = pointer_colours['500']
    uta_hand_colour = pointer_colours['800']

    display = '    <g id="watchface_time_display">\n'

    display += f'''        <circle id="base" style="fill:#000000;" cx="108" cy="108" r="90" />\n'''
    display += f'''        <circle id="number_base" style="fill:none;" cx="108" cy="108" r="66" />\n'''

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
    elif locale.base == 14:  # locale.HOUR_FORMAT == '12h':
        zero_position = 270
        hand_initial_angle = 0
    else:
        zero_position = 90
        hand_initial_angle = 180

    if locale.base == 10:
        shape_vertices = 3

        for i in range(36):
            if i in (0, 6, 12, 18, 24, 30):
                angle = zero_position + ((i / 6) * 60) - 1
                tick = ring(inner_radius=78, outer_radius=90, x=108, y=108, start_angle=angle, end_angle=angle + 2)

                angle = ((i / 36) * 360) + zero_position

                if angle > 360:
                    angle -= 360

                if True:
                    cx = 108 + 64 * math.cos(angle / 360 * math.pi * 2)
                    cy = 108 + 6 + 64 * math.sin(angle / 360 * math.pi * 2)

                    if '!' in locale.format_token:
                        display += f'''<text x="{cx}" y="{cy}" style="font-family:{FONT_FAMILY};font-size:18px;fill:{time_display_colour};text-anchor:middle;text-align:center;font-weight:bold;">{default_to_sezimal_digits(str(SI(D(i))))}</text>\n'''
                    else:
                        display += f'''<text x="{cx}" y="{cy}" style="font-family:{FONT_FAMILY};font-size:18px;fill:{time_display_colour};text-anchor:middle;text-align:center;font-weight:bold;">{SI(D(i))}</text>\n'''
                else:
                    cx = 108 + 72 * math.cos(angle / 360 * math.pi * 2)
                    cy = 108 + 72 * math.sin(angle / 360 * math.pi * 2)
                    display += f'''        <circle style="fill:{time_display_colour};" cx="{cx}" cy="{cy}" r="2" />\n'''

            else:
                angle = zero_position + (i * 10) - 0.5
                tick = ring(inner_radius=84, outer_radius=90, x=108, y=108, start_angle=angle, end_angle=angle + 1)

            display += f'''        <path id="tick_{str(SI(D(i))).zfill(2)}" style="fill:{time_display_colour};" d="{tick}" />\n'''

    elif locale.base == 14:
        shape_vertices = 3

        if False and locale.HOUR_FORMAT == '24h':
            for i in range(120):
                if i % 5 == 0:
                    angle = zero_position + ((i / 5) * 15) - 1
                    tick = ring(inner_radius=78, outer_radius=90, x=108, y=108, start_angle=angle, end_angle=angle + 2)

                    angle = ((i / 120) * 360) + zero_position

                    if angle > 360:
                        angle -= 360

                    if True:
                        cx = 108 + 66 * math.cos(angle / 360 * math.pi * 2)
                        cy = 108 + 5 + 66 * math.sin(angle / 360 * math.pi * 2)
                        display += f'''<text x="{cx}" y="{cy}" style="font-family:{FONT_FAMILY};font-size:13px;fill:{time_display_colour};text-anchor:middle;text-align:center;font-weight:normal;">{(i // 5)}</text>\n'''
                    else:
                        cx = 108 + 72 * math.cos(angle / 360 * math.pi * 2)
                        cy = 108 + 72 * math.sin(angle / 360 * math.pi * 2)
                        display += f'''        <circle style="fill:{time_display_colour};" cx="{cx}" cy="{cy}" r="2" />\n'''

                else:
                    angle = zero_position + (i * 7.5) - 0.5
                    tick = ring(inner_radius=84, outer_radius=90, x=108, y=108, start_angle=angle, end_angle=angle + 1)

                display += f'''        <path id="tick_{str(SI(D(i))).zfill(2)}" style="fill:{time_display_colour};" d="{tick}" />\n'''

        else:
            for i in range(60):
                if i in (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55):
                    angle = zero_position + ((i / 5) * 30) - 1
                    tick = ring(inner_radius=78, outer_radius=90, x=108, y=108, start_angle=angle, end_angle=angle + 2)

                    angle = ((i / 60) * 360) + zero_position

                    if angle > 360:
                        angle -= 360

                    if True:
                        cx = 108 + 66 * math.cos(angle / 360 * math.pi * 2)
                        cy = 108 + 6 + 66 * math.sin(angle / 360 * math.pi * 2)
                        display += f'''<text x="{cx}" y="{cy}" style="font-family:{FONT_FAMILY};font-size:16px;fill:{time_display_colour};text-anchor:middle;text-align:center;font-weight:bold;">{(i // 5) if i != 0 else '12'}</text>\n'''
                    else:
                        cx = 108 + 72 * math.cos(angle / 360 * math.pi * 2)
                        cy = 108 + 72 * math.sin(angle / 360 * math.pi * 2)
                        display += f'''        <circle style="fill:{time_display_colour};" cx="{cx}" cy="{cy}" r="2" />\n'''

                else:
                    angle = zero_position + (i * 6) - 0.5
                    tick = ring(inner_radius=84, outer_radius=90, x=108, y=108, start_angle=angle, end_angle=angle + 1)

                display += f'''        <path id="tick_{str(SI(D(i))).zfill(2)}" style="fill:{time_display_colour};" d="{tick}" />\n'''

    elif locale.base == 20:
        shape_vertices = 3

        for i in range(0, 144):
            if i % 12 == 0:
                angle = zero_position + 2 + ((i - 1) * 2.5)
                tick = ring(inner_radius=78, outer_radius=90, x=108, y=108, start_angle=angle, end_angle=angle + 1)

                display += f'''        <path id="tick_{str(i).zfill(3)}" style="fill:{time_display_colour};" d="{tick}" />\n'''

                angle = ((i / 144) * 360) + zero_position

                if angle > 360:
                    angle -= 360

                if True:
                    cx = 108 + 66 * math.cos(angle / 360 * math.pi * 2)
                    cy = 108 + 6 + 66 * math.sin(angle / 360 * math.pi * 2)
                    display += f'''<text x="{cx}" y="{cy}" style="font-family:{FONT_FAMILY};font-size:18px;fill:{time_display_colour};text-anchor:middle;text-align:center;font-weight:bold;">{DozenalInteger(D(i // 12))}</text>\n'''
                else:
                    cx = 108 + 72 * math.cos(angle / 360 * math.pi * 2)
                    cy = 108 + 72 * math.sin(angle / 360 * math.pi * 2)
                    display += f'''        <circle style="fill:{time_display_colour};" cx="{cx}" cy="{cy}" r="2" />\n'''

            else:
                angle = zero_position + 2 + ((i - 1) * 2.5)

                if i % 6 == 0:
                    tick = ring(inner_radius=78, outer_radius=90, x=108, y=108, start_angle=angle, end_angle=angle + 0.5)
                elif i % 3 == 0:
                    tick = ring(inner_radius=81, outer_radius=90, x=108, y=108, start_angle=angle, end_angle=angle + 0.5)
                else:
                    tick = ring(inner_radius=84, outer_radius=90, x=108, y=108, start_angle=angle, end_angle=angle + 0.5)

                display += f'''        <path id="tick_{str(i).zfill(3)}" style="fill:{time_display_colour};" d="{tick}" />\n'''

    #
    # Hands
    #
    display += f'    <g id="hand_posha" cx="108" cy="108" transform-box="fill-box" transform-origin="center">'
    display += f'''        <circle id="hand_uta_base" style="fill:none;" cx="108" cy="108" r="60"  />\n'''

    cx = 108 + 60 * math.cos(zero_position / 360 * math.pi * 2)
    cy = 108 + 60 * math.sin(zero_position / 360 * math.pi * 2)
    triangle = polygon(
        x=cx,
        y=cy,
        radius=18,
        n=shape_vertices,
        angle=hand_initial_angle,
    )
    display += f'''        <path id="hand_uta_pointer" style="fill:{uta_hand_colour};" d="{triangle}" />\n'''
    # display += '''        <animateTransform id="animate_uta_pointer" attributeType="xml" attributeName="transform" type="rotate" from="0" to="360" begin="0" dur="86400s" repeatCount="indefinite" />\n'''
    display += '    </g>'

    display += '    <g id="hand_uta" transform-origin="center">'
    display += f'''        <circle id="hand_posha_base" style="fill:none;" cx="108" cy="108" r="60" />\n'''

    cx = 108 + 60 * math.cos(zero_position / 360 * math.pi * 2)
    cy = 108 + 60 * math.sin(zero_position / 360 * math.pi * 2)
    triangle = polygon(
        x=cx,
        y=cy,
        radius=12,
        n=shape_vertices,
        angle=hand_initial_angle,
    )
    display += f'''        <path id="hand_posha_pointer" style="fill:{posha_hand_colour};" d="{triangle}" />\n'''
    # display += '''        <animateTransform id="animate_posha_pointer" attributeType="xml" attributeName="transform" type="rotate" from="0" to="360" begin="0" dur="2400s" repeatCount="indefinite" />\n'''
    display += '    </g>'

    display += '    <g id="hand_agrima" transform-origin="center">'
    display += f'''        <circle id="hand_agrima_base" style="fill:none;" cx="108" cy="108" r="60" />\n'''

    cx = 108 + 60 * math.cos(zero_position / 360 * math.pi * 2)
    cy = 108 + 60 * math.sin(zero_position / 360 * math.pi * 2)
    triangle = polygon(
        x=cx,
        y=cy,
        radius=6,
        n=shape_vertices,
        angle=hand_initial_angle,
    )
    display += f'''        <path id="hand_agrima_pointer" style="fill:{agrima_hand_colour};" d="{triangle}" />\n'''
    # display += '''        <animateTransform id="animate_agrima_pointer" attributeType="xml" attributeName="transform" type="rotate" from="0" to="360" begin="0" dur="60606ms" repeatCount="indefinite" />\n'''
    display += '    </g>'

    if locale.base == 20:
        display += '    <g id="hand_dozenal" transform-origin="center">'
        display += f'''        <circle id="hand_dozenal_base" style="fill:none;" cx="108" cy="108" r="60" />\n'''

        cx = 108 + 60 * math.cos(zero_position / 360 * math.pi * 2)
        cy = 108 + 60 * math.sin(zero_position / 360 * math.pi * 2)
        triangle = polygon(
            x=cx,
            y=cy,
            radius=shape_vertices,
            n=shape_vertices,
            angle=hand_initial_angle,
        )
        display += f'''        <path id="hand_dozenal_pointer" style="fill:{pointer_colours['100']};" d="{triangle}" />\n'''
        # display += '''        <animateTransform id="animate_agrima_pointer" attributeType="xml" attributeName="transform" type="rotate" from="0" to="360" begin="0" dur="60606ms" repeatCount="indefinite" />\n'''
        display += '    </g>'

    display += '    </g>\n'

    return display
