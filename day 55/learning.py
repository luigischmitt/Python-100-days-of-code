from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# ----------- Creating Decorators -----------

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

# -------------------------------------------

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "<p>Bye, Bye!</p>"

@app.route("/user/<username>/<number>")
def user(username, number):
    return f"<h1 style='text-align: center'>Hello, {username}! You're {number} years old!</h1>"


if __name__ == "__main__":
    app.run(debug=True)


