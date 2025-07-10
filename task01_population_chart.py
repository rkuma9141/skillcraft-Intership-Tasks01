task01_population_chart.py
import matplotlib.pyplot as plt

# Data from the chart
age_groups = ['0-20 Years', '21-44 Years', '45+ Years']
population_millions = [612, 673, 135]
percentages = [34.1, 37.3, 7.5]

# Create Bar Chart
plt.figure(figsize=(8, 5))
bars = plt.bar(age_groups, population_millions, color=['gold', 'blue', 'magenta'])

# Add percentage labels on top of bars
for bar, pct in zip(bars, percentages):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 10, f'{pct}%', ha='center', fontsize=12)

plt.title("India's Population Distribution by Age in 2022")
plt.xlabel("Age Groups")
plt.ylabel("Population (in Millions)")
plt.ylim(0, 800)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the output chart
plt.savefig("india_population_age_distribution.png")
plt.show()
