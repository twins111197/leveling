def locate_header(actual_header, desired_header_objects):
    """Returns dictionary with index of each header object"""
    cols = {}
    for i, cell in enumerate(actual_header):
        if cell.value in desired_header_objects:
            cols[cell.value] = i
    return cols
