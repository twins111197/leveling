class Camper:
    def __init__(self, name, edah, bunk, preferences, past_activities, past_preferences):
        self.name = name
        self.edah = edah
        self.bunk = bunk
        self.preferences = preferences
        self.past_activities = past_activities
        self.past_preferences = past_preferences

    def pref_of(self, activity):
        try:
            return self.preferences.index(activity)
        except ValueError:
            return len(self.preferences)



def merge_objects(preferences, activities, histories):    # These are all list objects
    """Takes in lists of histories, activities, preferences, and gives back a list of campers with all traits in one place"""
    histories_dict = {history.name: (history.past_activities, history.past_preferences) for history in histories}
    activities_dict = {activity.name: activity for activity in activities}
    campers = [create_camper(preference, histories_dict, activities_dict) for preference in preferences]
    return campers



def create_camper(preference, histories_dict, activities_dict):
    """Takes the preference object to be made a camper and dictionaries of histories and activities, outputs a Camper object"""
    past_activities_strings, past_preferences  = histories_dict[preference.name]
    past_activities = [activities_dict[activity_string] for activity_string in past_activities_strings]
    preferences = [activities_dict[activity_string] for activity_string in preference.preferences]
    camper = Camper(preference.name, preference.edah, preference.bunk,
                    preferences, past_activities, past_preferences)
    return camper
