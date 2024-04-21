import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib


def train_model():
    # Load data
    data_path = "data/raw_data/df_iris_dev_raw.csv"
    df = pd.read_csv(data_path)

    # Define features and target
    X = df.drop("species", axis=1)
    y = df["species"]

    # Standard Scale numerical values in X
    ss = StandardScaler()
    X_transformed = ss.fit_transform(X)
    joblib.dump(ss, "models/StandardScaler.pkl")

    # Label encode categorical values in y
    le = LabelEncoder()
    y_transformed = le.fit_transform(y)
    joblib.dump(le, "models/LabelEncoder.pkl")

    # Train  model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_transformed, y_transformed)

    # Save model
    model_path = "models/trained_model.pkl"
    joblib.dump(model, model_path)


if __name__ == "__main__":
    train_model()
