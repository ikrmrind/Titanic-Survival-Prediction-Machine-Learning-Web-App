import streamlit as st
import pandas as pd
import joblib

# ===================================
# Page Configuration
# ===================================
st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="centered"
)

# ===================================
# Load Files
# ===================================
model = joblib.load("Titanic_Survival.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

# ===================================
# Header
# ===================================
st.title("🚢 Titanic Survival Prediction")
st.write("Predict whether a passenger survived the Titanic disaster.")

st.divider()

# ===================================
# Input Section
# ===================================
st.subheader("Passenger Information")

col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox(
        "Passenger Class",
        [1, 2, 3]
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=100,
        value=25
    )

with col2:
    fare = st.number_input(
        "Fare",
        min_value=0.0,
        value=32.0,
        step=1.0
    )

    embarked = st.selectbox(
        "Embarked",
        ["S", "C", "Q"]
    )

st.divider()

# ===================================
# Predict Button
# ===================================
if st.button("Predict Survival", use_container_width=True):

    # Encode values
    gender = 1 if gender == "Male" else 0

    embarked = {
        "S": 0,
        "C": 1,
        "Q": 2
    }[embarked]

    # Create DataFrame
    data = pd.DataFrame({
        "Pclass": [pclass],
        "Gender": [gender],
        "Age": [age],
        "Fare": [fare],
        "Embarked": [embarked]
    })

    # Arrange columns exactly like training
    data = data[columns]

    # Scale input
    data = pd.DataFrame(
        scaler.transform(data),
        columns=columns
    )

    # Prediction
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("✅ Passenger is likely to Survive")
    else:
        st.error("❌ Passenger is likely to Not Survive")

    st.progress(float(probability[1]))

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Survival Chance",
            f"{probability[1]*100:.2f}%"
        )

    with col2:
        st.metric(
            "Non-Survival Chance",
            f"{probability[0]*100:.2f}%"
        )