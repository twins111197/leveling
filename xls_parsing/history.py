from typing import Sequence, Callable

from openpyxl.worksheet import Worksheet
from openpyxl.cell import Cell

from xls_parsing.common import locate_header


Row = Sequence[Cell]

class History:
    def __init__(self, name: str, bunk: str,
                 past_activities: Sequence[str],
                 past_preferences: Sequence[int]) -> None:
        self.name = name
        self.bunk = bunk
        self.past_activities = past_activities
        self.past_preferences = past_preferences

def parse_sheet(sheet: Worksheet) -> Sequence[History]:
    """Takes in an Excel sheet and spits out a list of objects containing camper histories"""
    header_row = sheet[1]

    create_history = _parse_header(header_row)
    # Create list of history objects to return
    histories = [create_history(row) for row in sheet.iter_rows(min_row=2)]

    return histories


def _parse_header(header: Row) -> Callable[[Row], History]:
    """Takes in the row we believe to be the header, returns a function that creates history objects"""
    header_name = "Chanich Name"
    header_bunk = "Chanich Tzrif"
    # Determine number of past activities -- assumes same number of preference columns as activity columns
    counter = 0
    for cell in header:
        if cell.value is not None and "Activity" in cell.value:
            counter += 1
    header_past_activities = ["Past Activity %d" % (i + 1) for i in range(counter)]
    header_past_preferences = ["Past Preference %d" % (i + 1) for i in range(counter)]

    # Create a list of expected header items
    header_items = [header_name, header_bunk] + header_past_activities + header_past_preferences

    # Create a dictionary mapping the header items to column numbers
    cols = locate_header(header, header_items)


    def create_history(row: Row) -> History:
        """Takes in a row, returns a history object"""
        name = row[cols[header_name]].value
        bunk = row[cols[header_bunk]].value
        past_activities = [row[cols[i]].value for i in header_past_activities]
        past_preferences = [int(row[cols[i]].value) for i in header_past_preferences]

        history = History(name, bunk, past_activities, past_preferences)

        return history

    return create_history
