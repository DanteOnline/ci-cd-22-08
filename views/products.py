"""
Products
"""
from flask import Blueprint, render_template, request, redirect
from werkzeug.exceptions import NotFound

from views.forms.products import ProductForm

products_app = Blueprint(
    "products_app",
    __name__,
    # url_prefix="/products",
)


PRODUCTS = {
    1: "Laptop",
    2: "Smartphone",
    3: "Tablet",
}


# @products_app.get()
@products_app.route("/", endpoint="list")
def products_list():
    """
    products_list
    :return:
    """
    return render_template(
        "products/list.html",
        products=PRODUCTS,
        # products=PRODUCTS.items(),
    )


@products_app.route("/<int:product_id>/", endpoint="details")
def get_product_by_id(product_id: int):
    """
    get_product_by_id
    :param product_id:
    :return:
    """
    product_name = PRODUCTS.get(product_id)
    if product_name is None:
        raise NotFound(f"Product #{product_id} not found!")
    return render_template(
        "products/details.html",
        product_id=product_id,
        product_name=product_name,
    )


@products_app.route(
    "/add/",
    methods=["GET", "POST"],
    endpoint="add",
)
def add_product():
    """
    Add product
    :return:
    """
    form = ProductForm()

    if request.method == "GET":
        return render_template("products/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), 400

    # post
    product_name = form.name.data
    print(product_name)

    return redirect('/')
