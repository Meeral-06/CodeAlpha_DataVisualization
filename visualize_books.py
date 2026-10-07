import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("books.csv")

# Map rating text to numbers for correlation
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["rating_num"] = df["rating"].map(rating_map)
rating_order = ["One", "Two", "Three", "Four", "Five"]

# Set visual theme
sns.set_theme(style="whitegrid")

# 1. Rating count
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="rating", order=rating_order, palette="viridis")
plt.title("Number of Books by Rating")
plt.savefig("01_rating_count.png", dpi=150, bbox_inches="tight")
plt.close()

# 2. Price histogram
plt.figure(figsize=(8, 5))
sns.histplot(df["price"], bins=25, kde=True, color="teal")
plt.title("Book Price Distribution")
plt.savefig("02_price_hist.png", dpi=150, bbox_inches="tight")
plt.close()

# 3. Price by rating
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="rating", y="price", order=rating_order, palette="Set2")
plt.title("Price Distribution by Rating")
plt.savefig("03_price_by_rating.png", dpi=150, bbox_inches="tight")
plt.close()

# 4. Scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="rating_num", y="price", alpha=0.6)
plt.title("Price vs Rating")
plt.savefig("04_price_vs_rating.png", dpi=150, bbox_inches="tight")
plt.close()

# 5. Correlation heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(df[["price", "rating_num"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation: Price and Rating")
plt.savefig("05_correlation.png", dpi=150, bbox_inches="tight")
plt.close()

# 6. Combined Dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.countplot(ax=axes[0, 0], data=df, x="rating", order=rating_order, palette="viridis")
axes[0, 0].set_title("Books by Rating")

sns.histplot(ax=axes[0, 1], data=df, x="price", bins=20, kde=True, color="teal")
axes[0, 1].set_title("Price Distribution")

sns.boxplot(ax=axes[1, 0], data=df, x="rating", y="price", order=rating_order, palette="Set2")
axes[1, 0].set_title("Price by Rating")

sns.scatterplot(ax=axes[1, 1], data=df, x="rating_num", y="price", alpha=0.6)
axes[1, 1].set_title("Price vs Rating")

plt.tight_layout()
plt.savefig("06_dashboard.png", dpi=150, bbox_inches="tight")
plt.close()

print("✅ All visualizations saved successfully.")