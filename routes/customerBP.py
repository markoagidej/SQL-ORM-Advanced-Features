from flask import Blueprint
from controllers.customerController import save, getAll, get_customers_value_over1000

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(getAll)
customer_blueprint.route('/over1000', methods=['GET'])(get_customers_value_over1000)