"""Flask app for adopt app."""

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()


# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get("/")
def display_homepage():
    """Display homepage with all pets"""

    pets = Pet.query.all()
    return render_template("homepage.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add pet form; handle displaying and processing form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()

        print(pet)

        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)


@app.route("/<int:id>", methods=["GET", "POST"])
def edit_pet_and_display(id):
    """
    GET: Display pet detail page
   
    POST: Handle the form processing to edit
    
    """

    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available

        # db.session.add(pet)
        db.session.commit()

        print(pet)

        return redirect(f"/{pet.id}")
    else:
        return render_template("display_and_edit_pet.html", form=form, pet=pet)
