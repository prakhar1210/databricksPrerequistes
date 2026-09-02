# Day 3 - Pandas and Databricks Gen AI Basics

This folder contains Day 3 practice work for the Databricks Gen AI Associate certification preparation. The main focus is learning pandas, which is useful for loading, exploring, cleaning, and analyzing tabular data.

## What We Covered

### 1. Databricks Gen AI concepts

`day3.py` contains a small Python list of dictionaries with examples of:

- Databricks as a data and AI platform
- RAG (Retrieval-Augmented Generation)
- LLMs (Large Language Models)
- Accessing dictionary values inside a list

### 2. Creating pandas DataFrames

`pandasBasic.py` demonstrates:

- Importing pandas as `pd`
- Creating a DataFrame from a Python dictionary
- Creating a `Series` from a dictionary
- Selecting specific labels for a Series
- Creating a DataFrame with multiple columns
- Checking the installed pandas version

### 3. Loading and exploring CSV data

`pandasbasics1.py` loads `pandas_exercise_data.csv` with `pd.read_csv()` and practices:

- Displaying the first rows with `head()`
- Accessing a value with `.loc`
- Checking DataFrame settings with `pd.options.display.max_rows`
- Inspecting columns, data types, and non-null counts with `info()`

The `.loc` example uses a column label, such as `df.loc[0, 'Pulse']`. `.loc` is label-based, so a column name must exist in the DataFrame.

## Data Files

### `employees_100.csv`

A 100-row employee dataset containing:

- Employee ID and name
- Age and years of experience
- Department and city
- Salary
- AI skills score
- Performance score

This dataset will be useful for practicing filtering, sorting, grouping, aggregation, and creating calculated columns.

### `pandas_exercise_data.csv`

An exercise dataset containing workout information:

- `Duration`
- `Date`
- `Pulse`
- `Maxpulse`
- `Calories`

This file intentionally contains common data quality issues for pandas cleaning practice:

- Missing dates
- Missing calorie values
- Duplicate rows
- An unusually large duration value
- Inconsistent date quoting and formatting
- A pulse value that should be checked against the other data

## pandas Environment

Pandas was installed in the Python 3.11 environment. The scripts can be run with:

```powershell
C:/Python311/python.exe pandasBasic.py
C:/Python311/python.exe pandasbasics1.py
C:/Python311/python.exe day3.py
```

Run the commands from this `day3` folder.

## Next Learning Steps

We will work through the pandas cleaning functions one at a time using `pandas_exercise_data.csv`:

1. Detect missing values with `isnull()` and `isna()`
2. Fill or remove missing values with `fillna()` and `dropna()`
3. Remove duplicate rows with `drop_duplicates()`
4. Convert dates with `pd.to_datetime()`
5. Correct invalid or inconsistent values
6. Validate the cleaned DataFrame
