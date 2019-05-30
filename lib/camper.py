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
