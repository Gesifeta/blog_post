from flask import Flask, render_template
import json
app = Flask(__name__)

with open("blog.json") as f:
    posts = json.load(f)
@app.route('/')
def index():
    return render_template('index.html',posts=posts)

@app.route('/post/<int:id>')
def get_post(id):
    post = posts[id]
    return render_template("index.html",posts=[post],id=id, len = len(post))


if __name__ == '__main__':
    app.run(debug=True)