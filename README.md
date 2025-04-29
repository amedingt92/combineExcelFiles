# Excel Combiner Script

This Python script combines all `.xlsx` files from a given folder (in this case, anything you place in the data directory) into one single file. It only keeps the header row from the first file and appends just the data rows from subsequent files.

## 🛠️ Features
- Combines .xlsx files into a single Excel file
- Keeps only the header row from the first file
- Skips empty Excel files
- Ignores headers in subsequent files (after the first)
- Calculates and prints:
  - Expected number of data rows (excluding headers)
  - Actual number of combined rows (in the final 'combined.xlsx' file)

## ⚙️ Setting Up in VS Code
If you are using VS Code, here's how to get started setting everything up to run this script. 

### 1. Create a Virtual Environment
```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment 
Windows (PowerShell):
```bash
.venv\Scripts\Activate.ps1
```

Windows (CMD)
```bash
.venv\Scripts\activate.bat
```

macOS/Linux
```bash
source .venv/bin/activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Select the Python Interpreter in VS Code
- Press Ctrl + Shift + P (or Cmd + Shift + P on Mac)
- Search for Python: Select Interpreter 
- Choose the one that says .venv (should also indicate "Recommended")

### 5. Run the Script
You can now run the script in the VS Code Terminal:
```bash
python combine_excel.py
```


## 📥 Input
Place all the '.xlsx' files you want to combine in the 'data/' folder. 
Anything you drop into 'data/' will be included in the combined output (so don't forget to delete any files you don't want included before adding your own).

## 📁 Output
The combined file will be saved as:
```bash
combined.xlsx
``` 
