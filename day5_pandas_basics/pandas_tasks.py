# 📅 Day 5: Pandas Basics
# Focus: DataFrames, CSV loading, rows & columns

import pandas as pd

# 🔹 Task 1: Create a DataFrame from a dictionary with the following data:
# Name: ["Alice", "Bob", "Charlie"]
# Age: [25, 30, 35]
# City: ["NYC", "LA", "Chicago"]

user_data = {
  'Name': ["Alice", "Bob", "Charlie"],
  'Age': [25, 30, 35],
  'City': ["NYC", "LA", "Chicago"]
}

df = pd.DataFrame(user_data)

# 🔹 Task 2: Print the entire DataFrame, then print only the 'Name' column.
print(df)
print(df['Name'])
# 🔹 Task 3: Print the first and last row using head() and tail()
print(df.head(1))
print(df.tail(1))
# 🔹 Task 4: Add a new column called 'Score' with values [85, 90, 95]
df['Score'] =  [85, 90, 95]
# 🔹 Task 5: Filter and print rows where Age > 28
filtered_df = df[df['Age'] > 28]
print(filtered_df)

# 🧠 Stretch Goal (Optional):
# Save the DataFrame to a CSV file called "people.csv" and reload it
df.to_csv('people.csv', index=False)
csv_df = pd.read_csv('people.csv')
print(csv_df)

# 👉 Use this space below to write your code and test each task!
# Let me know when you'd like help reviewing your code or explaining anything.
