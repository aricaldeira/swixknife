#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# SezimalCalendar - The Symmetry454 Calendar, with Holocene Epoch and Sezimal in Python
#
# Copyright (C) 2023–
# Copyright (C) Ari Caldeira <aricaldeira at gmail.com>
#
# Original calendar documentation is Public Domain by it’s author:
# http://individual.utoronto.ca/kalendis/symmetry.htm
#

__all__ = ('SezimalDateTimeDelta')

from typing import TypeVar

Self = TypeVar('Self', bound='SezimalDateTimeDelta')


from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger


class SezimalDateTimeDelta():
    __slots__ = ('_years', '_quarters', '_months', '_weeks', '_days', '_utas', '_poshas', '_agrimas', '_anugas', '_bodas', '_shaditibodas', '_total_days', '_total_agrimas')

    def __new__(
        cls,
        years: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        quarters: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        months: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        weeks: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        days: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        utas: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        poshas: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        agrimas: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        anugas: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        bodas: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        shaditibodas: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        ):
        self = object.__new__(cls)

        if years and Sezimal(years) != SezimalInteger(years):
            raise ValueError('Since not all years have the same length, only integer years are allowed')

        if months and Sezimal(months) != SezimalInteger(months):
            raise ValueError('Since not all months have the same length, only integer months are allowed')

        self._years = Sezimal(years)
        self._quarters = Sezimal(quarters)
        self._months = Sezimal(months)
        self._weeks = Sezimal(weeks)
        self._days = Sezimal(days)
        self._utas = Sezimal(utas)
        self._poshas = Sezimal(poshas)
        self._agrimas = Sezimal(agrimas)
        self._anugas = Sezimal(anugas)
        self._bodas = Sezimal(bodas)
        self._shaditibodas = Sezimal(shaditibodas)

        #
        # Since only months and years have varying lengths,
        # we store all other deltas as days (for sezimal dates)
        # and agrimas (for sezimal times)
        #
        total_days = self._quarters * SezimalInteger(231)
        total_days += self._weeks * SezimalInteger(11)
        total_days += self._days

        total_agrimas = self._utas * 10_000
        total_agrimas += self._poshas * 100
        total_agrimas += self._agrimas
        total_agrimas += self._anugas / 100
        total_agrimas += self._bodas / 10_000
        total_agrimas += (self._shaditibodas / 100_000_000) / 10_000

        if total_agrimas > 1_000_000:
            days = SezimalInteger(total_agrimas // 1_000_000)
            total_days += days
            total_agrimas -= days * 1_000_000

        if total_days != SezimalInteger(total_days):
            agrimas = (total_days - SezimalInteger(total_days)) * 1_000_000
            total_agrimas += agrimas
            total_days = SezimalInteger(total_days)

        self._total_days = total_days
        self._total_agrimas = total_agrimas

        return self

    def __repr__(self):
        return f'{self.__class__.__qualname__}(years={self.years.formatted_number}, quarters={self.quarters.formatted_number}, months={self.months.formatted_number}, weeks={self.weeks.formatted_number}, days={self.days.formatted_number}, utas={self.utas.formatted_number}, poshas={self.poshas.formatted_number}, agrimas={self.agrimas.formatted_number}, anugas={self.anugas.formatted_number}, bodas={self.bodas.formatted_number}, shaditibodas={self.shaditibodas.formatted_number})'

    @property
    def years(self):
        return self._years

    @property
    def quarters(self):
        return self._quarters

    @property
    def months(self):
        return self._months

    @property
    def weeks(self):
        return self._weeks

    @property
    def days(self):
        return self._days

    @property
    def utas(self):
        return self._utas

    @property
    def poshas(self):
        return self._poshas

    @property
    def agrimas(self):
        return self._agrimas

    @property
    def anugas(self):
        return self._anugas

    @property
    def bodas(self):
        return self._bodas

    @property
    def shaditibodas(self):
        return self._shaditibodas

    def _add_date_time_delta(self, other: Self) -> Self:
        years = self.years + other.years
        quarters = self.quarters + other.quarters
        months = self.months + other.months
        weeks = self.weeks + other.weeks
        days = self.days + other.days
        utas = self.utas + other.utas
        poshas = self.poshas + other.poshas
        agrimas = self.agrimas + other.agrimas
        anugas = self.anugas + other.anugas
        bodas = self.bodas + other.bodas
        shaditibodas = self.shaditibodas + other.shaditibodas
        return SezimalDateTimeDelta(years, quarters, months, weeks, days, utas, poshas, agrimas, anugas, bodas, shaditibodas)

    def _subtract_date_time_delta(self, other: Self) -> Self:
        years = self.years - other.years
        quarters = self.quarters - other.quarters
        months = self.months - other.months
        weeks = self.weeks - other.weeks
        days = self.days - other.days
        utas = self.utas - other.utas
        poshas = self.poshas - other.poshas
        agrimas = self.agrimas - other.agrimas
        anugas = self.anugas - other.anugas
        bodas = self.bodas - other.bodas
        shaditibodas = self.shaditibodas - other.shaditibodas
        return SezimalDateTimeDelta(years, quarters, months, weeks, days, utas, poshas, agrimas, anugas, bodas, shaditibodas)

    def _mutiply_date_time_delta(self, other: Sezimal) -> Self:
        other = Sezimal(other)
        years = SezimalInteger(self.years * other)
        quarters = self.quarters * other
        months = SezimalInteger(self.months * other)
        weeks = self.weeks * other
        days = self.days * other
        utas = self.utas * other
        poshas = self.poshas * other
        agrimas = self.agrimas * other
        anugas = self.anugas * other
        bodas = self.bodas * other
        shaditibodas = self.shaditibodas * other
        return SezimalDateTimeDelta(years, quarters, months, weeks, days, utas, poshas, agrimas, anugas, bodas, shaditibodas)

    def _divide_date_time_delta(self, other: Sezimal) -> Self:
        other = Sezimal(other)
        years = SezimalInteger(self.years / other)
        quarters = self.quarters / other
        months = SezimalInteger(self.months / other)
        weeks = self.weeks / other
        days = self.days / other
        utas = self.utas / other
        poshas = self.poshas / other
        agrimas = self.agrimas / other
        anugas = self.anugas / other
        bodas = self.bodas / other
        shaditibodas = self.shaditibodas / other
        return SezimalDateTimeDelta(years, quarters, months, weeks, days, utas, poshas, agrimas, anugas, bodas, shaditibodas)
