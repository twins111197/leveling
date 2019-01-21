from typing import Mapping, Iterable

from openpyxl.cell import Cell

def locate_header(header: Iterable[Cell],
                  header_names: Iterable[str]) -> Mapping[str, int]:
    """Returns dictionary with index of each header object"""

    cols = {}
    for i, cell in enumerate(header):
        if cell.value in header_names:
            cols[cell.value] = i
    return cols
