import pandas as pd
import matplotlib.pyplot as plt

names = [
    " fatima ", "ALI", " laiba", "YUMNA ",
    " ahmed", "SARA", " usman ", "AYESHA"
]

marks = ["85", "78", "92", "absent", "88", "76", "90", "82"]

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

df["Name"] = df["Name"].str.strip().str.title()
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("Cleaned Student Marks Dataset:")
print(df)

plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("marks_bar.png")
plt.show()
