# 💻 Laptop Recommendation System

### *Predict Performance. Recommend Smarter.*

An end-to-end Machine Learning web application that predicts laptop performance using **XGBoost Regressor** and recommends the most suitable laptops based on user hardware requirements.

---

# 📌 Project Overview

Choosing a laptop can be difficult because of the huge variety of processors, graphics cards, RAM capacities, storage options, and display configurations available today.

This project simplifies that decision by predicting a laptop's **Performance Score** using an **XGBoost Regression model** trained on engineered hardware features. Based on the predicted score, the system recommends the closest matching laptops through an interactive **Streamlit** web application.

---

# 🎯 Project Objectives

- Build an XGBoost Regression model to predict laptop performance.
- Perform complete data cleaning and feature engineering.
- Create an intelligent recommendation engine.
- Develop an interactive Streamlit web application.
- Demonstrate an end-to-end Machine Learning workflow.

---

# 🚀 Features

## 🤖 Performance Prediction

- Predicts laptop performance using XGBoost.

## 💻 Smart Recommendation Engine

- Recommends the Top 3 laptops closest to the predicted performance.

## 📊 Interactive Web Interface

- Clean Streamlit UI for selecting hardware preferences.

## 🧹 Data Preprocessing

- Missing value handling
- Feature extraction
- Feature encoding
- Performance score generation

## ⚡ Fast XGBoost Model

- Accurate regression model
- Low prediction latency

---

# 🛠 Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Machine Learning | XGBoost |
| Data Processing | Pandas, NumPy |
| Model Serialization | Joblib |
| Web Framework | Streamlit |
| Visualization | Matplotlib |

---

# 📂 Repository Structure

```text
Laptop-Recommendation-System/

│
├── datasets/
│   ├── laptops_raw.csv
│   ├── laptops_clean.csv
│   └── laptops_Featured.csv
│
├── notebooks/
│   ├── 01_Data_Collection.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Model_Training.ipynb
│   └── 05_Recommendation_Engine.ipynb
│
├── models/
│   └── model_artifacts.joblib
│
├── app.py
├── requirements.txt
├── README.md
│
└── images/
```

---

# 📊 Dataset Features

The dataset contains real-world laptop specifications.

### Features

- Brand
- Product Name
- Processor
- GPU
- RAM
- Storage
- Display Resolution
- Refresh Rate
- Price

### Engineered Features

- CPU Score
- GPU Score
- RAM (GB)
- Storage (GB)
- Refresh Rate (Hz)
- Resolution Score
- Performance Score

---

# 🤖 Machine Learning Pipeline

```text
Laptop Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Feature Encoding
        │
        ▼
XGBoost Regressor
        │
        ▼
Performance Score Prediction
        │
        ▼
Recommendation Engine
        │
        ▼
Streamlit Web Application
```

---

# 📈 Application Workflow

```text
User Inputs Hardware Requirements
        │
        ▼
XGBoost Predicts Performance Score
        │
        ▼
Recommendation Engine Finds Closest Match
        │
        ▼
Top 3 Laptop Recommendations
```

---

# 🖥 Application Features

- Performance Prediction
- Laptop Recommendation
- Hardware Preference Selection
- Interactive Streamlit Dashboard

---

# 🔮 Future Improvements

- Laptop Images
- Live Price Tracking
- Benchmark Integration
- Price Filters
- Brand Filters
- Personalized Recommendations

---

# 👨‍💻 Developed By

**Daniel**

Artificial Intelligence & Machine Learning Student

---

# ⭐ Project Status

✅ Completed
