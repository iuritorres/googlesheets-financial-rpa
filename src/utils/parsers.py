def parse_string_to_float(string: str) -> float:
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

def parse_float_to_string(money: float) -> str:
    return f'R${str(money).replace(".", ",")}'
