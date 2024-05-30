from models import db, Pet
from app import app

db.drop_all()
db.create_all()


pet1 = Pet(
    name="Duck",
    species="dog",
    photo_url="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQgByBT5IiAT_a2x9pUVb4VMoOrlzHH7Jrzj-HB5jzHlR4lNLMS",
    age=1,
    notes="Very Good Boy",
    available=True,
)

pet2 = Pet(
    name="Moose",
    species="dog",
    age=3,
    notes="Very bad girl",
    available=True,
)

pet3 = Pet(
    name="Floofy",
    species="cat",
    photo_url="https://static.boredpanda.com/blog/wp-content/uploads/2015/12/fluffy-cats-funny-animal-pics-102__605.jpg",
    age=9,
    notes="Crazy cat",
    available=False,
)

pet4 = Pet(
    name="Spike",
    species="porcupine",
    photo_url="https://i.natgeofe.com/n/d0c2bc16-95be-4d1f-a1e4-322a0669a7f2/porcupines_thumb.JPG",
    age=29,
    notes="Tough to pet",
    available=True,
)


db.session.add_all([pet1, pet2, pet3, pet4])
db.session.commit()
