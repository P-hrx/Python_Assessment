import pandas as pd
import os
from src.configs.schemas import CUSTOMER_SCHEMA, SALES_SCHEMA , PRODUCT_SCHEMA
from src.configs.file_configs import CONFIGS
from datetime import date

def validate_data(source_name, dataframe):
    #TDOO: Add validation logic here
    # Added validation logic #Ticket MIDP-313
    try:
        clean_rows, error_rows = validate_dataframe(source_name,dataframe)
    except ValueError as e:
        print(e)
    return clean_rows, error_rows

def generate_validation_rules(source_name): # Validation Rule creation function #Ticket MIDP-313
    """
    Generate validation rules dynamically based on column information.
    :param columns_info: A dictionary where keys are column names and values are expected data types or rules.
    :return: A dictionary of validation rules.
    """
    validation_rules = {}
    config = CONFIGS[source_name]
    schema_details = config['schema']
    # Create a lambda function for each column to validate its type
    for details in schema_details:
        if details.get("required") == True:
            validation_rules[details['name']] = lambda x, dtype = details['type'] : type(x) == dtype
    return validation_rules

# Apply validation rules to the DataFrame #Ticket MIDP-313
def validate_dataframe(source_name,dataframe):
    """
    Validate a DataFrame based on dynamically generated rules.
    :param df: The DataFrame to validate.
    :param rules: A dictionary of validation rules.
    :return: None. Raises an error if validation fails.
    """
    rules = generate_validation_rules(source_name)
    invalid_columns = {}
    for column, rule in rules.items():
        # Check if the column exists
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' not found in the DataFrame.")
        
        # Apply the validation rule get error values #Ticket MIDP-313
        
        dataframe['validation_result'] = dataframe.apply(lambda row: validate_row(row, rules), axis=1)
    # Filter from the if row is valid #Ticket MIDP-313
    dataframe['is_valid'] = dataframe['validation_result'].apply(lambda results: all(results.values()))

    # Separate valid and invalid rows #Ticket MIDP-313
    clean_rows = dataframe[dataframe['is_valid'] == True]
    error_rows = dataframe[dataframe['is_valid'] == False]

    clean_rows = clean_rows.drop(['validation_result', 'is_valid'], axis=1)
    error_rows = error_rows.drop(['validation_result', 'is_valid'], axis=1)

    return clean_rows, error_rows

# Function to validate a single row #Ticket MIDP-313
def validate_row(row,rules):
    validation_results = {}
    for col, rule in rules.items():
        value = row[col]
        validation_results[col] = rule(value)  # Apply the rule to the value
    return validation_results