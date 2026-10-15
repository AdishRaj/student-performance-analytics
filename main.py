import pandas as pd
import numpy as np

from functions import assign_grade, check_result, calculate_total

# Load student data from CSV
df = pd.read_csv("students.csv")
# Calculate total marks for each student
df["Total_Marks"] = df.apply(calculate_total, axis=1)
df["Average_Marks"] = df[["Python", "Maths", "AI"]].mean(axis=1)
df["Percentage"] = df["Total_Marks"] / 300 * 100

df["Grade"] = df["Percentage"].apply(assign_grade)
df["Result"] = df.apply(check_result, axis=1)

# Display selected columns
print("\nStudent Marks Analysis:")
print(df[["Name", "Total_Marks", "Average_Marks", "Percentage"]].to_string(index=False))

# Function to assign grades
def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


# Apply the grading function
df["Grade"] = df["Percentage"].apply(assign_grade)

# Function to check pass or fail
def check_result(row):
    if (
        row["Python"] >= 35
        and row["Maths"] >= 35
        and row["AI"] >= 35
    ):
        return "Pass"
    else:
        return "Fail"


# Apply pass/fail logic
df["Result"] = df.apply(check_result, axis=1)

# Display results
print("\nGrade and Result Analysis:")
print(
    df[["Name", "Percentage", "Grade", "Result"]]
    .to_string(index=False)
)

# Overall class performance
class_average = df["Percentage"].mean()

# Subject-wise average marks
subject_averages = df[["Python", "Maths", "AI"]].mean()

# Count passed and failed students
pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()

print("\n--- Class Performance Summary ---")
print(f"Overall Class Average: {class_average:.2f}%")

print("\n--- Class Performance Summary ---")
print(f"Overall Class Average: {class_average:.2f}%")

print("\nSubject-wise Average Marks:")

subjects = ["Python", "Maths", "AI"]

for subject in subjects:
    average = df[subject].mean()
    print(f"{subject}: {average:.2f}")

print(f"\nTotal Students: {len(df)}")
print(f"Students Passed: {pass_count}")
print(f"Students Failed: {fail_count}")

# Top 3 students
top_students = df.sort_values(
    by="Percentage", ascending=False
).head(3)

print("\n--- Top 3 Students ---")
print(top_students[
    ["Name", "Total_Marks", "Percentage", "Grade"]
].to_string(index=False))

# Lowest performer
lowest_student = df.loc[df["Percentage"].idxmin()]

print("\n--- Lowest Performer ---")
print(lowest_student[
    ["Name", "Percentage", "Grade", "Result"]
])


# Find the student with the lowest percentage
lowest_student = df.loc[df["Percentage"].idxmin()]

print("\n--- Lowest Performing Student ---")
print(
    lowest_student[
        ["Name", "Percentage", "Grade", "Result"]
    ]
)

# Display the first five records
print("\nFirst 5 Student Records:")
print(df.head())

# Display dataset size
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Display data types and missing values
print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())