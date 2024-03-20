from __future__ import annotations

from decimal import Decimal
from typing import Protocol


class Taxable(Protocol):
    tax_name: str
    tax_rate: Decimal
    tax_value: Decimal


def get_tax_category(item: Taxable) -> str | None:
    # We store the tax category in the tax_name field of the item
    # N1 is used for hotel services, N2.2 for donations

    tax_name = item.tax_name.upper()

    if tax_name in ("N1", "N2.2"):
        return tax_name

    # Returning None is excpected, the tax category is
    # only used when the tax rate is 0.00, and in that case
    # we do have a validation

    return None
