# **StrokeShield: AI-Powered Stroke Risk Prediction**  

[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-brightgreen)](https://stroke-shield.streamlit.app/)  
🔗 **Live Demo:** [StrokeShield on Streamlit](https://stroke-shield.streamlit.app/)  

💡 **Tip:** The app may go to sleep due to inactivity. Simply click on "Get up app" and enjoy seamless predictions! 🚀   



## **Overview**  

Stroke is a serious global health concern, often caused by factors like age, hypertension, and lifestyle choices. **StrokeShield** is an **AI-powered risk assessment tool** that predicts stroke probability based on individual health metrics.  

This project utilizes **machine learning** to analyze key health parameters and estimate stroke risk using a **Linear Discriminant Analysis (LDA) model** with a **ROC-AUC score of ~0.85**. The model is integrated into a **Streamlit web app**, offering **real-time predictions** with an intuitive and visually structured UI.  

---

## **How It Works**  

1️⃣ **User Inputs Health Data**: Age, hypertension, heart disease, glucose levels, BMI, etc.  
2️⃣ **Model Predicts Stroke Risk**: The AI model processes the input and returns either **"High Risk"** (🔴) or **"Low Risk"** (🟢).  
3️⃣ **Instant Feedback**: The result is displayed dynamically, with a **red or green indicator** for easy interpretation.  

### **Key Features**  

✅ **Easy-to-use UI** with a **3-column layout** (no scrolling required).  
✅ **Color-coded results** for better visibility:  
   - 🟢 **Low Risk** (Green Background)  
   - 🔴 **High Risk** (Red Background)  
✅ **Accurate AI Model** trained on healthcare data.  
✅ **Accessible on Web**—No installation needed.  

---

## **Dataset & Model**  

The project uses the **Healthcare Dataset Stroke Data** (5,110 records, 12 features) from **Kaggle**.  

### **Key Health Factors Considered:**  
- **Age, Hypertension, Heart Disease** (Major contributors)  
- **Glucose Levels, BMI, Smoking Status** (Additional risk factors)  
- **Work Type, Residence Type, Marital Status** (Lifestyle aspects)  

### **Modeling Approach:**  
- **Data Preprocessing**:
  - Handled missing BMI values using **median imputation**.
  - Applied **one-hot encoding** for categorical features.
  - Balanced dataset using **SMOTE** (Synthetic Minority Oversampling Technique).  
- **Machine Learning**:
  - **LDA model** chosen for best performance (**ROC-AUC: 0.85**).
  - The trained model is saved as **`models/stroke_prediction_model.joblib`**.  

---

## **Key Insights from Data**  

📌 **Hypertension & Heart Disease**: **3-4x higher risk** of stroke.  
📌 **Age Factor**: Stroke risk **increases significantly** with age.  
📌 **Self-employed Individuals**: **Highest stroke risk** among work types.  
📌 **Rural vs. Urban**: Slightly higher risk in **rural areas**.  
📌 **Smoking & BMI**: **Minimal direct correlation** but still considered.  

---

## **How to Run the Application**  

### **🚀 Online (Recommended)**  
Simply visit: **[StrokeShield Streamlit App](https://stroke-shield.streamlit.app/)**  

### **🖥️ Run Locally (Optional)**  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/Prateekkp/StrokeShield.git  
   cd StrokeShield

2. **Install dependencies:**:
   ```bash
   pip install -r requirements.txt

3. **Run the Streamlit app::**:
   ```bash
   streamlit run app.py

## **Conclusion**  
StrokeShield successfully bridges data science and healthcare by providing a fast, AI-powered stroke risk assessment tool. The Streamlit-based UI ensures a smooth and intuitive experience, while the LDA model delivers highly accurate predictions.

This project is a strong proof-of-concept for AI in health-tech, demonstrating predictive analytics, model deployment, and interactive UI design. 🚀

## **👤 Developed by Prateek Kumar Prasad**  

📩 **Email:** [prateekkumarprasad15@gmail.com](mailto:prateekkumarprasad15@gmail.com)  
📌 **LinkedIn:** [linkedin.com/in/prateekkp](https://www.linkedin.com/in/prateekkp/)  


**If you found this project useful, don't forget to give it a ⭐ on GitHub!**

   
