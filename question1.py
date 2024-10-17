# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 
def temperature_classifier(temp):
    if temp < 0:
        return "Freezing"
    elif 0 <= temp <= 10:
        return "Cold"
    elif 11 <= temp <= 20:
        return "Moderate"
    elif 21 <= temp <= 30:
        return "Warm"
    else:
        return "Hot"
temperature = float(input("Enter the temperature in °C: "))
category = temperature_classifier(temperature)
print(f"The temperature is classified as: {category}")
