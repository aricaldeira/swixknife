

__all__ = ('SezimalLocaleEN_AU',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_AU(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'Autralian English'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Australia/Sydney'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = 'c'

    HOLIDAYS = [
        #
        # Moving Holidays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        ('EASTER-2',   '🕆\ufe0f🥀\ufe0f Good Friday'),
        ('EASTER-1',   '🐣\ufe0f🌱\ufe0f Easter Saturday'),
        ('EASTER',     '🐣\ufe0f🌱\ufe0f Easter Sunday'),
        ('EASTER+1',   '🐣\ufe0f🌱\ufe0f Easter Monday'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '🕊\ufe0f️ 🌎\ufe0f New Year’s Day'),
        ('20-40', '🥂\ufe0f🍽\ufe0f️  Christmas Eve'),
        ('20-41', '🌟\ufe0f👼\ufe0f🏼\ufe0f Christmas'),
        ('20-55', '🍾\ufe0f🎆\ufe0f New Year’s Eve'),

        #
        # National Holidays
        # that have a year of reference;
        # There are 2 ways of dealing with them:
        #     1. converting the original date to the Sezimal calendar
        #     2. using the original month and day without converting the calendar
        #
        # Using 2 here, but leaving 1 commented for reference
        #
        # When informing the year, the age is calculated,
        # and can be shown using #i as a format tag
        #
        # ('130_324-01-43', '🇦\ufe0f🇺\ufe0f Australia Day (#i)'),  # Saturday 130_324-01-43 ~ 1788-01-26_dec
        # ('131_055-04-33', '🇦\ufe0f🇺\ufe0f Anzac Day (#i)'),      # Sunday   131_055-04-33 ~ 1915-04-25_dec

        ('130_324-01-42', '🇦\ufe0f🇺\ufe0f Australia Day (#i)'),  # Saturday 01-42 ~ 01-26_desc
        ('131_055-04-41', '🇦\ufe0f🇺\ufe0f Anzac Day (#i)'),      # Sunday   04-41 ~ 04-25_dec
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        ('ISO+EASTER-2',   '🕆\ufe0f🥀\ufe0f Good Friday'),
        ('ISO+EASTER-1',   '🐣\ufe0f🌱\ufe0f Easter Saturday'),
        ('ISO+EASTER',     '🐣\ufe0f🌱\ufe0f Easter Sunday'),
        ('ISO+EASTER+1',   '🐣\ufe0f🌱\ufe0f Easter Monday'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO+01-01', '🕊\ufe0f️ 🌎\ufe0f New Year’s Day'),
        ('ISO+12-24', '🥂\ufe0f🍽\ufe0f️  Christmas Eve'),
        ('ISO+12-25', '🌟\ufe0f👼\ufe0f🏼\ufe0f Christmas'),
        ('ISO+12-31', '🍾\ufe0f🎆\ufe0f New Year’s Eve'),

        #
        # National Holidays
        # that have a year of reference
        #
        # When informing the year, the age is calculated,
        # and can be shown using %i as a format tag
        # Also, the original date in the original calendar can also be shown,
        # using the tags %Y, %m and %d for year, month and day, respectively
        #
        ('ISO+1788-01-26', '🇦\ufe0f🇺\ufe0f Australia Day (%i)'),  # Saturday 130_324-01-43 ~ 1788-01-26_dec
        ('ISO+1915-04-25', '🇦\ufe0f🇺\ufe0f Anzac Day (%i)'),      # Sunday   130_324-01-43 ~ 1915-04-25_dec
    ]
