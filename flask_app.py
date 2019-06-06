from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,
                                                                    'dbsqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
database = SQLAlchemy(app)
# Init ma
marshmallow = Marshmallow(app)


# Event Class/Model
class BicycleAccessories(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
    weight = database.Column(database.Float)
    manufacturer = database.Column(database.String)

    def __init__(self, name, weight, manufacturer):
        self.name = name
        self.weight = weight
        self.manufacturer = manufacturer


class BicycleAccessoriesSchema(marshmallow.Schema):
    class Meta:
        fields = ('name', 'weight', 'manufacturer')


bicycle_accessory_schema = BicycleAccessoriesSchema(strict=True)
bicycle_accessories_schema = BicycleAccessoriesSchema(many=True, strict=True)


@app.route('/accessory', methods=['POST'])
def add_bicycle_accessory():
    name = request.json['name']
    weight = request.json['weight']
    manufacturer = request.json['manufacturer']

    new_accessory = BicycleAccessories(name, weight, manufacturer)

    database.session.add(new_accessory)
    database.session.commit()

    return bicycle_accessory_schema.jsonify(new_accessory)


@app.route('/accessory', methods=['GET'])
def get_all_bicycle_accessories():
    all_accessories = BicycleAccessories.query.all()
    result = bicycle_accessories_schema.dump(all_accessories)
    return jsonify(result.data)


@app.route('/accessory/<id>', methods=['GET'])
def get_bicycle_accessory(id):
    accessory = BicycleAccessories.query.get(id)
    return bicycle_accessory_schema.jsonify(accessory)


@app.route('/accessory/<id>', methods=['PUT'])
def update_bicycle_accessory(id):
    accessory = BicycleAccessories.query.get(id)

    name = request.json["name"]
    weight = request.json["weight"]
    manufacturer = request.json["manufacturer"]

    accessory.name = name
    accessory.weight = weight
    accessory.manufacturer = manufacturer

    database.session.commit()

    return bicycle_accessory_schema.jsonify(accessory)


@app.route('/accessory/<id>', methods=['DELETE'])
def delete_accessory(id):
    accessory = BicycleAccessories.query.get(id)
    database.session.delete(accessory)
    database.session.commit()
    return bicycle_accessory_schema.jsonify(accessory)


# database.create_all()


if __name__ == '__main__':
    app.run(debug=True)
