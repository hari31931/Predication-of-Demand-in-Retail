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

