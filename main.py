import streamlit as st
import numpy as np 
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

@st.cache_resource
def generate_data_and_model(n_samples=100):
    np.random.seed(50)
    size = np.random.normal(1400, 50, n_samples)
    price = size * 50 + np.random.normal(0, 50, n_samples)
    df = pd.DataFrame({'size': size, 'price': price})
    X = df[['size']]
    Y = df['price']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, Y_train)
    return model, df

def main():
    st.title("🏡 Simple Linear Regression House Price Prediction")
    st.write("Enter your house size to estimate its price:")

    model, df = generate_data_and_model()

    size = st.number_input('House size (sq ft)', min_value=200, value=1500)

    if st.button('Predict price'):
        predicted_price = model.predict([[size]])
        st.success(f'Estimated price: ${predicted_price[0]:,.2f}')

        fig = px.scatter(df, x="size", y="price", title="Size vs House Price")
        fig.add_scatter(x=[size], y=[predicted_price[0]],
                        mode='markers',
                        marker=dict(size=15, color='red'),
                        name='Your Prediction')

        st.plotly_chart(fig)

if __name__ == '__main__':
    main()










