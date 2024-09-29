from sqlalchemy.orm import Session
from database import db
from models.customer import Customer
from sqlalchemy.sql import text

def save(customer_data):
    with Session(db.engine) as session:
        with session.begin():
            new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])
            session.add(new_customer)
            session.commit()

        session.refresh(new_customer)
        return new_customer
    
def getAll():
    with Session(db.engine) as session:
        customers = session.query(Customer).all()
        print(customers)
        return customers
    
def get_customers_value_over1000():
    query = text("SELECT c.name, SUM(total_price) AS customer_value FROM orders AS o LEFT JOIN customers AS c ON o.customer_id = c.id GROUP BY o.customer_id HAVING customer_value > 1000.00 ORDER BY customer_value DESC;")
    products = db.session.execute(query).scalars().all()
    return products