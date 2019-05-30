# Setting up for online ability
from flask import Flask, flash, redirect, render_template, request, send_file, Response

# Reading and writing an excel file using Python
import openpyxl
from tempfile import NamedTemporaryFile


# Helper functions I wrote to clean up application.py code
import lib.xls.parsing.preference as preference
import lib.xls.parsing.activity as activity
import lib.xls.parsing.history as history


import lib.hungarian as hungarian
import lib.camper as camper
from lib.xls.output import output_master_excel
from lib.xls.validation import check_preferences_for_input_errors, output_errors


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

def get_workbook(request, key):
    stream = request.files[key]
    with NamedTemporaryFile() as tmp:
        tmp.write(stream.read())
        tmp.seek(0)
        workbook = openpyxl.load_workbook(tmp)
    return workbook

@app.route("/sorted", methods=["POST"])
def sorted():
    """Sort campers and download the results as an Excel document"""

    # Open the input file
    preferences_workbook = get_workbook(request, "preferences")
    preferences_sheet = preferences_workbook.active
    # Check input file for proper input
    errors = check_preferences_for_input_errors(preferences_sheet)
    if errors:
        wb = output_errors(errors)
        # Download errors file
        with NamedTemporaryFile() as tmp:
            wb.save(tmp.name)
            tmp.seek(0)
            stream = tmp.read()

            r = Response(response=stream, status=200, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            r.headers["Content-Disposition"] = 'attachment; filename="errors.xlsx"'
            return r

    # Initializes the list
    preferences = preference.parse_sheet(preferences_sheet)

    # Create activity objects
    activities_workbook = get_workbook(request, "activities")
    activities_sheet = activities_workbook.active
    activities = activity.parse_sheet(activities_sheet)

    # Update camper objects
    if "histories" in request.files and request.files["histories"].filename != '':
        histories_workbook = get_workbook(request, "histories")
        if len(histories_workbook.worksheets) >= 2:
            histories_sheet = histories_workbook.worksheets[1]
        else:
            histories_sheet = histories_workbook.active
        histories = history.parse_sheet(histories_sheet)
    else:
        histories = [ history.History(p.name, p.bunk, [], []) for p in preferences ]

    campers = camper.merge_objects(preferences, activities, histories)

    # Sort camper
    assignments = hungarian.sort_campers(campers, activities)

    wb = output_master_excel(assignments, activities)

    with NamedTemporaryFile() as tmp:
        wb.save(tmp.name)
        tmp.seek(0)
        stream = tmp.read()

        r = Response(response=stream, status=200, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        r.headers["Content-Disposition"] = 'attachment; filename="%s.xlsx"' % request.form.get("filename")
        return r
