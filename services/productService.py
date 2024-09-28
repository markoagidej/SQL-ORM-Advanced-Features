from sqlalchemy.orm import Session
from sqlalchemy import select
from database import db
from models.product import Product
from models.order import Order
from sqlalchemy.sql import text

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
    
def find_all_pagination(page=1, per_page=1):
    products = db.paginate(select(Product), page=page, per_page=per_page)
    return products

def find_most_sold():
    query = text("SELECT p.name, product_id, SUM(quantity) AS sold_units FROM orders LEFT JOIN products AS p ON p.id=product_id GROUP BY product_id ORDER BY sold_units DESC;")
    products = db.session.execute(query).scalars().all()
    return products