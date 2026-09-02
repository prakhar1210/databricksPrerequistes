import pandas as pd

df = pd.read_csv('pandas_exercise_data.csv')

# print(df.to_string())

# print(df.head(10))  # Display the first 10 rows of the DataFrame

# print(df.loc[0, 'Pulse'])  # Access the value at row label 0 and column label 'Pulse'

print(pd.options.display.max_rows)

print(df.info())  # Display information about the DataFrame, including column names, data types, and non-null counts