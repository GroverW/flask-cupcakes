"""Flask app for Cupcakes"""
from flask import Flask, request
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


app.config['SECRET_KEY'] = 'apoisdhfpaiosdhfpioasd'

@app.route('/api/cupcakes')
def get_cupcakes():
    cupcakes = Cupcake.query.all()

    