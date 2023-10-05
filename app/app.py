
from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from models import db_instance, Hero, Power, HeroPower
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db_instance)

db_instance.init_app(app)

@app.route('/')
def home():
    return 'Welcome to my app'

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    hero_list = []
    for hero_instance in heroes:
        hero_list.append({
            'id': hero_instance.id,
            'name': hero_instance.name,
            'super_name': hero_instance.super_name,
        })
    return jsonify(hero_list)

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero is None:
        return make_response(jsonify({'error': 'Hero not found'}), 404)

    powers = []
    for power_instance in hero.powers:
        powers.append({
            'id': power_instance.id,
            'name': power_instance.name,
            'description': power_instance.description
        })

    hero_data = {
        'id': hero.id,
        'name': hero.name,
        'super_name': hero.super_name,
        'powers': powers
    }
    return jsonify(hero_data)

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    power_list = []
    for power_instance in powers:
        power_list.append({
            'id': power_instance.id,
            'name': power_instance.name,
            'description': power_instance.description
        })
    return jsonify(power_list)

@app.route('/powers/', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power is None:
        return make_response(jsonify({'error': 'Power not found'}), 404)
    power_data = {
        'id': power.id,
        'name': power.name,
        'description': power.description
    }
    return jsonify(power_data)

@app.route('/powers/', methods=['PATCH'])
def update_power(id):
    power_instance = Power.query.get(id)
    if power_instance is None:
        return make_response(jsonify({'error': 'Power not found'}), 404)

    try:
        data = request.get_json()
        if 'description' in data:
            power_instance.description = data['description']
            db.session.commit()
            return jsonify({
                'id': power_instance.id,
                'name': power_instance.name,
                'description': power_instance.description
            })
        else:
            return make_response(jsonify({'errors': ['validation errors']}), 400)
    except Exception as e:
        return make_response(jsonify({'errors': ['validation errors']}), 400)
