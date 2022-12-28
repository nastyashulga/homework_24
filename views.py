from typing import Any

from flask import Blueprint, request, jsonify
from schema import RequestParamsListSchema
from marshmallow import ValidationError

from utils import build_query

main_bp = Blueprint('main', __name__)

@main_bp.route('/perform_query', method=['POST'])
def perform_query() -> tuple[Any, str]:

    try:
        params = RequestParamsListSchema().load(request.json)
    except ValidationError as error:
        return error.messages, "400"

    result = None
    for query in params['queries']:
        result = build_query(
            cmd=query['cmd'],
            param=query['value'],
            data=result,
        )

    return jsonify(result), '200'