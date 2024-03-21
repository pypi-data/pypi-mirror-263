"""
who in the world would use this
"""

__author__ = "tema5002 <tema5002@gmail.com>"
__version__ = "1.1"
__license__ = "MIT"
__copyright__ = "2024, tema5002"
__short_description__ = "who in the world would use this"


def decode(num: str) -> int:
    if not isinstance(num, str):
        raise TypeError(f"Incorrect data type: {type(num)}")

    return sum(1114112 ** index * ord(i) for index, i in enumerate(num))


def encode(num: int) -> str:
    if not isinstance(num, int):
        raise TypeError(f"Incorrect data type: {type(num)}")

    def _encode(num_):
        return chr(num_ % 1114112) + _encode(num_ // 1114112) if num_ else ""

    return _encode(num)
