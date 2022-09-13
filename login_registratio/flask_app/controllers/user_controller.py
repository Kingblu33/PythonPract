from flask import render_template, redirect, session, request
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask import flash
bcrypt = Bcrypt(app)


@app.route('/')
def default():

    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    if not User.validate(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    query_data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : pw_hash,
        }

    userid=User.save(query_data)
    print(userid)
        
    session['userid']= userid

    return redirect('/showuser')

@app.route('/showuser')
def neewp():
    return render_template('showuser.html')

@app.route('/login/page',methods=['post'])
def beep():
    data = { 
        "email" : request.form["email"] 
        }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/showuser")
    

@app.route('/login')
def sheep():

    return render_template('login.html')

