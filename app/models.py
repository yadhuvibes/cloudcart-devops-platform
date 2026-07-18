from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    description = db.Column(db.Text)

    price = db.Column(db.Float, nullable=False)

    category = db.Column(db.String(50), nullable=False)

    brand = db.Column(db.String(50))

    stock = db.Column(db.Integer)

    rating = db.Column(db.Float)

    image = db.Column(db.String(300))

    def __repr__(self):

        return f"<Product {self.name}>"
