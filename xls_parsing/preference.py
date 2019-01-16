from xls_parsing.common import locate_header


class Preference:
    def __init__(self, name, edah, bunk, preferences):
        self.name = name
        self.edah = edah
        self.bunk = bunk
        self.preferences = preferences




def parse_sheet(sheet):
    """Takes in the preferences excel sheet, spits out a list of campers"""
    header_row = sheet[1]
    # create camper is now a function, takes in a row and gives you a camper
    create_preference = _parse_header(header_row)
    # Create list of campers    # Min row = 2 to avoid the header row
    campers = [create_preference(row) for row in sheet.iter_rows(min_row=2)]

    return campers



def _parse_header(header_row):
    """Takes in header row, returns a function that should create campers from rows"""

    # Explicitly declare the header objects I'm looking for
    header_name = "Chanich Name"
    header_edah = "Edah"
    header_bunk = "Chanich Tzrif"
    header_prefs = ["Preference %d" % (i + 1) for i in range(6)]

    # Make list of expected header row
    header_objects = [header_name, header_edah, header_bunk] + header_prefs
    # Creates dictionary connecting row numbers to
    cols = locate_header(header_row, header_objects)

    def create_preference(row):
        name = row[cols[header_name]].value
        edah = row[cols[header_edah]].value
        bunk = row[cols[header_bunk]].value
        # Use list comprehensions to generate the list of preferences
        preference_indexes = [cols[pref] for pref in header_prefs]
        preferences = [row[i].value for i in preference_indexes]

        return Preference(name, edah, bunk, preferences)

    return create_preference
