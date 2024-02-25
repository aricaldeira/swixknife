

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from decimal import Decimal


#
# Length
#
PADA_TO_NAUTICAL_MILE = SezimalFraction('2_211 / 3_341_151_300')
NAUTICAL_MILE_TO_PADA = PADA_TO_NAUTICAL_MILE.reciprocal
