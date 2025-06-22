import os
import random
from dotenv import load_dotenv
load_dotenv()
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, render_template

from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Flask app
app = Flask(__name__)

# Build path to cafes.db
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# SQLAlchemy setup
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# MAIN ROUTE - Serve the cafe explorer page
@app.route("/")
def cafe_explorer():

    return render_template("cafe_explorer.html")


# SEARCH ROUTE - Serve the search results page
@app.route('/search')
def search_page():
    return render_template("search_results.html")


# API Routes
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    if all_cafes:
        random_cafe = random.choice(all_cafes)
        return jsonify(cafe=random_cafe.to_dict())
    else:
        return jsonify(error="No cafes found"), 404


@app.route('/all', methods=['GET'])
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


# SEARCH API - This returns JSON data for the search results page
@app.route('/search-api')
def search_cafes_api():
    query_location = request.args.get("loc")

    if not query_location:
        return jsonify(error="Missing query parameter ?loc="), 400

    # Use LIKE for partial matching instead of exact match
    result = db.session.execute(
        db.select(Cafe).where(Cafe.location.like(f'%{query_location}%'))
    )
    all_cafes = result.scalars().all()

    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(cafes=[])  # Return empty array instead of error
@app.route("/form.html")
def show_add_cafe_form():
    return render_template("form.html")

# Add this new route to your existing Flask code
@app.route("/cafe/<name>")
def show_cafe_details(name):
    cafe = db.session.execute(
        db.select(Cafe).where(Cafe.name == name.replace("-", " "))
    ).scalar_one_or_none()

    if cafe:
        return render_template("cafe_detail.html", cafe=cafe)
    return "Cafe not found", 404


# Add or Edit Cafe
@app.route("/add", methods=["POST"])
def add_or_edit_cafe():
    data = request.get_json()
    cafe_name = data.get("name")
    existing_cafe = db.session.execute(db.select(Cafe).where(Cafe.name == cafe_name)).scalar_one_or_none()

    if existing_cafe:
        # Update existing cafe
        try:
            existing_cafe.map_url = data.get("map_url")
            existing_cafe.img_url = data.get("img_url")
            existing_cafe.location = data.get("location")
            existing_cafe.seats = data.get("seats")
            existing_cafe.has_toilet = bool(data.get("has_toilet"))
            existing_cafe.has_wifi = bool(data.get("has_wifi"))
            existing_cafe.has_sockets = bool(data.get("has_sockets"))
            existing_cafe.can_take_calls = bool(data.get("can_take_calls"))
            existing_cafe.coffee_price = data.get("coffee_price")
            db.session.commit()
            return jsonify(response={"success": "Cafe updated successfully."}), 200
        except Exception as e:
            return jsonify(error=str(e)), 400
    else:
        # Add new cafe
        try:
            new_cafe = Cafe(
                name=cafe_name,
                map_url=data.get("map_url"),
                img_url=data.get("img_url"),
                location=data.get("location"),
                seats=data.get("seats"),
                has_toilet=bool(data.get("has_toilet")),
                has_wifi=bool(data.get("has_wifi")),
                has_sockets=bool(data.get("has_sockets")),
                can_take_calls=bool(data.get("can_take_calls")),
                coffee_price=data.get("coffee_price")
            )
            db.session.add(new_cafe)
            db.session.commit()
            return jsonify(response={"success": "Cafe added successfully."}), 201
        except Exception as e:
            return jsonify(error=str(e)), 400


@app.route("/delete", methods=["DELETE"])
def delete_cafe():
    cafe_name = request.args.get("name")
    cafe = db.session.execute(db.select(Cafe).where(Cafe.name == cafe_name)).scalar_one_or_none()

    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": f"Cafe '{cafe_name}' deleted permanently."}), 200
    else:
        return jsonify(error={"Not Found": "Cafe not found."}), 404


@app.route("/update/<int:cafe_id>", methods=["PATCH"])
def update_cafe(cafe_id):
    cafe_to_update = db.get_or_404(Cafe, cafe_id)

    if request.form.get("coffee_price"):
        cafe_to_update.coffee_price = request.form.get("coffee_price")

    if request.form.get("name"):
        cafe_to_update.name = request.form.get("name")

    db.session.commit()
    return jsonify(response={"success": f"Cafe ID {cafe_id} updated."}), 200


# Form routes (keep your existing ones)
@app.route("/add-cafe-form")
def add_cafe_form():
    return render_template("search_results.html")


# App runner
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
