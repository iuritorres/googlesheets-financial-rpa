"""This module provides generic parsers."""
from math import floor


class Parser:
    """This class provides parsers methods."""

    @staticmethod
    def string_to_float(string: str) -> float:
        """Parse string to float based on suffixe, Ex.: "1K" = "1000"."""

        suffixes = {
            'K': 1e3,
            'M': 1e6,
            'B': 1e9,
            'T': 1e12
        }

        if string[-1].isalpha():
            value_str = string[:-1]
            suffix = string[-1]

            if suffix in suffixes:
                multiplier = suffixes[suffix]
                return float(value_str) * multiplier

        string = string.replace('R$', '')
        string = string.replace('.', '')
        string = string.replace(',', '.')

        return float(string)

    @staticmethod
    def float_to_string(money: float) -> str:
        """Parse float to string, Ex.: "12.03" = "R$12,03"."""

        return f'R${str(money).replace(".", ",")}'

    @staticmethod
    def var_to_title(variable: str) -> str:
        """Turns variable into a title, Ex.: "my_var" = "My Var"."""

        return variable.replace('_', ' ').title()

    @staticmethod
    def float_to_percentage(number: float) -> str:
        """Turns number into a % string, Ex.: "57.6015503" = "57.6%"."""

        return f'{number:.1f}%'
