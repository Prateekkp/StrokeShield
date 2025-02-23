# Stroke Prediction Application

## Background and Overview

Stroke is a critical health issue globally, often linked to factors like age, hypertension, and lifestyle choices. This project aims to leverage data science and full-stack development to predict stroke risk based on individual health metrics. The application combines a machine learning model trained on a healthcare dataset with a Flask backend and a React frontend, providing an accessible tool for users to assess their stroke probability. Built as a personal project inspired by a YouTube tutorial, it showcases exploratory data analysis (EDA), predictive modeling, and web development skills.

The core model uses Linear Discriminant Analysis (LDA), selected for its strong performance (ROC-AUC ~0.85), and is deployed via a Flask API. The React interface offers an intuitive, visually appealing form for inputting health data, delivering real-time predictions without page reloads.

---

## Data Structure and Overview

The project uses the "Healthcare Dataset Stroke Data" from Kaggle, containing 5,110 records with 12 features. Below is an overview of the dataset:

- **Source**: `/backend/healthcare-dataset-stroke-data.csv`
- **Key Features**:
  - `id`: Unique identifier (dropped during preprocessing)
  - `gender`: Male, Female, Other (categorical)
  - `age`: Age in years (numerical)
  - `hypertension`: 0 (No), 1 (Yes) (binary)
  - `heart_disease`: 0 (No), 1 (Yes) (binary)
  - `ever_married`: Yes, No (categorical)
  - `work_type`: Private, Self-employed, Govt_job, Children, Never_worked (categorical)
  - `Residence_type`: Urban, Rural (categorical)
  - `avg_glucose_level`: Average glucose level in mg/dL (numerical)
  - `bmi`: Body Mass Index (numerical)
  - `smoking_status`: Formerly smoked, Never smoked, Smokes (categorical)
  - `stroke`: 0 (No stroke), 1 (Stroke) (target variable, binary)

- **Preprocessing**:
  - Dropped `id` column.
  - Handled missing `bmi` values using median imputation.
  - Applied one-hot encoding to categorical features and power transformation to numerical features.
  - Addressed class imbalance with SMOTE (Synthetic Minority Oversampling Technique).

The trained LDA model is saved as `stroke_prediction_model.joblib` in the `backend` directory.

---

## Executive Summary

This project delivers a full-stack solution for stroke risk prediction:
- **EDA**: Conducted via Python (Pandas, Plotly), revealing key risk factors like hypertension and age.
- **Modeling**: Evaluated Logistic Regression, LDA, and Random Forest, with LDA achieving the best ROC-AUC (0.85) after cross-validation.
- **Backend**: Flask API serves predictions using the saved LDA model, accessible at `http://localhost:5000/predict`.
- **Frontend**: React app with a three-column form design, styled with CSS gradients and Google Fonts (Poppins), providing a seamless user experience.
- **Deployment**: Local setup with Flask and React, integrated via CORS.

The application successfully predicts stroke risk with high accuracy, demonstrating a practical blend of data science and web development.

---

## Insights Deep Dive

Exploratory Data Analysis uncovered actionable insights:
1. **Age**: Weak positive correlation (0.25) with stroke risk, increasing with older age.
2. **Hypertension**: 3.3x higher stroke risk for individuals with hypertension (13.25% vs. 4.01%).
3. **Heart Disease**: 4.07x increased risk (17.65% vs. 4.34% without heart disease).
4. **Gender**: Males slightly more prone (5.1% vs. 4.6% for females).
5. **Marital Status**: Married individuals show a 5.7% stroke rate, possibly tied to age or stress factors.
6. **Work Type**: Self-employed individuals have the highest stroke rate (7.82%), potentially due to stress or lifestyle.
7. **Residence Type**: Rural residents slightly more at risk (5.0% vs. 4.7% urban).
8. **Glucose Levels**: Slight elevation in average glucose levels for stroke patients, but not definitive.
9. **BMI**: No significant correlation with stroke risk.
10. **Smoking**: Minimal difference across smoking statuses (e.g., 5.6% for smokers vs. 4.6% never smoked).

Mutual information scores confirmed hypertension (0.02) and heart disease (0.01) as top predictors. The LDA model effectively captured these patterns, enhanced by SMOTE to handle the imbalanced target (95% no stroke, 5% stroke).

---

## Conclusion

The Stroke Prediction Application successfully integrates data science and web technologies to provide an accessible, accurate tool for assessing stroke risk. Key findings highlight hypertension, heart disease, and age as critical factors, aligning with medical research. The LDA model’s robust performance and the sleek React-Flask interface make this project a strong proof-of-concept for health-tech applications.

Future enhancements could include:
- Adding a probability score alongside binary predictions.
- Deploying to a cloud platform (e.g., Heroku, AWS).
- Expanding the dataset or incorporating real-time health data.

This project demonstrates the power of combining machine learning with user-friendly design to address real-world challenges.

# Frontend Setup (in a new terminal)
cd ../frontend
npm install  # Install Node.js dependencies
npm start  # Start React app (runs on http://localhost:3000)
