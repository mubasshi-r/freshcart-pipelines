if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter, test

import json
import os
import pandas as pd

@data_exporter
def export_metrics_summary(metrics_df: pd.DataFrame, *args, **kwargs) -> str:
    """
    Custom block: Logs the evaluation metrics summary to a JSON report file.
    """
    summary_data = metrics_df.to_dict(orient='records')
    report = {
        "pipeline": "iris_classifier",
        "status": "success",
        "metrics": summary_data
    }
    
    output_path = "model_performance_summary.json"
    with open(output_path, "w") as f:
        json.dump(report, f, indent=4)
        
    print(f"Custom Block: Successfully exported metrics summary to {output_path}")
    return output_path

@test
def test_summary_file_exists(output_path, *args) -> None:
    """
    Test block: Ensure the summary report file was successfully created.
    """
    assert output_path is not None, "Output path is None"
    assert os.path.exists(output_path), "Performance summary JSON file was not created!"
    print("Custom Block Test: Summary file verification passed successfully!")