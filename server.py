from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_socketio import SocketIO
import util

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def home():
    return render_template("index.html", locations=util.get_location_names())


@socketio.on("estimate_price")
def handle_house_data(data):
    location = data["location"]
    sqft = float(data["sqft"])
    bhk = float(data["bhk"])
    bath = float(data["bath"])
    price = util.get_estimated_price(location, sqft, bhk, bath)
    socketio.emit("receive_price", price)


if __name__ == "__main__":
    socketio.run(app, debug=True)
