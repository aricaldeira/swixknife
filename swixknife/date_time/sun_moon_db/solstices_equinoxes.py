from sun_moon_astronomy import SezimalSun
from swixknife import SezimalRange
from swixknife import SezimalDate as SD

arq = open('solstice_equinox_dates.csv', 'w')

name = 'YEAR_START'
arq.write(f'{name}_SEZIMAL_DATE|IS_LEAP|{name}_SYM454_DATE|{name}_ISO_HOLOCENE_DATE|{name}_ISO_DATE|{name}_JULIAN_DATE|{name}_RATA_DIE|')

for name in [
        'FEBRUARY_CROSS_QUARTER',
        'MARCH_EQUINOX',
        'MAY_CROSS_QUARTER',
        'JUNE_SOLSTICE',
        'AUGUST_CROSS_QUARTER',
        'SEPTEMBER_EQUINOX',
        'NOVEMBER_CROSS_QUARTER',
        'DECEMBER_SOLSTICE',
    ]:
    arq.write(f'{name}_SEZIMAL_DATE|{name}_SYM454_DATE|{name}_ISO_HOLOCENE_DATE|{name}_ISO_DATE|{name}_JULIAN_DATE|{name}_RATA_DIE|')

arq.write('\n')

from tqdm import tqdm

for year in tqdm(SezimalRange(0, 140_001)):
    ss = SezimalSun(year, 'UTC')

    year_start = SD(year, 1, 1)
    date = year_start

    line = date.isoformat() + '|'
    line += 'Yes|' if date.is_leap else 'No|'
    line += date.symmetric_isoformat + '|'
    line += date.gregorian_holocene_isoformat + '|'
    line += date.gregorian_isoformat + '|'
    line += str(round(date.julian_date.decimal,1)) + '|'
    line += str(date.ordinal_date.decimal) + '|'

    for date in [
        ss.february_cross_quarter,
        ss.march_equinox,
        ss.may_cross_quarter,
        ss.june_solstice,
        ss.august_cross_quarter,
        ss.september_equinox,
        ss.november_cross_quarter,
        ss.december_solstice,
    ]:
        line += date.isoformat() + '|'
        line += date.symmetric_isoformat + ' ' + date.format('%H:%M:%S') + '|'
        line += date.gregorian_holocene_isoformat + ' ' + date.format('%H:%M:%S') + '|'
        line += date.gregorian_isoformat  + ' ' + date.format('%H:%M:%S') + '|'
        line += str(round(date.julian_date.decimal,9)) + '|'
        line += str(round(date.as_days.decimal, 9)) + '|'

    arq.write(line + '\n')

    print(year_start.isoformat(), year_start.is_leap, year_start.gregorian_isoformat)
