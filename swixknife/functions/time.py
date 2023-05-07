
import datetime
import time
from decimal import Decimal

from ..sezimal import Sezimal
from ..base import sezimal_format
from ..units.conversions import SECOND_TO_AGRIMA


def agrimas_since_midnight() -> Sezimal:
    today = datetime.date.today()
    seconds_since_midnight = time.time() - time.mktime(today.timetuple())
    agrimas_since_midnight = Decimal(str(seconds_since_midnight)) * SECOND_TO_AGRIMA
    return agrimas_since_midnight


def uta_posha_agrima_now(anuga_and_boda=False) -> str:
    agrimas = agrimas_since_midnight()

    if anuga_and_boda:
        now = sezimal_format(agrimas_since_midnight(), group_separator=':', subgroup_separator=':', sezimal_places=4, minimum_size=10)
    else:
        now = sezimal_format(agrimas_since_midnight(), group_separator=':', subgroup_separator=':', sezimal_places=0, minimum_size=10)

    return now
