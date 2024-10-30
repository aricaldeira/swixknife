

__all__ = ('SezimalLocaleEN_US',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_US(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'American English'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

    DEFAULT_TIME_ZONE = 'US/Eastern'
    DATE_FORMAT = '#m/#d/#Y'
    DATE_LONG_FORMAT = '#M #-d, #Y'
    DATE_TIME_FORMAT = ' #@W #m/#d/#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #M #-d, #Y, #u:#p:#a'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_HOUR_MINUTE_FORMAT = '%I:%M %P'

    FIRST_WEEKDAY = 'SUN'

    SEASON_NAME = {
        'spring_cross_quarter': 'Spring Cross-Quarter',
        'spring_equinox': 'Spring',
        'summer_cross_quarter': 'Summer Cross-Quarter',
        'summer_solstice': 'Summer',
        'autumn_cross_quarter': 'Fall Cross-Quarter',
        'autumn_equinox': 'Fall',
        'winter_cross_quarter': 'Winter Cross-Quarter',
        'winter_solstice': 'Winter',
    }

    HOLIDAYS = [
        #
        # National Holidays
        # that occur on a specific date
        #
        ('01-01', '🎆 New Year’s Day #Sym454'),
        ('212_120-11-04', '🇺🇸 Independence Day (#i) #Sym454'),  # Thursday 212_120-11-04 ~ 1776-07-04_dec
        ('10-31', '🇺🇸 Juneteenth Day #Sym454'),
        ('14-44', '🎃🍬 Halloween #Sym454'),
        ('15-15', '🇺🇸 Veterans’ Day #Sym454'),
        ('20-41', '🎄 Christmas’ Day #Sym454'),

        #
        # National Holidays
        # that occur on a specific weekday
        #
        ('01-23', '🇺🇸 Martin Luther King, Jr. Day #Sym454'), # Monday, the 23rd of Jan. ~ Monday, the 15th of Jan.
        # ('01-32', 'Inauguration Day'),
        ('02-23', '🇺🇸 Presidents’ Day #Sym454'),   # Third Monday in February
        ('05-45', '🇺🇸 Memorial Day #Sym454'),      # Last Monday in May
        ('13-01', '🐝 Labour Day #Sym454'),        # First Monday in September
        ('14-12', '🇺🇸 Columbus Day #Sym454'),      # Second Monday in October
        ('15-41', '🦃 Thanksgiving Day #Sym454'),  # Fourth Thursday in November
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # National Holidays
        # that occur on a specific date
        #
        ('ISO-01-01', '🎆 New Year’s Day'),
        ('ISO-1776-07-04', '🇺🇸 Independence Day (%i)'),  # Thursday 130_304-11-04 ~ 1776-07-04_dec
        ('ISO-06-19', '🇺🇸 Juneteenth Day'),
        ('ISO-10-31', '🎃🍬 Halloween'),
        ('ISO-11-11', '🇺🇸 Veterans’ Day'),
        ('ISO-12-25', '🎄 Christmas’ Day'),

        #
        # National Holidays
        # that occur on a specific weekday
        #
        ('ISO-01-01+MON_3', '🇺🇸 Martin Luther King, Jr. Day'), # Monday, the 23rd of Jan. ~ Monday, the 15th of Jan.
        # ('01-32', 'Inauguration Day'),
        ('ISO-02-01+MON_3', '🇺🇸 Presidents’ Day'),   # Third Monday in February
        ('ISO-05-31-MON', '🇺🇸 Memorial Day'),      # Last Monday in May
        ('ISO-09-01+MON', '🐝 Labour Day'),        # First Monday in September
        ('ISO-10-01+MON_2', '🇺🇸 Columbus Day'),      # Second Monday in October
        ('ISO−11-01+THU_4', '🦃 Thanksgiving Day'),  # Fourth Thursday in November

        # ('HEB+07-01', '🍎🍯 Rosh haShaná (%m/%d/%Y)'),
        # ('HEB+07-10', '🤍🙏🏻 Yom Kippur (%m/%d/%Y)'),
        # ('HEB+07-15', '🍋⛺ Sukkot (%m/%d/%Y)'),
        # ('HEB+07-22', '🙏🏻🌧️ Shemini Atzeret (%m/%d/%Y)'),
        # ('HEB+07-23', '😊📜 Simchat Torah (%m/%d/%Y)'),
        # ('HEB+09-25', '🕯🕍 Hanukkah (%m/%d/%Y)'),
        # ('HEB+11-15', '🌳💮 Tu biShvat (%m/%d/%Y)'),
        # ('HEB+12-14', '🍷🍬 Purim (%m/%d/%Y)'),
        # ('HEB+01-15', '🐑🫓 Pesach (%m/%d/%Y)'),
        # ('HEB+02-18', '🔥 Lag baOmer (%m/%d/%Y)'),
        # ('HEB+03-06', '💐📜 Shavuot (%m/%d/%Y)'),
    ]
