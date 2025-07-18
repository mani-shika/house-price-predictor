# House Price Predictor

Welcome to the **House Price Predictor** repository! This project leverages machine learning and a Streamlit-powered web application to predict house prices based on various features. Whether you're a data enthusiast, student, or real estate professional, this repository shows how predictive modeling can be applied to real-world housing data with an interactive user interface.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model](#model)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The House Price Predictor trains machine learning models to estimate the price of a house given its attributes (location, square footage, number of rooms, etc.). The project demonstrates the full pipeline: data preprocessing, feature engineering, model training, evaluation, and prediction — all accessible through a Streamlit web app.

## Features

- Data cleaning and preprocessing
- Exploratory data analysis (EDA) with visualizations
- Feature engineering and selection
- Multiple regression models (e.g., Linear Regression, Random Forest, XGBoost)
- Model evaluation and comparison
- Interactive Streamlit web app for predictions
- User-friendly input forms and visualization

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/mani-shika/house-price-predictor.git
    cd house-price-predictor
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare the data:**  
   Place your dataset in the `data/` directory. Make sure the format matches the expected input features.

2. **Train the model:**  
   Run the training script (replace with actual script name if different):
    ```bash
    python train.py
    ```

3. **Launch the Streamlit app:**  
    ```bash
    streamlit run app.py
    ```
   The app will open in your browser, allowing you to input house features and see predicted prices.

## Data

- The project uses housing data with features such as:
  - Location
  - Size (square footage)
  - Number of bedrooms and bathrooms
  - Year built
  - Amenities
- Sample datasets and instructions are provided in the `data/` folder.

## Model

- Various regression algorithms implemented and compared
- Model hyperparameter tuning for optimal performance
- Model artifacts saved in the `models/` directory

## Evaluation

- Performance metrics include RMSE, MAE, and R² score
- Visualization of predictions vs actual prices
- Model comparison results displayed in reports

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes
4. Push to your branch (`git push origin feature-name`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*If you have any questions, feel free to open an issue or contact the repository owner.*
