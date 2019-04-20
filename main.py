from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

# This displays signup form
@app.route("/")
def display_signup():
    return render_template("home.html")

@app.route("/", methods=["POST"])
def process_user_signup():

    username_arg = request.form["username"]
    password_arg = request.form["password"]
    verify_arg = request.form["verify"]
    email_arg = request.form["email"]

    # Set error message variables to empty
    username_error_arg = ""
    password_error_arg= ""
    verify_error_arg = ""
    email_error_arg = ""

    # Validate -- Are username or pw fields blank?
     # Validate -- username and pw characters must be between 3 and 20 characters.
    if username_arg == "":
        username_error_arg = "Username is required."
    elif len(username_arg) < 3 or len(username_arg) > 20:
        username_error_arg = "Username must be between 3 and 20 characters."
    if password_arg == "":
        password_error_arg = "Password is required."
    elif len(password_arg) < 3 or len(password_arg) > 20:
        password_error_arg = "Password must be between 3 and 20 characters."
    if verify_arg == "":
        verify_error_arg = "Password is required."
    elif len(verify_arg) < 3 or len(verify_arg) > 20:
        verify_error_arg = "Password must be between 3 and 20 characters."

    # Validate -- #  username and pw must not contain a space character
    if " " in username_arg:
        username_error_arg = "Space in username not allowed."
    if " " in password_arg:
        password_error_arg = "Space in Password not allowed."
    if " " in verify_arg:
        verify_error_arg = "Space in Password not allowed."

    # Validate -- The user's password and password-verify must match
    if password_arg != verify_arg:
        password_error_arg = "Passwords must match."
        verify_error_arg = "Passwords must match."
    # Validate -- # The user provides an email, but it's not a valid email.
    # Note: the email field may be left empty, but if there is content in it,
    # then it must be validated. The criteria for a valid email address in this
    # assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
    if email_arg != "":
        if email_arg.count("@") == 0:
            email_error_arg = "Missing '@'"
        elif email_arg.count("@") > 1:
            email_error_arg = "Email may only contain one '@'"
        elif email_arg.count(".") == 0:
            email_error_arg = "Missing '.'"
        elif email_arg.count(".") > 1:
            email_error_arg = "Email may only contain one '.'"  
        elif " " in email_arg:
            email_error_arg = "Space not allowed."
        elif len(email_arg) < 3 or len(email_arg) > 20:
            email_error_arg = "Email must be between 3 and 20 characters."

    
    # Clear pw and verify fields
    password_arg = ""
    verify_arg = ""

    # If all error args are blank, render welcome page.
    if not username_error_arg and not password_error_arg and not verify_error_arg and not email_error_arg:
        return redirect("/welcome", code=307)
    else:
        return render_template("home.html", username = username_arg, email=email_arg,username_error = username_error_arg,
            password_error=password_error_arg,verify_error=verify_error_arg,email_error=email_error_arg)

@app.route("/welcome", methods=['POST'])
def display_welcome():
    username_arg =request.form['username']

    return render_template("welcome.html",username=username_arg)

app.run()
