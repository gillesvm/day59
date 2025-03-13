from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_posts = requests.get("https://api.npoint.io/8095b19b769a4b014a69").json()

@app.route('/')
def home():
    return render_template("index.html", blog=blog_posts)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post/<id>')
def get_post(id):
    adjusted_id = int(id) -1
    post = blog_posts[adjusted_id]
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)