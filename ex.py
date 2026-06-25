import pandas as pd
import matplotlib.pyplot as plt

# Your Details
name = "Prathamesh Jotiram Magar"
roll_no = "AI(B)-40"

# Load dataset - PUT THE CORRECT PATH TO YOUR CSV FILE HERE
file_path = r"C:\Python Learning\Observation_well_locations_03122025.csv"
data = pd.read_csv(file_path, encoding='latin1')

# Select numeric data
numeric_data = data.select_dtypes(include=['number'])
subset = numeric_data.iloc[:25]

# X and Y
x = subset.index + 1
y = subset.iloc[:, 0]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', color='green')

# FORCE GRAPH FROM ORIGIN
plt.xlim(0, 26)
plt.ylim(0, max(y) + 2)

# Labels
plt.xlabel("Observation Number")
plt.ylabel("Water Level (ft)")
plt.title("Environmental Data Graph")

# SCALE
plt.xticks(range(0, 26, 2))
plt.yticks(range(0, int(max(y)) + 3, 2))

# Grid
plt.grid(True, linestyle='--', alpha=0.7)

# SCALE TEXT ON GRAPH
plt.text(0.02, 0.95,
         "Scale:\nX-axis: 1 cm = 2 observations\nY-axis: 1 cm = 2 ft",
         transform=plt.gca().transAxes,
         fontsize=10,
         verticalalignment='top',
         bbox=dict(facecolor='white', alpha=0.8))

# Name & Roll No
plt.figtext(0.5, 0.01,
            f"Name: {name} | Roll No: {roll_no}",
            ha='center', fontsize=11)

plt.tight_layout()
plt.show()