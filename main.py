from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True

header = """
        <!DOCTYPE html>
            <html>
                <head>
                    <title>User Signup</title>
                </head>
                <body>
        """
footer = """
                </body>
            </html>
        """

@app.route("/welcome", methods=["POST"])
def display_welcome():
    username = request.form["username"]
    content = header + "<p>Welcome, " + username + "!</p>" + footer
    
    return content

@app.route("/")
def index():

    content = header + """        
            <h1>Signup</h1>
                <form action = "/welcome" method="post">
                    <table>
                        <tr>
                            <td><label for="username">Username</label></td>
                            <td>
                                <input name="username" type="text" value="">
                                <span class="error"></span>
                            </td>
                        </tr>
                        <tr>
                            <td><label for="password">Password</label></td>
                            <td>
                                <input name="password" type="password">
                                <span class="error"></span>
                            </td>
                        </tr>
                        <tr>
                            <td><label for="verify">Verify Password</label></td>
                            <td>
                                <input name="verify" type="password">
                                <span class="error"></span>
                            </td>
                        </tr>
                        <tr>
                            <td><label for="email">Email (optional)</label></td>
                            <td>
                                <input name="email" type= "text" value="">
                                <span class="error"></span>
                            </td>
                        </tr>
                    </table>
                    <input type="submit">
                </form>
        """ + footer
    return content

app.run()
