from flask import Blueprint
from flask import request, jsonify, json
from db import session
from models.test_model import TestModel

blueprint = Blueprint("test", __name__)

@blueprint.route("/test", methods=["PUT"])
def test_put():
    try:
        json_data = json.loads(request.data)
        # do something with data
        res_data = json_data
        res_json = {'status': 1, 'data': res_data}
    except Exception as e:
        if e.args:
            res_data = e.args[0]
        else:
            res_data = e
        res_json = {'status': 0, 'error': res_data}
    return jsonify(res_json)

@blueprint.route("/test", methods=["POST"])
def test_post():
    try:
        json_data = json.loads(request.data)
        # do something with data
        res_data = json_data
        res_json = {'status': 1, 'data': res_data}
    except Exception as e:
        if e.args:
            res_data = e.args[0]
        else:
            res_data = e
        res_json = {'status': 0, 'error': res_data}
    return jsonify(res_json)

@blueprint.route("/test", methods=["GET"])
def test_get():
    try:
        _id = request.args['id']
        # do something with _id
        res_json = {'status': 1, 'data': _id}
    except Exception as e:
        if e.args:
            res_data = e.args[0]
        else:
            res_data = e
        res_json = {'status': 0, 'error': res_data}
    return jsonify(res_json)

@blueprint.route("/test", methods=["DELETE"])
def test_delete():
    try:
        _id = request.args['id']
        # do something with data
        res_json = {'status': 1, 'data': _id}
    except Exception as e:
        if e.args:
            res_data = e.args[0]
        else:
            res_data = e
        res_json = {'status': 0, 'error': res_data}
    return jsonify(res_json)