from flask import Flask, render_template
from flask import redirect, Response
from flask_sqlalchemy import SQLAlchemy
from flask import request
from io import StringIO
import csv



app = Flask(__name__) # start the application
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///BugsyDB.db"
db = SQLAlchemy(app)

class User(db.Model):
    id_User = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    email_address = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    job_title = db.Column(db.String(50))

class Bug(db.Model):
    id_Bug = db.Column(db.Integer, primary_key = True)
    bug_code = db.Column(db.String(50))
    status = db.Column(db.String(50))
    priority = db.Column(db.String(50))
    defect_clasification = db.Column(db.String(50))
    defect_origin = db.Column(db.String(50))
    
class Project(db.Model):
    id_Project = db.Column(db.Integer, primary_key = True)
    project_name = db.Column(db.String(50))
    status = db.Column(db.String(50))
    period = db.Column(db.Integer)
    project_type = db.Column(db.String(50))

@app.route("/") # when accessing http://localhost:5000/ the following functiion will be executed

def home():
    return render_template("index.html")

@app.route("/overview", endpoint="overview")
def get_overview():
    project_counts = {
        "Open": Project.query.filter_by(status="Open").count(),
        "In Progress": Project.query.filter_by(status="In Progress").count(),
        "Closed": Project.query.filter_by(status="Closed").count()
    }

    bug_counts = {
        "Open": Bug.query.filter_by(status="Open").count(),
        "In Progress": Bug.query.filter_by(status="In Progress").count(),
        "Closed": Bug.query.filter_by(status="Closed").count()
    }

    user_counts = {
        "QA": User.query.filter_by(job_title="QA").count(),
        "Project Manager": User.query.filter_by(job_title="Project Manager").count(),
        "Software Developer": User.query.filter_by(job_title="Software Developer").count()
    }

    totals = {
        "projects": sum(project_counts.values()),
        "bugs": sum(bug_counts.values()),
        "users": sum(user_counts.values())
    }

    return render_template(
        "overview.html",
        projects=project_counts,
        bugs=bug_counts,
        users=user_counts,
        totals=totals
    )

@app.route("/projects", methods = ["GET"],  endpoint="projects")
def get_projects():
    project_filter = request.args.get("status", default=None)
    sort_order = request.args.get("sort", default=None)

    query = Project.query

    if project_filter=="Open":
        query = query.filter_by(status=project_filter)
    elif project_filter=="In Progress":
        query = query.filter_by(status=project_filter)
    elif project_filter=="Closed":
        query = query.filter_by(status=project_filter)

    if sort_order == "asc":
        query = query.order_by(Project.project_name.asc())
    elif sort_order =="desc":
        query = query.order_by(Project.project_name.desc())
    
    projects = query.all()
    all_status = db.session.query(Project.status).distinct().all()
    statuses = [st[0] for st in all_status]

    return render_template("projects.html", projects=projects, statuses=statuses)


@app.route("/projects/add", methods=["GET", "POST"])
def add_projects():
    if request.method == "POST":
        project_name = request.form["project_name"]
        status = request.form["status"]
        period = request.form["period"]
        project_type = request.form.get("project_type")

            # Check if project already exists
        existing_project = Project.query.filter_by(project_name=project_name).first()
        if existing_project:
            projects = Project.query.all()
            error = f"Project '{project_name}' is already in database."
            return render_template("projects.html", projects=projects, error=error)

        new_project = Project(
            project_name=project_name, 
            status= status, 
            period=period, 
            project_type=project_type
        )
        
        db.session.add(new_project)
        db.session.commit()
        projects = Project.query.all()
        return render_template("projects.html", projects = projects, active_tab = "Project List")

@app.route("/projects/update", methods=["GET", "POST"])
def update_projects():
    if request.method == "POST":
        project_name = request.form.get("project_name")

            # Check if project already exists
        existing_project = Project.query.filter_by(project_name=project_name).first()
        if not existing_project:
            projects =Project.query.all()
            error = f"Project '{project_name}' cannot be found in database."
            return render_template("projects.html", projects=projects, error=error, active_tab="Update Project")
        
        status = request.form.get("status")
        period = request.form.get("period")
        project_type = request.form.get("project_type")

        if status:
            existing_project.status = status
        if period:
            existing_project.period = period
        if project_type:
            existing_project.project_type = project_type
        
        db.session.commit()

        success_message = f"Project '{project_name}' has been updated."
        projects = Project.query.all()
        return render_template("projects.html", projects=projects, success_message=success_message ,active_tab="Update Project")


@app.route("/projects/delete", methods=["GET", "POST"])
def delete_projects():
    if request.method == "POST":
        project_name = request.form.get("project_name")

        if not project_name:
            projects = Project.query.all()
            error = "Please enter the Project name."
            return render_template("projects.html", projects=projects, error=error, active_tab="Delete Project")

        existing_project = Project.query.filter_by(project_name=project_name).first()

        if existing_project:
            db.session.delete(existing_project)
            db.session.commit()
            projects = Project.query.all()
            success_message = f"Project '{project_name}' has been successfully deleted."
            return render_template("projects.html", projects=projects, success_message=success_message)
        else:
            projects = Project.query.all()
            error = f"Project '{project_name}' was not found in the database."
            return render_template("projects.html", projects=projects, error=error, active_tab="Delete Project")

    projects = Project.query.all()
    return render_template("projects.html", projects=projects, active_tab="Delete Project")


@app.route("/projects/export", methods=["GET"])
def export_projects():
    status = request.args.get("status", default=None)
    sort_order = request.args.get("sort", default=None)

    query = Project.query

    if status:
        query = query.filter_by(status=status)

    if sort_order == "asc":
        query = query.order_by(Project.project_name.asc())
    elif sort_order == "desc":
        query = query.order_by(Project.project_name.desc())

    projects = query.all()

    # Generate CSV
    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(["Project Name", "Status", "Period", "Project Type"])

    for project in projects:
        writer.writerow([project.project_name, project.status, project.period, project.project_type])

    output = si.getvalue()
    si.close()

    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=projects_export.csv"}
    )



@app.route("/bugs", methods = ["GET"],  endpoint="bugs")
def get_bugs():
    bugs_filter = request.args.get("status", default=None)
    sort_order = request.args.get("sort", default=None)

    query = Bug.query

    if bugs_filter=="Open":
        query = query.filter_by(status=bugs_filter)
    elif bugs_filter=="Closed":
        query = query.filter_by(status=bugs_filter)

    if sort_order == "asc":
        query = query.order_by(Bug.bug_code.asc())
    elif sort_order =="desc":
        query = query.order_by(Bug.bug_code.desc())
    
    bugs = query.all()
    all_status = db.session.query(Bug.status).distinct().all()
    statuses = [st[0] for st in all_status]

    return render_template("bugs.html", bugs=bugs, statuses=statuses, active_tab = "Bugs List")

@app.route("/bugs/add", methods=["GET", "POST"])
def add_bugs():
    if request.method == "POST":
        bug_code = request.form["bug_code"]
        status = request.form["status"]
        priority = request.form["priority"]
        defect_clasification = request.form.get("defect_clasification")
        defect_origin = request.form.get("defect_origin")

            # Check if bug already exists
        existing_bug = Bug.query.filter_by(bug_code=bug_code).first()
        if existing_bug:
            bugs = Bug.query.all()
            error = f"Bug '{bug_code}' is already in database."
            return render_template("bugs.html", bugs=bugs, error=error, active_tab = "Add Bugs")

        new_bug = Bug(
            bug_code=bug_code, 
            status= status, 
            priority=priority, 
            defect_clasification=defect_clasification, 
            defect_origin=defect_origin)
        
        db.session.add(new_bug)
        db.session.commit()
        bugs = Bug.query.all()
        return render_template("bugs.html", bugs = bugs, active_tab = "Add Bugs")
    

@app.route("/bugs/update", methods=["GET", "POST"])
def update_bugs():
    if request.method == "POST":
        bug_code = request.form.get("bug_code")

            # Check if bug already exists
        existing_bug = Bug.query.filter_by(bug_code=bug_code).first()
        if not existing_bug:
            bugs =Bug.query.all()
            error = f"Bug '{bug_code}' cannot be found in database."
            return render_template("bugs.html", bugs=bugs, error=error, active_tab="Update Bugs")
        
        status = request.form.get("status")
        priority = request.form.get("priority")
        defect_clasification = request.form.get("defect_clasification")
        defect_origin = request.form.get("defect_origin")

        if status:
            existing_bug.status = status
        if priority:
            existing_bug.priority = priority
        if defect_clasification:
            existing_bug.defect_clasification = defect_clasification
        if defect_origin:
            existing_bug.defect_origin = defect_origin
        
        db.session.commit()

        success_message = f"Bug '{bug_code}' has been updated."
        bugs = Bug.query.all()
        return render_template("bugs.html", bugs=bugs, success_message=success_message ,active_tab="Update Bugs")


@app.route("/bugs/delete", methods=["GET", "POST"])
def delete_bugs():
    if request.method == "POST":
        bug_code = request.form.get("bug_code")

        if not bug_code:
            bugs = Bug.query.all()
            error = "Please enter the Bug code."
            return render_template("bugs.html", bugs=bugs, error=error, active_tab="Delete Bugs")

        existing_bug = Bug.query.filter_by(bug_code=bug_code).first()

        if existing_bug:
            db.session.delete(existing_bug)
            db.session.commit()
            bugs = Bug.query.all()
            success_message = f"Bug '{bug_code}' has been successfully deleted."
            return render_template("bugs.html", bugs=bugs, success_message=success_message)
        else:
            bugs = Bug.query.all()
            error = f"Bug '{bug_code}' was not found in the database."
            return render_template("bugs.html", bugs=bugs, error=error, active_tab="Delete Bugs")

    bugs = Bug.query.all()
    return render_template("bugs.html", bugs=bugs, active_tab="Delete Bugs")


@app.route("/bugs/export", methods=["GET"])
def export_bugs():
    status = request.args.get("status", default=None)
    sort_order = request.args.get("sort", default=None)

    query = Bug.query

    if status:
        query = query.filter_by(status=status)

    if sort_order == "asc":
        query = query.order_by(Bug.bug_code.asc())
    elif sort_order == "desc":
        query = query.order_by(Bug.bug_code.desc())

    bugs = query.all()

    # Generate CSV
    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(["Bug Code", "Status", "Priority", "Defect Clasification", "Defect Origin"])

    for bug in bugs:
        writer.writerow([bug.bug_code, bug.status, bug.priority, bug.defect_clasification, bug.defect_origin])

    output = si.getvalue()
    si.close()

    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=bugs_filtered_export.csv"}
    )


@app.route("/users", methods = ["GET"], endpoint="users")
def get_users():
    job_filter = request.args.get("job_title", default=None)
    sort_order = request.args.get("sort", default=None)

    query = User.query

    if job_filter:
        query = query.filter_by(job_title=job_filter)

    if sort_order == "asc":
        query = query.order_by(User.username.asc())
    elif sort_order =="desc":
        query = query.order_by(User.username.desc())


    users = query.all()
    all_job_titles = db.session.query(User.job_title).distinct().all()
    job_titles = [jt[0] for jt in all_job_titles]

    return render_template("users.html", users=users, job_titles = job_titles)

@app.route("/users/add", methods=["GET", "POST"])
def add_users():
    if request.method == "POST":
        username = request.form["username"]
        email_address = request.form["email_address"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        job_title = request.form["job_title"]

            # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            users = User.query.all()
            error = f"Username '{username}' is already in database."
            return render_template("users.html", users=users, error=error)

        new_user = User(
            first_name=first_name, 
            last_name=last_name, 
            job_title=job_title, 
            username=username, 
            email_address=email_address)
        
        db.session.add(new_user)
        db.session.commit()
        users = User.query.all()
        return render_template("users.html", users = users)
    

@app.route("/users/update", methods=["GET", "POST"])
def update_users():
    if request.method == "POST":
        username = request.form.get("username")

            # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if not existing_user:
            users = User.query.all()
            error = f"Username '{username}' cannot be found in database."
            return render_template("users.html", users=users, error=error, active_tab="Update User")
        
        email_address = request.form.get("email_address")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        job_title = request.form.get("job_title")

        if email_address:
            existing_user.email_address = email_address
        if first_name:
            existing_user.first_name = first_name
        if last_name:
            existing_user.last_name = last_name
        if job_title:
            existing_user.job_title = job_title
        
        db.session.commit()

        success_message = f"Username {username} has been updated."
        users = User.query.all()
        return render_template("users.html", users=users, success_message=success_message ,active_tab="Update User")


@app.route("/users/delete", methods=["GET", "POST"])
def delete_users():
    if request.method == "POST":
        username = request.form.get("username")

        if not username:
            users = User.query.all()
            error = "Please enter an username."
            return render_template("users.html", users=users, error=error, active_tab="Delete User")

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            db.session.delete(existing_user)
            db.session.commit()
            users = User.query.all()
            success_message = f"Username '{username}' has been successfully deleted."
            return render_template("users.html", users=users, success_message=success_message)
        else:
            users = User.query.all()
            error = f"Username '{username}' was not found in the database."
            return render_template("users.html", users=users, error=error, active_tab="Delete User")

    users = User.query.all()
    return render_template("users.html", users=users, active_tab="Delete User")



@app.route("/users/export", methods=["GET"])
def export_users():
    job_filter = request.args.get("job_title", default=None)
    sort_order = request.args.get("sort", default=None)

    query = User.query

    if job_filter:
        query = query.filter_by(job_title=job_filter)

    if sort_order == "asc":
        query = query.order_by(User.username.asc())
    elif sort_order == "desc":
        query = query.order_by(User.username.desc())

    users = query.all()

    # Generate CSV
    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(["Username", "Email", "First Name", "Last Name", "Job Title"])

    for user in users:
        writer.writerow([user.username, user.email_address, user.first_name, user.last_name, user.job_title])

    output = si.getvalue()
    si.close()

    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=users_filtered_export.csv"}
    )

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug = True)
