import re
from typing import Any
from decimal import Decimal
from typing import Optional
from urllib.parse import urlparse, parse_qs

UTM_PARAMS = [
    'utm_source',
    'utm_medium',
    'utm_campaign',
    'utm_term',
    'utm_content',
    'utm_referrer',
]


REGEX_PATTERN_VALUES = [
    '"',
    "'",
    ';',
    ',',
    '==',
    '!=',
    '=@',
    '!@',
    '>',
    '<',
    '>=',
    '<=',
    '=^',
    '!^',
    '=\\^',
    '!\\^',
    '=$',
    '!$',
    '=\\$',
    '!\\$',
    '=~',
    '!~',
    '!=',
    '==',
    '!@',
    '=@',
    '<',
    '>',
    '<=',
    '>=',
    '!~',
    '=~',
    '!^',
    '=^',
    '!\\^',
    '=\\^',
    '!$',
    '=$',
    '!\\$',
    '=\\$',
    'undefined',
    '\n',
    '\t',
    '\r',
]


__all__ = (
    'parse_utm',
    'get_operations',
    'calc',
    'calculate',
    'remove_tags',
    'replacer',
    'UTM_PARAMS',
    'remove_unacceptable_chars',
    'REGEX_PATTERN_VALUES',
)


def remove_unacceptable_chars(
    value: Optional[str],
    pattern_values: list = REGEX_PATTERN_VALUES,
    default_value: Optional[str] = 'none',
) -> Optional[str]:
    pattern = r'|'.join(f'{v}' for v in pattern_values)
    if value is None or value == '':
        return default_value
    value = re.sub(pattern, ' ', str(value)).strip()
    words = value.split()
    return ' '.join(sorted(set(words), key=words.index))


def parse_utm(url: str) -> dict:
    """
    :param url: str
    :return: dict
    """
    out = {}
    try:
        url_params = parse_qs(urlparse(url.replace('#', '')).query)
        for utm in UTM_PARAMS:
            if utm in url_params:
                out[utm] = url_params[utm][0]
        return out
    except (KeyError, ValueError, IndexError, TypeError):
        return {}


def get_operations(data: dict) -> dict:
    """
    create valid calculation dict
    :param data: dict
    :return: dict
    """
    if data:
        if "cogs" in data or "crm_net_cost" in data:
            data["first_cost"] = (
                data.pop('cogs') if "cogs" in data else data.pop('crm_net_cost')
            )
        if "revenue" in data or "crm_deal_cost" in data:
            data['transaction_amount'] = (
                data.pop('revenue') if "revenue" in data else data.pop('crm_deal_cost')
            )
        return {
            field: str(data[field]).replace('{', '').replace('}', '')
            for field in data
            if data[field]
        }
    return {}


def calc(s: str) -> str:
    """
    :param s: str (value like ('(1 * 2) / 3'))
    :return: str (result of math operation)
    """
    val = s.group()  # type: ignore
    if not val.strip():
        return val
    return "%s" % eval(val.strip(), {'__builtins__': None})


def calculate(s: str) -> str:
    """
    :param s: str
    :return: str
    """
    return re.sub(r"([0-9\ \.\+\*\-\/(\)]+)", calc, s)  # type: ignore


def replacer(string: str, name: str, value: Any) -> str:
    """
    replace for calculated data
    :param string: str
    :param name: str
    :param value: Any
    :return: str
    """
    string = string.replace(name, Decimal(value).__str__())
    return string


def remove_tags(text: str) -> str:
    """
    remove html tags from text
    :param text: str
    :return: str
    """
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)
