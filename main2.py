import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a Pandas DataFrame
#df = pd.read_csv(r'C:\Users\prest\OneDrive\Desktop\2023-11-23 10-16-38.csv')
df = pd.read_csv(r'C:\PS\logs\CTC-02 2023-11-30 11-44-50 small.csv')

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the first line chart
ax.plot(df['Time'], df['services(712)CPU'], label='line1')

# Plot the second line chart
#ax.plot(df['Time'], df['Aggregation(2748)CPU'], label='Aggregation(2748)CPU')

# Add a title and axis labels
ax.set_title('Title of Your Chart')
ax.set_xlabel('Time')
ax.set_ylabel('MEM/CPU')

# Add a legend
ax.legend()

# Display the chart
plt.show()
