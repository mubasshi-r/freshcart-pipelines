if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

@transformer
def train_and_evaluate(df: pd.DataFrame, *args, **kwargs) -> pd.DataFrame:
    """
    Train a Decision Tree Classifier using max_depth from runtime variables.
    """
    max_depth = kwargs.get('max_depth', 2)
    if isinstance(max_depth, str):
        max_depth = int(max_depth)

    feature_cols = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    
    train_data = df[df['split'] == 'train']
    test_data = df[df['split'] == 'test']
    
    X_train = train_data[feature_cols]
    y_train = train_data['target']
    X_test = test_data[feature_cols]
    y_test = test_data['target']
    
    model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    result_df = test_data.copy()
    result_df['prediction'] = predictions
    result_df['test_accuracy'] = accuracy
    result_df['max_depth'] = max_depth
    
    return result_df

@test
def test_accuracy_passed(output, *args) -> None:
    """
    Ensure the test accuracy meets the minimum acceptable threshold.
    """
    accuracy = output['test_accuracy'].iloc[0]
    assert accuracy > 0.5, f"Model accuracy {accuracy} is too low!"