import requests
import streamlit as st

# Your Finnhub API key
api_key = 'cumud0hr01qpmvdcv360cumud0hr01qpmvdcv36g'

# Function to fetch stock data
def fetch_stock_data(symbol):
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

# Streamlit app
st.set_page_config(page_title="Stock Price App", page_icon="📈", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .stTitle {
        color: #2c3e50;
        font-size: 3rem;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        background-color: #ecf0f1;
        border: 1px solid #bdc3c7;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        font-size: 1rem;
    }
    .stock-price {
        font-size: 1.5rem;
        font-weight: bold;
        color: #e74c3c;
    }
    .stock-data {
        font-size: 1.2rem;
        color: #34495e;
    }
    </style>
""", unsafe_allow_html=True)

st.title('📈 Stock Price App')
symbol = st.text_input('Enter a stock symbol:', placeholder='e.g., AAPL, TSLA')

if symbol:
    st.button('Get Stock Price')
    with st.spinner('Fetching stock data...'):
        stock_data = fetch_stock_data(symbol)
        if stock_data:
            st.markdown(f"<div class='stock-price'>Current Price: ${stock_data['c']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='stock-data'>Open: ${stock_data['o']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='stock-data'>High: ${stock_data['h']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='stock-data'>Low: ${stock_data['l']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='stock-data'>Previous Close: ${stock_data['pc']}</div>", unsafe_allow_html=True)
        else:
            st.write("No data found for the given stock symbol.")
