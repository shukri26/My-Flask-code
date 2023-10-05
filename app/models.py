from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates

db_instance = SQLAlchemy()

class Hero(db_instance.Model):
    __tablename__ = 'heroes'

    id = db_instance.Column(db_instance.Integer, primary_key=True)
    name = db_instance.Column(db_instance.String)
    super_name = db_instance.Column(db_instance.String)

    creation_time = db_instance.Column(db_instance.DateTime, default=db_instance.func.current_timestamp(), nullable=False)
    modification_time = db_instance.Column(db_instance.DateTime, default=db_instance.func.current_timestamp(), onupdate=db_instance.func.current_timestamp(), nullable=False)

    powers = db_instance.relationship('Power', secondary='hero_powers', back_populates='heroes')

class Power(db_instance.Model):
    __tablename__ = 'powers'

    id = db_instance.Column(db_instance.Integer, primary_key=True)
    name = db_instance.Column(db_instance.String(255), nullable=False)
    description = db_instance.Column(db_instance.String(255), nullable=False)
    creation_time = db_instance.Column(db_instance.DateTime, default=db_instance.func.current_timestamp(), nullable=False)
    modification_time= db_instance.Column(db_instance.DateTime, default=db_instance.func.current_timestamp(), onupdate=db_instance.func.current_timestamp(), nullable=False)

    heroes = db_instance.relationship('Hero', secondary='hero_powers', back_populates='powers')

    @db_instance.validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return description

class HeroPower(db_instance.Model):
    __tablename__ = 'hero_powers'

    id = db_instance.Column(db_instance.Integer, primary_key=True)
    strength = db_instance.Column(db_instance.String(255), CheckConstraint("strength IN ('Strong', 'Weak', 'Average')"), nullable=False)
    hero_id = db_instance.Column(db_instance.Integer, db_instance.ForeignKey('heroes.id'), nullable=False)
    power_id = db_instance.Column(db_instance.Integer, db_instance.ForeignKey('powers.id'), nullable=False)
    creation_time = db_instance.Column(db_instance.DateTime, default=db_instance.func.current_timestamp(), nullable=False)
    modification_time = db_instance.Column(db_instance.DateTime, default=db_instance.func.current_timestamp(), onupdate=db_instance.func.current_timestamp(), nullable=False)
