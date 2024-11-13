from datetime import datetime

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_food.db'
db = SQLAlchemy(app)


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_food = db.Column(db.String(30), nullable=False)
    category = db.Column(db.Integer, nullable=False)
    weight_gr = db.Column(db.Integer)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    ingredients = db.Column(db.Text)
    image = db.Column(db.String(30))
    time_create = db.Column(db.DateTime)
    time_update = db.Column(db.DateTime)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    full_name = db.Column(db.String(120))
    time_create = db.Column(db.DateTime)
    time_update = db.Column(db.DateTime)


@app.route('/base/')
@app.route('/')
def base():
    return render_template('base.html')


@app.route('/menu/')
def menu():
    return render_template('menu.html')


@app.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        user = User(username=username
                    , password=password
                    , email=email
                    , full_name=username
                    , time_create=datetime.now()
                    , time_update=datetime.now())

        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except:
            return "При добавлении статьи произошла ошибка"
    else:
        return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)




# pip install flask_sqlalchemy
# в python консоли
# from app import app, db
# app.app_context().push()
# db.create_all()




