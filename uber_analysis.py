import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("uber.csv")

# Display first records
print("\n===== UBER DATA ANALYSIS =====")
print(df.head())

# Total rides
print("\nTotal Rides:", len(df))

# Average fare
print("Average Fare:", round(df["Fare"].mean(), 2))

# Average distance
print("Average Distance:", round(df["Distance"].mean(), 2), "km")

# Most popular pickup city
popular_city = df["Pickup"].value_counts().idxmax()
print("Most Popular Pickup City:", popular_city)

# Highest fare ride
highest_fare = df["Fare"].max()
print("Highest Fare:", highest_fare)

# Ride count by city
city_rides = df["Pickup"].value_counts()

plt.figure(figsize=(6,4))
city_rides.plot(kind="bar")
plt.title("Number of Rides by City")
plt.xlabel("City")
plt.ylabel("Number of Rides")
plt.tight_layout()
plt.show()

# Fare distribution
plt.figure(figsize=(6,4))
plt.hist(df["Fare"], bins=5)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()