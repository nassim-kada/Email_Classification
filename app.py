from flask import Flask, request, jsonify
import joblib
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

print("Loading model and vectorizer...")
start_time = time.time()
model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
print(f"Model and vectorizer loaded in {time.time() - start_time:.2f} seconds")

@app.route("/classify", methods=["POST"])
def classify():
    try:
        data = request.json
        email_content = data.get("email_content", "")

        if not email_content:
            return jsonify({"error": "No email content provided"}), 400

        process_start = time.time()
        
        vectorization_start = time.time()
        email_vectorized = vectorizer.transform([email_content])
        vectorization_time = time.time() - vectorization_start

        prediction_start = time.time()
        prediction = model.predict(email_vectorized)[0]
        probability = model.predict_proba(email_vectorized)[0]
        prediction_time = time.time() - prediction_start

        total_time = time.time() - process_start

        response = {
            "prediction": "spam" if prediction == 0 else "ham",
            "spam_probability": round(probability[0] * 100, 2),
            "ham_probability": round(probability[1] * 100, 2),
            "timing": {
                "vectorization_time": round(vectorization_time, 3),
                "prediction_time": round(prediction_time, 3),
                "total_time": round(total_time, 3)
            }
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
