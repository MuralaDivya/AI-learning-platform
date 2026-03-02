import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify
from flask_cors import CORS
from routes import ai_routes   # local import

app = Flask(__name__)
CORS(app)

app.register_blueprint(ai_routes)

@app.route("/")
def home():
    return jsonify({"status": "AI Personalized Learning Platform Backend Running"})

if __name__ == "__main__":
    app.run(debug=True)