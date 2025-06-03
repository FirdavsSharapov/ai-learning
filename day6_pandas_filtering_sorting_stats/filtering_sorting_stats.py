# 📅 Day 6: Pandas - Filtering, Sorting, and Stats
# Focus: conditional filtering, sorting rows, and descriptive stats

import pandas as pd

# 🔹 Task 1: Load the DataFrame from 'people.csv'
df = pd.read_csv('people.csv')

# 🔹 Task 2: Filter rows where Score >= 90
print("\n -------- Task 2 --------")
filtered_score_df = df[df['Score'] >= 90]
print(filtered_score_df)


# 🔹 Task 3: Sort DataFrame by Age (ascending) and Score (descending)
print("\n -------- Task 3 --------")
sorted_values = df.sort_values(by=['Age', 'Score'], ascending=[True, False])
print(sorted_values)

# 🔹 Task 4: Print the average Age and Score
print("\n -------- Task 4 --------")
print("Average Age:", df['Age'].mean())
print("Average Score:", df['Score'].mean())

# 🔹 Task 5: Count how many people are from each city
print("\n -------- Task 5 --------")
count_ppl_by_city = df['City'].value_counts()
print(count_ppl_by_city)

# 🧠 Stretch Goal (Optional):
# Filter people who are older than 28 AND have a score >= 90
print("\n -------- Stretch Goal --------")
filtered_data = df[(df['Age'] > 28) & (df['Score'] >= 90)]
print(filtered_data)

# 👉 Use this space to write your code. Let me know if you'd like help understanding filtering or chaining operations.
