import pandas as pd

# Step 1: Load data from a CSV file
data = pd.read_csv("students.csv")

# Step 2: Show the first 5 rows
print("First 5 rows of data:")
print(data.head())

# Step 3: Filter students with marks greater than 75
high_scores = data[data["Marks"] > 75]

print("\nStudents with marks > 75:")
print(high_scores)

# Step 4: Calculate average marks
average_marks = data["Marks"].mean()
print(f"\nAverage marks of all students: {average_marks}")
