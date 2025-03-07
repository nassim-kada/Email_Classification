# Email Spam Classifier API

A Flask-based REST API that classifies email content as either spam or ham (legitimate) using a pre-trained machine learning model.

## Overview

This API provides a simple endpoint to classify email content using a trained classifier. The system uses TF-IDF vectorization and a machine learning model to determine whether an email is spam or legitimate.

## Features

- Fast classification of email content
- Returns probability scores for both spam and ham classifications
- Includes performance metrics for each prediction
- Cross-Origin Resource Sharing (CORS) enabled
- Error handling for invalid requests

## Prerequisites

- Python 3.6+
- Flask
- Flask-CORS
- scikit-learn
- joblib

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/nassim-kada/Email_Classification.git
   cd email-spam-classifier
   ```

2. Install the required packages:
   ```
   pip install flask flask-cors scikit-learn joblib
   ```

3. Ensure you have the model files in the project directory:
   - `spam_classifier_model.pkl` - The trained machine learning model
   - `tfidf_vectorizer.pkl` - The TF-IDF vectorizer

## Usage

### Starting the Server

Run the following command to start the API server:

```
python app.py
```

The server will start on `http://127.0.0.1:5000/` by default.


## Performance

The API includes timing information with each response:
- `vectorization_time`: Time taken to convert the email text to a TF-IDF vector
- `prediction_time`: Time taken by the model to make a prediction
- `total_time`: Total processing time

## Error Handling

The API returns appropriate error messages with HTTP status codes:
- 400: Bad Request (e.g., missing email content)
- 500: Internal Server Error (for any unexpected errors)


## Model Information

The spam classifier is pre-trained using [brief description of your training data and algorithm]. The model file and TF-IDF vectorizer are serialized using joblib.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
