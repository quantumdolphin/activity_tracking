# 🗂️ File Creation Logger by Extension

This script helps you **search for files created after a specific date** on selected drives, **filter them by extension**, and **save the results to a CSV** for easy review or backup planning.

---

## 📌 Features

- Recursive search through one or more drives/directories
- Filter by any file extensions (e.g., `.sdf`, `.moe`, `.pdb`)
- Groups results by **creation date**
- Saves a clean CSV report with full paths
- Annotated and written in debug-friendly Python

---

## ✅ Use Case

Ideal for chemists, data managers, or IT teams who:
- Regularly download or generate structure files (e.g., MOE, PDB, SDF)
- Want to audit files created since a project began
- Need to log all recent files for reporting, backup, or submission

---

## 🛠️ Requirements

- Python 3.6+
- Works on Windows (tested with drive letters like `C:\`, `D:\`)
- No third-party packages needed (uses only standard library)

---

## 🚀 How to Run

### 1. **Edit the Script (if needed)**

Open `file_logger.py` and customize the following section:

```python
start_date = datetime.datetime(2025, 1, 5)
root_dirs = ["C:\\", "D:\\"]
extensions = ['.mae', '.moe', '.sdf', '.pdb', '.cif', '.mdb']
output_file = "filtered_files_created_since_2025-01-05.csv"
