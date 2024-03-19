#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from holidays.calendars.gregorian import JUL
from holidays.countries.united_kingdom import UnitedKingdom, UnitedKingdomStaticHolidays
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_MON


class IsleOfMan(UnitedKingdom):
    """Using existing code in UnitedKingdom for now."""

    country = "IM"
    subdivisions = ()  # Override UnitedKingdom subdivisions.

    def __init__(self, *args, **kwargs):  # Override UnitedKingdom __init__().
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, UnitedKingdomStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        ObservedHolidayBase.__init__(self, *args, **kwargs)

    def _populate_public_holidays(self) -> None:
        super()._populate_public_holidays()
        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Whit Monday.
        if self._year <= 1970:
            self._add_whit_monday("Whit Monday")

        # Late Summer bank holiday (last Monday in August)
        if self._year >= 1971:
            self._add_holiday_last_mon_of_aug("Late Summer Bank Holiday")

        # Isle of Man exclusive holidays
        # TT bank holiday (first Friday in June)
        self._add_holiday_1st_fri_of_jun("TT Bank Holiday")

        # Tynwald Day
        # Move to the next Monday if falls on a weekend.
        dt = date(self._year, JUL, 5)
        self._add_holiday(
            "Tynwald Day",
            self._get_observed_date(dt, SAT_SUN_TO_NEXT_MON) if self._year >= 1992 else dt,
        )


class IM(IsleOfMan):
    pass


class IMN(IsleOfMan):
    pass
