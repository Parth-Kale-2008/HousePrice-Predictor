# 🏡 Real Estate Price Predictor

An AI-powered machine learning application that predicts residential property prices based on important housing features such as area, number of bedrooms, bathrooms, property age, parking availability, and location score.

The project uses **XGBoost Regression** to estimate property prices and demonstrates how machine learning can support data-driven real estate analysis.

## 🚀 Project Overview

Property prices depend on several factors, including property size, location, amenities, and age. Estimating a reasonable price can be challenging when comparing multiple properties.

The Real Estate Price Predictor uses a trained machine learning model to analyze these features and generate an estimated property price.

## ✨ Features

- 🏠 **Price Prediction:** Estimate property prices using a trained regression model.
- 📐 **Area-Based Analysis:** Consider property area when generating predictions.
- 🛏️ **Property Features:** Account for bedrooms, bathrooms, property age, and parking.
- 📍 **Location Scoring:** Incorporate a numerical location score into the prediction.
- 🤖 **XGBoost Regression:** Apply gradient-boosted decision trees to a regression problem.
- 📊 **Data-Driven Estimation:** Use historical property data to learn pricing patterns.
- 🌐 **Deployment Ready:** Prepare the application for deployment using Streamlit Community Cloud.

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Data splitting and model evaluation |
| XGBoost | Price prediction model |
| Streamlit | Interactive web application |
| Joblib | Saving and loading trained models |

## 🏗️ Machine Learning Workflow

1. **Data Collection:** Load the property dataset.
2. **Data Preprocessing:** Inspect missing values and prepare the required features.
3. **Feature Selection:** Use the selected housing attributes.
4. **Train-Test Split:** Divide the data into training and testing sets.
5. **Model Training:** Train an XGBoost regression model.
6. **Model Evaluation:** Evaluate predictions against actual test-set prices.
7. **Price Prediction:** Accept property details and estimate the price.
8. **Deployment:** Make the application accessible through a web interface.

## 📂 Dataset Features

The project uses the following input features:

| Feature | Description |
|---|---|
| `Area_sqft` | Property area in square feet |
| `Bedrooms` | Number of bedrooms |
| `Bathrooms` | Number of bathrooms |
| `Age_years` | Age of the property |
| `Parking` | Parking availability or capacity |
| `Location_Score` | Numerical score representing location quality |

**Target variable:** `Price_INR` — the property's price in Indian rupees.

*Ensure that the column names match your actual dataset.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/real-estate-price-predictor.git
cd real-estate-price-predictor
```

Replace the URL with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install pandas numpy scikit-learn xgboost streamlit joblib
```

### 4. Run the application

If your Streamlit entry file is named `app.py`:

```bash
streamlit run app.py
```

If your entry file has another name, replace `app.py` with that filename.

## 🧠 Model Configuration

The model was developed using XGBoost Regression with the following configuration:

```python
XGBRegressor(
    random_state=42
)
```

The project workflow uses an 80/20 train-test split with `random_state=42`.

*Use the exact hyperparameters from your training script when documenting the final model.*

## 📈 Model Evaluation

For a meaningful evaluation, report metrics such as:

- **MAE (Mean Absolute Error):** Average absolute difference between predicted and actual prices.
- **RMSE (Root Mean Squared Error):** Penalizes larger prediction errors more heavily.
- **R² Score:** Measures how well the model explains variation in property prices.

Add the actual measured values after running the evaluation. Do not report unverified accuracy figures.

## 🔮 Future Enhancements

- Interactive property-price dashboard
- Geographic maps and neighborhood comparisons
- Real-time property listings integration
- Model comparison with Random Forest and Linear Regression
- Improved location-based features
- Model performance and error visualizations
- Cloud deployment with a public demo

## ⚠️ Disclaimer

Predictions are estimates based on the dataset and trained model. They are not professional property valuations, legal advice, or guarantees of market price. Actual prices can vary with market conditions, property condition, and local demand.

## 👨‍💻 Author

**Parth Kale**

B.Tech Student | AI/ML | Machine Learning | Full-Stack Development

GitHub: https://github.com/YOUR-USERNAME

## 📄 License

Add a `LICENSE` file to specify how others may use, modify, and distribute this project.
