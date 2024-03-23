"""Python script that updates the color enums."""
from typing import Iterator, Tuple, Union

# Table obtained from https://www.rapidtables.com/web/color/RGB_Color.html
# This approach is takes as accessing the url through 'requests' provides a
# security error.
_basic_color_code_table = [
    "Black	#000000	(0,0,0)",
    "White	#FFFFFF	(255,255,255)",
    "Red	#FF0000	(255,0,0)",
    "Green	#00FF00	(0,255,0)",
    "Blue	#0000FF	(0,0,255)",
    "Yellow	#FFFF00	(255,255,0)",
    "Cyan 	#00FFFF	(0,255,255)",
    "Aqua	#00FFFF	(0,255,255)",
    "Magenta	#FF00FF	(255,0,255)",
    "Fuchsia	#FF00FF	(255,0,255)",
    "Silver	#C0C0C0	(192,192,192)",
    "Gray	#808080	(128,128,128)",
    "Maroon	#800000	(128,0,0)",
    "Olive	#808000	(128,128,0)",
    "Dark_Green	#008000	(0,128,0)",
    "Purple	#800080	(128,0,128)",
    "Teal	#008080	(0,128,128)",
    "Navy	#000080	(0,0,128)",
]


def _get_name_and_value(
    bgr_format: bool, hex_format: bool = False
) -> Iterator[Tuple[str, Union[Tuple, str]]]:
    """Extracts and yields the color name in uppercase, and its color code.

    Parameters
    ----------
    bgr_format : bool
        If True, the color code is returned as BGR. Otherwise, as RGB.
    hex_format : bool
        If True, returns the color code as hexadecimal.
    """
    _basic_color_code_table.sort()
    for color_item in _basic_color_code_table:
        name, hex_val_str, code_val_str = color_item.replace("\t", " ").split()
        if hex_format:
            code_val = hex_val_str.replace("#", "")
        else:
            code_val = tuple(
                int(c)
                for c in code_val_str.replace("(", "").replace(")", "").split(",")
            )
        if bgr_format:
            code_val = code_val[::-1]
        yield name.upper(), code_val


def generate_color_enum(
    class_name: str, enum_type: str, description: str, **kwargs
) -> str:
    """Wrapper to define a whole color enum class."""
    return (
        f"class {class_name}({enum_type}): \n"
        f'\t"""\n\t{description}\n\t"""\n\t'
        + "\n\t".join(
            [f"{name} = {value}" for name, value in _get_name_and_value(**kwargs)]
        )
    )


if __name__ == "__main__":
    color_classes = [
        generate_color_enum(
            class_name="RGB",
            enum_type="TupleEnum",
            description="Each member contains RGB color codes.",
            bgr_format=False,
        ),
        generate_color_enum(
            class_name="BGR",
            enum_type="TupleEnum",
            description="Each member contains BGR color codes.",
            bgr_format=True,
        ),
    ]

    mod_text = (
        '"""Enumerations containing fix color values, extracted from '
        'https://www.rapidtables.com/web/color/RGB_Color.html."""\n'
        "from py_back.enum import TupleEnum\n" + "\n\n".join(color_classes)
    )

    with open("colors.py", "w", encoding="utf-8") as color_module:
        color_module.write(mod_text)
