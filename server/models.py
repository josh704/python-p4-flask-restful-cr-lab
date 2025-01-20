from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    image = db.Column(db.String(200))
    price = db.Column(db.Numeric(10,2))

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "price": str(self.price) 
        }
