from typing import overload

from openpyxl.worksheet import Worksheet

class Workbook:
    active: Worksheet
    @overload
    def create_sheet(self, title: str) -> Worksheet: ...
    @overload
    def create_sheet(self, title: str, pos: int) -> Worksheet: ...
