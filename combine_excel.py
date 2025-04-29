import os
import pandas as pd


def read_excel_files(directory):
    """Read all Excel files in the specified
    directory and return a list of DataFrames."""
    data_frames = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(directory, file_name)
            try:
                df = pd.read_excel(file_path)
                data_frames.append(df)
                print(f"Read {len(df)} rows from {file_path}")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    return data_frames


def combine_data_frames(data_frames):
    """Combine multiple DataFrames into a single DataFrame."""
    combined_df = pd.concat(data_frames, ignore_index=True)
    return combined_df


def save_combined_excel(combined_df, output_path):
    """Save the combined DataFrame to an Excel file."""
    try:
        combined_df.to_excel(output_path, index=False)
        print(f"Combined file saved to {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")


def main():
    directory = 'data'  # Directory containing the Excel files
    output_file = 'combined.xlsx'  # Output file name

    data_frames = read_excel_files(directory)
    if not data_frames:
        print("No Excel files found in the directory. Exiting.")
        return

    combined_df = combine_data_frames(data_frames)
    expected_rows = sum(len(df) for df in data_frames)
    actual_rows = len(combined_df)

    print(f"Expected rows: {expected_rows}, Actual rows: {actual_rows}")

    save_combined_excel(combined_df, output_file)


if __name__ == "__main__":
    main()
