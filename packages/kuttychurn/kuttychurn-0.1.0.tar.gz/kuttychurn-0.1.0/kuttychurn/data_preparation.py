import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

# Load the E-Commerce Dataset
def load_data(filepath):
    return pd.read_excel(filepath)

# Handle missing values
def impute_missing_values(data, strategy='mean'):
    imputer = SimpleImputer(strategy=strategy)
    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
    data[numerical_columns] = imputer.fit_transform(data[numerical_columns])
    return data

# Data splitting
def split_data(data, target_column, test_size=0.3, random_state=42):
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test
