from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User
@app.route('/default')
def defaultt():

    return render_template('newrecipe.html')

@app.route('/new',methods=["post"])
def newrec():
    if not Recipe.validate_recipe(request.form):
        return redirect('/default')
    query_data={
        "name":request.form["name"],
        "description":request.form["description"],
        "instructions":request.form["instructions"],
        "under_30":request.form["under_30"],
        "date_made":request.form["date_made"],
        "user_id":session["userid"],
    }
    print(session['userid'])
    
    Recipe.save(query_data)


    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def onlyone(id):
    query_data={
        "id" : id
    }
    data={
        "id": session["userid"]
    }
    user=User.getoneu(data)
    print(user)

    recipe=Recipe.get_one(query_data)
    return render_template('showone.html',recipe=recipe,user=user)

@app.route('/recipes/edit/<int:id>')

def editone(id):
    query_data= {
        "id": id
    }
    

    recipe= Recipe.get_one(query_data)

    return render_template('edit.html',recipe=recipe)



@app.route('/update/recipe/<int:id>',methods=['POST'])
def updateu(id):

    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/edit/{id}')
    data={
        "name":request.form["name"],
        "description":request.form["description"],
        "instructions":request.form["instructions"],
        "under_30":request.form["under_30"],
        "date_made":request.form["date_made"],
        "id": id

    }
    Recipe.update_recipe(data)
    print(data)

    return redirect('/dashboard')


@app.route('/delete/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')