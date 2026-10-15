# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details
**Project Title:** Student Performance Analytics System  
**Student Name:** Ashish Kumar  
**Course:** B.Tech Computer Science and Engineering  
**College:** Maharana Pratap Engineering College, Kanpur

## 2. Objective
The objective of this project is to use Python to organize student marks and attendance and turn them into a clear performance summary. It helps identify strong subject areas, students who may need support, and the overall class result.

## 3. Technologies Used
- Python for program logic, functions, loops, and conditions
- Pandas for reading CSV data, organizing records, filtering, grouping, and summaries
- NumPy for numerical operations and attendance status calculation
- CSV for storing the dataset and exported results

## 4. Dataset Description
The project uses a sample dataset containing 100 student records. The columns include Student_ID, Name, Department, marks in Python, Mathematics, English, Computer Science and Statistics, and Attendance. Marks are represented on a 0–100 scale and attendance is represented as a percentage. The data is sample data and is not an official student record.

## 5. Implementation
1. The program reads `students.csv` into a Pandas DataFrame.
2. It checks that the expected columns are present.
3. It calculates total marks and average marks across five subjects.
4. A reusable function assigns a grade from the student's average.
5. A student passes when every subject mark is at least 35; otherwise the result is Fail.
6. NumPy is used to classify attendance of 75% or more as Eligible and lower attendance as Low Attendance.
7. Pandas operations calculate class statistics, subject averages, top performers, and department summaries.
8. A menu allows the user to select the analysis to display.
9. The export option saves detailed student results and subject averages as CSV files.

## 6. Key Features
- Display all student records and calculated results
- Calculate total and average marks
- Assign grades and pass/fail status
- Show class average, highest and lowest average, and pass percentage
- Compare subject-wise averages
- Display the top 10 students
- Search by student ID or name
- Compare department performance
- Export analysis files

## 7. Output / Screenshots
Run `python main.py` in a terminal and choose menu options 2, 3, 4, 6, and 7 to view the summary, subject analysis, top students, department analysis, and saved files. Add screenshots of these outputs here after running the program on your computer.

## 8. Final Outcome
The project turns a CSV file into a readable performance report using Python, NumPy, and Pandas. It gives a quick overview of individual results, class performance, subject averages, attendance, and department summaries.

## 9. Challenges and Learning
The main tasks are keeping the dataset organized, applying the same grading rule to all records, and summarizing many rows without calculating each result manually. This project provides practice with reading CSV files, DataFrames, reusable functions, conditions, loops, filtering, grouping, and numerical operations.

## 10. GitHub Repository
https://github.com/ashish543kr/student-performance-analytics
