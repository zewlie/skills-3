from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application")
def application():
    """Show an application page."""

    return render_template("application-form.html")


@app.route("/congratulations", methods=["POST"])
def application_complete():
    """Show a response after a user has submitted an application."""

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    jobtype = request.form.get("jobtype")

    if jobtype == "se":
        jobtype = "Software Engineer"
    if jobtype == "qa":
        jobtype = "QA Engineer"
    if jobtype == "pm":
        jobtype = "Product Manager"

    salary = salary.strip("$")

    return render_template("application-response.html", firstname=firstname, lastname=lastname, salary=salary, jobtype=jobtype)

if __name__ == "__main__":
    app.run(debug=True)
