from flask import Flask
from models import db, SalesDaily

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pharmacy.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    
    data = SalesDaily.query.limit(10).all()

    for row in data:
        print(row.datum, row.Paracetamol, row.weekdayname)