if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

import pandas as pd

@data_exporter
def export_data(df: pd.DataFrame, *args, **kwargs) -> None:
    """
    Export predictions to iris_predictions.csv.
    """
    df.to_csv('iris_predictions.csv', index=False)