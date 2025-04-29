# combine_excel.py
import pandas as pd
from pathlib import Path

def combine_excels(input_dir: str, output_file: str):
    folder = Path(input_dir)
    all_files = list(folder.glob("*.xlsx"))

    if not all_files:
        print("No Excel files found in the directory.")
        return

    combined_df = None
    total_rows_expected = 0 

    for idx, file in enumerate(all_files):
        df = pd.read_excel(file, engine='openpyxl')
        if df.empty:
            continue 

        data_rows = len(df) - 1 #exclude headers
        total_rows_expected += data_rows 

        if idx == 0: 
            combined_df = df
        else:
            combined_df = pd.concat([combined_df, df.iloc[1:]], ignore_index=True)  # Skip header row

    actual_data_rows = len(combined_df) - 1
    
    print(f"Expected number of data rows (excluding headers): {total_rows_expected}")
    print(f"Actual number of combined rows: {actual_data_rows}")
    
    combined_df.to_excel(output_file, index=False)
    print(f"Combined Excel saved as: {output_file}")

if __name__ == "__main__":
    input_folder = "data"  # Change if needed
    output_filename = "combined.xlsx"
    combine_excels(input_folder, output_filename)
    