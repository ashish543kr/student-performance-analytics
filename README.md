# Student Performance Analytics System

## Project Overview
This Python project analyzes student marks and attendance. It calculates totals, averages, grades, pass/fail results, class statistics, subject averages, and department-level summaries.

## Technologies Used
- Python
- Pandas
- NumPy

## Dataset
The `students.csv` file contains 100 sample student records. Each record includes a student ID, name, department, marks in five subjects, and attendance percentage.

## Features
- Loads records from a CSV file using Pandas
- Calculates total and average marks
- Assigns grades using a fixed grading scale
- Marks a student as Pass when every subject mark is at least 35
- Displays class performance and attendance statistics
- Compares average marks by subject and department
- Lists the top 10 students
- Searches for students by ID or name
- Exports processed results to CSV files

## Grading Rule
- A+: 90 and above
- A: 80 to below 90
- B: 70 to below 80
- C: 60 to below 70
- D: 50 to below 60
- F: below 50

The grade is based on the average across the five subjects. A student passes only if the mark in every subject is at least 35.

## Requirements
Python 3.10 or later, Pandas, and NumPy.

Install the libraries:
```bash
python -m pip install pandas numpy
```

## Run the Project
Keep `main.py` and `students.csv` in the same folder, then run:
```bash
python main.py
```

Choose an option from the menu to view the analysis. Option 7 exports `student_results.csv` and `subject_summary.csv`.

## Files
- `main.py` — main program and reusable functions
- `students.csv` — sample dataset
- `Project_Documentation.md` — project documentation
- `requirements.txt` — required libraries

## Dataset Note
The student records are sample data for demonstration and do not represent actual students or official academic records.
