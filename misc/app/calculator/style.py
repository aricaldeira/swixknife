
import os

DIR_NAME = os.path.dirname(__file__)

FONTS_PATH = os.path.join(DIR_NAME, f'static{os.sep}fonts{os.sep}')

from kivy.core.text import LabelBase


FONTS = [
    {
        'name': 'Andika',
        'fn_regular': FONTS_PATH + 'AndikaTauga-Regular.ttf',
        'fn_italic': FONTS_PATH + 'AndikaTauga-Italic.ttf',
        'fn_bold': FONTS_PATH + 'AndikaTauga-Bold.ttf',
        'fn_bolditalic': FONTS_PATH + 'AndikaTauga-BoldItalic.ttf',
    },
    {
        'name': 'Gentium',
        'fn_regular': FONTS_PATH + 'GentiumBookPlus-Regular.ttf',
        'fn_italic': FONTS_PATH + 'GentiumBookPlus-Italic.ttf',
        'fn_bold': FONTS_PATH + 'GentiumBookPlus-Bold.ttf',
        'fn_bolditalic': FONTS_PATH + 'GentiumBookPlus-BoldItalic.ttf',
    },
]


for font in FONTS:
    LabelBase.register(**font)

from kivy.properties import DictProperty

ANDIKA_FONT_STYLE = {
    'H1': ['Andika', 96, False, -1.5],
    'H2': ['Andika', 60, False, -0.5],
    'H3': ['Andika', 48, False, 0],
    'H4': ['Andika', 34, False, 0.25],
    'H5': ['Andika', 24, False, 0],
    'H6': ['Andika', 20, False, 0.15],
    'Subtitle1': ['Andika', 16, False, 0.15],
    'Subtitle2': ['Andika', 14, False, 0.1],
    'Body1': ['Andika', 16, False, 0.5],
    'Body2': ['Andika', 14, False, 0.25],
    'Button': ['Andika', 14, True, 1.25],
    'Caption': ['Andika', 12, False, 0.4],
    'Overline': ['Andika', 10, True, 1.5],
    'Icon': ['Icons', 24, False, 0],
}

GENTIUM_FONT_STYLE = {
    'H1': ['Gentium', 96, False, -1.5],
    'H2': ['Gentium', 60, False, -0.5],
    'H3': ['Gentium', 48, False, 0],
    'H4': ['Gentium', 34, False, 0.25],
    'H5': ['Gentium', 24, False, 0],
    'H6': ['Gentium', 20, False, 0.15],
    'Subtitle1': ['Gentium', 16, False, 0.15],
    'Subtitle2': ['Gentium', 14, False, 0.1],
    'Body1': ['Gentium', 16, False, 0.5],
    'Body2': ['Gentium', 14, False, 0.25],
    'Button': ['Gentium', 14, True, 1.25],
    'Caption': ['Gentium', 12, False, 0.4],
    'Overline': ['Gentium', 10, True, 1.5],
    'Icon': ['Icons', 24, False, 0],
}
