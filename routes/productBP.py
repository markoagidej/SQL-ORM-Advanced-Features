from flask import Blueprint
from controllers.productController import save, getAll, find_all_pagination, find_most_sold

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/', methods=['GET'])(getAll)
product_blueprint.route('/paginate', methods=['GET'])(find_all_pagination)
product_blueprint.route('/most_sold', methods=['GET'])(find_most_sold)