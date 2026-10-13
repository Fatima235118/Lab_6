import pandas as pd
import matplotlib.pyplot as plt

# Create a messy 15-day weather log with one duplicate row
data = {
    "Date": [
        "2026-09-01", "2026-09-02", "2026-09-03",
        "2026-09-04", "2026-09-05", "2026-09-06",
        "2026-09-07", "2026-09-08", "2026-09-09",
        "2026-09-10", "2026-09-11", "2026-09-12",
        "2026-09-13", "2026-09-14", "2026-09-15",
        "2026-09-01"
    ],
    "City": [
        " Islamabad ", "LAHORE", "karachi ", "Islamabad",
        " lahore", "KARACHI", "Islamabad ", "LAHORE ",
        "karachi", " ISLAMABAD", "Lahore", "KARACHI ",
        "islamabad", " LAHORE ", "Karachi", " Islamabad "
    ],
    "Temperature": [
        "32C", "35C", "34C", "31C", "36C",
        "33C", "30C", "34C", "35C", "29C",
        "37C", "32C", "31C", "36C", "33C", "32C"
    ],
    "Humidity": [
        55, 60, None, 58, 65, 62, None, 57,
        63, 52, 68, None, 56, 64, 61, 55
    ],
    "Condition": [
        "sunny", " CLOUDY", "Rainy ", "SUNNY",
        "cloudy ", " RAINY", "Sunny ", "CLOUDY",
        " rainy ", "sunny", "CLOUDY ", "Rainy",
        " SUNNY", "cloudy", "RAINY ", " SUNNY "
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Clean text columns
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()

# Clean Temperature and convert it to numeric
df["Temperature"] = (
    df["Temperature"]
    .str.replace("C", "", regex=False)
    .astype(float)
)

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Remove duplicate rows
df = df.drop_duplicates().copy()

print("\nRows after dropping duplicates:", len(df))

# Fill missing Humidity values with the median
humidity_median = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(humidity_median)

print("Missing Humidity filled with median:", humidity_median)

# One-hot encode Condition
df_encoded = pd.get_dummies(
    df, columns=["Condition"], dtype=int
)

print("\nOne-Hot Encoded Condition Columns:")
print(df_encoded.filter(like="Condition_").head())

# Print cleaned dataset
print("\nCleaned Weather Dataset:")
print(df)

# Calculate correlation
correlation = df["Temperature"].corr(df["Humidity"])
print("\nCorrelation (Temperature, Humidity):", round(correlation, 2))

# Create the required 2 x 2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Line chart: Temperature over Date
axes[0, 0].plot(
    df["Date"], df["Temperature"], marker="o"
)
axes[0, 0].set_title("Temperature Over Date")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", rotation=45)
axes[0, 0].grid(True, alpha=0.3)

# 2. Scatter plot: Temperature vs Humidity
axes[0, 1].scatter(
    df["Temperature"], df["Humidity"]
)
axes[0, 1].set_title("Temperature vs Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity (%)")
axes[0, 1].grid(True, alpha=0.3)

# 3. Pie chart: Weather condition counts
condition_counts = df["Condition"].value_counts()
axes[1, 0].pie(
    condition_counts.values,
    labels=condition_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 0].set_title("Weather Condition Distribution")

# 4. Histogram: Temperature distribution
axes[1, 1].hist(
    df["Temperature"], bins=5, edgecolor="black"
)
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")

fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout()
plt.savefig("weather_dashboard.png", dpi=150)
plt.show()

print("\nSaved weather_dashboard.png")
