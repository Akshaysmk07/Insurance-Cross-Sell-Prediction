# 🚗 Health Insurance Cross-Sell Prediction

**Predict which health insurance customers are likely to purchase vehicle insurance using machine learning.**

---

## 📌 Problem Statement

The client is a leading insurance company offering Health Insurance. Now, they plan to cross-sell **Vehicle Insurance** to existing customers.  
They require a predictive model that can determine **whether a customer from the past year is likely to be interested in Vehicle Insurance**.

---

## 🎯 Business Objective

Building a reliable prediction model serves multiple business purposes:

- 🎯 **Targeted Campaigns** – Focus marketing efforts on high-potential customers.
- 💡 **Improved ROI** – Optimize conversion rates and reduce customer acquisition costs.
- 📊 **Data-Driven Strategy** – Make strategic decisions based on predictive insights.
- 💰 **Revenue Growth** – Increase cross-sell opportunities and customer lifetime value.

---

## 🔁 Workflow

<img src="workflow.png" alt="Project Workflow" width="700"/>

---

## 📊 Exploratory Data Analysis (EDA)

_🚧 Section in Progress_

> This section will include key insights from EDA such as:

- Distribution of key features (e.g., Age, Annual Premium, Policy Sales Channel).
- Customer segments more likely to purchase vehicle insurance.
- Analysis of missing values, outliers, and class imbalance.
- Correlation heatmap of numerical variables.
- Feature importance overview.

---

## 🤖 Model Development & Evaluation

_🚧 Section in Progress_

> This section will cover the machine learning pipeline including:

- Data preprocessing: Handling nulls, encoding categoricals, scaling.
- Algorithms tried: Logistic Regression, Random Forest, XGBoost, etc.
- Model performance comparison using:
  - Accuracy
  - Precision, Recall, F1-score
  - ROC-AUC Curve
- Hyperparameter tuning (GridSearchCV / RandomizedSearchCV).
- Final model export and explanation.

---

## 📈 Business Conclusion

_🚧 Section in Progress_

> This section will summarize:

- Overall model performance and trustworthiness.
- Predicted conversion rates and business value.
- How this model supports smarter outreach campaigns.
- Recommendations for production deployment.

---

🚀 **Business Conclusion**  
This project successfully built a machine learning solution to predict which health insurance customers are likely to buy vehicle insurance, enabling the company to strategically target the right audience and boost cross-sell conversions.

✅ **Model Performance & Trustworthiness**  
The final **Random Forest model**, after hyperparameter tuning, achieved:

- **Accuracy**: 90%  
- **Precision / Recall / F1-score**: 90% across both classes  

This shows a balanced and robust model, performing well on both interested and uninterested customer segments.

Performance improved from **89% to 90% accuracy** after optimization, indicating a measurable gain in predictive quality. Feature importance from the Random Forest also adds to the model's interpretability and trust.

📈 **Predicted Conversion & Business Value**  
- Out of ~195,000 customers, ~98,000 (50%) were predicted as interested in vehicle insurance.  
- The model can reduce marketing costs by focusing outreach only on high-probability converters.  
- Even a modest increase in conversion through targeted campaigns could result in **significant revenue uplift**.

💡 **Strategic Marketing Support**  
With this predictive model:
- Marketing teams can segment and prioritize customers intelligently.  
- Outreach strategies (e.g., emails, calls) can be personalized based on predicted interest.  
- Resources can be better allocated to maximize ROI.

🔧 **Recommendations for Deployment**    
- Use **MLflow** (already used during training) for tracking and version control.  


## 💻 Streamlit App

An interactive web app is developed using **Streamlit** to:

- Input customer details dynamically.
- Get instant predictions about their likelihood of vehicle insurance interest.
- View prediction probability with a clean, user-friendly interface.

---

## 🛠️ Tech Stack

| Category        | Tools & Libraries                                |
|----------------|--------------------------------------------------|
| Language        | Python                                           |
| Data Handling   | Pandas, NumPy                                    |
| Visualization   | Matplotlib, Seaborn, Plotly                      |
| ML Models       | Scikit-learn, XGBoost, Random Forest             |
| Web App         | Streamlit                                        |
| Serialization   | Joblib                                           |
| Deployment      | Streamlit Cloud                                  |

---


