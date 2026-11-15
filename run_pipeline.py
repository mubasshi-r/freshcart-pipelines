import sys
import os
import pandas as pd

sys.path.append(os.path.abspath("iris_project"))

from data_loaders.load_iris import load_data
from transformers.prepare_data import transform as prepare_transform
from transformers.train_model import train_and_evaluate
from transformers.evaluate_model import evaluate as evaluate_model_block
from data_exporters.log_metrics_summary import export_metrics_summary, test_summary_file_exists

def run_part_c4():
    print("1. Loading Iris dataset...")
    df = load_data()
    
    print("2. Preparing and splitting data...")
    df_prepared = prepare_transform(df)
    
    print("3. Training model (max_depth=2)...")
    df_trained = train_and_evaluate(df_prepared, max_depth=2)
    
    print("4. Evaluating model...")
    metrics_summary = evaluate_model_block(df_trained)
    
    print("5. Running Custom Block (log_metrics_summary)...")
    output_path = export_metrics_summary(metrics_summary)
    
    print("6. Running Custom Block Test (@test)...")
    test_summary_file_exists(output_path)
    print("   -> Part C4 custom block and test executed successfully!")

if __name__ == "__main__":
    run_part_c4()