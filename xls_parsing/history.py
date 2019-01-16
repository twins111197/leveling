from xls_parsing.common import locate_header

class History:
    def __init__(self, name, bunk, past_activities, past_preferences):
        self.name = name
        self.bunk = bunk
        self.past_activities = past_activities
        self.past_preferences = past_preferences

def parse_sheet(sheet):
    """Takes in an Excel sheet and spits out a list of objects containing camper histories"""
    header_row = sheet[1]

    create_history = _parse_header(header_row)
    # Create list of history objects to return
    histories = [create_history(row) for row in sheet.iter_rows(min_row=2)]

    return histories


def _parse_header(header_row):
    """Takes in the row we believe to be the header, returns a function that creates history objects"""
    header_name = "Chanich Name"
    header_bunk = "Chanich Tzrif"
    # Determine number of past activities -- assumes same number of preference columns as activity columns
    counter = 0
    for cell in header_row:
        if cell.value is not None and "Activity" in cell.value:
            counter += 1
    header_past_activities = ["Past Activity %d" % (i + 1) for i in range(counter)]
    header_past_preferences = ["Past Preference %d" % (i + 1) for i in range(counter)]

    # Create a list of expected header items
    header_items = [header_name, header_bunk] + header_past_activities + header_past_preferences

    # Create a dictionary mapping the header items to column numbers
    cols = locate_header(header_row, header_items)


    def create_history(row):
        """Takes in a row, returns a history object"""
        name = row[cols[header_name]].value
        bunk = row[cols[header_bunk]].value
        past_activities = [row[cols[i]].value for i in header_past_activities]
        past_preferences = [row[cols[i]].value for i in header_past_preferences]

        history = History(name, bunk, past_activities, past_preferences)

        return history

    return create_history
