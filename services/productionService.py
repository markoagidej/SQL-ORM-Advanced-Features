from sqlalchemy.orm import Session
from database import db
from models.production import Production
from models.product import Product
from datetime import datetime
from sqlalchemy.sql import text
from sqlalchemy import select

def save(production_data):
    with Session(db.engine) as session:
        with session.begin():
            new_production = Production(product_id=production_data['product_id'], quantity_produced=production_data['quantity_produced'], date_produced=datetime.now())
            session.add(new_production)
            session.commit()

        session.refresh(new_production)
        return new_production
    
def getAll():
    with Session(db.engine) as session:
        productions = session.query(Production).all()
        print(productions)
        return productions
    

def find_production_total():
    query = text("SELECT p.name, SUM(pn.quantity_produced) AS total_produced, CURDATE() FROM production AS pn LEFT JOIN products AS p ON pn.product_id=p.id WHERE pn.date_produced = CURDATE() GROUP BY p.name;")
    products = db.session.execute(query).all()
    return products