import pandas as pd
import matplotlib.pyplot as plt

# Sample data (you can replace it with your own dataset)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 35, 28],
    'Salary': [50000, 60000, 45000, 75000, 55000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the dataset
print("Sample Dataset:")
print(df)

# Basic statistics summary
summary = df.describe()
print("\nStatistics Summary:")
print(summary)

# Data Visualization
plt.figure(figsize=(8, 4))

# Bar plot of Age
plt.subplot(1, 2, 1)
plt.bar(df['Name'], df['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age Distribution')

# Pie chart of Salary
plt.subplot(1, 2, 2)
plt.pie(df['Salary'], labels=df['Name'], autopct='%1.1f%%')
plt.title('Salary Distribution')

plt.tight_layout()

# Show the plots
plt.show()
