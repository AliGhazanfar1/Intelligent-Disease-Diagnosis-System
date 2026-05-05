# Multiple Disease Prediction System 🏥

A comprehensive machine learning-based web application that predicts multiple diseases including **Diabetes**, **Heart Disease**, and **Parkinson's Disease**. This system uses trained machine learning models to provide accurate predictions based on user-provided clinical data.

## 🚀 Overview
This project is built using **Python** and **Streamlit** to create an interactive and user-friendly interface. It allows users to navigate through different disease prediction systems seamlessly using a sidebar menu.

## 📋 Features
- **Diabetes Prediction**: Predicts if a person is diabetic based on parameters like Glucose, BMI, Age, etc.
- **Heart Disease Prediction**: Analyzes cardiovascular health using parameters like age, cholesterol, chest pain type, and resting blood pressure.
- **Parkinson's Disease Prediction**: Utilizes vocal features (MDVP) to detect the presence of Parkinson's Disease.

## 📊 Model Performance
The models were trained using various algorithms, and the best-performing models were integrated into the system:

| Disease | Best Model | Accuracy |
|---------|------------|----------|
| **Diabetes** | Support Vector Machine (SVM) | ~78% |
| **Heart Disease** | Logistc Regression | ~80% |
| **Parkinson's** | SVM / Random Forest | ~88% |

## 🛠️ Technology Stack
- **Language**: Python
- **Web Framework**: Streamlit
- **Machine Learning**: Scikit-learn (Models saved as `.sav` files)
- **Navigation**: streamlit-option-menu

## 📂 Project Structure
```text
Multiple Disease Prediction/
│
├── MDP.py                      # Main Streamlit application
├── saved model/                # Directory containing trained ML models
│   ├── diabetes_model.sav      # Trained model for Diabetes
│   ├── heart_model.sav         # Trained model for Heart Disease
│   └── parkinson_model.sav     # Trained model for Parkinson's
├── diabetes_once_again.ipynb   # Jupyter notebook for Diabetes model training
├── heartdisease.ipynb          # Jupyter notebook for Heart Disease model training
└── parkinson's_disease.ipynb   # Jupyter notebook for Parkinson's model training
```

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/multiple-disease-prediction.git
   cd multiple-disease-prediction
   ```

2. **Install Dependencies**
   Ensure you have Python installed, then run:
   ```bash
   pip install streamlit streamlit-option-menu scikit-learn
   ```

3. **Run the Application**
   ```bash
   streamlit run MDP.py
   ```

## 📈 How it Works
1. Select the disease you want to test from the sidebar.
2. Enter the required clinical values in the input fields.
3. Click the **Test Result** button.
4. The system will process the data through the respective trained model and display whether the result is positive or negative.

## 👥 Team Members
This project was a collaborative effort by:
- **aaliiya**
- **abhishekpatelcs27**
- **akshitaaa1**


## ⚠️ Disclaimer
This system is intended for informational and educational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.

---
*Created with ❤️ using Python and Streamlit.*
# Intelligent-Disease-Diagnosis-System
