from lib.camper import Camper

from ..validation import check_for_input_errors
from . import activity, history, preference


class InvalidPreferences(Exception):
    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return repr(self.errors)


def parse_xls(prefs_wb, activities_wb, histories_wb):
    # Parse the preferences
    prefs_sheet = prefs_wb.active

    # Parse the activities
    activities_sheet = activities_wb.active
    activities = activity.parse_sheet(activities_sheet)

    errors = check_for_input_errors(prefs_sheet, activities_sheet)
    if errors:
        raise InvalidPreferences(errors)

    preferences = preference.parse_sheet(prefs_sheet)

    # Parse the histories
    if histories_wb:
        if len(histories_wb.worksheets) >= 2:
            histories_sheet = histories_wb.worksheets[1]
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
    # 2nd session campers will have different length histories than full-summer campers, must guard for this, hence if/else
    if preference.name in histories_dict:
        past_activities_strings, past_preferences  = histories_dict[preference.name]
        # Some None values might exist for the shorter history lists of 2nd session campers, so remove the None values below
        past_preferences = [past_pref for past_pref in past_preferences if past_pref is not None]
        past_activities = [activities_dict[activity_string] for activity_string in past_activities_strings if activity_string != None]
    else:
        past_activities = []
        past_preferences = []
    # If a camper has had an unrepeatable activity already, remove it from preferences altogether
    preferences = [activities_dict[activity_string] for activity_string in preference.preferences if not
                   (activities_dict[activity_string] in past_activities and activities_dict[activity_string].repeatability == False)]
    camper = Camper(
        preference.name,
        preference.edah,
        preference.bunk,
        preferences,
        past_activities,
        past_preferences,
    )
    return camper
