import pandas as pd

# Encode categorical variables
def encode_categorical_variables(data):
    categorical_columns = data.select_dtypes(include=['object', 'category']).columns
    return pd.get_dummies(data, columns=categorical_columns, drop_first=True)