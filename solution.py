import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    
    # Check arguments datatypes
    if not isinstance(df, pd.DataFrame) or not isinstance(role, str) or not isinstance(new_column, str):
        return pd.DataFrame() 

    # Check 
    if not re.fullmatch(r'^[a-zA-Z_]+$', new_column):
        return pd.DataFrame()
    
    # Check role expression. Acceptable format = col_1 [* OR + OR -] col_2
    # Delete spaces for easier parsing
    clean_role = role.replace(" ", "")
    if not re.fullmatch(r'([a-zA-Z_]+(?:[+\-*][a-zA-Z_]+)+)', clean_role):
        return pd.DataFrame()

    # Get all potential columns from role expression
    cols = re.findall(r'[a-zA-Z_]+', clean_role)

    # Check if all potential columns are in original DataFrame
    for col in cols:
        if col not in df.columns:
            return pd.DataFrame()
    
    # Return empty DataFrame if we want to add column that already exist.
    if new_column in df.columns:
        return pd.DataFrame()
    
    try:
        # Keep original DataFrame as is
        result_df = df.copy()
        
        # Expression for pd.eval func
        expression = f"{new_column} = {role}"
        
        # Apply eval
        result_df = result_df.eval(expression)
        
        return result_df
        
    except Exception:
        return pd.DataFrame()