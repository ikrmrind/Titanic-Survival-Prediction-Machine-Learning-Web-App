# 🚢 Titanic Survival Prediction

A professional **Machine Learning web application** that predicts whether a Titanic passenger would survive based on passenger information such as **class, gender, age, fare, and embarkation port**.

Built with **Python, Scikit-learn, Pandas, and Streamlit**.

---

## 📸 Project Preview

## ✨ Features

* Real-time survival prediction
* Probability-based output
* Clean Streamlit web interface
* Data preprocessing pipeline
* Feature engineering
* Trained Scikit-learn model
* Easy to customize and extend

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**
* **Joblib**

---

## 📂 Project Structure

```text
Titanic-Survival-Prediction/
│── app.py                 # Streamlit web app
│── model.pkl              # Trained ML model
│── scaler.pkl             # Scaler object (if used)
│── requirements.txt       # Python dependencies
│── train_model.py         # Model training script
│── data/
│   └── titanic.csv
│── screenshots/
│   └── app_preview.png
│── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ikrmrind/Titanic-Survival-Prediction-Machine-Learning-Web-App/tree/main
```

### 2️⃣ Move into the project folder

```bash
cd Titanic-Survival-Prediction
```

### 3️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
```

### 4️⃣ Activate the virtual environment

**Windows**

```bash
venv\\Scripts\\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` file yet, install manually:

```bash
pip install streamlit pandas numpy scikit-learn joblib
```

---

## ▶️ Run the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

After running the command, open your browser and visit:

```text
http://localhost:8501
```

---

## 📋 Input Features

| Feature  | Description                   |
| -------- | ----------------------------- |
| Pclass   | Passenger class (1, 2, 3)     |
| Sex      | Male or Female                |
| Age      | Passenger age                 |
| Fare     | Ticket fare                   |
| Embarked | Port of embarkation (C, Q, S) |

---

## 🤖 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Model Training
7. Model Evaluation
8. Model Serialization (`.pkl`)
9. Streamlit Deployment

---

## 📊 Example Prediction

**Input**

* Passenger Class: **1**
* Gender: **Female**
* Age: **18**
* Fare: **70**
* Embarked: **S**

**Output**

```text
Passenger is likely to Survive
Survival Probability: 89.82%
```

---

## 🚀 Future Improvements

* Add more passenger features
* Compare multiple ML algorithms
* Improve UI/UX
* Deploy on Streamlit Community Cloud
* Add SHAP explainability
* Add model performance dashboard

---

## 👨‍💻 Author

**Muhammad Ikram**

* LinkedIn: https://www.linkedin.com/in/muhammad-ikram-a6b74b31a/

---

## ⭐ Support

If you found this project helpful, please **star ⭐ the repository** and share it with others.

---

## 🏷️ Tags

`machine-learning` `python` `streamlit` `scikit-learn` `pandas` `numpy` `classification` `titanic` `data-science`
