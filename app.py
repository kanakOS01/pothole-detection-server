from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
import model

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return "Hello, World!"

@app.route('/detect', methods=['POST'])
def detect_pothole():
    data = request.json
    image_url = data['image_url']
    confidence = data['confidence']

    print(f"Image URL: {image_url}")
    print(F"Confidence: {confidence}")

    response = model.predict(
        image_url=image_url,
        conf=confidence
    )

    response = jsonify(
        {"response": response}
    )

    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Content-Type", "application/json")
    
    return response


if __name__ == '__main__':
    app.run(debug=True)