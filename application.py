# Setting up for online ability
from flask import Flask, flash, redirect, render_template, request, send_file

# Reading and writing an excel file using Python
import xlrd
import openpyxl

# Helper functions I wrote to clean up application.py code
from Helpers import create_campers, create_activities, update_campers, output_cycle_excel, output_master_excel, sort_campers

# ======================================================================================
"""This is code for creating camper objects with name, edah, bunk, and preferences (up to 9 of them)"""

campers_location = "/Users/shelly/Documents/Ramah/Leveling/Test File Campers.xlsx"          # Give the location of the input file
campers = list()                                                                            # Initializes the list
create_campers(campers, campers_location)


"""This is code for creating activity objects"""

activities_location = "/Users/shelly/Documents/Ramah/Leveling/Test File Activities.xlsx"    # Give the location of the input file
activities = list()                                                                         # Initializes the list
create_activities(activities, activities_location)


"""This is code for updating camper objects"""

history_location = "/Users/shelly/Documents/Ramah/Leveling/Test File Past Activities.xlsx"  # Give the location of the input file
update_campers(campers, history_location)                                                   # Update camper objects


"""This is code for sorting campers into their activities for the coming cycle"""
sort_campers(campers, activities)


"""This is code for outputting the end of the project"""
#output_cycle_excel(campers, "testing-cycle")
output_master_excel(campers, "testing-master")


# import urllib.request
# filename = "test.txt"
# file_ = open(filename, 'w')
# with urllib.request.urlopen("https://wordpress.org/plugins/about/readme.txt") as resource:
#     for line in resource:
#         line = line.decode('utf-8')
#         file_.write(line)
#     file_.close()
#
# data =  resource.read().decode(resource.headers.get_content_charset())






# ======================================================================================

"""This is code for creating a web-based app, mostly taken from CS50 final project"""
# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# Create homescreen
@app.route("/")
def index():
    """Display homescreen"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Create camper objects
        campers_location = request.form.get(preferences)                                            # Give the location of the input file
        campers = list()                                                                            # Initializes the list
        create_campers(campers, campers_location)

        # Create activity objects
        activities_location = request.form.get(activities)                                          # Give the location of the input file
        activities = list()                                                                         # Initializes the list
        create_activities(activities, activities_location)

        # Update camper objects
        history_location = request.form.get(histories)                                              # Give the location of the input file
        update_campers(campers, history_location)                                                   # Update camper objects

        # Sort campers
        sort_campers(campers, activities)

        # Save update to my computer -- NEEDS TO BE CHANGED TO DOWNLOADING
        file = output_master_excel(campers, "testing-master")
        return render_template("sorted.html", file=file)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("index.html")


@app.route("/sorted")
def sorted():
    """Display homescreen"""
    return render_template("sorted.html")

        #####NEED TO DEVELOP THIS IF THIS MATTERS


# 
# @app.route('/download/', methods=['GET'])
# def download():
#     url = request.args['url']
#     filename = request.args.get('filename', 'image.png')
#     r = requests.get(url)
#     strIO = StringIO.StringIO(r.content)
#     return send_file(strIO, as_attachment=True, attachment_filename=filename)
