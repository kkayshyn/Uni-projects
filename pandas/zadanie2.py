import pandas as pd

#ZADANIE 6
weather = pd.read_csv("weather.csv")
print(weather)

weather = weather.drop(columns=["Location"])

weather["Date"] = pd.to_datetime(weather["Date"])

print(weather.info())
print("\nOstatnie 7 wierszy:")
print(weather.tail(7))

#ZADANIE 7
weather["RainToday"] = weather["RainToday"].map({"Yes": True, "No": False})
weather["RainTomorrow"] = weather["RainTomorrow"].map({"Yes": True, "No": False})

wind_cols = ["WindGustDir", "WindDir9am", "WindDir3pm"]

for col in wind_cols:
    weather[col] = weather[col].astype("category")

print(weather.info())

luty_2008 = weather[
    (weather["Date"] >= "2008-02-01") &
    (weather["Date"] <= "2008-02-10")
]

print(luty_2008)

south_west = weather[
    weather["WindDir9am"].isin(["SW", "SSW", "WSW"])
]

print(south_west)
