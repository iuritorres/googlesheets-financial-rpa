"""Module that provides a class with statusinvest route paths."""
from dataclasses import dataclass

@dataclass
class StatusInvest:
    """Class that provides https://statusinvest.com.br route paths."""

    DOMAIN = 'https://statusinvest.com.br'
    ROUTE_REAL_STATE = '/fundos-imobiliarios'
