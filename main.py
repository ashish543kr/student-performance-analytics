import pandas as pd
import numpy as np

DATA_FILE = "students.csv"
SUBJECTS = ["Python", "Mathematics", "English", "Computer_Science", "Statistics"]

def load_data():
    try:
        data = pd.read_csv(DATA_FILE)
        required_columns = ["Student_ID", "Name", "Department"] + SUBJECTS + ["Attendance"]
        missing = [column for column in required_columns if column not in data.columns]
        if missing:
            raise ValueError("Missing columns: " + ", ".join(missing))
        return data
    except FileNotFoundError:
        print("students.csv was not found. Keep it in the same folder as main.py.")
        return None

def calculate_results(data):
    data = data.copy()
    data["Total"] = data[SUBJECTS].sum(axis=1)
    data["Average"] = data[SUBJECTS].mean(axis=1).round(2)
    data["Grade"] = data["Average"].apply(assign_grade)
    data["Result"] = data[SUBJECTS].ge(35).all(axis=1).map({True: "Pass", False: "Fail"})
    data["Attendance_Status"] = np.where(data["Attendance"] >= 75, "Eligible", "Low Attendance")
    return data

def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def show_student_records(data):
    columns = ["Student_ID", "Name", "Department"] + SUBJECTS + ["Attendance", "Total", "Average", "Grade", "Result"]
    print(data[columns].to_string(index=False))

def show_class_summary(data):
    print("\nCLASS SUMMARY")
    print("-" * 42)
    print(f"Number of students : {len(data)}")
    print(f"Class average      : {data['Average'].mean():.2f}")
    print(f"Highest average    : {data['Average'].max():.2f}")
    print(f"Lowest average     : {data['Average'].min():.2f}")
    print(f"Students passed    : {(data['Result'] == 'Pass').sum()}")
    print(f"Students failed    : {(data['Result'] == 'Fail').sum()}")
    print(f"Pass percentage    : {(data['Result'].eq('Pass').mean() * 100):.2f}%")
    print(f"Average attendance : {data['Attendance'].mean():.2f}%")

def show_subject_analysis(data):
    averages = data[SUBJECTS].mean().sort_values(ascending=False)
    print("\nSUBJECT-WISE AVERAGE")
    print("-" * 42)
    for subject, average in averages.items():
        print(f"{subject.replace('_', ' '):20} {average:.2f}")
    print(f"Best subject       : {averages.index[0].replace('_', ' ')}")
    print(f"Lowest subject     : {averages.index[-1].replace('_', ' ')}")

def show_top_students(data):
    top = data.sort_values(["Average", "Total"], ascending=False).head(10)
    print("\nTOP 10 STUDENTS")
    print("-" * 68)
    print(top[["Student_ID", "Name", "Department", "Average", "Grade", "Result"]].to_string(index=False))

def search_student(data):
    query = input("Enter student ID or name: ").strip()
    matches = data[
        data["Student_ID"].str.contains(query, case=False, na=False) |
        data["Name"].str.contains(query, case=False, na=False)
    ]
    if matches.empty:
        print("No matching student found.")
    else:
        show_student_records(matches)

def show_department_analysis(data):
    summary = data.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Average_Marks=("Average", "mean"),
        Average_Attendance=("Attendance", "mean"),
        Pass_Count=("Result", lambda values: (values == "Pass").sum())
    ).round(2)
    print("\nDEPARTMENT-WISE ANALYSIS")
    print("-" * 72)
    print(summary.to_string())

def save_results(data):
    data.to_csv("student_results.csv", index=False)
    subject_summary = data[SUBJECTS].mean().round(2).rename("Average_Marks").reset_index()
    subject_summary.columns = ["Subject", "Average_Marks"]
    subject_summary.to_csv("subject_summary.csv", index=False)
    print("Saved student_results.csv and subject_summary.csv.")

def main():
    raw_data = load_data()
    if raw_data is None:
        return
    data = calculate_results(raw_data)
    while True:
        print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
        print("1. Show all student records")
        print("2. Show class summary")
        print("3. Show subject-wise analysis")
        print("4. Show top 10 students")
        print("5. Search for a student")
        print("6. Show department-wise analysis")
        print("7. Save analysis files")
        print("8. Exit")
        choice = input("Choose an option (1-8): ").strip()
        if choice == "1":
            show_student_records(data)
        elif choice == "2":
            show_class_summary(data)
        elif choice == "3":
            show_subject_analysis(data)
        elif choice == "4":
            show_top_students(data)
        elif choice == "5":
            search_student(data)
        elif choice == "6":
            show_department_analysis(data)
        elif choice == "7":
            save_results(data)
        elif choice == "8":
            print("Project closed.")
            break
        else:
            print("Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()
