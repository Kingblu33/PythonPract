from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.models.user_model import User
from flask import flash
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app) 



@app.route('/')
def defaultroute():


    return render_template('index.html')


@app.route('/dashboard')
def dash():
    data={
    "id": session["userid"]
    }
    
    # user = User.idek(data)
    food=User.join(data)
    print(food)
    
    return render_template('dashboard.html',food=food)


#===============================================================
# register route
#===============================================================
@app.route('/register', methods=["POST"])
def regis():
    if not User.validate_info(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print("pw_hash")
    query_data={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "password":pw_hash,
    }

    userid=User.save_new_user(query_data)
    session['userid']= userid
    return redirect('/dashboard')

#===============================================================
# login route
#===============================================================
@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.login(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['userid'] = user_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")


