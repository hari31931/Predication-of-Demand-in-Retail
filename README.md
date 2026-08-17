# Demand-Forecasting-in-Retail

## Project Overview
This project focuses on predicting daily sales for retail stores using historical sales data and machine learning techniques. Accurate sales forecasting is critical for inventory management, staffing, and operational planning. By leveraging features such as date components, holidays, weekends, and cyclical patterns, this project builds predictive models to forecast sales for the next 30 days.

---

## Project Objectives
1. **Data Exploration and Cleaning:** Understand the dataset, detect missing values, and remove outliers.  
2. **Feature Engineering:** Extract meaningful features such as day, month, weekday, weekend, holidays, and cyclical month encoding.  
3. **Visualization:** Analyze patterns in sales across different dimensions (day, month, store, holidays) and detect outliers.  
4. **Model Development:** Compare multiple regression models (Linear, Lasso, Ridge, XGBoost) for accuracy.  
5. **Forecasting:** Predict sales for future dates to aid in business decision-making.  
6. **Export Results:** Save processed datasets and future predictions for reporting or integration.

---

## Dataset
The dataset `StoreDemand.csv` contains the following columns:
- `date`: The date of the sales record  
- `store`: Store ID  
- `sales`: Number of units sold  

**Notes:**
- Outliers with extremely high sales are removed to improve model performance.
- Holidays are flagged using the Indian public holiday calendar.  

---

## Feature Engineering
The following features are generated to improve model accuracy:

| Feature | Description |
|---------|-------------|
| `day` | Day of the month (1–31) |
| `month` | Month (1–12) |
| `weekday` | Day of the week (0=Monday, 6=Sunday) |
| `weekend` | Binary indicator (1 if Saturday/Sunday, 0 otherwise) |
| `holidays` | Binary indicator for public holidays |
| `m1`, `m2` | Sine and cosine transformations of the month for cyclical encoding |

---

## Exploratory Data Analysis (EDA)
- **Sales Distribution:** Histogram and KDE plots to understand distribution and skewness.  
- **Outlier Detection:** Boxplots used to detect extreme sales values.  
- **Trend Analysis:** Bar plots of average sales by day, month, weekday, and store.  
- **Correlation Analysis:** Heatmaps to detect highly correlated features (>0.8).  

EDA helps understand sales patterns and guides feature engineering.

---

## Modeling
The project trains and evaluates multiple regression models:

1. **Linear Regression** – Simple linear relationship between features and sales.  
2. **Lasso Regression** – Linear model with L1 regularization to reduce overfitting.  
3. **Ridge Regression** – Linear model with L2 regularization.  
4. **XGBoost Regressor** – Gradient boosting model that handles non-linear relationships and interactions effectively.  

**Evaluation Metric:**  
- Mean Absolute Error (MAE) is used to measure prediction accuracy.  
- The model with the lowest MAE on the validation set is selected for future predictions (usually XGBoost).

---

## Future Sales Prediction
- Predicts sales for the **next 30 days** for a selected store.  
- Generates future date features: day, month, weekday, weekend, holidays, cyclical month encoding.  
- Uses the trained XGBoost model to forecast future sales.  
- Output is saved as `future_sales_predictions.csv`.

---
## Innovation
This project introduces several innovative approaches to retail demand forecasting:

1. **Cyclical Feature Engineering**  
   - Months are encoded using **sine and cosine transformations** to capture cyclical seasonality.  

2. **Incorporation of Holidays & Weekends**  
   - Public holidays and weekends are flagged using the **Indian holiday calendar**, allowing the model to learn behavioral sales patterns.  

3. **Outlier Detection & Removal**  
   - Extreme sales values are automatically detected and removed to **reduce noise**, resulting in more robust predictions.  

4. **Multi-Model Evaluation**  
   - Multiple regression models (Linear, Lasso, Ridge, XGBoost) are compared to ensure **best performance**.  

5. **Future Prediction Pipeline**  
   - Generates a **ready-to-use 30-day forecast** for individual stores, including all feature transformations.  

6. **Modular & Scalable Architecture**  
   - Code is split into four Python modules (data loading, feature engineering, modeling, export), allowing **easy maintenance and extension**.  

7. **Visual Insights**  
   - Bar plots, histograms, and correlation heatmaps provide **actionable insights** into sales patterns.  

8. **Business Impact Focus**  
   - Predictions help **optimize inventory, reduce stockouts, and improve staffing decisions**, translating directly into cost savings.
     
---

## 📄 License

This project is licensed under the **MIT License**.See the  License file for details.

---

## 💻 Installation & Execution

Follow these steps to run the **Demand-Forecasting-in-Retail** project locally:

### 1. Download or Clone the Project

You can either:

* **Download ZIP:**

  1. Go to [Demand-Forecasting-in-Retail GitHub](https://github.com/Ashok-777/Demand-Forecasting-in-Retail)
  2. Click **Code → Download ZIP**
  3. Extract the ZIP to a folder on your computer

* **Or Clone with Git:**

```bash
git clone https://github.com/Ashok-777/Demand-Forecasting-in-Retail.git
cd Demand-Forecasting-in-Retail
```

---

### 2. Install Required Python Packages

Make sure you have **Python 3.x** installed. Then, install dependencies using `pip`:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost holidays
```

> ⚠️ Optional: If using **Google Colab**, most libraries are pre-installed; only `holidays` may need installation:

```python
!pip install holidays
```

---

### 3. Run the Project

You can execute the Python scripts in multiple ways:

* **From Command Line / Terminal:**

```bash
python demand_forecasting.py
```

* **From Google Colab:**

1. Open Google Colab.
2. Upload the project files.
3. Run each cell sequentially to load data, perform feature engineering, train models, visualize results, and generate forecasts.

The program will perform:

* **Data Cleaning & EDA**: Check for missing values, remove outliers, visualize trends.
* **Feature Engineering**: Create day, month, weekday, weekend, holiday, and cyclical month features.
* **Model Training & Evaluation**: Train Linear, Lasso, Ridge, and XGBoost regressors and compare MAE.
* **Future Forecasting**: Predict the next 30 days of sales for selected stores.
* **Export Results**: Save processed datasets and predictions as CSV files (`processed_StoreDemand.csv`, `future_sales_predictions.csv`).

---

### 4. CSV Dataset Format

The input CSV `StoreDemand.csv` should have the following structure:

```csv
date,store,sales
2023-01-01,1,120
2023-01-01,2,200
2023-01-02,1,150
```

> ⚠️ Ensure dates are in `YYYY-MM-DD` format and `sales` are numeric.

---

### 5. Optional: Visualizations

The project automatically generates:

* Average sales by store, month, day, weekday, weekend, holidays
* Sales distribution histograms and boxplots
* Correlation heatmaps for numeric features

These visualizations help understand patterns and improve forecasting accuracy.

---

<p align="center">
  © <a href="https://github.com/Ashok-777" target="_blank">Ashok-777</a> | Crafted with ❤️ and curiosity
</p>

---
