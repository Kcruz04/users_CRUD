from flask import Flask, render_template, redirect, request;

from user import User
    
app = Flask(__name__)
            

@app.route("/")
def index():
    # call the get all classmethod to get all userss
    users = User.get_all()
    print(users)
    return render_template("read(all).html",users_from_controller=users)

# relevant code snippet from server.py
from user import User
#This takes the anchor tag to create a new user and returns creat.html
@app.route('/new_user')
def new_user():
    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the User class.
    User.save(data)
    #If values in html are same as in db we can use
    #@app.route('/friends/create', methods=['POST'])
    # def create_friend():
    #     Friend.save(request.form)
    #     return redirect('/')

    # Don't forget to redirect after saving to the database.
    return redirect('/')

#Recieves requests from client direct to  show, edit, or delete and pages
@app.route('/read(one)/<int:id>')
def read_one(id):
    users_from_controller = User.get_one(id)
    return render_template("read(one).html", users_from_controller = users_from_controller)

@app.route('/edit/<int:id>')
def edit_user(id):
    user = User.get_one(id)
    return render_template("edit.html", user = user)

@app.route('/update', methods = ["POST"])
def update():
    print(request.form)
    User.update(request.form)
    return redirect(f"/read(one)/{request.form['id']}")

@app.route('/delete/<int:id>')
def delete(id):
    print(id)
    User.delete(id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True, port = 5001)