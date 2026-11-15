if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
from sklearn.datasets import load_iris
import pandas as pd

@data_loader
def load_data(*args, **kwargs):
    """
    Load the Iris dataset as a pandas DataFrame.
    """
    iris = load_iris(as_frame=True)
    df = iris.frame
    return df