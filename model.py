import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("data/food_data.csv")

# Encode categorical columns
le_day = LabelEncoder()
le_meal = LabelEncoder()
le_weather = LabelEncoder()
le_event = LabelEncoder()

df["day"] = le_day.fit_transform(df["day"])
df["meal_type"] = le_meal.fit_transform(df["meal_type"])
df["weather"] = le_weather.fit_transform(df["weather"])
df["event"] = le_event.fit_transform(df["event"])

# Features & target
X = df[["day", "meal_type", "prepared_qty", "consumed_qty", "weather", "event"]]
y = df["surplus_qty"]

# Train model
model = RandomForestRegressor()
model.fit(X, y)

def predict_surplus(day, meal, prepared, consumed, weather, event):
    d = le_day.transform([day])[0]
    m = le_meal.transform([meal])[0]
    w = le_weather.transform([weather])[0]
    e = le_event.transform([event])[0]

    prediction = model.predict([[d, m, prepared, consumed, w, e]])
    return round(prediction[0], 2)