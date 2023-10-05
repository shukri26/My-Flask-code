from app import app, db_instance, Hero, Power, HeroPower
import random

app_ctx = app.app_context()
app_ctx.push()

with app.app_context():
    Hero.query.delete()
    Power.query.delete()
    HeroPower.query.delete()

    # db.create_all()

heroes = [
"spider man",
"ant man",
'Wolverine',
'Legion'
]
supernames = [
'BAT Man',
'Green Lantern',
'Iron Man',
'Captain America'

]
mighty_heroes = []
for h in range(4):
    place_heroes = Hero(name=heroes[h], super_name=supernames[h])
    mighty_heroes.append(place_heroes)
    db_instance.session.add_all(mighty_heroes)
    db_instance.session.commit()

powers = [
    'LEGITIMATE',
    'EXPERT',
    'REWARD',
    'REFERENT'

]
description_powers =[
    'being in accordace with law some common legitimate are lawful,legal',
    'having great knowledge and experience in a trade or profession',
    'a thing given in recognition of service, or ahievements',
    'a person or thing to which a name logistics or other symbol'

]

mighty_powers = []
for a in range(4):
    place_powers = Power(name=powers[a], description=description_powers[a])
    mighty_powers.append(place_powers)
    db_instance.session.add_all(mighty_powers)
    db_instance.session.commit()

hero_power = []
for x in  range(4):

    place_heroes = HeroPower(strength=random.choice(['powerful', 'very_powerful', 'mid']), hero_id=random.randint(1, len(mighty_heroes)),  power_id=random.randint(1, len(mighty_powers)))
    hero_power.append(place_heroes)

    db_instance.session.add_all(hero_power)
    db_instance.session.commit()

# powers = [
#     {"name": "super strength", "description": "gives the wielder super-human strengths"},
#     {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"}
# ]

# for power_data in powers:
#     power = Power(**power_data)
#     db.session.add(power)

# hero_powers = [
#     {"strength": "Strong", "hero_id": 1, "power_id": 1},
#     {"strength": "Weak", "hero_id": 1, "power_id": 2},
#     {"strength": "Average", "hero_id": 2, "power_id": 1},
# ]

# for hero_power_data in hero_powers:
#     # hero_power = from app import app, db, Hero, Power, HeroPower

# app_context = app.app_context()
# app_context.push()

# with app.app_context():
#     db.create_all()

# heroes_data = [
#     {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
#     {"name": "Doreen Green", "super_name": "Squirrel Girl"},
#     {"name": "Gwen Stacy", "super_name": "Spider-Gwen"}
# ]

# for hero_data in heroes_data:
#     hero_instance = Hero(**hero_data)
#     db.session.add(hero_instance)

# powers_data = [
#     {"name": "super strength", "description": "gives the wielder super-human strengths"},
#     {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"}
# ]

# for power_data in powers_data:
#     power_instance = Power(**power_data)
#     db.session.add(power_instance)

# hero_powers_data = [
#     {"strength": "Strong", "hero_id": 1, "power_id": 1},
#     {"strength": "Weak", "hero_id": 1, "power_id": 2},
#     {"strength": "Average", "hero_id": 2, "power_id": 1},
# ]

# for hero_power_data in hero_powers_data:
#     hero_power_instance = HeroPower(**hero_power_data)
#     db.session.add(hero_power_instance)

# db.session.commit()

# app_context.pop()

# print("Database seeded successfully!")
# HeroPower(**hero_power_data)
#     db.session.add(hero_power)

# db.session.commit()

# app_ctx.pop()

# print("Database seeded successfully!")
