import streamlit as st
import pandas as pd
import numpy as np
import joblib
from streamlit_option_menu import option_menu

# Set page title and layout
st.set_page_config(page_title="Insurance Cross-Sell Prediction", layout="wide")

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["About Project", "Prediction"],
        icons=["info-circle", "graph-up"],
        menu_icon="house",
        default_index=0
    )

# Custom CSS for better styling
# Updated CSS for sub-header
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem !important;
        color: #1E3A8A;
        font-weight: 800;
        margin-bottom: 1rem;
        text-align: center;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #3B82F6;
        margin-bottom: 0.5rem; /* reduced to avoid spacing box */
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)



# Load the model and scaler (place this outside the form to avoid reloading)
@st.cache_resource
def load_model():
    try:
        model = joblib.load('../model/random_forest_model.pkl')
        scaler = joblib.load('../model/scaler.pkl')
        return model, scaler, True
    except FileNotFoundError:
        return None, None, False

model, scaler, model_loaded = load_model()

# About Project page
if selected == "About Project":

    st.markdown('<h1 class="main-header">Insurance Cross-Sell Prediction</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Enhancing targeted marketing with machine learning</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Overview - Business Aspect</h2>', unsafe_allow_html=True)
    st.markdown("""
    * Cross-selling in insurance is the practice of promoting products that are complementary to the policies that existing customers already own.
    * The goal of cross-selling is to create a win-win situation where customers can obtain comprehensive protection at a lower bundled cost, while insurers can boost revenue through enhanced policy conversions.
    * The aim of this project is to build a predictive ML pipeline (on the Health Insurance Cross-Sell dataset) to identify health insurance customers who are interested in purchasing additional vehicle insurance, in a bid to make cross-sell campaigns more efficient and targeted.
    """)
    
    st.markdown('<h2 class="section-header">Objective</h2>', unsafe_allow_html=True)
    st.markdown("""
    * Make cross-selling more efficient and targeted by building a predictive ML pipeline to identify health insurance customers interested in purchasing additional vehicle insurance.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    
    # Section header
    st.markdown('<h2 class="section-header">How It Works</h2>', unsafe_allow_html=True)

    # Show the workflow diagram image
    st.image("../workflow.png", caption="Machine Learning Workflow", width= 500)

# Prediction page
elif selected == "Prediction":
    st.markdown('<h1 class="main-header">Insurance Cross-Sell Prediction</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Enter customer details to predict interest in vehicle insurance</p>', unsafe_allow_html=True)
    
    # Create a form
    with st.form(key="insurance_form"):
        st.markdown('<h2 class="section-header">Customer Information</h2>', unsafe_allow_html=True)
        
        # Create two columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            gender = st.selectbox("Gender", ["Male", "Female"])
            age = st.number_input("Age", min_value=18, max_value=100, step=1)
            driving_license = st.selectbox("Driving License", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
            region_code = st.number_input("Region Code", min_value=0, step=1)
            previously_insured = st.selectbox("Previously Insured", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
            
        with col2:
            vehicle_age_option = st.selectbox(
                            "Vehicle Age",
                            options=["< 1 Year", "1-2 Year", "> 2 Years"])
            vehicle_damage = st.selectbox("Vehicle Damage", ["Yes", "No"])
            annual_premium = st.number_input("Annual Premium", min_value=0.0, step=100.0)
            policy_sales_channel = st.number_input("Policy Sales Channel", min_value=0, step=1)
            vintage = st.number_input("Vintage (days)", min_value=0, step=1)
        
        submit_button = st.form_submit_button(label="Predict Interest")

    # Handle form submission
    if submit_button:
        # Map values for prediction
        vehicle_age_map = {
            "< 1 Year": 0,
            "1-2 Year": 1,
            "> 2 Years": 2
        }
        
        # Create dictionary of entered values
        data = {
            "Gender": gender,
            "Age": age,
            "Driving_License": driving_license,
            "Region_Code": region_code,
            "Previously_Insured": previously_insured,
            "Vehicle_Age": vehicle_age_option,
            "Vehicle_Damage": vehicle_damage,
            "Annual_Premium": annual_premium,
            "Policy_Sales_Channel": policy_sales_channel,
            "Vintage": vintage
        }
        
        # Convert to DataFrame for display
        display_df = pd.DataFrame([data])
        
        # Create a copy for prediction processing
        prediction_data = data.copy()
        
        # Process data for prediction
        prediction_df = pd.DataFrame([prediction_data])
        prediction_df['Vehicle_Age'] = prediction_df['Vehicle_Age'].map(vehicle_age_map)
        prediction_df['Gender'] = prediction_df['Gender'].map({'Male': 1, 'Female': 0})
        prediction_df['Vehicle_Damage'] = prediction_df['Vehicle_Damage'].map({'Yes': 1, 'No': 0})
        
        # Display the entered information
        st.markdown('<h2 class="section-header">Customer Details</h2>', unsafe_allow_html=True)
        st.write(display_df)
        
        if model_loaded:
            try:
                # Scale the input and make prediction
                data_scaled = scaler.transform(prediction_df)
                prediction = model.predict(data_scaled)
                prediction_proba = model.predict_proba(data_scaled)
                
                # Display prediction results
                st.markdown('<h2 class="section-header">Prediction Results</h2>', unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Predicted Response", "Interested" if prediction[0] == 1 else "Not Interested")
                with col2:
                    st.metric("Probability of Interest", f"{prediction_proba[0][1]:.2%}")
                
                # Visualization of the probability
                st.markdown("#### Interest Probability")
                st.progress(float(prediction_proba[0][1]))
                
                if prediction[0] == 1:
                    st.success("This customer is likely to be interested in vehicle insurance. Consider including them in your cross-sell campaign.")
                else:
                    st.info("This customer is less likely to be interested in vehicle insurance. You may want to focus your cross-sell efforts elsewhere.")
                    
            except Exception as e:
                st.error(f"Error making prediction: {e}")
        else:
            st.warning("Model not loaded. Cannot make predictions.")

# Add footer
st.markdown("---")
st.markdown("© 2025 Insurance Cross-Sell Prediction Tool | All Rights Reserved")