from flask import Flask, render_template

'''
Dynamic Routes:
    1. A variable in the route<variable>
    2. A parameter passed in to the function

eg:
@app.route('/page/<name>')
def pageMethod(name):
    -------
    -------
    -------
    return ...;
'''

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    movies = ["Rio", "Harrypotter", "matrix", "Avenger"]
    is_logged_in = True
    return render_template('index.html', movies = movies, is_logged_in= is_logged_in)

@app.route('/about')
def about():
    return '<h3>About Me</h3>'

@app.route('/contact')
def contact():
    return '<h3>Contact</h3><p>Emailid@gmail.com</p><p>xxxxxxxxxx</p>'

# dinamic routing

@app.route('/users/<name>')
def users(name):
    # return "<h3>Welcome {}</h3>".format(name.capitalize())
    fruits = ["apple", "orange", "pineapple"]
    profile = {'name' : 'johnWick', 'age' : 25, 'city' : 'mexico'}
    return render_template("users.html", user_name=name, Fruit=fruits, profile = profile)

if __name__ == '__main__':
    app.run(debug=True)
