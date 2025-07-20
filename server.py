from flask import Flask, render_template
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


if __name__ == '__main__':
    app.run(debug=True)