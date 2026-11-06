if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
data_loader, *args, **kwargs:
    # If using dataframe directly
    df = kwargs.get('df', data_loader)
    # Simple train/test split column addition for the iris dataset
    import pandas as pd
    import numpy as np
    
    np.random.seed(42)
    shuffled = df.sample(frac=1, random_state=42)
    # 120 train, 30 test (80-20 split)
    shuffled['split'] = ['train'] * 120 + ['test'] * 30
    return shuffled

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'