# Reading and writing an excel file using Python
import xlrd


"""Takes in an empty list and the Excel sheet location with preferences for the upcoming cycle, returns populated list of camper objects with Name, Edah, Bunk, and Preferences"""
def create_campers(empty_campers_list, sheet):
    # Creates the proper number of campers in the list
    for i in range(sheet.nrows - 1):             # Assumes header row
        empty_campers_list.append(Camper())

    # Loop over all columns, gathering spreadsheet information
    for i in range(sheet.ncols):
        # Adds names to each camper object
        if "name" in sheet.cell_value(0, i).lower() or "camper" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_campers_list[j].name = sheet.cell_value(j + 1, i)

        # Adds bunks to each camper object -- same for loop as above
        elif "bunk" in sheet.cell_value(0, i).lower() or "tzrif" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_campers_list[j].bunk = sheet.cell_value(j + 1, i)

        # Adds edah to each camper object -- same for loop as above
        elif "edah" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_campers_list[j].edah = sheet.cell_value(j + 1, i)

        # Adds preferences to camper objects, up to 9 preferences -- same for loop as above
        elif "1" in sheet.cell_value(0, i) or "first" in sheet.cell_value(0, i).lower(): # If name becomes first + last, problem here
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_campers_list[j].pref_1 = sheet.cell_value(j + 1, i)
        elif "2" in sheet.cell_value(0, i) or "second" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_campers_list[j].pref_2 = sheet.cell_value(j + 1, i)
        elif "3" in sheet.cell_value(0, i) or "third" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_campers_list[j].pref_3 = sheet.cell_value(j + 1, i)
        elif "4" in sheet.cell_value(0, i) or "fourth" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_campers_list[j].pref_4 = sheet.cell_value(j + 1, i)
        elif "5" in sheet.cell_value(0, i) or "fifth" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_campers_list[j].pref_5 = sheet.cell_value(j + 1, i)
        elif "6" in sheet.cell_value(0, i) or "sixth" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_campers_list[j].pref_6 = sheet.cell_value(j + 1, i)
        elif "7" in sheet.cell_value(0, i) or "seventh" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_campers_list[j].pref_7 = sheet.cell_value(j + 1, i)
        elif "8" in sheet.cell_value(0, i) or "eigth" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_campers_list[j].pref_8 = sheet.cell_value(j + 1, i)
        elif "9" in sheet.cell_value(0, i) or "ninth" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_campers_list[j].pref_9 = sheet.cell_value(j + 1, i)



# ===================================================================================================




"""Takes in an empty list and the Excel sheet of activities, their capacities and their repeatabilities, returns populated list of activities objects with Name, Capacity, and Repeatability"""
def create_activities(empty_activities_list, excel_location):
    # Define the class of activity objects
    class Activity:
        def __init__(self):
            self.name = ""
            self.capacity = 0            # for tracking max # of campers to be placed in the activity
            self.repeatability = True    # Assume activity is repeatable unless told otherwise
            self.members = 0             # for tracking # of campers assigned to this activity
            self.popularity_1 = 0        # for tracking how many campers want the activity when calculating popularity
            self.popularity_2 = 0        # for tracking how many campers want the activity when calculating popularity
            self.popularity_3 = 0        # for tracking how many campers want the activity when calculating popularity

    # Open excel sheet of interest
    wb = xlrd.open_workbook(file_contents=excel_location.read())
    sheet = wb.sheet_by_index(0)          # Index to the sheet of interest

    # Creates the proper number of activities in the list
    for i in range(sheet.nrows - 1):   # Assumes header row
        empty_activities_list.append(Activity())

    # Loop over all columns, extracting information
    for i in range(sheet.ncols):
        # Adds names to each activity object
        if "activ" in sheet.cell_value(0, i).lower() or "peula" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_activities_list[j].name = sheet.cell_value(j + 1, i)

        # Adds capacity to each activity object
        elif "capacity" in sheet.cell_value(0, i).lower() or "max" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    empty_activities_list[j].capacity = int(sheet.cell_value(j + 1, i))

        # Updates repeatability to each activity object
        elif "repeat" in sheet.cell_value(0, i).lower():
            for j in range(sheet.nrows - 1):
                if sheet.cell_type(j + 1, i) != xlrd.XL_CELL_EMPTY:  # Check if empty
                    if "n" in sheet.cell_value(j + 1, i).lower():
                        empty_activities_list[j].repeatability = False

# ===================================================================================================



"""Takes in the list of campers and the Excel sheet location containing information about previous cycles, returns sorted list of camper objects now including previous activities awarded and the preferences of those activities"""
def update_campers(campers_list, excel_location):

    # Open excel sheet of interest
    wb = xlrd.open_workbook(file_contents=excel_location.read())    # Open the workbook of interest
    sheet = wb.sheet_by_index(0)               # Index to the sheet of interest

    # Extract data from the spreadsheet
    for k in range(sheet.ncols):       # k represents the excel column that contains names
        if "name" in sheet.cell_value(0, k).lower() or "camper" in sheet.cell_value(0, k).lower():   # Find names column
            for i in range(sheet.nrows - 1):  # Loop over names in the new spreadsheet
                for j in range(len(campers_list)):  # Loop over names in camper list
                    if campers_list[j].name.lower() == sheet.cell_value(i + 1, k).lower():  # Identifies camper object corresponding to spreadsheet row
                        for l in range(sheet.ncols):   # Loop over columns to gather relevant information
                            if "activity" in sheet.cell_value(0, l).lower() or "peula" in sheet.cell_value(0, l).lower():
                                if sheet.cell_type(i + 1, l) != xlrd.XL_CELL_EMPTY:  # Check if empty
                                    campers_list[j].past_activities.append(sheet.cell_value(i + 1, l))
                            elif "pref" in sheet.cell_value(0, l).lower() or "choice" in sheet.cell_value(0, l).lower():
                                if sheet.cell_type(i + 1, l) != xlrd.XL_CELL_EMPTY:  # Check if empty
                                    campers_list[j].past_preferences.append(sheet.cell_value(i + 1, l))
                                    campers_list[j].avg_pref += sheet.cell_value(i + 1, l)
                                    if sheet.cell_value(i + 1, l) == 1:
                                        campers_list[j].had_first = True


    # Divide avg_pref variable by the number of activities campers have had
    for i in range(len(campers_list)):
        if len(campers_list[i].past_activities) != 0:
            campers_list[i].avg_pref = campers_list[i].avg_pref / len(campers_list[i].past_activities)


# ===================================================================================================


"""Sort campers into their activities for the coming cycle"""    # Takes in updated campers list and created activities list
def sort_campers(updated_campers_list, created_activities_list):
    # Determine how many campers want each activity for their first or second choice
    for i in range(len(updated_campers_list)):
        for j in range(len(created_activities_list)):
            if updated_campers_list[i].pref_1.lower() == created_activities_list[j].name.lower() or updated_campers_list[i].pref_2.lower() == created_activities_list[j].name.lower():
                created_activities_list[j].popularity_1 += 1

                # Note: popularity_1 is initially used to determine if something is unpopular, meaning that all first and second choices of this activity can be assigned. After assigning those campers, popularity_1 reverts to its originally intended goal of telling us which activities have contested spots with first-choices only.
    # Assign choices for activities with enough spots for all first and second requests (if repeatable or the camper hasn't had it yet)
    for i in range(len(created_activities_list)):
        if created_activities_list[i].popularity_1 <= created_activities_list[i].capacity:              # Activities with enough spots
            for j in range(len(updated_campers_list)):
                # Assign if unpopular activity is 1st choice
                if updated_campers_list[j].pref_1.lower() == created_activities_list[i].name.lower():   # If a camper's first choice
                    if created_activities_list[i].repeatability or created_activities_list[i].name.lower() not in [x.lower() for x in updated_campers_list[j].past_activities]:                                           # As long as no illegal repeat
                        assign_activity(updated_campers_list[j], created_activities_list[i], 1)
                # Assign if unpopular activity is 2nd choice
                elif updated_campers_list[j].pref_2.lower() == created_activities_list[i].name.lower():   # If a camper's 2nd choice
                    if created_activities_list[i].repeatability or created_activities_list[i].name.lower() not in [x.lower() for x in updated_campers_list[j].past_activities]:                                           # As long as no illegal repeat
                        assign_activity(updated_campers_list[j], created_activities_list[i], 2)         # Assign the activity
        created_activities_list[i].popularity_1 = 0                                                     # Reset for next use

    # Check how contested activities are from first, second, and third choices. Popularity 1 reverts to intended goal.
    for i in range(len(updated_campers_list)):
        if updated_campers_list[i].next_activity == "":             # Only consider those still unassigned
            for j in range(len(created_activities_list)):
                if updated_campers_list[i].pref_1.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_1 += 1       # Update popularity of 1st choice for requests
                if updated_campers_list[i].pref_2.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_2 += 1       # Update popularity of 2nd choice for requests
                    created_activities_list[j].popularity_3 += 1       # 3rd choice popularity reflects 2nd choices handed out first
                if updated_campers_list[i].pref_3.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_3 += 1       # Update popularity of 3rd choice for requests
    for i in range(len(created_activities_list)):
        if (created_activities_list[i].capacity - created_activities_list[i].members - created_activities_list[i].popularity_1) <= 0:    # If no spots left after 1st choice
            created_activities_list[i].popularity_2 = 10000                                         # Set popularity super high
            created_activities_list[i].popularity_3 = 10000                                         # Set popularity super high
        else:                                                                                       # If spots left
            created_activities_list[i].popularity_2 = created_activities_list[i].popularity_2 / (created_activities_list[i].capacity - created_activities_list[i].members)                                                     # Calculate popularity value
            created_activities_list[i].popularity_3 = created_activities_list[i].popularity_3 / (created_activities_list[i].capacity - created_activities_list[i].members)                                                     # Calculate popularity value

    # Assign first choices
    for j in range(len(created_activities_list)):
        # If an activity has enough spots to assign first choices, assign them
        if created_activities_list[j].popularity_1 <= created_activities_list[j].capacity:     # Activities with enough spots
            for i in range(len(updated_campers_list)):
                if updated_campers_list[i].pref_1.lower() == created_activities_list[j].name.lower() and updated_campers_list[i].next_activity == "":
                    if created_activities_list[j].repeatability or created_activities_list[j].name.lower() not in [x.lower() for x in updated_campers_list[i].past_activities]:                                  # Check for illegal repeats
                        assign_activity(updated_campers_list[i], created_activities_list[j], 1)


        # If an activity doesn't have enough spots, sort by 2nd and 3rd choices of campers requesting
        elif created_activities_list[j].popularity_1 > created_activities_list[j].capacity:        # Activities w/contested spots
            temp_list = []                                                                         # Create temp list to sort
            counter = 0
            for i in range(len(updated_campers_list)):
                if updated_campers_list[i - counter].next_activity == "":
                    if updated_campers_list[i - counter].pref_1.lower() == created_activities_list[j].name.lower(): # Campers that want this activity
                        temp_list.append(updated_campers_list.pop(i - counter))                       # Place them in a new list
                        counter += 1                                                                  # Ensure index not out of range
            for k in range(len(temp_list)):                                                           # Campers that want this activity
                for m in range(len(created_activities_list)):                                         # Gather popularity values
                    if temp_list[k].pref_2.lower() == created_activities_list[m].name.lower():
                        temp_list[k].pop_2 = created_activities_list[m].popularity_2
                    if temp_list[k].pref_3.lower() == created_activities_list[m].name.lower():
                        temp_list[k].pop_3 = created_activities_list[m].popularity_3
            # Bubble sort based on difficulty of filling next spots, had_first, and avg_pref
            index = len(temp_list) - 1
            while index >= 0:
                for i in range(index):
                    if temp_list[i].pop_2 < temp_list[i + 1].pop_2:                # If easier to fill first camper's 2nd pref, switch
                        temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                    elif temp_list[i].pop_2 == temp_list[i + 1].pop_2:             # If equal difficulty...
                        if temp_list[i].pop_3 < temp_list[i + 1].pop_3:            # If easier to fill first camper's 3rd pref, switch
                            temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                        elif temp_list[i].pop_3 == temp_list[i + 1].pop_3:                 # If equal difficulty...
                            if temp_list[i].had_first and not temp_list[i + 1].had_first:  # If 1st camper had first, not 2nd,  switch
                                temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                            elif temp_list[i].avg_pref < temp_list[i + 1].avg_pref:
                                temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                index -= 1

            # Assign first choices until capacity is reached
            counter = 0
            for i in range(len(temp_list)):
                if created_activities_list[j].members < created_activities_list[j].capacity:
                    if created_activities_list[j].repeatability or created_activities_list[j].name.lower() not in [x.lower() for x in temp_list[i - counter].past_activities]:                                        # As long as no illegal repeat
                        assign_activity(temp_list[i - counter], created_activities_list[j], 1)
                updated_campers_list.append(temp_list.pop(i - counter))
                counter += 1


    # Check if done, if so quit to avoid any later bugs in the code / processing time
    if are_campers_sorted(updated_campers_list):
        clean(updated_campers_list, created_activities_list)
        return



    """Now we move on to doing second choices! All popularity_i is now popularity_(i+1)"""

    # Reset values
    for i in range(len(created_activities_list)):
        created_activities_list[i].popularity_1 = 0
        created_activities_list[i].popularity_2 = 0
        created_activities_list[i].popularity_3 = 0

    # Determine how many campers want each activity for their second choice
    for i in range(len(updated_campers_list)):
        if updated_campers_list[i].next_activity == "":
            for j in range(len(created_activities_list)):
                if updated_campers_list[i].pref_2.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_1 += 1

    # Assign choices for activities with enough spots for all second requests (if repeatable or the camper hasn't had it yet)
    for j in range(len(created_activities_list)):
        if created_activities_list[j].popularity_1 <= (created_activities_list[j].capacity - created_activities_list[j].members):              # Activities with enough spots for all 2nd choice requests
            for i in range(len(updated_campers_list)):
                # Assign if camper is currently unassigned and activity is 2nd choice
                if updated_campers_list[i].next_activity == "":                                             # Only unassigned campers
                    if updated_campers_list[i].pref_2.lower() == created_activities_list[j].name.lower():   # If a camper's 2nd choice
                        if created_activities_list[j].repeatability or created_activities_list[j].name.lower() not in [x.lower() for x in updated_campers_list[i].past_activities]:                                        # No illegal repeat
                            assign_activity(updated_campers_list[i], created_activities_list[j], 2)

    # Check how contested third and fourth choices are
    for i in range(len(updated_campers_list)):
        if updated_campers_list[i].next_activity == "":             # Only consider those still unassigned
            for j in range(len(created_activities_list)):
                if updated_campers_list[i].pref_3.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_2 += 1       # Update popularity of 3rd choice for requests
                    created_activities_list[j].popularity_3 += 1       # 4th choice popularity reflects 3rd choices handed out first
                if updated_campers_list[i].pref_4.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_3 += 1       # Update popularity of 4th choice for requests
    for i in range(len(created_activities_list)):
        if (created_activities_list[i].capacity - created_activities_list[i].members - created_activities_list[i].popularity_1) <= 0:    # If no spots left after 2nd choice
            created_activities_list[i].popularity_2 = 10000                                         # Set popularity super high
            created_activities_list[i].popularity_3 = 10000                                         # Set popularity super high
        else:                                                                                       # If spots left
            created_activities_list[i].popularity_2 = created_activities_list[i].popularity_2 / (created_activities_list[i].capacity - created_activities_list[i].members)                                                     # Calculate popularity value
            created_activities_list[i].popularity_3 = created_activities_list[i].popularity_3 / (created_activities_list[i].capacity - created_activities_list[i].members)                                                     # Calculate popularity value

    # If an activity doesn't have enough spots, sort by 3rd and 4th choices of campers requesting
    for j in range(len(created_activities_list)):
        if created_activities_list[j].popularity_1 > (created_activities_list[j].capacity - created_activities_list[j].members):          # Activities w/contested spots
            temp_list = []                                                                         # Create temp list to sort
            counter = 0
            for i in range(len(updated_campers_list)):
                if updated_campers_list[i - counter].next_activity == "":
                    if updated_campers_list[i - counter].pref_2.lower() == created_activities_list[j].name.lower(): # Campers that want this activity
                        temp_list.append(updated_campers_list.pop(i - counter))                       # Place them in a new list
                        counter += 1                                                                  # Ensure index not out of range
            for k in range(len(temp_list)):                                                           # Campers that want this activity
                for m in range(len(created_activities_list)):                                         # Gather popularity values
                    if temp_list[k].pref_3.lower() == created_activities_list[m].name.lower():
                        temp_list[k].pop_2 = created_activities_list[m].popularity_2
                    elif temp_list[k].pref_4.lower() == created_activities_list[m].name.lower():
                        temp_list[k].pop_3 = created_activities_list[m].popularity_3
            # Bubble sort based on difficulty of filling next spots and avg_pref
            index = len(temp_list) - 1
            while index >= 0:
                for i in range(index):
                    if temp_list[i].pop_2 < temp_list[i + 1].pop_2:                # If easier to fill first camper's 3rd pref, switch
                        temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                    elif temp_list[i].pop_2 == temp_list[i + 1].pop_2:             # If equal difficulty...
                        if temp_list[i].pop_3 < temp_list[i + 1].pop_3:            # If easier to fill first camper's 4th pref, switch
                            temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                        elif temp_list[i].pop_3 == temp_list[i + 1].pop_3:         # If equal difficulty...
                            if temp_list[i].avg_pref < temp_list[i + 1].avg_pref:  # If one camper previously got higher choices
                                temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                index -= 1

            # Assign 2nd choices until capacity is reached
            counter = 0
            for i in range(len(temp_list)):
                if created_activities_list[j].members < created_activities_list[j].capacity:
                    if created_activities_list[j].repeatability or created_activities_list[j].name.lower() not in [x.lower() for x in temp_list[i - counter].past_activities]:                                        # As long as no illegal repeat
                        assign_activity(temp_list[i - counter], created_activities_list[j], 2)
                updated_campers_list.append(temp_list.pop(i - counter))
                counter += 1

    # Check if done, if so quit to avoid any later bugs in the code / processing time
    if are_campers_sorted(updated_campers_list):
        clean(updated_campers_list, created_activities_list)
        return




    """Now we move on to doing third choices! All popularity_i is now popularity_(i+2)"""

    # Reset values
    for i in range(len(created_activities_list)):
        created_activities_list[i].popularity_1 = 0
        created_activities_list[i].popularity_2 = 0
        created_activities_list[i].popularity_3 = 0

    # Determine how many campers want each activity for their third choice
    for i in range(len(updated_campers_list)):
        if updated_campers_list[i].next_activity == "":
            for j in range(len(created_activities_list)):
                if updated_campers_list[i].pref_3.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_1 += 1

    # Assign choices for activities with enough spots for all third requests (if repeatable or the camper hasn't had it yet)
    for j in range(len(created_activities_list)):
        if created_activities_list[j].popularity_1 <= (created_activities_list[j].capacity - created_activities_list[j].members):              # Activities with enough spots for all 3rd choice requests
            for i in range(len(updated_campers_list)):
                # Assign if camper is currently unassigned and activity is 3rd choice
                if updated_campers_list[i].next_activity == "":                                             # Only unassigned campers
                    if updated_campers_list[i].pref_3.lower() == created_activities_list[j].name.lower():   # If a camper's 3rd choice
                        if created_activities_list[j].repeatability or created_activities_list[j].name.lower() not in [x.lower() for x in updated_campers_list[i].past_activities]:                                        # No illegal repeat
                            assign_activity(updated_campers_list[i], created_activities_list[j], 3)

    # Check how contested fourth and fifth choices are
    for i in range(len(updated_campers_list)):
        if updated_campers_list[i].next_activity == "":             # Only consider those still unassigned
            for j in range(len(created_activities_list)):
                if updated_campers_list[i].pref_4.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_2 += 1       # Update popularity of 4th choice for requests
                    created_activities_list[j].popularity_3 += 1       # 5th choice popularity reflects 4th choices handed out first
                if updated_campers_list[i].pref_5.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_3 += 1       # Update popularity of 5th choice for requests
    for i in range(len(created_activities_list)):
        if (created_activities_list[i].capacity - created_activities_list[i].members - created_activities_list[i].popularity_1) <= 0:    # If no spots left after 3rd choice
            created_activities_list[i].popularity_2 = 10000                                         # Set popularity super high
            created_activities_list[i].popularity_3 = 10000                                         # Set popularity super high
        else:                                                                                       # If spots left
            created_activities_list[i].popularity_2 = created_activities_list[i].popularity_2 / (created_activities_list[i].capacity - created_activities_list[i].members)                                                     # Calculate popularity value
            created_activities_list[i].popularity_3 = created_activities_list[i].popularity_3 / (created_activities_list[i].capacity - created_activities_list[i].members)                                                     # Calculate popularity value

    # If an activity doesn't have enough spots, sort by 4th and 5th choices of campers requesting
    for j in range(len(created_activities_list)):
        if created_activities_list[j].popularity_1 > (created_activities_list[j].capacity - created_activities_list[j].members):          # Activities w/contested spots
            temp_list = []                            # Create temp list to sort
            counter = 0                               # Used to track members pulled from original list, keeps index in range
            for i in range(len(updated_campers_list)):
                if updated_campers_list[i - counter].next_activity == "":
                    if updated_campers_list[i - counter].pref_3.lower() == created_activities_list[j].name.lower(): # Campers that want this activity
                        temp_list.append(updated_campers_list.pop(i - counter))                       # Place them in a new list
                        counter += 1                                                                  # Ensure index not out of range
            for k in range(len(temp_list)):                                                           # Campers that want this activity
                for m in range(len(created_activities_list)):                                         # Gather popularity values
                    if temp_list[k].pref_4.lower() == created_activities_list[m].name.lower():
                        temp_list[k].pop_2 = created_activities_list[m].popularity_2
                    elif temp_list[k].pref_5.lower() == created_activities_list[m].name.lower():
                        temp_list[k].pop_3 = created_activities_list[m].popularity_3
            # Bubble sort based on difficulty of filling next spots and avg_pref
            index = len(temp_list) - 1
            while index >= 0:
                for i in range(index):
                    if temp_list[i].pop_2 < temp_list[i + 1].pop_2:                # If easier to fill first camper's 4th pref, switch
                        temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                    elif temp_list[i].pop_2 == temp_list[i + 1].pop_2:             # If equal difficulty...
                        if temp_list[i].pop_3 < temp_list[i + 1].pop_3:            # If easier to fill first camper's 5th pref, switch
                            temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                        elif temp_list[i].pop_3 == temp_list[i + 1].pop_3:         # If equal difficulty...
                            if temp_list[i].avg_pref < temp_list[i + 1].avg_pref:  # If one camper previously got higher choices
                                temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                index -= 1

            # Assign 3rd choices until capacity is reached
            counter = 0                        # Variable used to keep list indexes in range
            for i in range(len(temp_list)):
                if created_activities_list[j].members < created_activities_list[j].capacity:
                    if created_activities_list[j].repeatability or created_activities_list[j].name.lower() not in [x.lower() for x in temp_list[i - counter].past_activities]:                                        # As long as no illegal repeat
                        assign_activity(temp_list[i - counter], created_activities_list[j], 3)
                updated_campers_list.append(temp_list.pop(i - counter))
                counter += 1

    # Check if done, if so quit to avoid any later bugs in the code / processing time
    if are_campers_sorted(updated_campers_list):
        clean(updated_campers_list, created_activities_list)
        return



    """Now we move on to doing fourth choices! All popularity_i is now popularity_(i+3)"""

    # Reset values
    for i in range(len(created_activities_list)):
        created_activities_list[i].popularity_1 = 0
        created_activities_list[i].popularity_2 = 0
        created_activities_list[i].popularity_3 = 0

    # Determine how many campers want each activity for their 4th choice
    for i in range(len(updated_campers_list)):
        if updated_campers_list[i].next_activity == "":
            for j in range(len(created_activities_list)):
                if updated_campers_list[i].pref_4.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_1 += 1

    # Assign choices for activities with enough spots for all 4th requests (if repeatable or the camper hasn't had it yet)
    for j in range(len(created_activities_list)):
        if created_activities_list[j].popularity_1 <= (created_activities_list[j].capacity - created_activities_list[j].members):              # Activities with enough spots for all 4th choice requests
            for i in range(len(updated_campers_list)):
                # Assign if camper is currently unassigned and activity is 4th choice
                if updated_campers_list[i].next_activity == "":                                             # Only unassigned campers
                    if updated_campers_list[i].pref_4.lower() == created_activities_list[j].name.lower():   # If a camper's 4th choice
                        if created_activities_list[j].repeatability or created_activities_list[j].name.lower() not in [x.lower() for x in updated_campers_list[i].past_activities]:                                           # No illegal repeat
                            assign_activity(updated_campers_list[i], created_activities_list[j], 4)

    # Check how contested 5th and 6th choices are
    for i in range(len(updated_campers_list)):
        if updated_campers_list[i].next_activity == "":                # Only consider those still unassigned
            for j in range(len(created_activities_list)):
                if updated_campers_list[i].pref_5.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_2 += 1       # Update popularity of 5th choice for requests
                    created_activities_list[j].popularity_3 += 1       # 6th choice popularity reflects 5th choices handed out first
                if updated_campers_list[i].pref_6.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_3 += 1       # Update popularity of 6th choice for requests
    for i in range(len(created_activities_list)):
        if (created_activities_list[i].capacity - created_activities_list[i].members - created_activities_list[i].popularity_1) <= 0:    # If no spots left after 4th choice
            created_activities_list[i].popularity_2 = 10000                                         # Set popularity super high
            created_activities_list[i].popularity_3 = 10000                                         # Set popularity super high
        else:                                                                                       # If spots left
            created_activities_list[i].popularity_2 = created_activities_list[i].popularity_2 / (created_activities_list[i].capacity - created_activities_list[i].members)                                                     # Calculate popularity value
            created_activities_list[i].popularity_3 = created_activities_list[i].popularity_3 / (created_activities_list[i].capacity - created_activities_list[i].members)                                                     # Calculate popularity value

    # If an activity doesn't have enough spots, sort by 5th and 6th choices of campers requesting
    for j in range(len(created_activities_list)):
        if created_activities_list[j].popularity_1 > (created_activities_list[j].capacity - created_activities_list[j].members):          # Activities w/contested spots
            temp_list = []                            # Create temp list to sort
            counter = 0                               # Used to track members pulled from original list, keeps index in range
            for i in range(len(updated_campers_list)):
                if updated_campers_list[i - counter].next_activity == "":
                    if updated_campers_list[i - counter].pref_4.lower() == created_activities_list[j].name.lower(): # Campers that want this activity
                        temp_list.append(updated_campers_list.pop(i - counter))                       # Place them in a new list
                        counter += 1                                                                  # Ensure index not out of range
            for k in range(len(temp_list)):                                                           # Campers that want this activity
                for m in range(len(created_activities_list)):                                         # Gather popularity values
                    if temp_list[k].pref_5.lower() == created_activities_list[m].name.lower():
                        temp_list[k].pop_2 = created_activities_list[m].popularity_2
                    elif temp_list[k].pref_6.lower() == created_activities_list[m].name.lower():
                        temp_list[k].pop_3 = created_activities_list[m].popularity_3
            # Bubble sort based on difficulty of filling next spots and avg_pref
            index = len(temp_list) - 1
            while index >= 0:
                for i in range(index):
                    if temp_list[i].pop_2 < temp_list[i + 1].pop_2:                # If easier to fill first camper's 5th pref, switch
                        temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                    elif temp_list[i].pop_2 == temp_list[i + 1].pop_2:             # If equal difficulty...
                        if temp_list[i].pop_3 < temp_list[i + 1].pop_3:            # If easier to fill first camper's 6th pref, switch
                            temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                        elif temp_list[i].pop_3 == temp_list[i + 1].pop_3:         # If equal difficulty...
                            if temp_list[i].avg_pref < temp_list[i + 1].avg_pref:  # If one camper previously got higher choices
                                temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                index -= 1

            # Assign 4th choices until capacity is reached
            counter = 0                        # Variable used to keep list indexes in range
            for i in range(len(temp_list)):
                if created_activities_list[j].members < created_activities_list[j].capacity:
                    if created_activities_list[j].repeatability or created_activities_list[j].name.lower() not in [x.lower() for x in temp_list[i - counter].past_activities]:                                        # As long as no illegal repeat
                        assign_activity(temp_list[i - counter], created_activities_list[j], 4)
                updated_campers_list.append(temp_list.pop(i - counter))
                counter += 1

    # Check if done, if so quit to avoid any later bugs in the code / processing time
    if are_campers_sorted(updated_campers_list):
        clean(updated_campers_list, created_activities_list)
        return



    """Now we move on to doing fifth choices! All popularity_i is now popularity_(i+4)"""
    """Code that would index choice 7+ has been removed"""

    # Reset values
    for i in range(len(created_activities_list)):
        created_activities_list[i].popularity_1 = 0
        created_activities_list[i].popularity_2 = 0
        created_activities_list[i].popularity_3 = 0

    # Determine how many campers want each activity for their 5th choice
    for i in range(len(updated_campers_list)):
        if updated_campers_list[i].next_activity == "":
            for j in range(len(created_activities_list)):
                if updated_campers_list[i].pref_5.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_1 += 1

    # Assign choices for activities with enough spots for all 5th requests (if repeatable or the camper hasn't had it yet)
    for j in range(len(created_activities_list)):
        if created_activities_list[j].popularity_1 <= (created_activities_list[j].capacity - created_activities_list[j].members):              # Activities with enough spots for all 5th choice requests
            for i in range(len(updated_campers_list)):
                # Assign if camper is currently unassigned and activity is 5th choice
                if updated_campers_list[i].next_activity == "":                                             # Only unassigned campers
                    if updated_campers_list[i].pref_5.lower() == created_activities_list[j].name.lower():   # If a camper's 5th choice
                        if created_activities_list[j].repeatability or created_activities_list[j].name.lower() not in [x.lower() for x in updated_campers_list[i].past_activities]:                                        # No illegal repeat
                            assign_activity(updated_campers_list[i], created_activities_list[j], 5)

    # Check how contested 6th choices are
    for i in range(len(updated_campers_list)):
        if updated_campers_list[i].next_activity == "":                # Only consider those still unassigned
            for j in range(len(created_activities_list)):
                if updated_campers_list[i].pref_5.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_2 += 1       # Update popularity of 6th choice for requests
    for i in range(len(created_activities_list)):
        if (created_activities_list[i].capacity - created_activities_list[i].members - created_activities_list[i].popularity_1) <= 0:    # If no spots left after 5th choice
            created_activities_list[i].popularity_2 = 10000                                         # Set popularity super high
        else:                                                                                       # If spots left
            created_activities_list[i].popularity_2 = created_activities_list[i].popularity_2 / (created_activities_list[i].capacity - created_activities_list[i].members)                                                     # Calculate popularity value

    # If an activity doesn't have enough spots, sort by 6th choices of campers requesting the activity
    for j in range(len(created_activities_list)):
        if created_activities_list[j].popularity_1 > (created_activities_list[j].capacity - created_activities_list[j].members):          # Activities w/contested spots
            temp_list = []                            # Create temp list to sort
            counter = 0                               # Used to track members pulled from original list, keeps index in range
            for i in range(len(updated_campers_list)):
                if updated_campers_list[i - counter].next_activity == "":
                    if updated_campers_list[i - counter].pref_5.lower() == created_activities_list[j].name.lower(): # Campers that want this activity
                        temp_list.append(updated_campers_list.pop(i - counter))                       # Place them in a new list
                        counter += 1                                                                  # Ensure index not out of range
            for k in range(len(temp_list)):                                                           # Campers that want this activity
                for m in range(len(created_activities_list)):                                         # Gather popularity values
                    if temp_list[k].pref_6.lower() == created_activities_list[m].name.lower():
                        temp_list[k].pop_2 = created_activities_list[m].popularity_2
            # Bubble sort based on difficulty of filling next spot and avg_pref
            index = len(temp_list) - 1
            while index >= 0:
                for i in range(index):
                    if temp_list[i].pop_2 < temp_list[i + 1].pop_2:                # If easier to fill first camper's 6th pref, switch
                        temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                    elif temp_list[i].pop_2 == temp_list[i + 1].pop_2:             # If equal difficulty...
                        if temp_list[i].avg_pref < temp_list[i + 1].avg_pref:      # If one camper previously got higher choices
                            temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                index -= 1

            # Assign 5th choices until capacity is reached
            counter = 0                        # Variable used to keep list indexes in range
            for i in range(len(temp_list)):
                if created_activities_list[j].members < created_activities_list[j].capacity:
                    if created_activities_list[j].repeatability or created_activities_list[j].name.lower() not in [x.lower() for x in temp_list[i - counter].past_activities]:                                        # As long as no illegal repeat
                        assign_activity(temp_list[i - counter], created_activities_list[j], 5)
                updated_campers_list.append(temp_list.pop(i - counter))
                counter += 1

    # Check if done, if so quit to avoid any later bugs in the code / processing time
    if are_campers_sorted(updated_campers_list):
        clean(updated_campers_list, created_activities_list)
        return



    """Now we move on to doing sixth choices! All popularity_i is now popularity_(i+5)"""
    """Code that would index choice 7+ has been removed"""

    # Reset values
    for i in range(len(created_activities_list)):
        created_activities_list[i].popularity_1 = 0
        created_activities_list[i].popularity_2 = 0
        created_activities_list[i].popularity_3 = 0

    # Determine how many campers want each activity for their 6th choice
    for i in range(len(updated_campers_list)):
        if updated_campers_list[i].next_activity == "":
            for j in range(len(created_activities_list)):
                if updated_campers_list[i].pref_6.lower() == created_activities_list[j].name.lower():
                    created_activities_list[j].popularity_1 += 1

    # Assign choices for activities with enough spots for all 6th requests (if repeatable or the camper hasn't had it yet)
    for j in range(len(created_activities_list)):
        if created_activities_list[j].popularity_1 <= (created_activities_list[j].capacity - created_activities_list[j].members):              # Activities with enough spots for all 6th choice requests
            for i in range(len(updated_campers_list)):
                # Assign if camper is currently unassigned and activity is 6th choice
                if updated_campers_list[i].next_activity == "":                                             # Only unassigned campers
                    if updated_campers_list[i].pref_6.lower() == created_activities_list[j].name.lower():   # If a camper's 6th choice
                        if created_activities_list[j].repeatability or created_activities_list[j].name.lower() not in [x.lower() for x in updated_campers_list[i].past_activities]:                                        # No illegal repeat
                            assign_activity(updated_campers_list[i], created_activities_list[j], 6)

    # If an activity doesn't have enough spots, sort by avg_pref of campers requesting the activity
    for j in range(len(created_activities_list)):
        if created_activities_list[j].popularity_1 > (created_activities_list[j].capacity - created_activities_list[j].members):          # Activities w/contested spots
            temp_list = []                            # Create temp list to sort
            counter = 0                               # Used to track members pulled from original list, keeps index in range
            for i in range(len(updated_campers_list)):
                if updated_campers_list[i - counter].next_activity == "":
                    if updated_campers_list[i - counter].pref_6.lower() == created_activities_list[j].name.lower(): # Campers that want this activity
                        temp_list.append(updated_campers_list.pop(i - counter))                       # Place them in a new list
                        counter += 1                                                                  # Ensure index not out of range
            # Bubble sort based on avg_pref
            index = len(temp_list) - 1
            while index >= 0:
                for i in range(index):
                    if temp_list[i].avg_pref < temp_list[i + 1].avg_pref:      # If one camper previously got higher choices
                        temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
                index -= 1

            # Assign 6th choices until capacity is reached
            counter = 0                        # Variable used to keep list indexes in range
            for i in range(len(temp_list)):
                if created_activities_list[j].members < created_activities_list[j].capacity:
                    if created_activities_list[j].repeatability or created_activities_list[j].name.lower() not in [x.lower() for x in temp_list[i - counter].past_activities]:                                        # As long as no illegal repeat
                        assign_activity(temp_list[i - counter], created_activities_list[j], 6)
                updated_campers_list.append(temp_list.pop(i - counter))
                counter += 1

    if are_campers_sorted(updated_campers_list):            # Need if statement because clean function assumes full camper list
        clean(updated_campers_list, created_activities_list)
    else:
        counter = 0
        temporary_list = []
        for i in range(len(updated_campers_list)):
            if updated_campers_list[i - counter].next_activity == "":
                temporary_list.append(updated_campers_list.pop(i - counter))
                counter += 1
        clean(updated_campers_list, created_activities_list)
        for i in range(len(temporary_list)):
            updated_campers_list.append(temporary_list.pop())



# ===================================================================================================


"""Assigns campers their activity -- to be used in the sort_campers function"""
def assign_activity(camper, activity, preference):
    camper.next_activity = activity.name
    camper.past_preferences.append(preference)
    activity.members += 1

"""Removes activity - to be used in cleaner function to fix mistakes of algorithm"""
def remove_activity(camper, activities_list):
    del camper.past_preferences[len(camper.past_preferences) - 1]
    for j in range(len(activities_list)):
        if activities_list[j].name.lower() == camper.next_activity.lower():
            activities_list[j].members -= 1
    camper.next_activity = ""



"""Returns boolean indicating if all campers have been sorted - to be used in the sort_campers function"""
def are_campers_sorted(campers_list):         # Takes in list of campers
    done = True
    for i in range(len(campers_list)):
        if campers_list[i].next_activity == "":
            done = False
    return done



# ===================================================================================================




"""Cleans up mistakes my code made"""
def clean(campers_list, activities_list):
    tracker = 1
    while tracker != 0:
        tracker = 0
        for i in range(len(campers_list)):
            if campers_list[i].past_preferences[len(campers_list[i].past_preferences) - 1] == 6:     # If you got your 6th choice
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_5:                            # Check 5th choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 5)
                            tracker += 1
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_4:                            # Check 4th choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 4)
                            tracker += 1
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_3:                            # Check 3rd choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 3)
                            tracker += 1
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_2:                            # Check 2nd choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 2)
                            tracker += 1
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_1:                            # Check 1st choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 1)
                            tracker += 1

            elif campers_list[i].past_preferences[len(campers_list[i].past_preferences) - 1] == 5:   # If you got your 5th choice
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_4:                            # Check 4th choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 4)
                            tracker += 1
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_3:                            # Check 3rd choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 3)
                            tracker += 1
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_2:                            # Check 2nd choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 2)
                            tracker += 1
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_1:                            # Check 1st choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 1)
                            tracker += 1

            elif campers_list[i].past_preferences[len(campers_list[i].past_preferences) - 1] == 4:   # If you got your 4th choice
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_3:                            # Check 3rd choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 3)
                            tracker += 1
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_2:                            # Check 2nd choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 2)
                            tracker += 1
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_1:                            # Check 1st choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 1)
                            tracker += 1

            elif campers_list[i].past_preferences[len(campers_list[i].past_preferences) - 1] == 3:   # If you got your 3rd choice
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_2:                            # Check 2nd choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 2)
                            tracker += 1
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_1:                            # Check 1st choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 1)
                            tracker += 1

            elif campers_list[i].past_preferences[len(campers_list[i].past_preferences) - 1] == 2:   # If you got your 2nd choice
                for j in range(len(activities_list)):
                    if activities_list[j].name == campers_list[i].pref_1:                            # Check 1st choice for openings
                        if activities_list[j].capacity > activities_list[j].members:
                            remove_activity(campers_list[i], activities_list)
                            assign_activity(campers_list[i], activities_list[j], 1)
                            tracker += 1





    """Now we're moving to the switcheroos to promote 2 seconds instead of 1st and 3rd/4th/5th/6th"""
    for i in range(len(campers_list)):
        if campers_list[i].past_preferences[len(campers_list[i].past_preferences) - 1] == 1:   # Find campers w/ 1st choice
            for j in range(len(campers_list)):
                if campers_list[j].past_preferences[len(campers_list[j].past_preferences) - 1] == 3 or campers_list[j].past_preferences[len(campers_list[j].past_preferences) - 1] == 4 or campers_list[j].past_preferences[len(campers_list[j].past_preferences) - 1] == 5 or campers_list[j].past_preferences[len(campers_list[j].past_preferences) - 1] == 6:  # Compare all campers with 3+ choice
                    if campers_list[i].pref_2 == campers_list[j].next_activity and campers_list[j].pref_2 == campers_list[i].next_activity:                                                # If activities are others' 2nd prefs
                        campers_list[i].next_activity, campers_list[j].next_activity = campers_list[j].next_activity, campers_list[i].next_activity                                             # Switch activities
                        campers_list[j].past_preferences[len(campers_list[j].past_preferences) - 1] = 2  # Update preferences
                        campers_list[i].past_preferences[len(campers_list[i].past_preferences) - 1] = 2  # Update preferences
