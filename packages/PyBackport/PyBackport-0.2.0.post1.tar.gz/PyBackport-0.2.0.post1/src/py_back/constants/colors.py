"""
Enumerations containing fix color values, extracted from
https://www.rapidtables.com/web/color/RGB_Color.html
"""
from py_back.enum import TupleEnum


class RGB(TupleEnum):
    """Each member contains RGB color codes."""

    AQUA = (0, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    DARK_GREEN = (0, 128, 0)
    FUCHSIA = (255, 0, 255)
    GRAY = (128, 128, 128)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    MAROON = (128, 0, 0)
    NAVY = (0, 0, 128)
    OLIVE = (128, 128, 0)
    PURPLE = (128, 0, 128)
    RED = (255, 0, 0)
    SILVER = (192, 192, 192)
    TEAL = (0, 128, 128)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)


class BGR(TupleEnum):
    """Each member contains BGR color codes."""

    AQUA = (255, 255, 0)
    BLACK = (0, 0, 0)
    BLUE = (255, 0, 0)
    CYAN = (255, 255, 0)
    DARK_GREEN = (0, 128, 0)
    FUCHSIA = (255, 0, 255)
    GRAY = (128, 128, 128)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    MAROON = (0, 0, 128)
    NAVY = (128, 0, 0)
    OLIVE = (0, 128, 128)
    PURPLE = (128, 0, 128)
    RED = (0, 0, 255)
    SILVER = (192, 192, 192)
    TEAL = (128, 128, 0)
    WHITE = (255, 255, 255)
    YELLOW = (0, 255, 255)
