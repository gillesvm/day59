from flask import Flask, render_template, request
import requests
import smtplib

my_email= "gilles.vanmarcke@gmail.com"
password = REDACTED
app = Flask(__name__)

blog_posts = requests.get("https://api.npoint.io/8095b19b769a4b014a69").json()

##code from day 60 below
"""
@app.route('/')
def home():
    return render_template("index.html")
@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"
"""

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == 'POST':
        data = request.form
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="gillesvanmarcke.100daysofcode@gmail.com",
                msg=f"Subject:Contact form\n\n"
                    f"Name: {data['name']}\n"
                    f"email: {data['email']}\n"
                    f"phone: {data['phone']}\n"
                    f"message: {data['message']}\n"
            )
        return render_template("contact.html", method="post")
    else:
        return render_template("contact.html", method="get")


##Code from day 59 below

@app.route('/')
def home():
    return render_template("index.html", blog=blog_posts)

# @app.route('/contact')
# def contact():
#     return render_template("contact.html")

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