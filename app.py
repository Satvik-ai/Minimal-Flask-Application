#Simple web applications using python based framework (FLASK). It's not a fullstack application. It just has frontend and middle application layer.
#It accepts user's name as input and then greets them by calling there name.
from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method == "GET":
        return render_template("get_details.html")
    elif request.method == "POST":
        username = request.form["user_name"]
        return render_template("display_details.html", display_name=username)
    else:
        print("Error Check")


if __name__ == '__main__':
    app.debug=True
    app.run()

 