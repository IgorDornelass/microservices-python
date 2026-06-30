from flask import Blueprint, jsonify, request
from data.orders import orders
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
def create_order():

    data = request.get_json()

    response = requests.get(
        f"http://localhost:5001/products/{data['product_id']}"
    )

    if response.status_code != 200:
        return jsonify({
            "error": "Produto nao encontrado"
        }), 404

    new_order = {
        "id": len(orders) + 1,
        "product_id": data["product_id"],
        "quantity": data["quantity"],
        "status": "created"
    }

    orders.append(new_order)

    return jsonify(new_order), 201