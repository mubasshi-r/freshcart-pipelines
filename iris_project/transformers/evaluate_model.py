if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

@transformer
def evaluate(df: pd.DataFrame, *args, **kwargs) -> pd.DataFrame:
    """
    Evaluate the model predictions, computing the confusion matrix and metrics table.
    """
    y_true = df['target']
    y_pred = df['prediction']
    
    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    cm_df = pd.DataFrame(cm, index=['Actual 0', 'Actual 1', 'Actual 2'], 
                             columns=['Pred 0', 'Pred 1', 'Pred 2'])
    
    print("--- CONFUSION MATRIX ---")
    print(cm_df)
    
    # Return metrics summary dataframe
    metrics_summary = pd.DataFrame({
        'metric': ['accuracy', 'total_samples'],
        'value': [df['test_accuracy'].iloc[0], len(df)]
    })
    
    return metrics_summary