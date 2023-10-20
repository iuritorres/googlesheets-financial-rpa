from typing import Dict

from utils.parsers import parse_float_to_string

class RealStateFund:
    def __init__(
        self,
        name: str,
        current_value: float,
        dividenv_yield: float,
        asset_value: float,
        p_vp: float,
        last_income: float,
        net_equity: (float | None),
        allocation_by_segments: Dict[str, float]
    ) -> None:
        self.name = name
        self.current_value = current_value
        self.dividend_yield = dividenv_yield
        self.asset_value = asset_value
        self.p_vp = p_vp
        self.last_income = last_income
        self.net_equity = net_equity
        self.allocation_by_segments = allocation_by_segments

    def show_data(self) -> None:
        for attribute, value in self.__dict__.items():
            key = attribute.replace('_', ' ').title()
            value = value

            print(f'{"->" if key == "Name" else "  "} {key}: {parse_float_to_string(value) if type(value) == float else value}')

        print('\n')
