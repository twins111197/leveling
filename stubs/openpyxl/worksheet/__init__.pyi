from typing import Iterable, Sequence

from openpyxl.cell import Cell
from openpyxl.worksheet.dimensions import DimensionHolder

Row = Sequence[Cell]

class Worksheet:
    title: str
    column_dimensions: DimensionHolder
    def cell(self, row: int, column: int) -> Cell: ...
    def __getitem__(self, row: int) -> Row: ...
    def iter_rows(self, min_row: int) -> Iterable[Row]: ...
