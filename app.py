# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Neelaksh Mishra" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    name_father = "Nagendra prasad" # write your name
    age_father = "48" # write your age

    return render_template('father.html' , name = name_father , age = age_father)

# define the route to mother webpage
@app.route("/mother")
def mother():
    name_mother = "Nidhi Mishra" # write your name
    age_mother = "39" # write your age

    return render_template('mother.html' , name = name_mother , age = age_mother)

# define the route to friends webpage
@app.route("/friends")
def friend():
    name_friend = "Anikt p.n" # write your name
    age_frind = "17" # write your age

    return render_template('friend.html' , name = name_friend , age = age_frind)
# add other routes, if you want

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
