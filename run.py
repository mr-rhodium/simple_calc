from flask import Flask, render_template
from calc import Logic
from models import CalcQuery
from flask_pydantic import validate


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/calculate", methods=["POST"])
@validate()
def calculate(body: CalcQuery):
    logic = Logic(body).run()
    return {"result": logic}


if __name__ == "__main__":
    app.run(debug=True)
