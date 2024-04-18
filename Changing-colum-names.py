'''
READ ME:
- This module contains the function `change_column_names`.

DESCRIPTION:
- `change_column_names` is a function that modifies the column names of a pandas DataFrame, converting them to either uppercase or lowercase based on the boolean parameter `to_uppercase`.
- The DataFrame is modified in-place and does not return a value.

PARAMETERS:
- `df` - a pandas DataFrame whose column names are to be modified.
- `to_uppercase` - a boolean value. If True, the column names are converted to uppercase. If False, they are converted to lowercase.

LIMITATIONS:
- The function assumes that the DataFrame's column names are strings. If they are not, an error may be raised.
- The function modifies the DataFrame in-place. If the original DataFrame needs to be preserved, a copy should be made before calling this function.

STRUCTURES:
- An if-else construct is used to decide whether to convert the column names to uppercase or lowercase based on the `to_uppercase` parameter.

OUTPUT:
- The function does not have a return statement as it modifies the DataFrame in-place.
- The function does not contain any print statements. Any changes made to the DataFrame can be viewed by printing the DataFrame after calling the function.
'''


import pandas as pd

def change_column_names(df, to_uppercase):
    if to_uppercase:
        df.columns = df.columns.str.upper()
    else:
        df.columns = df.columns.str.lower()


# Test Code for change_column_names()
df = pd.DataFrame({'Name': ['John', 'Alice'], 'Age': [25, 30]})
print("Before:")
print(df)

change_column_names(df, True)
print("After changing to uppercase:")
print(df)

change_column_names(df, False)
print("After changing to lowercase:")
print(df)