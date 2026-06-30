from flask import Blueprint, jsonify, request
from data.orders import orders
from services.order_service import create_order
import requests

order_bp = Blueprint("order_bp", __name__)


@order_bp.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)


@order_bp.route("/orders/products/<int:product_id>", methods=["GET"])
def get_product_from_service(product_id):

    response = requests.get(
        f"http://localhost:5001/products/{product_id}"
    )

    return jsonify(response.json()), response.status_code


@order_bp.route("/orders", methods=["POST"])
def create():

    data = request.get_json()

    result, status = create_order(
        data["product_id"],
        data["quantity"]
    )

    return jsonify(result), status