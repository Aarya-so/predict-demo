import psycopg2
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="ap@calculas",
    host="localhost",
    port="5432"
)

# Load data from PostgreSQL
query = """
    SELECT arrivals_tonnes, max_price, commodity, district_name, modal_price 
    FROM commodity_data
    WHERE arrivals_tonnes IS NOT NULL AND max_price IS NOT NULL 
          AND commodity IS NOT NULL AND district_name IS NOT NULL 
          AND modal_price IS NOT NULL;
"""
df = pd.read_sql(query, conn)

# Encode categorical variables
from sklearn.preprocessing import LabelEncoder

le_commodity = LabelEncoder()
le_district = LabelEncoder()

df["commodity"] = le_commodity.fit_transform(df["commodity"])
df["district_name"] = le_district.fit_transform(df["district_name"])

# Features and target variable
features = ["arrivals_tonnes", "max_price", "commodity", "district_name"]
target = "modal_price"

X = df[features]
y = df[target]

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model and encoders
with open("randome_commodity.pkl", "wb") as file:
    pickle.dump((model, le_commodity, le_district), file)

print("Model trained and saved successfully!")
