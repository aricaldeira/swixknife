

from .calendar import *
from ..date import SezimalDate
from ..date_time import SezimalDateTime
from ..sun_moon import list_sun_moon
from ..sezimal_functions import system_time_zone
from ...sezimal import SezimalInteger


class SezimalCalendarTerminal(SezimalCalendar):
    def __init__(self, *args, **kwargs):
        self = super().__init__(*args, **kwargs)
        self.color_scheme = 'FULL_COLOR'
