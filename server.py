from sys import exception
from flask import Flask, render_template, request
from  api import GMAIL_PASSWORD,GMAIL_USERNAME

import smtplib,os
import json
import datetime
app = Flask(__name__)
year = datetime.date.today().year

with open("blog.json") as f:
    posts = json.load(f)
@app.route('/')
def index():
    return render_template('index.html',posts=posts, year=year)

@app.route('/post/<int:id>')
def get_post(id):
    post = posts[id]
    return render_template("post.html",posts=[post],id=id, len = len(post),year=year)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact",methods=["GET","POST"])
def contact():
    return render_template("contact.html")


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        if request.form["email"] != "":
            try:
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=GMAIL_USERNAME,password= GMAIL_PASSWORD)
            except Exception as e:
                    return f"Login Failed: {e}"
            else:
                connection.sendmail(from_addr=GMAIL_USERNAME, to_addrs="adamgemechu@outlook.com",
                    msg=f"Subject:Blog Post\n\n{request.form['message']}")
                connection.quit()

    else:
        return render_template("contact.html")

@app.route("/posts")
def sample_blog_posts():
    return render_template("post.html")


if __name__ == '__main__':
    app.run(debug=True)