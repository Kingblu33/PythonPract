from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)   
app.secret_key='Bluebearasdadsa asdasd'


@app.route("/")  
def count(): 

    if 'visits' in session:
        session['visits']= session['visits'] + 1
    else:
        session['visits']= 1

    visits= session['visits']
    
    return render_template('index.html',visits=visits)


@app.route("/counter")
def counter():
    session['visits'] = session['visits'] + 1
    return redirect("/")

@app.route("/destroy")
def reset():
    session.clear()
    return redirect("/")



if __name__=="__main__":    
    app.run(debug=True)    

