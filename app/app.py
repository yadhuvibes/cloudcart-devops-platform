from flask import (

    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    jsonify
)

from models import db, Product
from config import Config
from prometheus_flask_exporter import PrometheusMetrics
app = Flask(__name__)
app.config.from_object(Config)

metrics = PrometheusMetrics(app)

db.init_app(app)

with app.app_context():
    db.create_all()


# ---------------- HOME ---------------- #

@app.route("/")
def home():
    products = Product.query.all()
    return render_template("home.html", products=products)


@app.route("/products")
def products():
    products = Product.query.all()
    return render_template("products.html", products=products)


@app.route("/product/<int:product_id>")
def product_details(product_id):

    product = Product.query.get_or_404(product_id)

    return render_template(
        "product_details.html",
        product=product
    )


@app.route("/search")
def search():

    query = request.args.get("q", "")

    products = Product.query.filter(
        Product.name.ilike(f"%{query}%")
    ).all()

    return render_template(
        "products.html",
        products=products,
        search=query
    )


@app.route("/category/<category>")
def category(category):

    products = Product.query.filter_by(
        category=category
    ).all()

    return render_template(
        "products.html",
        products=products
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# ---------------- LOGIN ---------------- #

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "cloudcart123":

            session["logged_in"] = True
            session["username"] = username

            return redirect(url_for("admin"))

        flash("Invalid username or password.")

    return render_template("login.html")


# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# ---------------- ADMIN ---------------- #

@app.route("/admin", methods=["GET", "POST"])
def admin():

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if request.method == "POST":

        product = Product(

            name=request.form["name"],

            description=request.form["description"],

            price=float(request.form["price"]),

            category=request.form["category"],

            brand=request.form["brand"],

            stock=int(request.form["stock"]),

            rating=float(request.form["rating"]),

            image=request.form["image"]

        )

        db.session.add(product)
        db.session.commit()

        flash("Product added successfully!")

        return redirect(url_for("admin"))

    products = Product.query.all()

    return render_template(
        "admin.html",
        products=products,
        username=session.get("username")
    )


# ---------------- HEALTH ---------------- #

@app.route("/health")
def health():

    return jsonify({

        "status": "UP",

        "application": "CloudCart",

        "database": "Connected",

        "version": "1.0.0"

    })


# ---------------- API ---------------- #

@app.route("/api/products")
def api_products():

    products = Product.query.all()

    data = []

    for product in products:

        data.append({

            "id": product.id,

            "name": product.name,

            "description": product.description,

            "price": product.price,

            "category": product.category,

            "brand": product.brand,

            "stock": product.stock,

            "rating": product.rating,

            "image": product.image

        })

    return jsonify(data)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
