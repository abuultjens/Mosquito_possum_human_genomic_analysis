import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import sys

# Load data
df = pd.read_csv(sys.argv[1], header=None)
df.columns = ['position']

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 2))

# Create grey rectangle
rectangle = Rectangle((0, 0.45), 5600000, 0.1, facecolor="lightgrey")

# Create collection of rectangles and add to axes
pc = PatchCollection([rectangle], match_original=True)
ax.add_collection(pc)

# Plot SNP positions
plt.scatter(df['position'], [0.5]*len(df['position']), marker="v", color='black', s=30)

# Remove axes
ax.axis('off')

# Set limit of x-axis
plt.xlim(0, 5600000)

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig(sys.argv[2], format='pdf')
