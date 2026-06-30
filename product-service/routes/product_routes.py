from flask import Blueprint, jsonify, request
from data.products import products

product_bp = Blueprint("product_bp", __name__)


@product_bp.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


@product_bp.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )

    if not product:
        return jsonify({
            "error": "Produto nao encontrado"
        }), 404

    return jsonify(product)

@product_bp.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()

    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"],
        "stock": data["stock"]
    }

    products.append(new_product)

    return jsonify(new_product), 201