import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv
from PIL import Image

st.set_option("deprecation.showPyplotGlobalUse", False)

load_dotenv(find_dotenv())

# Define the base URL of your FastAPI backend
BASE_URL = os.environ["BASE_URL_PROD"]

root_path = "../"
data_path = os.path.join(root_path, "data/raw_data/")


@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df


df = load_data(os.path.join(data_path, "df_iris_raw.csv"))

# Streamlit UI
st.title("Model Prediction App")

# Sidebar with options
st.sidebar.title("Dashboard Options")
option = st.sidebar.selectbox(
    "Select an option", ["About", "View Data", "Visualizations", "Predictions"]
)

if option == "View Data":
    st.subheader("Raw data")
    st.dataframe(df)
    st.write(f"Number of rows is: {len(df)}")

elif option == "About":
    st.subheader("About")
    # Text input
    st.write("Enter your name:")
    name = st.text_input("Name", "")

    if name:
        st.write(
            f"Hello, {name} and welcome to an interactive dashboard powered by Streamlit!"
        )
    # Get default response request
    response = requests.get(f"{BASE_URL}/")
    message = response.json()["message"]
    st.write(f"{message}")
    image = Image.open(os.path.join(data_path, "iris-machinelearning.png"))
    st.image(image, caption="Example Image", use_column_width=True)
    st.write("Check the box if you think this is great:")
    checked = st.checkbox("Checkbox")
    if checked:
        st.markdown(
            "###### Great! Thank you! You can now try other tabs now on the sidebar"
        )

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("Powered by Streamlit")

# User inputs
elif option == "Predictions":
    st.subheader("Predictions")

    sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.0)
    sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.0)
    petal_length = st.slider("Petal Length", 1.0, 7.0, 4.0)
    petal_width = st.slider("Petal Width", 0.1, 2.5, 1.0)

    # Create payload dictionary from user inputs
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }

    # Make prediction request
    if st.button("Predict"):
        try:
            st.write("Used data")
            st.json(payload)

            response = requests.post(f"{BASE_URL}/predict", json=payload)
            prediction = response.json()["prediction"]
            st.success(f"Prediction: {prediction}")
            path_image_prediction = {
                "setosa": os.path.join(data_path, "Iris_setosa.jpg"),
                "virginica": os.path.join(data_path, "Iris_virginica.jpg"),
                "versicolor": os.path.join(data_path, "Iris_versicolor.jpg"),
            }
            image_prediction = Image.open(path_image_prediction[prediction])
            # st.image(image_prediction)
            # resize image
            width, height = image_prediction.size
            new_width = 300
            new_height = int((new_width / width) * height)
            resized_image = image_prediction.resize((new_width, new_height))
            st.image(resized_image)

        except Exception as e:
            st.error(f"Error occurred: {str(e)}")


elif option == "Visualizations":
    st.subheader("Data Visualizations")

    # Bar chart
    st.subheader("Bar Chart")
    species_counts = df["species"].value_counts()
    st.bar_chart(species_counts, color="#ff009c")

    # Histogram
    df.hist()
    st.pyplot()
