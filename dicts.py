weather = {"city": "Москва", "temperature": 20}
print(weather["city"])
weather["temperature"] = weather["temperature"] - 5
print(weather)

print(weather.get("country", "Россия"))
weather = {"date": "27.05.2019"} | weather
print(len(weather))
print(weather)