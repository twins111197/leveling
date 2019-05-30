import numpy as np
from scipy.optimize import linear_sum_assignment
import random


def create_matrix(campers, activities):
    """Creates the matrix to pass into the Hungarian algorithm."""

    # Create the column headers
    col_headers = sum((multiply_activity(activity) for activity in activities), [])

    # Define the function that determines the cost of putting a camper in a specific activity
    def cost_of(i, j):
        camper = campers[i]
        activity = col_headers[j]
        cost = np.square(camper.pref_of(activity)) * 5
        if activity in camper.past_activities:
            if activity.repeatability:
                cost += 1
            else:
                cost += 10000
        if camper.past_preferences:
            cost += sum(camper.past_preferences) * 3 / len(camper.past_preferences)

        return cost

    matrix = np.fromfunction(np.vectorize(cost_of), (len(campers), len(col_headers)), dtype=int)

    return col_headers, matrix



def multiply_activity(activity):
    """Creates a list of the activity that is as long as there are spots in the activity. Primary use in matrix creation."""
    return [activity] * activity.capacity



def sort_campers(campers, activities):
    """""" ## TODO:

    # Make a copy so that the original list isn't messed with
    campers = campers.copy()
    # Shuffle the campers so that we don't inadvertently preferences those entered at the top
    random.shuffle(campers)

    col_headers, matrix = create_matrix(campers, activities)

    _, assignments = linear_sum_assignment(matrix)

    final_assignments = { camper: col_headers[index] for camper, index in zip(campers, assignments) }

    # Add the campers who aren't assigned an activity if not enough spots for all campers
    final_assignments.update({ camper: None for camper in campers if camper not in final_assignments })

    return final_assignments
