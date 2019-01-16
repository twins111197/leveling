from common import locate_header

class Activity:
    def __init__(self, name, capacity, repeatability):
        self.name = name
        self.capacity = capacity
        self.repeatability = repeatability



def parse_sheet(sheet):
    """Takes in the activities Excel sheet, outputs a list of activity objects"""
    header_row = sheet[1]
    # create_activity is a function because that is returned from _parse_header, takes in a row and returns an activity
    create_activity = _parse_header(header_row)
    # Create a list of activities   # Min row = 2 to avoid the header row
    activities = [create_activity(row) for row in sheet.iter_rows(min_row=2)]

    return activities


def _parse_header(header_row):
    """Takes in header row, returns a function that can be used to create activity objects"""
    # Declare what header objects I'm expecting
    header_name = "Peulah"
    header_capacity = "Capacity"
    header_repeatability = "Repeatable"

    # Prepare list of header objects, to be passed into locate_header
    header_objects = [header_name, header_capacity, header_repeatability]
    # Create dictionary of header objects mapped to the columns they appear in
    cols = locate_header(header_row, header_objects)


    def create_activity(row):
        name = row[cols[header_name]].value
        capacity = row[cols[header_capacity]].value
        repeatability = row[cols[header_repeatability]].value

        return Activity(name, capacity, repeatability)


    return create_activity
