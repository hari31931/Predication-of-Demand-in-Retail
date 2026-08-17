# © Ashok-777
# GitHub: https://github.com/Ashok-777
# Part 3/4: Modeling, Evaluation & Future Prediction

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error as mae
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from datetime import timedelta
import numpy as np

# Assuming df is ready
X = df.drop(['sales'], axis=1)
y = df['sales'].values

# Train/Test Split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.05, random_state=22)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

# Define Models
models = [
    LinearRegression(),
    XGBRegressor(objective='reg:squarederror', random_state=42),
    Lasso(alpha=0.1),
    Ridge(alpha=1.0)
]
model_names = ['Linear Regression', 'XGBoost Regressor', 'Lasso Regression', 'Ridge Regression']

# Train & Evaluate
for i, model in enumerate(models):
    model.fit(X_train_scaled, y_train)
    print(f"\n🔍 {model_names[i]} Results:")

    train_preds = model.predict(X_train_scaled)
    val_preds = model.predict(X_val_scaled)

    print(f"Training MAE: {mae(y_train, train_preds):.2f}")
    print(f"Validation MAE: {mae(y_val, val_preds):.2f}")
    print('-' * 40)

# Choose best model
best_model = XGBRegressor(objective='reg:squarederror', random_state=42)
best_model.fit(X_train_scaled, y_train)

# Future Prediction for store 1 (next 30 days)
last_date = df.index.max()
future_dates = [last_date + timedelta(days=i) for i in range(1, 31)]

future_df = pd.DataFrame({
    'store': 1,
    'month': [d.month for d in future_dates],
    'day': [d.day for d in future_dates]
})

future_df['weekday'] = [d.weekday() for d in future_dates]
future_df['weekend'] = future_df['weekday'].apply(lambda x: 1 if x > 4 else 0)
future_df['holidays'] = [1 if d.strftime('%Y-%m-%d') in holidays.country_holidays('IN') else 0 for d in future_dates]
future_df['m1'] = np.sin(future_df['month'] * (2 * np.pi / 12))
future_df['m2'] = np.cos(future_df['month'] * (2 * np.pi / 12))

future_X_scaled = scaler.transform(future_df)
future_df['predicted_sales'] = best_model.predict(future_X_scaled)

print("\nFuture sales predictions for next 30 days:")
print(future_df[['store', 'month', 'day', 'predicted_sales']])
# © Ashok-777
# GitHub: https://github.com/Ashok-777
