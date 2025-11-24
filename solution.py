import pandas as pd
import re



fruits_sales = pd.DataFrame(
    {'name': ['banana','apple'],
     'quantity': [10,3],
     'price': [10,1]}
)

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame: