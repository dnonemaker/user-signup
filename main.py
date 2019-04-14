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
    if username_arg == "":
        username_error_arg = "Username is required."
    if password_arg == "":
        password_error_arg = "Password is required."
    if verify_arg == "":
        verify_error_arg = "Password is required."

    # Validate -- #  username and pw must not contain a space character
    if " " in username_arg:
        username_error_arg = "Space in username not allowed."
    if " " in password_arg:
        password_error_arg = "Space in Password not allowed."
    if " " in verify_arg:
        verify_error_arg = "Space in Password not allowed."


    # Validate --   username and pw characters must be between 3 and 20 characters.
    if len(username_arg) < 3 or len(username_arg) > 20:
        username_error_arg = "Username must be between 3 and 20 characters."
    if len(password_arg) < 3 or len(password_arg) > 20:
        password_error_arg = "Password must be between 3 and 20 characters."
    if len(verify_arg) < 3 or len(verify_arg) > 20:
        verify_error_arg = "Password must be between 3 and 20 characters."

    # alidate -- The user's password and password-verify must match
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
        return redirect("/welcome?username={0}".format(username_arg))
    else:
        return render_template("home.html", username = username_arg, email=email_arg,username_error = username_error_arg,
            password_error=password_error_arg,verify_error=verify_error_arg,email_error=email_error_arg)

@app.route("/welcome")
def display_welcome():
    username_arg = request.args.get("username")

    return render_template("welcome.html",username=username_arg)

"""
@app.route("/")
def index():

    # Set error message variables to empty
    username_error_arg = ""
    password_error_arg = ""
    verify_error_arg = ""
    email_error_arg = ""
    # error_msg = cgi.escape(request.args.get("error"))

    
    if not username_error and not password_error and not password_validate_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('main.html', username_error=username_error, username=username, password_error=password_error, password=password, password_validate_error=password_validate_error, password_validate=password_validate, email_error=email_error, email=email)
    
    
    return render_template("home.html", username_error = username_error_arg,
        password_error=password_error_arg,verify_error=verify_error_arg,email_error=email_error_arg)
"""
# Error Handling


# For the username and email fields,
# you should preserve what the user typed,
# so they don't have to retype it.
# With the password fields, you should clear them, for security reasons.




app.run()
