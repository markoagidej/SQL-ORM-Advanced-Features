from flask import request, jsonify
from models.schemas.productionSchema import production_schema, productions_schema
from services import productionService
from marshmallow import ValidationError

def save():
    try:
        production_data = production_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    production_save = productionService.save(production_data)
    return production_schema.jsonify(production_save), 201

def getAll():
    try:
        productions = productionService.getAll()
        return productions_schema.jsonify(productions), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    
def find_production_total():
    try:
        productions = productionService.find_production_total()
        return jsonify(productions), 201
    except ValidationError as err:
        return jsonify(err.messages), 400  