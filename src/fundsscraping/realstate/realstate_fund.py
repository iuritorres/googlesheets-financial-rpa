"""This module provides a class for real state funds."""
from dataclasses import dataclass
from typing import Dict

from utils.parsers import Parser


@dataclass
class RealStateFund:
    """This class represents a real state fund."""

    def __init__(
        self,
        name: str,
        metrics: Dict[str, float],
        allocation_by_segments: Dict[str, float]
    ) -> None:
        self.name = name
        self.metrics = metrics
        self.allocation_by_segments = allocation_by_segments

    def show_data(self) -> None:
        """Iterate self attributes and shows them."""

        for attribute, value in self.__dict__.items():
            key = Parser.var_to_title(attribute)
            prefix = '->' if key == 'Name' else '  '

            match key:
                case 'Name':
                    print(f'{prefix} {key}: {value}')

                case 'Metrics':
                    print(f'{prefix} {key}:')

                    for metric in self.metrics:
                        metric_title = Parser.var_to_title(metric)
                        metric_value = Parser.float_to_string(
                            self.metrics[metric])

                        print(f'\t {metric_title}: {metric_value}')

                case 'Allocation By Segments':
                    print(f'{prefix} {key}:')

                    for segment in self.allocation_by_segments:
                        segment_title = Parser.var_to_title(segment)
                        segment_value = Parser.float_to_percentage(
                            self.allocation_by_segments[segment])

                        print(f'\t {segment_title}: {segment_value}')

        print('\n')
