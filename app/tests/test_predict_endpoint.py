import requests

# Define the API base URL (update with your actual URL)
api_base_url = "http://127.0.0.1:8000"

# Define the endpoint URL for prediction
predict_url = f"{api_base_url}/predict"

# Sample payload for prediction (adjust as needed)
payload = {
    "sepal_length": 6.1,
    "sepal_width": 2.8,
    "petal_length": 4.7,
    "petal_width": 1.2,
}

# Send POST request to predict endpoint
response = requests.post(predict_url, json=payload)

# Check the response
if response.status_code == 200:
    prediction_result = response.json()["prediction"]
    print(f"Prediction result: {prediction_result}")
else:
    print(f"Error: {response.status_code} - {response.text}")
