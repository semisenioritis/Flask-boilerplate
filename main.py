from flask import Flask, render_template, redirect, url_for, request, session
# from datetime import timedelta
# for extending the number of days a user stays logged in

app = Flask(__name__)
app.secret_key= "hello"
# app.permanent_session_lifetime = timedelta(minutes=5)
# for extending the number of days a user stays logged in to five minutes total

@app.route('/')
def main_func():
    return render_template("index.html",var_to_insert="this is a flask variable")
    # funtion to demo dynamicity of the flask html template


@app.route('/form', methods=["POST", "GET"])
def form_func():
    if request.method == "POST":
        # this is triggered as soon as the form submit button is clicked. the data is sent via the post
        # request and then is processed. After the processing the user is redirected to wherever we want to.
        input1 = request.form["nm"]

        return redirect(url_for("displ", input1=input1))
        # else redirect to wherever you want to after processing the data.
    elif request.method == "GET":
        return render_template("form.html")
        # this is the default page that will be rendered on initial load

@app.route("/<input1>")
def displ(input1):
    # this fucntion just a sample function to display the data from the post made from the client to the server in the above POST.
    return f"<h1>{input1}</h1>"


@app.route('/forifinhtml')
def in_html_func():
    content=["tim", "joe", "rob"]
    return render_template("forifinhtml.html", content=content)
    # function route to demo for/if/ etc loops in the html. ie write python code in the html itself

@app.route('/base')
def template_demo_func():
    return render_template("base_user.html")
    # function to demo creating and using a base template and then inheriting it in other templates

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # session.permanent = True
        # <--- makes the permanent session
        # this is the line that ensures that the time limit mentioned above is followed
        user = request.form["nm"]
        session['user']=user
        # session is a dictionary that stores the details of the current user inlcuding the email and the username etc etc
        return redirect(url_for("user"))
        # once you actually login correctly this is what renders after the POST action.
    else:
        if "user" in session:
            return redirect(url_for("user"))
            # if the user is already logged in but tries to acess the login page this redirects them to their so called "profile" page
        return render_template("login.html")
        # the first thing that gets rendered in this system. this page is the landing page for the login system

@app.route("/user")
def user():
    if "user" in session:
        user=session['user']
        return f"<h1>{user}</h1>"
        # the profile page of the individual user
    else:
        return redirect(url_for("login"))
        # if the user login is not valid at the current moment, rediret him to the login page

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
    # the url to log the user out









if __name__=="__main__":
    app.run(debug=True)