
import re
import timeit

from kivymd.app import MDApp
from kivy.config import Config
from kivy.core.window import Window
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDFlatButton
from kivy.metrics import dp
from kivy.clock import Clock


from swixknife.calculator import SezimalCalculator
from swixknife.base import validate_clean_sezimal, validate_clean_decimal

from style import GENTIUM_FONT_STYLE, ANDIKA_FONT_STYLE

MAX_WIDTH = 383
MAX_HEIGHT = 550

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', MAX_WIDTH)
Config.set('graphics', 'height', MAX_HEIGHT)
Config.set('graphics', 'minimum_width', MAX_WIDTH)
Config.set('graphics', 'minimum_height', MAX_HEIGHT)


CALC = SezimalCalculator()

P_NOTATION_ALLOWED = re.compile('\.[0-9][0-9_]{0,}$')


class SKButton(MDFlatButton):
    def __init__(self, **kwargs):
        super(SKButton, self).__init__(**kwargs)
        self.start = 0
        self.single_hit = 0
        self.long_pressed_time = 0.3
        self.double_tap_time = 0.2
        self.press_state = False
        self.register_event_type('on_double_press')
        self.register_event_type('on_long_press')

    def on_touch_down(self, touch):
        if self.disabled:
            return

        if self.collide_point(touch.x, touch.y):
            self.start = timeit.default_timer()
            if touch.is_double_tap:
                self.press_state = True
                self.single_hit.cancel()
                self.dispatch('on_double_press')
        else:
            return super(SKButton, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.disabled:
            return

        if self.press_state is False:
            if self.collide_point(touch.x, touch.y):
                stop = timeit.default_timer()
                awaited = stop - self.start

                def not_double(time):
                    nonlocal awaited
                    if awaited > self.long_pressed_time:
                        self.dispatch('on_long_press')
                    else:
                        self.dispatch('on_press')

                self.single_hit = Clock.schedule_once(not_double, self.double_tap_time)
            else:
                return super(SKButton, self).on_touch_down(touch)
        else:
            self.press_state = False

    def on_double_press(self):
        pass

    def on_long_press(self):
        pass


class SezimalGrid(MDGridLayout):
    def do_layout(self, *args, **kwargs):
        super().do_layout()
        self.separator.text = CALC.locale.SEZIMAL_SEPARATOR
        self.update_display()

    def update_display(self):
        self.display.text = CALC.display or '0'
        self.secondary_display.text = CALC.decimal_display or '0'
        self.p_notation.disabled = not P_NOTATION_ALLOWED.search(CALC.expression)

        try:
            if CALC.expression != '':
                x = validate_clean_sezimal(CALC.expression)

            self.switch_base.disabled = False
        except:
            self.switch_base.disabled = True

    def button_clear(self, **kwargs):
        CALC.expression = '0'
        self.update_display()

    def button_eval(self):
        CALC.eval_expression()
        self.update_display()

    def button_press(self, text=''):
        if CALC.decimal:
            return

        CALC.expression += text
        self.update_display()

    def button_switch_base(self):
        CALC.decimal = True
        CALC.expression = CALC._decimal_expression
        self.parent.manager.current = 'DecimalScreen'
        self.parent.manager.children[1].children[0].update_display()

    def button_backspace(self):
        CALC.expression = CALC.expression[:-1]
        self.update_display()


class DecimalGrid(MDGridLayout):
    def do_layout(self, *args, **kwargs):
        super().do_layout()
        self.separator.text = CALC.locale.SEZIMAL_SEPARATOR
        self.update_display()

    def update_display(self):
        self.display.text = CALC.decimal_display or '0'
        self.secondary_display.text = CALC.display or '0'
        self.p_notation.disabled = not P_NOTATION_ALLOWED.search(CALC.expression)

        try:
            if CALC.expression != '':
                x = validate_clean_decimal(CALC.expression)

            self.switch_base.disabled = False
        except:
            self.switch_base.disabled = True

    def button_clear(self, **kwargs):
        CALC.expression = '0'
        self.update_display()

    def button_eval(self):
        CALC.eval_expression()
        self.update_display()

    def button_press(self, text=''):
        if not CALC.decimal:
            return

        CALC.expression += text
        self.update_display()

    def button_switch_base(self):
        CALC.decimal = False
        CALC.expression = CALC._sezimal_expression
        self.parent.manager.current = 'SezimalScreen'
        self.parent.manager.children[0].children[0].update_display()

    def button_backspace(self):
        CALC.expression = CALC.expression[:-1]
        self.update_display()


class SezimalScreen(MDScreen):
    def do_layout(self, *args, **kwargs):
        super().do_layout()

        width, height = Window.size

        if width > MAX_WIDTH:
            Window.size = MAX_WIDTH, Window.size[1]

        if height > MAX_HEIGHT:
            Window.size = Window.size[0], MAX_HEIGHT


class DecimalScreen(MDScreen):
    def do_layout(self, *args, **kwargs):
        super().do_layout()

        width, height = Window.size

        if width > MAX_WIDTH:
            Window.size = MAX_WIDTH, Window.size[1]

        if height > MAX_HEIGHT:
            Window.size = Window.size[0], MAX_HEIGHT


class SwixknifeScreenManager(MDScreenManager):
    pass


class SwixknifeApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.font_styles = ANDIKA_FONT_STYLE
        self.theme_cls._text_color = 'ffffff'
        return SwixknifeScreenManager()


if __name__ == '__main__':
    SwixknifeApp().run()
