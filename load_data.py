import csv
from flask import Flask
from models import db, SalesDaily

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pharmacy.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():

    with open("salesdaily.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            sale = SalesDaily(
                datum=row["datum"],
                Anti_inflammatory_drugs=float(row["Anti-inflammatory drugs"]),
                Anti_inflammatory_derivatives=float(row["Anti-inflammatory derivatives"]),
                Salicylic_acid_analgesics=float(row["Salicylic acid analgesics"]),
                Paracetamol=float(row["Paracetamol"]),
                Anxiolytics_anti_anxiety_drugs=float(row["Anxiolytics (anti-anxiety drugs)"]),
                Sedatives_sleeping_pills=float(row["Sedatives / sleeping pills"]),
                Asthma_medicines=float(row["Asthma medicines"]),
                Antihistamines=float(row["Antihistamines"]),
                year=int(row["Year"]),
                month=int(row["Month"]),
                hour=int(row["Hour"]),
                weekdayname=row["Weekday Name"],
                leftover=float(row["Left Over"])
            )

            db.session.add(sale)

        db.session.commit()

    print("CSV data inserted successfully!")