
import requests

from decimal import Decimal
from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..date_time import SezimalDateTime

from ..units import \
    MANI_TO_MISALI, MANI_TO_SATOSHI, MANI_TO_BITCOIN, \
    MISALI_TO_MANI, MISALI_TO_SATOSHI, MISALI_TO_BITCOIN, \
    BITCOIN_TO_MANI, BITCOIN_TO_SATOSHI, BITCOIN_TO_MISALI, \
    SATOSHI_TO_MANI, SATOSHI_TO_BITCOIN, SATOSHI_TO_MISALI \


class Mani:
    def __init__(self, decimal_currency = 'BTC'):
        if not decimal_currency:
            decimal_currency = 'sats'

        if decimal_currency == 'SMN' or decimal_currency == 'MSL':
            raise ValueError('Decimal currency cannot be sezimal currency SMN (mani) or MSL (misali)')

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

    def _check_mani_to_decimal_currency_rate(self) -> Decimal:
        if not self._rates:
            self.update_rates()

        if self.decimal_currency.lower() not in self._rates:
            raise ValueError(f'Current rates for {self.decimal_currency} are unavailable')

        rate = self._rates[self.decimal_currency.lower()]

        self.decimal_symbol = rate['unit'].strip() if 'unit' in rate else self.decimal_currency

        return Decimal(str(rate['value'])) / BITCOIN_TO_MANI.decimal

    def mani_to_decimal_currency(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        mani = self._check_mani_to_decimal_currency_rate()
        return Sezimal(Sezimal(amount).decimal * mani)

    def misali_to_decimal_currency(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        return self.mani_to_decimal_currency(Sezimal(amount).decimal * MISALI_TO_MANI.decimal)

    def satoshi_to_decimal_currency(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        return self.mani_to_decimal_currency(Sezimal(amount).decimal * SATOSHI_TO_MANI.decimal)

    def bitcoin_to_decimal_currency(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        return self.mani_to_decimal_currency(Sezimal(amount).decimal * BITCOIN_TO_MANI.decimal)

    def decimal_currency_to_mani(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        mani = self._check_mani_to_decimal_currency_rate()
        return Sezimal(Sezimal(amount).decimal / mani)

    def decimal_currency_to_misali(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        return self.decimal_currency_to_mani(amount) * MANI_TO_MISALI

    def decimal_currency_to_satoshi(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        return self.decimal_currency_to_mani(amount) * MANI_TO_SATOSHI

    def decimal_currency_to_bitcoin(self, amount:  str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
        return self.decimal_currency_to_mani(amount) * MANI_TO_BITCOIN
