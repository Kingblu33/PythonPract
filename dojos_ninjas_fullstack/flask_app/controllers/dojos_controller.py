from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojos_models import Dojo
from flask_app.models.ninjas_models import Ninja

@app.route('/')
def default():
    return  redirect('/dojo')

@app.route('/dojo')
def dojo():
    dojos=Dojo.alldojos()
    print(dojos)
    return render_template("dojos.html",dojos=dojos)

@app.route('/dojo/newdojo',methods=['POST'])
def newdojo():
    data= {
            "name" : request.form['name']
        }
    Dojo.savedojo(data)
    return redirect ('/dojo')

@app.route('/dojos/showall/<int:id>')
def showall(id):
    data={
        "id" : id 
    }

    return render_template('showall.html',dojo=Dojo.get_ninjas_with_dojos(data))