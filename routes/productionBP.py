from flask import Blueprint
from controllers.productionController import save, getAll, find_production_total

production_blueprint = Blueprint('production_bp', __name__)
production_blueprint.route('/', methods=['POST'])(save)
production_blueprint.route('/', methods=['GET'])(getAll)
production_blueprint.route('/total', methods=['GET'])(find_production_total)