from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from transactions import Transaction
from db import db, Base
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:1234@localhost:5433/mydb'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir,'app.db')
db.init_app(app)

@app.route("/")
def index():
    transactions = Transaction.query.all()
    return render_template("index.html", transactions = transactions)

@app.route("/transaction_create", methods=["POST", "GET"])
def transaction_create():

    tr = Transaction(
        description = request.form['description'],
        category = request.form["category"],
        amount = request.form["amount"] 
    )
    db.session.add(tr)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, host='0.0.0.0')
    print(Transaction.query.all())