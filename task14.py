from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task11 import User


app = Flask(__name__)

engine = create_engine('sqlite:///mars_explorer.db')
Session = sessionmaker(bind=engine)


@app.route('/')
def registration_form():
    return render_template('task14.html')


@app.route('/register', methods=['POST'])
def register():
    session = Session()
    if request.method == 'POST':
        surname = request.form['surname']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        speciality = request.form['speciality']
        address = request.form['address']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return "Passwords do not match"

        new_user = User(surname=surname, name=name, age=age, position=position, speciality=speciality,
                        address=address, email=email, hashed_password=password, modified_date=datetime.now())

        session.add(new_user)
        session.commit()
        session.close()

        return redirect(url_for('registration_success'))
    else:
        return redirect(url_for('registration_form'))


@app.route('/registration_success')
def registration_success():
    return "Registration successful!"


if __name__ == '__main__':
    app.run(debug=True)
