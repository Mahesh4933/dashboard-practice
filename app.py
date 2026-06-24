from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/sales")
def sales():
    return render_template("sales.html")

@app.route("/customers")
def customers():
    return render_template("customers.html")

@app.route("/finance")
def finance():
    return render_template("finance.html")

@app.route("/inventory")
def inventory():
    return render_template("inventory.html")

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

if __name__ == "__main__":
    app.run(debug=True)