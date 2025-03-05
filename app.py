import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

def MCS(uploaded_file, column_name, target_date, num_simulations, bins):
    if uploaded_file is not None:
       df = pd.read_csv(uploaded_file)
       df['observation_date'] = pd.to_datetime(df['observation_date'])
       df[column_name] = pd.to_numeric(df[column_name])
       df = df.sort_values('observation_date').dropna()                       # Sorting in ascending order of time and dropping null values.
    
       df['Log Return'] = np.log(df[column_name]/df[column_name].shift(1))    # Calculating log returns.
       mean_returns = df['Log Return'].mean()
       std_returns = df['Log Return'].std()
    
       target_date = datetime.combine(target_date, datetime.min.time())       # Why this error?
       current_date = df['observation_date'].max()
       trading_days = np.busday_count(current_date.date(), target_date.date())
    
       current_rate = df[column_name].iloc[-1]
       simulated_rates = np.zeros((trading_days, num_simulations))
    
       for i in range(num_simulations):
           random_returns = np.random.normal(mean_returns, std_returns, trading_days)
           rate_path = current_rate * np.exp(np.cumsum(random_returns))
           simulated_rates[:, i] = rate_path
        
       predicted_rates = simulated_rates[-1:]     # Take the last row for the predictions. This corresponds to the value observed on the last day for all the runs computed.
    
       mean_predicted_rate = predicted_rates.mean()
       std_predicted_rate = predicted_rates.std()
    
       st.write(mean_predicted_rate)
       st.write(std_predicted_rate)
    
       labels = [f"{bins[i]}-{bins[i+1]}" for i in range(len(bins) - 1)]
       counts, _ = np.histogram(predicted_rates, bins=bins)
       probabilities = counts / num_simulations
       st.write("### Probability Distribution:")
       prob_df = pd.DataFrame({"Range": labels, "Probability": probabilities})
       st.dataframe(prob_df)
         
    

    
####    SIDEBAR INFORMATION    ####        
with st.sidebar:
    st.write('***')
    ques_option = st.selectbox("Select your question from the FRED Q1 2025 Challenge:",
                               ("What will be the closing value of the US dollar to Japanese yen exchange rate on 28 March 2025?",
                                "What will be the closing value of the S&P 500 Index on 31 March 2025?",
                                "What will be the spot price per barrel for West Texas Intermediate (WTI) crude oil on 31 March 2025?",
                               )
    ) 
    st.write('***')
    num_simulations = st.slider("🎲 Number of Simulations", 100, 50000, 10000, 100)
    target_date = st.sidebar.date_input("📅 Select Target Date", datetime(2025, 3, 28))
    st.write('***')
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
 
bins_data = {0: [0,132,136,140,144,148,152,156,160,164,168,np.inf],
             1: [0,5000,5250,5500,5750,6000,6250,6500,6750,7000,np.inf],
             2: [0,54,61,68,75,82,89,96,103,110,117,np.inf],
             }


if ques_option == "What will be the closing value of the US dollar to Japanese yen exchange rate on 28 March 2025?":
    st.title("Monte Carlo Simulation for USD/JPY Exchange Rate Prediction")
    MCS(uploaded_file, 'DEXJPUS', target_date, num_simulations, bins_data[0])
        
if ques_option == "What will be the closing value of the S&P 500 Index on 31 March 2025?":
    st.title("Monte Carlo Simulation for S&P 500 Index")
    MCS(uploaded_file, 'SP500', target_date, num_simulations, bins_data[1])
    
if ques_option == "What will be the spot price per barrel for West Texas Intermediate (WTI) crude oil on 31 March 2025?":
    st.title("Monte Carlo Simulation for WTI Crude Oil Spot Price")
    MCS(uploaded_file, 'DCOILWTICO', target_date, num_simulations, bins_data[2])
