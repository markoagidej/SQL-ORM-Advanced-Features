from sqlalchemy.orm import Session
from database import db
from models.product import Product

def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data['name'], price=product_data['price'])
            session.add(new_product)
            session.commit()

        session.refresh(new_product)
        return new_product
    
def getAll():
    with Session(db.engine) as session:
        products = session.query(Product).all()
        print(products)
        return products