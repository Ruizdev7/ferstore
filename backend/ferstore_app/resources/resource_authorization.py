from flask import jsonify
from flask import request
from flask import Blueprint
from flask import make_response

from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from ferstore_app import db
from ferstore_app.models.tbl_employee import Employee


blueprint_api_authorization_employee = Blueprint(
    "api_authorization_employee", __name__, url_prefix=""
)


@blueprint_api_authorization_employee.route(
    "/api/v1/login_employee/token", methods=["POST"]
)
def create_token():
    id_received = request.json.get("number_id_employee", None)
    password_received = request.json.get("employee_password", None)

    query_logged_employee = Employee.query.filter(
        Employee.number_id_employee == id_received
    ).first()

    if query_logged_employee == None:
        return make_response(jsonify({"msg": "Usuario no encontrado!!!"}), 401)

    if check_password_hash(query_logged_employee.employee_password, password_received):
        access_token = create_access_token(identity=id_received)
        return make_response(
            jsonify(
                {
                    "current_user": {
                        "ccn_employee": query_logged_employee.ccn_employee,
                        "token": access_token,
                        "full_name_employee": query_logged_employee.full_name_employee,
                        "informed_consent_law_1581": query_logged_employee.informed_consent_law_1581,
                    },
                }
            )
        )
    else:
        return make_response(jsonify({"msg": "Contraseña Invalida"}), 400)
