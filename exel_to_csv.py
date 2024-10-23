import pandas as pd
import os
from tqdm import tqdm

def excel_to_csv(excel_path):
    excel_file = pd.ExcelFile(excel_path)    # Read the Excel file
    
    # Create a directory with the name of the Excel file (without extension) next to the original file
    base_dir = os.path.dirname(excel_path)
    output_dir = os.path.join(base_dir, os.path.splitext(os.path.basename(excel_path))[0])
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert each sheet to a CSV file with a progress bar
    for sheet_name in tqdm(excel_file.sheet_names, desc="Converting sheets"):
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
        csv_path = os.path.join(output_dir, f"{sheet_name}.csv")
        df.to_csv(csv_path, index=False)
        # print(f"Saved {csv_path}")
    
    # Print the input file path and the output folder at the end of the operation
    print("Input file path:", excel_path)
    print("Output folder:", output_dir)

if __name__ == "__main__":
    excel_path = r"C:\Users\morit\Desktop\WUR_Field_data_24.xlsx"
    excel_to_csv(excel_path)