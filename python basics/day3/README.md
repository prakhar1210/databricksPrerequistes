# Day 3 - Pandas and REST API Basics

This folder contains Day 3 practice for the Databricks Gen AI Associate certification. The work covers pandas fundamentals, working with CSV data, REST APIs, and a simple document-search example related to Gen AI concepts.

## Files

### `day3.py`

Introduces basic Databricks Gen AI concepts using a list of dictionaries:

- Databricks as a data and AI platform
- RAG (Retrieval-Augmented Generation)
- LLMs (Large Language Models)
- Accessing dictionary values inside a list

### `pandasBasic.py`

Introduces core pandas objects and operations:

- Importing pandas as `pd`
- Creating a DataFrame from a Python dictionary
- Creating a Series from a dictionary
- Selecting specific Series labels
- Checking the pandas version

### `pandasbasics1.py`

Loads `pandas_exercise_data.csv` and demonstrates:

- Reading a CSV file with `pd.read_csv()`
- Viewing rows with `head()`
- Accessing values with `.loc`
- Checking display options
- Inspecting columns, data types, and non-null counts with `info()`

### `restbasics.py`

Practices REST API calls with the `requests` library using JSONPlaceholder:

- Sending a GET request
- Reading JSON responses
- Printing user names and email addresses
- Sending a POST request with JSON data
- Checking HTTP status codes
- Handling request errors with `try`/`except`
- Using a request timeout and `raise_for_status()`

### `genairestapi.py`

Contains a small document-search example for Gen AI fundamentals:

- Stores Databricks, RAG, and MLflow documents
- Searches document titles and content
- Performs case-insensitive matching
- Returns and prints matching documents

## Data Files

### `employees_100.csv`

Contains 100 employee records with employee ID, name, age, department, experience, salary, city, AI skills, and performance score. It can be used to practice pandas filtering, sorting, grouping, aggregation, and calculated columns.

### `pandas_exercise_data.csv`

Contains workout data with duration, date, pulse, maximum pulse, and calories. It includes data-quality issues for cleaning practice:

- Missing dates
- Missing calorie values
- Duplicate rows
- An unusually large duration value
- Inconsistent date quoting and formatting
- Values that should be checked for validity

## Python Environment

The scripts use Python 3.11. Pandas and `requests` are installed in the configured environment.

Run a script from this folder with:

```powershell
C:/Python311/python.exe pandasBasic.py
C:/Python311/python.exe pandasbasics1.py
C:/Python311/python.exe restbasics.py
C:/Python311/python.exe genairestapi.py
```

## Next Steps

Continue learning pandas one topic at a time with `pandas_exercise_data.csv`:

1. Detect missing values with `isnull()` and `isna()`
2. Fill or remove missing values with `fillna()` and `dropna()`
3. Remove duplicates with `drop_duplicates()`
4. Convert dates with `pd.to_datetime()`
5. Detect and correct invalid values
6. Validate the cleaned DataFrame
