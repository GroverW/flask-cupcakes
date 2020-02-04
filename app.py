"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake
from serializer import serialize_cupcake

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
    serialized = [Cupcake.serialize(c) for c in cupcakes]

    return (jsonify(cupcakes=serialized), 200)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get(id)

    if cupcake:
        serialized = Cupcake.serialize(cupcake)
        return (jsonify(cupcake=serialized), 200)
    else:
        return (jsonify(error="Cupcake doesn't exist."), 404)


@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    print("****************** IN POST ********", request.json)
    flavor = request.json.get('flavor')
    size = request.json.get('size')
    rating = request.json.get('rating')
    image = request.json.get('image') or None


    new_cupcake = Cupcake(
                        flavor=flavor,
                        size=size,
                        rating=rating,
                        image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = Cupcake.serialize(new_cupcake)

    return (jsonify(cupcake=serialized), 201)


@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor')
    cupcake.size = request.json.get('size')
    cupcake.rating = request.json.get('rating')
    cupcake.image = request.json.get('image') or "https://tinyurl.com/demo-cupcake"

    db.session.commit()

    serialized = Cupcake.serialize(cupcake)

    return (jsonify(cupcake=serialized), 200)


@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return (jsonify(message="Deleted"), 200)


@app.route('/')
def get_home_html():
    return render_template("index.html")
