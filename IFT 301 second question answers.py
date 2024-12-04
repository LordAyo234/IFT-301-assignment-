import pandas as pd
import matplotlib.pyplot as plt

data = { "Sex":["Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male"],
"Height":[175, 158, 166, 175, 160, 165, 166, 170, 170, 184, 182, 180, 191, 189, 180, 170, 176, 185], "Breath_Held":[22.22, 30.57, 17.47, 22.39, 26.90, 36.85, 27.33, 29.55, 13.87, 60.75, 67.41, 42.19, 59.74, 52.61, 73.27, 59.09, 51.15, 58.32] }

df = pd.DataFrame(data)

# Histogram
plt.figure(figsize=(10,5))
plt.hist(df["Breath_Held"], bins=8, color='skyblue', edgecolor='black')
plt.title("Histogram of Breath Holding Times")
plt.xlabel("Breath Holding Time (s)")
plt.ylabel("Frequency")
plt.show()

# Dot plot
plt.figure(figsize=(10,6))
male_data = df[df["Sex"]=="Male"]
female_data = df[df["Sex"]=="Female"]
plt.scatter(["Male"]*len(male_data), male_data["Breath_Held"], color='blue', label='Male')
plt.scatter(["Female"]*len(female_data), female_data["Breath_Held"], color='pink', label='Female')
plt.title("Side-by-Side Dot Plot")
plt.ylabel("Breath Holding Time (s)")
plt.legend()
plt.show()
