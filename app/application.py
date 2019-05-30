# Standard Library
from tempfile import NamedTemporaryFile

# Flask
from flask import Flask, Response, flash, redirect, render_template, request, send_file

# Packages
import openpyxl

from lib import hungarian
from lib.xls.output import output_master_excel
from lib.xls.parsing import InvalidPreferences, parse_xls
from lib.xls.validation import output_errors

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
    return render_template("index.html")


@app.route("/sorted", methods=["POST"])
def sorted():
    """Sort campers and download the results as an Excel document"""

    # Get the input workbooks
    preferences_wb = get_workbook(request, "preferences")
    activities_wb = get_workbook(request, "activities")
    if "histories" in request.files and request.files["histories"].filename != "":
        histories_wb = get_workbook(request, "histories")
    else:
        histories_wb = None

    # Parse the input
    try:
        campers, activities = parse_xls(preferences_wb, activities_wb, histories_wb)
    except InvalidPreferences as e:
        return render_workbook(output_errors(e.errors), "errors")

    # Sort campers
    assignments = hungarian.sort_campers(campers, activities)

    # Output results
    wb = output_master_excel(assignments, activities)
    return render_workbook(wb, request.form.get("filename"))


def get_workbook(request, key):
    stream = request.files[key]
    with NamedTemporaryFile() as tmp:
        tmp.write(stream.read())
        tmp.seek(0)
        workbook = openpyxl.load_workbook(tmp)
    return workbook


def render_workbook(wb, name):
    with NamedTemporaryFile() as tmp:
        wb.save(tmp.name)
        tmp.seek(0)
        stream = tmp.read()

        r = Response(
            response=stream,
            status=200,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        r.headers["Content-Disposition"] = 'attachment; filename="%s.xlsx"' % name
        return r
