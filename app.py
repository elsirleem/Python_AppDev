from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["secret_key"] = "mysecretkey000"
app.config["MAIL_PASSWORD"] = "rjgihzxihalgmpys"
app.config["MAIL_USERNAME"] = "lawalsalimk@gmail.com"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True

db = SQLAlchemy(app)
mail = Mail(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    date = db.Column(db.Date())
    occupation = db.Column(db.String(100))

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        date = request.form['date']
        date_obj = datetime.strptime(date, '%Y-%m-%d')  # convert string to date object
        occupation = request.form['occupation']

        form = Form(firstname=firstname, lastname=lastname, 
                    email=email, date=date_obj, occupation=occupation)
        
        db.session.add(form)
        db.session.commit()

        message_body = f"Hello {firstname}, your form has been submitted successfully"
        message = Message(subject="New Form Submission",
                          sender=app.config["MAIL_USERNAME"],
                          recipients=[email],
                          body=message_body)
        mail.send(message)

        # flash(f"{firstname}, Form submitted successfully", "success")

    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)

