# © Ashok-777
# GitHub: https://github.com/Ashok-777
# Part 4/4: Export Data & Predictions to CSV

# Save processed training data
df.to_csv("../data/processed_StoreDemand.csv", index=False)
print("Processed data saved as 'processed_StoreDemand.csv'")

# Save future predictions
future_df.to_csv("../data/future_sales_predictions.csv", index=False)
print("Future sales predictions saved as 'future_sales_predictions.csv'")
# © Ashok-777
# GitHub: https://github.com/Ashok-777
