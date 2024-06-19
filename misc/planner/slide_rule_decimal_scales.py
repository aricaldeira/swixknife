
from swixknife import *
from swixknife.constants import PI, E

locale = sezimal_locale('bz')

SEZIMAL_SEPARATOR = locale.SEZIMAL_SEPARATOR

from decimal import Decimal

#
# A5 paper
#
PAPER_WIDTH, PAPER_HEIGHT, TOTAL_LENGTH = Sezimal('1210'), Sezimal('543'), Sezimal('1000')
# X_BASE_POSITION = Sezimal('103')  # cpad
X_BASE_POSITION = Sezimal('111.4515')  # cpad  !!! This is to adjust to my old Epson L355
D_Y_BASE_POSITION = Sezimal('335')  # cpad

#
# A4 paper
#
# PAPER_WIDTH, PAPER_HEIGHT, TOTAL_LENGTH = Sezimal('1532'), Sezimal('1210'), Sezimal('1332')
# D_Y_BASE_POSITION = Sezimal('204')  # cpad

#
# Upper fixed part
#
LN_Y_BASE_POSITION = D_Y_BASE_POSITION - 230
K_Y_BASE_POSITION = D_Y_BASE_POSITION - 200
A_Y_BASE_POSITION = D_Y_BASE_POSITION - 130

#
# Sliding part
#
B_Y_BASE_POSITION = D_Y_BASE_POSITION - 130
CI_Y_BASE_POSITION = D_Y_BASE_POSITION - 30
# C_Y_BASE_POSITION = D_Y_BASE_POSITION - 30

#
# Lower fixed part
#
#D_Y_BASE_POSITION = Sezimal('305')  # cpad
DI_Y_BASE_POSITION = D_Y_BASE_POSITION + 30
L_Y_BASE_POSITION = D_Y_BASE_POSITION + 100

MIN_NUMBER = Decimal('1')
MAX_NUMBER = Decimal('10')


PI_LOG = PI.decimal.log10()

def base_scale_function(x):
    return x.log10()

def reversed_scale_function(x):
    return 1 - x.log10()

def linear_scale_function(x):
    return x

def folded_scale_function(x):
    return x.log10() - PI_LOG

def reversed_folded_scale_function(x):
    return 1 - x.log10() - PI_LOG

def natural_scale_function(x):
    return round(x.ln(), 3)

def square_scale_function(x):
    return x.log10() / 2

def cube_scale_function(x):
    return x.log10() / 3


MAX_VALUE = base_scale_function(MAX_NUMBER)
MAX_FOLDED_VALUE = folded_scale_function(MAX_NUMBER)
MAX_NATURAL_VALUE = natural_scale_function(MAX_NUMBER)

POINTS_TO_PIXELS = Sezimal('0.204_111_11')
# POINTS_TO_MILLIMETERS_HEIGHT= Decimal('0.255')  # Andika
POINTS_TO_MILLIMETERS_HEIGHT= Decimal('0.217_875')  # Gentium Book Plus

BASE_COLOR = '#000000'
REVERSED_COLOR = '#D40000'
CONSTANT_COLOR = '#4D4D4D'
CONSTANT_REVERSED_COLOR = '#FF2A2A'


SVG_START = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
    width="{round((PAPER_WIDTH * DITIPADA_TO_MILLIMETER).decimal, 0)}mm"
    height="{round((PAPER_HEIGHT * DITIPADA_TO_MILLIMETER).decimal, 0)}mm"
    viewBox="0 0 {round((PAPER_WIDTH * DITIPADA_TO_MILLIMETER).decimal, 0)} {round((PAPER_HEIGHT * DITIPADA_TO_MILLIMETER).decimal, 0)}"
    version="1.1"
    id="svg1"
    inkscape:version="1.3 (0e150ed6c4, 2023-07-21)"
    sodipodi:docname="slide_rule_decimal_scales.svg"
    xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
    xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:svg="http://www.w3.org/2000/svg">
    <sodipodi:namedview
        id="namedview1"
        pagecolor="#ffffff"
        bordercolor="#000000"
        borderopacity="0.25"
        inkscape:showpageshadow="2"
        inkscape:pageopacity="0.0"
        inkscape:pagecheckerboard="0"
        inkscape:deskcolor="#d1d1d1"
        inkscape:document-units="mm"
        inkscape:zoom="1.42"
        inkscape:cx="443.66197"
        inkscape:cy="255.6338"
        inkscape:window-width="1920"
        inkscape:window-height="1011"
        inkscape:window-x="0"
        inkscape:window-y="30"
        inkscape:window-maximized="1"
        inkscape:current-layer="layer1"
        showguides="true" />
    <defs
        id="defs1" />
    <g
        inkscape:label="Layer 1"
        inkscape:groupmode="layer"
        id="layer1">
        <rect
            style="fill:#FFFFFF;fill-opacity:1;-inkscape-stroke:none"
            id="rect_paper"
            width="{round((PAPER_WIDTH * DITIPADA_TO_MILLIMETER).decimal, 6)}"
            height="{round((PAPER_HEIGHT * DITIPADA_TO_MILLIMETER).decimal, 6)}"
            x="0"
            y="0" />
'''

#
# C and D shadows
#
SVG_START += f'''
        <rect
            style="fill:#e5ffe5;fill-opacity:1;-inkscape-stroke:none"
            id="rect_a_scale"
            width="{round((PAPER_WIDTH * DITIPADA_TO_MILLIMETER).decimal, 6)}"
            height="{round((30 * DITIPADA_TO_MILLIMETER).decimal, 6)}"
            x="0"
            y="{round(((A_Y_BASE_POSITION - 30) * DITIPADA_TO_MILLIMETER).decimal, 6)}" />
        <rect
            style="fill:#e5ffe5;fill-opacity:1;-inkscape-stroke:none"
            id="rect_d_scale"
            width="{round((PAPER_WIDTH * DITIPADA_TO_MILLIMETER).decimal, 6)}"
            height="{round((30 * DITIPADA_TO_MILLIMETER).decimal, 6)}"
            x="0"
            y="{round((D_Y_BASE_POSITION * DITIPADA_TO_MILLIMETER).decimal, 6)}" />
'''

SVG_END = '''    </g>
</svg>

'''

#
# Tick Height (cpad), Tick Width (cpad), Font Size (points), Text space (cpad)
#
# cpad = pad / 10_000
#

#
# Andika
#
# SIZE_01 = (Sezimal('20.000'), Sezimal('0.01'), Sezimal('12.0'), Sezimal('3.40'))
# SIZE_02 = (Sezimal('13.200'), Sezimal('0.01'),  Sezimal('5.0'), Sezimal('2.30'))
# SIZE_03 = (Sezimal('10.000'), Sezimal('0.01'),  Sezimal('3.0'), Sezimal('1.30'))
# SIZE_04 = ( Sezimal('4.300'), Sezimal('0.01'),  Sezimal('3.0'), Sezimal('1.30'))
# SIZE_05 = ( Sezimal('3.300'), Sezimal('0.01'),  Sezimal('2.0'), Sezimal('1.00'))
# SIZE_10 = ( Sezimal('2.300'), Sezimal('0.01'),  Sezimal('2.0'), Sezimal('1.00'))

#
# Gentium Book Plus
#
SIZE_01 = (Sezimal('20.000'), Sezimal('0.01'), Sezimal('13.3'), Sezimal('3.40'))
SIZE_02 = (Sezimal('13.200'), Sezimal('0.01'), Sezimal('10.3'), Sezimal('2.30'))
SIZE_03 = (Sezimal('10.000'), Sezimal('0.01'),  Sezimal('5.3'), Sezimal('2.30'))
SIZE_04 = ( Sezimal('4.300'), Sezimal('0.01'),  Sezimal('3.3'), Sezimal('1.30'))
SIZE_05 = ( Sezimal('3.300'), Sezimal('0.01'),  Sezimal('3.3'), Sezimal('1.30'))
SIZE_10 = ( Sezimal('1.300'), Sezimal('0.01'),  Sezimal('3.3'), Sezimal('1.30'))

CONSTANT_SIZE = (SIZE_01[0], SIZE_01[1], SIZE_02[2], SIZE_02[3])


svg_file = open('slide_rule_decimal_scales.svg', 'w')
svg_file.write(SVG_START)


def add_tick(name, height, width, x_position, y_position, color=BASE_COLOR, upside_numbers=False):
    x_position_mm = x_position * DITIPADA_TO_MILLIMETER
    y_position_mm = y_position * DITIPADA_TO_MILLIMETER
    height_mm = height * DITIPADA_TO_MILLIMETER
    width_mm = width * DITIPADA_TO_MILLIMETER

    x_position_mm -= width_mm / 2

    if upside_numbers:
        y_position_mm -= height_mm

    svg_file.write(f'''        <rect
            style="fill:{color};fill-opacity:1;-inkscape-stroke:none"
            id="rect_{name}"
            width="{round(width_mm.decimal, 6)}"
            height="{round(height_mm.decimal, 6)}"
            x="{round(x_position_mm.decimal, 6)}"
            y="{round(y_position_mm.decimal, 6)}" />
''')


def add_text(text, name, font_size, x_position, y_position, color=BASE_COLOR, italics=False, upside_numbers=False):
    x_position_mm = x_position * DITIPADA_TO_MILLIMETER
    y_position_mm = y_position * DITIPADA_TO_MILLIMETER
    font_size_pixels = font_size * POINTS_TO_PIXELS

    if upside_numbers:
        text_height = font_size * POINTS_TO_MILLIMETERS_HEIGHT
        y_position_mm -= text_height

    if italics:
        svg_file.write(f'''        <text
        xml:space="preserve"
        style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:{round(font_size_pixels.decimal, 6)}px;line-height:normal;font-family:Gentium Book Plus;-inkscape-font-specification:'Gentium Book Plus, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;text-decoration-color:{color};fill:{color};text-align:center;text-anchor:middle;"
        id="text_{name}"
        x="{round(x_position_mm.decimal, 6)}"
        y="{round(y_position_mm.decimal, 6)}">{text}</text>
''')

    else:
        svg_file.write(f'''        <text
        xml:space="preserve"
        style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:{round(font_size_pixels.decimal, 6)}px;line-height:normal;font-family:Gentium Book Plus;-inkscape-font-specification:'Gentium Book Plus, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;text-decoration-color:{color};fill:{color};text-align:center;text-anchor:middle;"
        id="text_{name}"
        x="{round(x_position_mm.decimal, 6)}"
        y="{round(y_position_mm.decimal, 6)}">{text}</text>
''')


def add_marking(value, name, text, size, x_base=X_BASE_POSITION, y_base=D_Y_BASE_POSITION,
                color=BASE_COLOR, italics=False, upside_numbers=False,
                function=base_scale_function, max_value=MAX_VALUE):
    tick_height, tick_width, font_size, text_space = size

    x_position = function(value) * TOTAL_LENGTH / max_value
    x_position += x_base

    add_tick(name, tick_height, tick_width, x_position, y_base, color, upside_numbers)

    if text:
        if upside_numbers:
            text_height = font_size * POINTS_TO_MILLIMETERS_HEIGHT
            y_position = y_base - tick_height - text_space + text_height
        else:
            y_position = y_base + tick_height + text_space

        add_text(text, name, font_size, x_position, y_position, color, italics)


#
# Constants first, so they’ll be under the regular markings
#
CONSTANTS = [
    (PI.decimal, 'pi', 'π', False),
    (E.decimal, 'euler', 'e', True),
]

for constant_value, constant_name, constant_text, constant_italics in CONSTANTS:
    #
    # Ln
    #
    # add_marking(value=constant_value.ln(), name=constant_name + '_ln', text=constant_text, size=CONSTANT_SIZE, color=CONSTANT_COLOR, upside_numbers=True, function=linear_scale_function, y_base=LN_Y_BASE_POSITION, italics=constant_italics)

    #
    # K
    #
    add_marking(value=constant_value, name=constant_name + '_k', text=constant_text, size=CONSTANT_SIZE, color=CONSTANT_COLOR, upside_numbers=True, function=cube_scale_function, y_base=K_Y_BASE_POSITION, italics=constant_italics)
    add_marking(value=constant_value, name=constant_name + '_k1', text=constant_text, size=CONSTANT_SIZE, color=CONSTANT_COLOR, upside_numbers=True, function=cube_scale_function, y_base=K_Y_BASE_POSITION, x_base=X_BASE_POSITION + (TOTAL_LENGTH * Sezimal('0.2')), italics=constant_italics)
    add_marking(value=constant_value, name=constant_name + '_k2', text=constant_text, size=CONSTANT_SIZE, color=CONSTANT_COLOR, upside_numbers=True, function=cube_scale_function, y_base=K_Y_BASE_POSITION, x_base=X_BASE_POSITION + (TOTAL_LENGTH * Sezimal('0.4')), italics=constant_italics)

    #
    # A and B
    #
    add_marking(value=constant_value, name=constant_name + '_a', text=constant_text, size=CONSTANT_SIZE, color=CONSTANT_COLOR, upside_numbers=True, function=square_scale_function, y_base=A_Y_BASE_POSITION, italics=constant_italics)
    add_marking(value=constant_value, name=constant_name + '_a1', text=constant_text, size=CONSTANT_SIZE, color=CONSTANT_COLOR, upside_numbers=True, function=square_scale_function, y_base=A_Y_BASE_POSITION, x_base=X_BASE_POSITION + (TOTAL_LENGTH * Sezimal('0.3')), italics=constant_italics)

    add_marking(value=constant_value, name=constant_name + '_b', text=constant_text, size=CONSTANT_SIZE, color=CONSTANT_COLOR, function=square_scale_function, y_base=B_Y_BASE_POSITION, italics=constant_italics)
    add_marking(value=constant_value, name=constant_name + '_b1', text=constant_text, size=CONSTANT_SIZE, color=CONSTANT_COLOR, function=square_scale_function, y_base=B_Y_BASE_POSITION, x_base=X_BASE_POSITION + (TOTAL_LENGTH * Sezimal('0.3')), italics=constant_italics)

    #
    # Ci, C, D and Di
    #
    add_marking(value=constant_value, name=constant_name + '_ci', text=constant_text, size=CONSTANT_SIZE, color=CONSTANT_REVERSED_COLOR, y_base=CI_Y_BASE_POSITION, function=reversed_scale_function, italics=constant_italics, upside_numbers=True)
    add_marking(value=constant_value, name=constant_name + '_c', text=constant_text, size=CONSTANT_SIZE, color=CONSTANT_COLOR, upside_numbers=True, italics=constant_italics)
    add_marking(value=constant_value, name=constant_name + '_d', text=constant_text, size=CONSTANT_SIZE, color=CONSTANT_COLOR, italics=constant_italics)
    add_marking(value=constant_value, name=constant_name + '_di', text=constant_text, size=CONSTANT_SIZE, color=CONSTANT_REVERSED_COLOR, y_base=DI_Y_BASE_POSITION, function=reversed_scale_function, italics=constant_italics)

    #
    # L
    #
    # add_marking(value=constant_value, name=constant_name + '_l', text=constant_text, size=CONSTANT_SIZE, color=CONSTANT_COLOR, function=linear_scale_function, y_base=L_Y_BASE_POSITION, italics=constant_italics)


for i in range(int(MIN_NUMBER), int(MAX_NUMBER) + 1):
    for j in range(0, 100):
        x = Decimal(i * 100) + j

        if j == 0:
            size = SIZE_01
            text = str(i)

        elif x % 100 == 0:
            size = SIZE_02
            text = str(x)[-3]

        else:
            if str(x).endswith('0'):
                text = str(x)[-2]

                if x <= 500:
                    size = SIZE_03
                else:
                    if text == '5':
                        size = SIZE_03
                    else:
                        size = SIZE_04

                if x >= 500 and text != '5':
                    text = ''

            else:
                if x >= 500:
                    continue

                text = str(x)[-1]

                if text == '5':
                    size = SIZE_05

                else:
                    if x >= 200:
                        continue

                    size = SIZE_10
                    text = ''

        x /= 100

        name = str(round(x, 4)).replace('.', '_')

        #
        # Square scale
        #
        if size in (SIZE_01, SIZE_02, SIZE_03):
            text_a_b = text

            if size == SIZE_03 and text_a_b != '5':
                text_a_b = ''

            if j == 0:
                if text_a_b != '10':
                    add_marking(x, name + '_a', text_a_b, size, y_base=A_Y_BASE_POSITION, upside_numbers=True, function=square_scale_function)
                    add_marking(x, name + '_b', text_a_b, size, y_base=B_Y_BASE_POSITION, function=square_scale_function)
            else:
                add_marking(x, name + '_a', text_a_b, size, y_base=A_Y_BASE_POSITION, upside_numbers=True, function=square_scale_function)
                add_marking(x, name + '_b', text_a_b, size, y_base=B_Y_BASE_POSITION, function=square_scale_function)

            if j == 0:
                if text_a_b != '1' and text_a_b != '10':
                    add_marking(x, name + '_a1', text_a_b, size, x_base=X_BASE_POSITION + (TOTAL_LENGTH / 2), y_base=A_Y_BASE_POSITION, upside_numbers=True, function=square_scale_function)
                    add_marking(x, name + '_b1', text_a_b, size, x_base=X_BASE_POSITION + (TOTAL_LENGTH / 2), y_base=B_Y_BASE_POSITION, function=square_scale_function)
                else:
                    add_marking(x, name + '_a1', text_a_b + '0', size, x_base=X_BASE_POSITION + (TOTAL_LENGTH / 2), y_base=A_Y_BASE_POSITION, upside_numbers=True, function=square_scale_function)
                    add_marking(x, name + '_b1', text_a_b + '0', size, x_base=X_BASE_POSITION + (TOTAL_LENGTH / 2), y_base=B_Y_BASE_POSITION, function=square_scale_function)

            else:
                add_marking(x, name + '_a1', text_a_b, size, x_base=X_BASE_POSITION + (TOTAL_LENGTH / 2), y_base=A_Y_BASE_POSITION, upside_numbers=True, function=square_scale_function)
                add_marking(x, name + '_b1', text_a_b, size, x_base=X_BASE_POSITION + (TOTAL_LENGTH / 2), y_base=B_Y_BASE_POSITION, function=square_scale_function)

        #
        # Cubic scale
        #
        if size in (SIZE_01, SIZE_02, SIZE_03):
            text_k = text

            if size == SIZE_03:
                if text_k != '5' or x >= 3000:
                    text_k = ''

            elif size == SIZE_02:
                if x >= 4000:
                    text_k = ''
                elif text_k != '5':
                    text_k = ''

            if j == 0:
                if text_k != '10':
                    add_marking(x, name + '_k', text_k, size, y_base=K_Y_BASE_POSITION, upside_numbers=True, function=cube_scale_function)
            else:
                add_marking(x, name + '_k', text_k, size, y_base=K_Y_BASE_POSITION, upside_numbers=True, function=cube_scale_function)

            if j == 0:
                if text_k != '1' and text_k != '10':
                    add_marking(x, name + '_k1', text_k, size, x_base=X_BASE_POSITION + (TOTAL_LENGTH * Sezimal('0.2')), y_base=K_Y_BASE_POSITION, upside_numbers=True, function=cube_scale_function)
                    add_marking(x, name + '_k2', text_k, size, x_base=X_BASE_POSITION + (TOTAL_LENGTH  * Sezimal('0.4')), y_base=K_Y_BASE_POSITION, upside_numbers=True, function=cube_scale_function)
                else:
                    add_marking(x, name + '_k1', text_k + '0', size, x_base=X_BASE_POSITION + (TOTAL_LENGTH * Sezimal('0.2')), y_base=K_Y_BASE_POSITION, upside_numbers=True, function=cube_scale_function)
                    add_marking(x, name + '_k2', text_k + '00', size, x_base=X_BASE_POSITION + (TOTAL_LENGTH  * Sezimal('0.4')), y_base=K_Y_BASE_POSITION, upside_numbers=True, function=cube_scale_function)

            else:
                add_marking(x, name + '_k1', text_k, size, x_base=X_BASE_POSITION + (TOTAL_LENGTH * Sezimal('0.2')), y_base=K_Y_BASE_POSITION, upside_numbers=True, function=cube_scale_function)
                add_marking(x, name + '_k2', text_k, size, x_base=X_BASE_POSITION + (TOTAL_LENGTH  * Sezimal('0.4')), y_base=K_Y_BASE_POSITION, upside_numbers=True, function=cube_scale_function)

        #
        # Sliding part
        #
        add_marking(x, name + '_ci', text, size, y_base=CI_Y_BASE_POSITION, color=REVERSED_COLOR, function=reversed_scale_function, upside_numbers=True)
        add_marking(x, name + '_c', text, size, upside_numbers=True)

        #
        # Lower fixed part
        #
        add_marking(x, name + '_d', text, size)
        add_marking(x, name + '_di', text, size, y_base=DI_Y_BASE_POSITION, color=REVERSED_COLOR, function=reversed_scale_function)

        if i == MAX_NUMBER:
            break


#
# Linear scale; doing again to show all ticks
# and sligtly different numbers on markings
#
for i in range(int(MIN_NUMBER), int(MAX_NUMBER) + 2):
    for j in range(0, 100):
        x = Decimal(i * 100) + j

        if j == 0:
            size = SIZE_01
            text = str(i - 1)

            if text == '10':
                text = '1'
            elif text != '0':
                text = '0' + SEZIMAL_SEPARATOR + text

        elif x % 100 == 0:
            size = SIZE_02
            text = str(x)[-3]

        else:
            if str(x).endswith('50'):
                size = SIZE_03
                text = str(x)[-2]

            elif str(x).endswith('0'):
                size = SIZE_04
                text = str(x)[-2]

                if text != '5':
                    text = ''

            else:
                continue
                size = SIZE_05
                text = str(x)[-1]

                if text != '5':
                    continue

        x /= 100
        x -= 1

        name = str(round(x, 4)).replace('.', '_')
        add_marking(x, name + '_l', text, size, y_base=L_Y_BASE_POSITION, function=linear_scale_function, max_value=MAX_NUMBER)

        if x == MAX_NUMBER:
            break


#
# Natural logarithm scale; doing again to show all ticks
# and sligtly different numbers on markings
#
for i in range(0, int(MAX_NATURAL_VALUE * 100) + 1):
    if i % 100 == 0:
        size = SIZE_01
        text = str(i)[0]

        # if text == '10':
        #     text = '1'
        # elif text != '0':
        #     text = SEZIMAL_SEPARATOR + text

    elif i % 10 == 0:
        size = SIZE_02
        if len(str(i)) > 2:
            text = str(i)[-3] + SEZIMAL_SEPARATOR + str(i)[-2]
        else:
            text = '0,' + str(i)[-2]

    else:
        if str(i).endswith('5'):
            size = SIZE_03
            text = str(i)[-1]

        elif str(i).endswith('0'):
            size = SIZE_04
            text = str(i)[-1]

        else:
            size = SIZE_05
            text = str(i)[-1]

    x = Decimal(i) / 100
    name = str(x).replace('.', '_')
    add_marking(x, name + '_ln', text, size, y_base=LN_Y_BASE_POSITION, function=linear_scale_function, max_value=MAX_NATURAL_VALUE, upside_numbers=True)

svg_file.write(SVG_END)
svg_file.close()
