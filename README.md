# FRED-Q1-2025-Challenge

**Live App:** [Live Link](https://fred-q1-2025-challenge.streamlit.app/)
This Streamlit app provides **probabilistic forecasts** for selected questions from the **Federal Reserve Economic Data (FRED) Q1 2025 Challenge** using **Monte Carlo simulations**. 

## 🔍 What This App Does
- Uses **Monte Carlo simulations** to generate probabilistic forecasts.
- Offers the **probability distribution** for the three questions I forecasted.

## ⚙️ How It Works
1. **Data Upload**: Download the data from the FRED website and upload it on the website.
2. **Select Forecast Date**: Choose the specific future date for which you want to generate a forecast. This sets the horizon for the Monte Carlo simulation.
3. **Choose number of simulations**:    Specify the number of Monte Carlo simulations you'd like to run. Higher values (e.g., 10,000+) generally yield more stable probability distributions but take slightly longer to compute.
4. 4. **Run Forecast & Visualize Results**: The app simulates thousands of potential futures based on historical trends and generates a probability distribution for the forecast variable. 
