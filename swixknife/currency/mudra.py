
import requests

from decimal import Decimal
from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..date_time import SezimalDateTime

#
# Mudra - “coin”
# https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A5%81%E0%A4%A6%E0%A5%8D%E0%A4%B0%E0%A4%BE#Sanskrit
#
# Dana - “treasure, capital”
# https://en.wiktionary.org/wiki/%E0%A4%A7%E0%A4%A8#Sanskrit
#
# 1 mud = 1 satoshi
# 1 dan = 1 Xmud = 1_000_000 mud (46_656_d)
#

DANA_TO_MUDRA = SezimalFraction('1_000_000 / 1')
MUDRA_TO_DANA = DANA_TO_MUDRA.reciprocal

MUDRA_TO_SATOSHI = SezimalFraction('1 / 1')
SATOSHI_TO_MUDRA = MUDRA_TO_SATOSHI.reciprocal

DANA_TO_SATOSHI = DANA_TO_MUDRA * MUDRA_TO_SATOSHI
SATOSHI_TO_DANA = DANA_TO_SATOSHI.reciprocal

BITCOIN_TO_MUDRA = SezimalFraction('13_531_202_544 / 1')
MUDRA_TO_BITCOIN = BITCOIN_TO_MUDRA.reciprocal

DANA_TO_BITCOIN = DANA_TO_MUDRA * MUDRA_TO_BITCOIN
BITCOIN_TO_DANA = DANA_TO_BITCOIN.reciprocal

SATOSHI_TO_BITCOIN = SATOSHI_TO_MUDRA * MUDRA_TO_BITCOIN
BITCOIN_TO_SATOSHI = SATOSHI_TO_BITCOIN.reciprocal


class Mudra:
    def __init__(self, decimal_currency = 'BTC'):
        if not decimal_currency:
            decimal_currency = 'sats'

        if decimal_currency == 'mud' or decimal_currency == 'dan':
            raise ValueError('Decimal currency cannot be sezimal currency mud (mudra) or dan (dana)')

        self.decimal_currency = decimal_currency
        self.decimal_symbol = decimal_currency
        self._rates = {}
        self._date_time = None

    def update_rates(self):
        req = requests.get('https://api.coingecko.com/api/v3/exchange_rates')

        if req.status_code != 200:
            return

        self._rates = req.json()['rates']
        self._date_time = SezimalDateTime.now()

    def _check_mudra_to_decimal_currency_rate(self) -> Decimal:
        if not self._rates:
            self.update_rates()

        if self.decimal_currency.lower() not in self._rates:
            raise ValueError(f'Current rates for {self.decimal_currency} are unavailable')

        rate = self._rates[self.decimal_currency.lower()]

        self.decimal_symbol = rate['unit'].strip() if 'unit' in rate else self.decimal_currency

        return Decimal(str(rate['value'])) / BITCOIN_TO_MUDRA.decimal

    def mudra_to_decimal_currency(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        mudra = self._check_mudra_to_decimal_currency_rate()
        return Sezimal(Sezimal(amount).decimal * mudra)

    def dana_to_decimal_currency(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        return self.mudra_to_decimal_currency(Sezimal(amount).decimal * DANA_TO_MUDRA.decimal)

    def satoshi_to_decimal_currency(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        return self.mudra_to_decimal_currency(Sezimal(amount).decimal * SATOSHI_TO_MUDRA.decimal)

    def bitcoin_to_decimal_currency(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        return self.mudra_to_decimal_currency(Sezimal(amount).decimal * BITCOIN_TO_MUDRA.decimal)

    def decimal_currency_to_mudra(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        mudra = self._check_mudra_to_decimal_currency_rate()
        return Sezimal(Sezimal(amount).decimal / mudra)

    def decimal_currency_to_dana(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        return self.decimal_currency_to_mudra(amount) * MUDRA_TO_DANA

    def decimal_currency_to_satoshi(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        return self.decimal_currency_to_mudra(amount) * MUDRA_TO_SATOSHI

    def decimal_currency_to_bitcoin(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        return self.decimal_currency_to_mudra(amount) * MUDRA_TO_BITCOIN
