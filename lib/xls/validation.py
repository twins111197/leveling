from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from collections import Counter


def check_preferences_for_input_errors(sheet):
    """Takes in the preferences spreadsheet, if there are errors then write them to an excel doc. Reads with xlrd."""
    errors = []

    # Check that all names are unique
    names_ive_seen = set()  # curly braces is an empty set
    for row in sheet.rows:
        if not row:
            continue
        name = row[0].value
        if name in names_ive_seen:
            errors.append(
                "At least two campers have the name %s in the preferences document"
                % name
            )
        else:
            names_ive_seen.add(name)

    # Check that no cells are empty
    for row in sheet.rows:
        for cell in row:
            if cell.value is None:
                errors.append("%s is empty." % cell.coordinate)

    return errors


def output_errors(errors_list):
    """Takes in a list of errors, outputs an Excel document with these errors. Writes with Openpyxl."""
    # Create the workbook
    book = Workbook()
    # Access the active sheet
    sheet = book.active
    sheet.title = "Errors"
    for i, error in enumerate(errors_list):
        sheet.cell(row=i + 1, column=1).value = error

    return book
