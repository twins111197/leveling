# Setting up for online ability
from flask import Flask, flash, redirect, render_template, request, send_file, Response

# Reading and writing an excel file using Python
import xlrd
import openpyxl
from tempfile import NamedTemporaryFile


# Helper functions I wrote to clean up application.py code
from Helpers import create_campers, create_activities, update_campers, output_cycle_excel, output_master_excel, sort_campers

# ======================================================================================
# """This is code for creating camper objects with name, edah, bunk, and preferences (up to 9 of them)"""
#
# campers_location = "/Users/shelly/Documents/Ramah/Leveling/Test File Campers.xlsx"          # Give the location of the input file
# campers = list()                                                                            # Initializes the list
# create_campers(campers, campers_location)
#
#
#
# """This is code for updating camper objects"""
#
# history_location = "/Users/shelly/Documents/Ramah/Leveling/Test File Past Activities.xlsx"  # Give the location of the input file
# update_campers(campers, history_location)                                                   # Update camper objects
#
#
# """This is code for sorting campers into their activities for the coming cycle"""
# sort_campers(campers, activities)
#
#
# """This is code for outputting the end of the project"""
# #output_cycle_excel(campers, "testing-cycle")
# output_master_excel(campers, "testing-master")


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
    return render_template("index.html")


@app.route("/sorted", methods=["POST"])
def sorted():
    """Display homescreen"""

    # Give the location of the input file
    campers_location = request.files["preferences"]
    # Initializes the list
    campers = list()
    create_campers(campers, campers_location)

    # Create activity objects
    activities_location = request.files["activities"]
    # Give the location of the input file
    activities = list()
    # Initializes the list
    create_activities(activities, activities_location)

    # Update camper objects
    history_location = request.files["histories"]
    # Give the location of the input file
    update_campers(campers, history_location)
    # Update camper objects

    # Sort campers
    sort_campers(campers, activities)

    wb = output_master_excel(campers, "foo")

    with NamedTemporaryFile() as tmp:
        wb.save(tmp.name)
        tmp.seek(0)
        stream = tmp.read()

        r = Response(response=stream, status=200, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        r.headers["Content-Disposition"] = 'attachment; filename="campers.xlsx"'
        return r
