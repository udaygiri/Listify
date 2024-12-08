from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///listify.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Listify(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(200),  nullable=False)
    date = db.Column(db.DateTime, default=db.func.now())

@app.route("/")
def main():
    
    todos = Listify.query.all()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        if len(title) > 0 or len(desc) > 0:            
            todos = Listify(title=title, desc=desc)
            db.session.add(todos)
            db.session.commit()            

    return redirect("/")

@app.route('/delete/<int:sno>')
def delete_Todo(sno):
    try:
        todo = Listify.query.filter_by(sno=sno).first()
        db.session.delete(todo)
        db.session.commit()
    except:
        return "An error occurred while deleting the todo item."
    
    return redirect("/")

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update_todo(sno):
    todo = Listify.query.filter_by(sno=sno).first()
    
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        
        if len(title) > 0 or len(desc) > 0:
            todo.title = title
            todo.desc = desc
            db.session.commit()
            return redirect("/")
    
    return render_template('update.html', todo=todo)

@app.route('/about')    
def about_me():
    return render_template('aboutMe.html')

if __name__ == "__main__":
    app.run(debug=True)