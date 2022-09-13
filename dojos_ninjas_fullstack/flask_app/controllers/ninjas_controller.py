from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninjas_models import Ninja
from flask_app.controllers.dojos_controller import Dojo

@app.route ('/ninjas')
def display():
    dojos=Dojo.alldojos()
    return render_template('ninjas.html',dojos=dojos)


@app.route('/newninja', methods=["POST"])
def ninja():

    Ninja.insertninja(request.form)
    # 3 - redirect elsewhere once query is done
    return redirect('/dojo')
