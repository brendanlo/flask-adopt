from models import Pet, db
from app import app
# Create all tables

db.drop_all()
db.create_all()
# If table isn't empty, empty it
Pet.query.delete()

# Add Pets
crystal = Pet(
    name = "Crystal",
    species = "Goldfish",
    photo_url = 'https://cdn.britannica.com/12/117212-050-3267CED6/Goldfish-behaviour-water-temperature.jpg',
    age = "senior",
    notes = "Very friendly"
)

# Add new pets to session, so they'll persist
db.session.add(crystal)


# Commit--otherwise, this never gets saved!
db.session.commit()
