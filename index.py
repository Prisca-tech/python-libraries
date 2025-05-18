import pandas as pandas
import numpy as numpy
import requests
import matplotlib.pyplot as plt

# Question 1
arr = numpy.arange(1, 11)
mean_val = numpy.mean(arr)
print("Mean of numbers 1 to 10:", mean_val)

# Question 2
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 95]
}
df = pandas.DataFrame(data)
print("\nSummary statistics:")
print(df.describe())

# question 3

# API endpoint for global COVID-19 data
url = "https://disease.sh/v3/covid-19/all"

response = requests.get(url)

#check if request was successful
if response.status_code == 200:
    data = response.json()
    print(f"🌍 Global COVID-19 Cases: {data['cases']}")
    print(f"🧪 Today's Cases: {data['todayCases']}")
    print(f"💀 Total Deaths: {data['deaths']}")
else:
    print("Failed to fetch COVID-19 data:", response.status_code)

# Question4 

# Plot a simple line graph
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

country = "Nigeria"
url = f"https://disease.sh/v3/covid-19/countries/{country}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"🇳🇬 COVID-19 in {country}:")
    print(f"   Cases: {data['cases']}")
    print(f"   Deaths: {data['deaths']}")
    print(f"   Recovered: {data['recovered']}")
else:
    print("Failed to fetch data:", response.status_code)
