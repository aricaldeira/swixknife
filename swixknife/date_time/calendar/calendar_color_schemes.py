

from ...sezimal import Sezimal, SezimalInteger
from ...functions import SezimalRange, SezimalDictionary
from ...localization import sezimal_locale, SezimalLocale

from .calendar_color_scheme_full_color import WEEKS_SHADE_SEASON_FULL_COLOR_SCHEME
from .calendar_color_scheme_gray import WEEKS_SHADE_SEASON_GRAY_SCHEME
from .calendar_color_scheme_color_blind import WEEKS_SHADE_SEASON_COLOR_BLIND_SCHEME


_SHADES = ('50', '100', '200', '300', '400', '500', '600', '700', '800', '900') #, 'A100', 'A200', 'A400', 'A700')


_WEEKLY_SEASON_FULL_COLOR_CACHE = SezimalDictionary()
_WEEKLY_SEASON_GRAY_CACHE = SezimalDictionary()
_WEEKLY_SEASON_BLIND_CACHE = SezimalDictionary()


def weekly_season_colors(
    year: SezimalInteger, hemisphere: str = 'N',
    time_zone: str | ZoneInfo = None,
    scheme: str = 'FULL_COLOR'
) -> dict[SezimalInteger | int, str, str]:
    if scheme == 'FULL_COLOR':
        cache = _WEEKLY_SEASON_FULL_COLOR_CACHE
        colors = WEEKS_SHADE_SEASON_FULL_COLOR_SCHEME
    elif scheme == 'GRAY':
        cache = _WEEKLY_SEASON_GRAY_CACHE
        colors = WEEKS_SHADE_SEASON_GRAY_SCHEME
    else:
        cache = _WEEKLY_SEASON_BLIND_CACHE
        colors = WEEKS_SHADE_SEASON_COLOR_BLIND_SCHEME

    if year in cache:
        if hemisphere in cache[year]:
            if time_zone in cache[year][hemisphere]:
                return cache[year][hemisphere][time_zone]

    prior_december_solstice = list_sun_moon(
        year - 1, time_zone=time_zone, event='december_solstice'
    )[0][0]
    march_equinox = list_sun_moon(
        year, time_zone=time_zone, event='march_equinox'
    )[0][0]
    june_solstice = list_sun_moon(
        year, time_zone=time_zone, event='june_solstice'
    )[0][0]
    september_equinox = list_sun_moon(
        year, time_zone=time_zone, event='september_equinox'
    )[0][0]
    december_solstice = list_sun_moon(
        year, time_zone=time_zone, event='december_solstice'
    )[0][0]
    next_march_equinox = list_sun_moon(
        year + 1, time_zone=time_zone, event='march_equinox'
    )[0][0]

    prior_year = prior_december_solstice.replace(day=55).week_in_year
    prior_year -= prior_december_solstice.week_in_year + 1
    first_december_length = prior_year
    first_december_length += march_equinox.week_in_year - 1

    march_length = june_solstice.week_in_year - march_equinox.week_in_year
    june_length = september_equinox.week_in_year - june_solstice.week_in_year
    september_length = december_solstice.week_in_year - september_equinox.week_in_year

    second_december_length = december_solstice.replace(day=55).week_in_year
    second_december_length -= december_solstice.week_in_year + 1
    next_year = next_march_equinox.week_in_year - 1
    second_december_length += next_year

    res = SezimalDictionary()

    lengths = [
        first_december_length, march_length,
        june_length, september_length, second_december_length
    ]
    starting_points = [
        int(prior_year.decimal), 0,
        0, 0, 0,
    ]
    finishing_points = [
        None, None,
        None, None, int(next_year.decimal),
    ]
    weeks_spans = [
        first_december_length - prior_year, march_length,
        june_length, september_length, second_december_length - next_year + 1
    ]

    if hemisphere == 'N':
        seasons = ['winter', 'spring', 'summer', 'autumn', 'winter']
    else:
        seasons = ['summer', 'autumn', 'winter', 'spring', 'summer']

    week_number= SezimalInteger(1)

    for i in SezimalRange(5):
        season = seasons[i]
        season_length = lengths[i]
        starting_point = starting_points[i]
        finishing_point = finishing_points[i]
        weeks_span = weeks_spans[i]

        for j in SezimalRange(weeks_span):
            res[week_number] = SezimalDictionary()

            for shade in _SHADES:
                res[week_number][shade] = \
                    colors[season_length][shade][season][starting_point:finishing_point][j]

            week_number += SezimalInteger(1)

    if not year in cache:
        cache[year] = SezimalDictionary({
            hemisphere: {
                time_zone: res
            }
        })

    elif not hemisphere in cache[year]:
        cache[year][hemisphere] = SezimalDictionary({
            time_zone: res
        })

    elif not time_zone in cache[year][hemisphere]:
        cache[year][hemisphere][time_zone] = res

    return res
