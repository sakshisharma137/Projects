from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}
tasks = {}

# ---------------- Home ----------------
@app.route("/")
def index():
    return redirect(url_for("register"))


# ---------------- Register ----------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm"]

        if password != confirm:
            return "Passwords do not match!"

        if username in users:
            return "Username already exists!"

        users[username] = {
            "fullname": fullname,
            "email": email,
            "password": password
        }

        tasks[username] = []

        return redirect(url_for("login"))

    return render_template("register.html")


# ---------------- Login ----------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            return redirect(url_for("home", username=username))

        return "Invalid Username or Password!"

    return render_template("login.html")


# ---------------- Home ----------------
@app.route("/home/<username>", methods=["GET", "POST"])
def home(username):

    if username not in tasks:
        tasks[username] = []

    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]

        task = {
            "title": title,
            "description": description
        }

        tasks[username].append(task)

    return render_template(
        "home.html",
        username=username,
        task_list=tasks[username]
    )


# ---------------- Update Password ----------------
@app.route("/update-password/<username>", methods=["GET", "POST"])
def update_password(username):

    if username not in users:
        return "User not found!"

    if request.method == "POST":
        old_password = request.form["old_password"]
        new_password = request.form["new_password"]
        confirm_password = request.form["confirm_password"]

        if users[username]["password"] != old_password:
            return "Old Password is Incorrect!"

        if new_password != confirm_password:
            return "New Passwords do not match!"

        users[username]["password"] = new_password

        return redirect(url_for("home", username=username))

    return render_template("update_password.html", username=username)


# ---------------- Delete Account ----------------
@app.route("/delete-account/<username>", methods=["GET", "POST"])
def delete_account(username):

    if request.method == "POST":

        if username in users:
            del users[username]

        if username in tasks:
            del tasks[username]

        return redirect(url_for("login"))

    return render_template("delete_account.html", username=username)


# ---------------- Logout ----------------
@app.route("/logout")
def logout():
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
















# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# users = {}
# tasks = {}

# @app.route("/")
# def index():
#     return redirect(url_for("register"))


# # ---------------- Home ----------------
# @app.route("/home/<username>", methods=["GET", "POST"])
# def home(username):

#     # Create task list if it doesn't exist
#     if username not in tasks:
#         tasks[username] = []

#     if request.method == "POST":
#         title = request.form["title"]
#         description = request.form["description"]

#         task = {
#             "title": title,
#             "description": description
#         }

#         tasks[username].append(task)

#     return render_template(
#         "home.html",
#         username=username,
#         task_list=tasks[username]
#     )


# # ---------------- Register ----------------
# @app.route("/register", methods=["GET", "POST"])
# def register():

#     if request.method == "POST":
#         fullname = request.form["fullname"]
#         email = request.form["email"]
#         username = request.form["username"]
#         password = request.form["password"]
#         confirm = request.form["confirm"]

#         if password != confirm:
#             return "Passwords do not match!"

#         if username in users:
#             return "Username already exists!"

#         users[username] = {
#             "fullname": fullname,
#             "email": email,
#             "password": password
#         }

#         # Create an empty task list for this user
#         tasks[username] = []

#         return redirect(url_for("login"))

#     return render_template("register.html")


# # ---------------- Login ----------------
# @app.route("/login", methods=["GET", "POST"])
# def login():

#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         if username in users and users[username]["password"] == password:
#             return redirect(url_for("home", username=username))

#         return "Invalid Username or Password!"

#     return render_template("login.html")

# # ---------------- Update Password ----------------
# @app.route("/update-password/<username>", methods=["GET", "POST"])
# def update_password(username):

#     if request.method == "POST":
#         old_password = request.form["old_password"]
#         new_password = request.form["new_password"]
#         confirm_password = request.form["confirm_password"]

#         if users[username]["password"] != old_password:
#             return "Old Password is Incorrect!"

#         if new_password != confirm_password:
#             return "New Passwords do not match!"

#         users[username]["password"] = new_password

#         return redirect(url_for("home", username=username))

#     return render_template("update_password.html", username=username)
    


# if __name__ == "__main__":
#     app.run(debug=True)



























# # from flask import Flask, render_template, request, redirect, url_for

# # app= Flask(__name__)

# # users = {}
# # tasks = {}

# # @app.route("/home/<username>", methods=["GET", "POST"])
# # def home(username):

# #     if request.method == "POST":
# #         title = request.form["title"]
# #         description = request.form["description"]

# #         task = {
# #             "title": title,
# #             "description": description
# #         }

# #         tasks[username].append(task)

# #     return render_template(
# #         "home.html",
# #         username=username,
# #         task_list=tasks[username]
# #     )


# # @app.route("/register", methods=["GET", "POST"])
# # def register():
# #     if request.method == "POST":
# #         fullname = request.form["fullname"]
# #         email = request.form["email"]
# #         username = request.form["username"]
# #         password = request.form["password"]
# #         confirm = request.form["confirm"]

# #         if password != confirm:
# #             return "Passwords do not match!"

# #         users[username] = {
# #             "fullname": fullname,
# #             "email": email,
# #             "password": password
# #         }

# #         return redirect(url_for("login"))
# #     return render_template("register.html")    

# # @app.route("/login", methods=["GET", "POST"])
# # def login():
# #     if request.method == "POST":
# #         username = request.form["username"]
# #         password = request.form["password"]

# #         if username in users:
# #             if users[username]["password"] == password:
# #                 return redirect(url_for("home", username=username))

# #         return "Invalid Username or Password!"
# #     return render_template("login.html")        

# # if __name__== "__main__":
# #     app.run(debug=True, use_reloader=True)