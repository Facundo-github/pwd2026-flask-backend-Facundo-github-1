from app.database import db
from app.models.base_model import BaseModel

class Proveedor(BaseModel):
    __tablename__ = "proveedores"

    nombre = db.Column(db.String(150), nullable=False)
    contacto = db.Column(db.String(100), nullable=True)
    telefono = db.Column(db.String(30), nullable=True)
    email= db.Column(db.String(120), nullable=True)

    productos = db.relationship("Producto", backref="proveedor", lazy=True)