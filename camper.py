class Camper:
    def __init__(self, name, edah, bunk, past_activities, past_preferences, preferences):
        self.name = name
        self.edah = edah
        self.bunk = bunk
        self.past_activities = past_activities   # for tracking the camper's previous activities
        self.past_preferences = past_preferences  # for tracking the camper's previous preferences
        self.preferences = preferences
