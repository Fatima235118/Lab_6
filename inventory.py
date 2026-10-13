import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": [
        "Cola", "Chips", "Milk", "Biscuits", "Juice",
        "Yogurt", "Water", "Chocolate", "Cheese", "Tea"
    ],
    "Category": [
        " beverages ", "SNACKS", " Dairy", "Snacks ",
        "BEVERAGES", " dairy ", "Beverages ", " snacks",
        "DAIRY", " Beverages"
    ],
    "Price": [
        "Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120",
        "Rs. 1,800", "Rs. 300", "Rs. 50", "Rs. 200",
        "Rs. 600", "Rs. 700"
    ],
    "Stock": [40, 120, 60, 100, 30, 50, 150, 80, 35, 70]
}

df = pd.DataFrame(data)

df["Category"] = df["Category"].str.strip().str.title()

df["Price"] = (
    df["Price"]
    .str.replace("Rs. ", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["Category_Code"] = df["Category"].astype("category").cat.codes

print("Cleaned Inventory Dataset:")
print(df)

avg_price = df.groupby("Category")["Price"].mean()
stock_share = df.groupby("Category")["Stock"].sum()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(avg_price.index, avg_price.values)
axes[0].set_title("Average Price per Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")
axes[0].tick_params(axis="x", rotation=30)

axes[1].pie(
    stock_share.values,
    labels=stock_share.index,
    autopct="%1.1f%%"
)
axes[1].set_title("Share of Total Stock")

plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()

print("Saved inventory_plots.png")
