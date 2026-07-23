import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(page_title="SentimentAlpha | Financial Engine", layout="wide")

# --- Sidebar: Market Inputs ---
st.sidebar.title("📈 Market Intelligence")
ticker = st.sidebar.text_input("Ticker Symbol", "AAPL")
sources = st.sidebar.multiselect("Data Sources", 
    ["SEC Filings", "Earnings Transcripts", "News Sentiment", "Reddit/Social"], 
    default=["News Sentiment", "Reddit/Social"]
)
time_window = st.sidebar.select_slider("Analysis Window", options=["24h", "7d", "30d", "90d"], value="7d")
st.sidebar.divider()
st.sidebar.warning("Model Status: Live Inference Active")

# --- Main Dashboard ---
st.title("SentimentAlpha: Market Sentiment Engine")
st.subheader(f"Synthesized Psychological Signal for {ticker.upper()}")

# --- Top-Level Sentiment Gauge ---
col1, col2, col3 = st.columns([1, 1, 2])
sentiment_score = 72 # Mock data
col1.metric("Alpha Signal Score", f"{sentiment_score}/100", "Bullish")

# Radial Gauge for Sentiment
fig_gauge = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = sentiment_score,
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#2ecc71"}},
    title = {'text': "Market Sentiment Index"}
))
col2.plotly_chart(fig_gauge, use_container_width=True)

# --- Sentiment Trend ---
with col3:
    st.subheader("Sentiment vs Price Correlation")
    df_trend = pd.DataFrame({
        'Date': pd.date_range(start='2026-07-06', periods=7),
        'Sentiment': [60, 62, 65, 68, 70, 72, 71],
        'Price': [150, 152, 151, 155, 158, 160, 159]
    })
    fig_trend = px.line(df_trend, x='Date', y=['Sentiment', 'Price'], markers=True)
    st.plotly_chart(fig_trend, use_container_width=True)

# --- Data Source Breakdown ---
st.divider()
st.subheader("Multi-Source Sentiment Decomposition")
tabs = st.tabs(["SEC Filings", "Earnings", "News", "Social Media"])

with tabs[0]:
    st.write("Extracting sentiment from latest 10-Q...")
    st.info("Sentiment: Neutral. Focus on: Margin compression risk.")

with tabs[1]:
    st.write("Earnings Call Analysis...")
    st.progress(85)
    st.write("CEO Tone: Optimistic. Analyst Q&A sentiment: Cautious.")

with tabs[2]:
    st.table(pd.DataFrame({
        'Outlet': ['Bloomberg', 'Reuters', 'CNBC'],
        'Score': [0.8, 0.6, 0.4],
        'Impact': ['High', 'Med', 'Med']
    }))

with tabs[3]:
    st.write("Aggregated Reddit/Twitter Sentiment:")
    st.area_chart(pd.DataFrame(np.random.randn(20, 1), columns=["Social Buzz"]))

# --- Bottom Action ---
st.divider()
with st.container():
    st.subheader("AI Trade Signal")
    st.success("Recommendation: LONG position based on strong earnings sentiment convergence.")
    if st.button("Export Alpha Report to PDF"):
        st.balloons()

# --- Footer ---
st.divider()
st.caption("SentimentAlpha Engine | Synthesizing cross-asset market psychology | Powered by LLM-based Sentiment Analysis")