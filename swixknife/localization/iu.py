

__all__ = ('SezimalLocaleIU',)


from .en_ca import SezimalLocaleEN_CA


class SezimalLocaleIU(SezimalLocaleEN_CA):
    LANG = 'iu'
    LANGUAGE = 'ᐃᓄᒃᑎᑐᑦ'

    WEEKDAY_NAME: list[str] = [
        'ᓇᒡᒐᔾᔭᐅ',
        'ᐊᐃᑉᐱᖅ',
        'ᐱᖓᑦᓯᖅ',
        'ᓯᑕᒻᒥᖅ',
        'ᑕᓪᓕᕐᒥᖅ',
        'ᓯᕙᑖᕐᕕᒃ',
        'ᓈᑦᑏᖑᔭ',
    ]

    WEEKDAY_ABBREVIATED_NAME: list[str] = [
        'ᓇᒡ',
        'ᐊᐃ',
        'ᐱᖓ',
        'ᓯᑕ',
        'ᑕᓪ',
        'ᓯᕙ',
        'ᓈᑦ',
    ]

    MONTH_NAME: list[str] = [
        'ᔮᓐᓄᐊᕆ',
        'ᕖᕝᕗᐊᕆ',
        'ᒫᑦᓯ',
        'ᐄᐳᕆ',
        'ᒪᐃ',
        'ᔫᓂ',
        'ᔪᓚᐃ',
        'ᐋᒡᒌᓯ',
        'ᓯᑎᐱᕆ',
        'ᐅᑐᐱᕆ',
        'ᓄᕕᐱᕆ',
        'ᑎᓯᐱᕆ',
    ]

    MONTH_ABBREVIATED_NAME: list[str] = [
        'ᔮᓐ',
        'ᕖᕝ',
        'ᒫᑦ',
        'ᐄᐳ',
        'ᒪᐃ',
        'ᔫᓂ',
        'ᔪᓚ',
        'ᐋᒡ',
        'ᓯᑎ',
        'ᐅᑐ',
        'ᓄᕕ',
        'ᑎᓯ',
    ]

