from flask import Flask, render_template
import requests
import random
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("/index.html", num=random_number, year=current_year)  # Jinja 

@app.route('/guess/<name>')
def guess(name):
    # Using request to the APIs
    response_gender = requests.get(f"https://api.genderize.io/?name={name}")
    response_age = requests.get(f"https://api.agify.io/?name={name}")
    # Get the json dict
    genderize = response_gender.json() 
    agefy = response_age.json() 
    return render_template("/guess.html", name=name, gender=genderize["gender"], age=agefy["age"])

@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/6f77a7ecbd432c3a3e0d"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

