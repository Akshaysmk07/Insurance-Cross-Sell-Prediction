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

- **Vehicle Age**:  
  - Customers with vehicle age **1-2 years** are more likely to be interested in purchasing vehicle insurance compared to those with older or newer vehicles.  
  - Customers with **Vehicle_Age < 1 year** have very low chances of purchasing vehicle insurance, possibly due to having newer vehicles or lower insurance needs.
  
- **Previous Insurance**:  
  - Customers who were **not previously insured** are more likely to show interest in vehicle insurance.
  
- **Driving License**:  
  - **Almost all customers** interested in vehicle insurance have a valid **driving license**, highlighting the importance of this factor in the decision-making process.

- **Age Group Analysis**:  
  - **Young customers** below 30 years old tend to be less interested in vehicle insurance. This could be due to factors like lack of experience, lower maturity, or not owning expensive vehicles yet.  
  - Customers aged between **30-60** are more likely to be interested in vehicle insurance, suggesting that this group is more financially stable and has higher vehicle ownership.

- **Outliers**:  
  - Based on the boxplot analysis, we observed that there were **no significant outliers** in the dataset, ensuring that the data quality was consistent.

### 📊 **Feature Importance**  
We identified the most important features influencing vehicle insurance interest using the model's feature importance scores, helping to focus on the key factors driving customer behavior.

---

## 🤖 Model Development & Evaluation

Built a clean ML pipeline with data preprocessing (null handling, encoding, scaling). Tried Logistic Regression, Random Forest, and XGBoost.

🎯 **Best Model**: Random Forest (after Optuna tuning)  
- **Accuracy**: 90%  
- **Precision / Recall / F1-score**: 90%  
- **ROC-AUC**: 0.97  

📌 Showed balanced performance across both classes.  
📈 Hyperparameter tuning boosted accuracy from 89% → 90%.  
🧪 Tracked experiments with MLflow.  
📦 Final model saved, versioned, and ready for deployment.

---

## 🚀 Business Conclusion

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
- **Streamlit** can be deployed as a web application to allow sales teams to input customer details dynamically and get instant predictions.
  
---

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

## 📌 **Final Recommendations for Business**

1. **Targeted Marketing**:  
   Focus marketing efforts on customers predicted to be interested in vehicle insurance. Use personalized campaigns (emails, phone calls, etc.) based on prediction outcomes.

2. **Budget Optimization**:  
   The model can help optimize marketing spend by allocating resources efficiently. The company can invest in targeting high-probability customers rather than broad-spectrum marketing.

3. **Real-Time Predictions**:  
   Integrating the model into a **Streamlit app** will provide sales teams with real-time predictions when engaging with customers, leading to more informed decisions.

4. **Monitor & Refine**:  
   Continuously monitor model performance as new customer data comes in. Retrain the model periodically with fresh data to ensure its predictions stay accurate over time.

5. **Expand Cross-Sell Potential**:  
   Leverage the insights from this model to explore cross-sell opportunities beyond vehicle insurance, such as life insurance or home insurance, based on customer segments identified in this analysis.

---
