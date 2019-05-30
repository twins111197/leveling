from lib.camper import Camper
from ..validation import check_preferences_for_input_errors
from . import preference, activity, history


class InvalidPreferences(Exception):
    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return repr(self.errors)


def parse_xls(prefs_wb, activities_wb, histories_wb):
    # Parse the preferences
    prefs_sheet = prefs_wb.active

    errors = check_preferences_for_input_errors(prefs_sheet)
    if errors:
        raise InvalidPreferences(errors)

    preferences = preference.parse_sheet(prefs_sheet)

    # Parse the activities
    activities_sheet = activities_wb.active
    activities = activity.parse_sheet(activities_sheet)

    # Parse the histories
    if histories_wb:
        if len(histories_wb.worksheets) >= 2:
            histories_sheet = histories_workbook.worksheets[1]
        else:
            histories_sheet = histories_wb.active
        histories = history.parse_sheet(histories_sheet)
    else:
        histories = [history.History(p.name, p.bunk, [], []) for p in preferences]

    # Merge the parsed information into campers
    campers = merge_objects(preferences, activities, histories)

    return campers, activities


def merge_objects(preferences, activities, histories):  # These are all list objects
    """Takes in lists of histories, activities, preferences, and gives back a list of campers with all traits in one place"""
    histories_dict = {
        history.name: (history.past_activities, history.past_preferences)
        for history in histories
    }
    activities_dict = {activity.name: activity for activity in activities}
    campers = [
        create_camper(preference, histories_dict, activities_dict)
        for preference in preferences
    ]
    return campers


def create_camper(preference, histories_dict, activities_dict):
    """Takes the preference object to be made a camper and dictionaries of histories and activities, outputs a Camper object"""
    past_activities_strings, past_preferences = histories_dict[preference.name]
    past_activities = [
        activities_dict[activity_string] for activity_string in past_activities_strings
    ]
    preferences = [
        activities_dict[activity_string] for activity_string in preference.preferences
    ]
    camper = Camper(
        preference.name,
        preference.edah,
        preference.bunk,
        preferences,
        past_activities,
        past_preferences,
    )
    return camper
