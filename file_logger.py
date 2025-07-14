import os
import datetime
import csv
from pathlib import Path

def get_files_created_since(start_date, root_dirs, extensions):
    """
    Recursively search for files in given directories that were created on or after a specific date
    and match the provided file extensions.

    Args:
        start_date (datetime.datetime): The earliest creation date to include.
        root_dirs (list): List of root directories to search.
        extensions (list): File extensions to include (e.g., ['.sdf', '.moe']).

    Returns:
        dict: A dictionary mapping creation dates (MM/DD/YYYY) to lists of file paths.
    """
    files_dict = {}
    start_timestamp = start_date.timestamp()

    print(f"\n🔍 Searching for files created since {start_date.strftime('%m/%d/%Y')}")
    print(f"📂 Searching directories: {', '.join(root_dirs)}")
    print(f"📄 Filtering extensions: {', '.join(extensions)}\n")

    for root_dir in root_dirs:
        print(f"🔎 Walking through: {root_dir}")

        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)

                # Skip files that don't match extension filter
                if not any(filename.lower().endswith(ext) for ext in extensions):
                    continue

                try:
                    creation_time = os.path.getctime(file_path)
                    if creation_time >= start_timestamp:
                        creation_date = datetime.datetime.fromtimestamp(creation_time).strftime("%m/%d/%Y")

                        # Initialize list for this date if not already present
                        if creation_date not in files_dict:
                            files_dict[creation_date] = []

                        files_dict[creation_date].append(file_path)

                        print(f"✅ {file_path} (Created: {creation_date})")
                except (PermissionError, FileNotFoundError) as e:
                    print(f"⚠️ Skipping {file_path}: {e}")

    print("\n✅ File search completed.\n")
    return files_dict


if __name__ == "__main__":
    # -------- USER CONFIGURATION --------
    # Set the starting date
    start_date = datetime.datetime(2025, 1, 5)

    # Define root directories to scan
    root_dirs = ["C:\\", "D:\\"]

    # Specify allowed file extensions
    extensions = ['.mae', '.moe', '.sdf', '.pdb', '.cif', '.mdb']

    # Output CSV filename
    output_file = "filtered_files_created_since_2025-01-05.csv"
    # ------------------------------------

    # Collect matching files
    files_created = get_files_created_since(start_date, root_dirs, extensions)

    # Write results to CSV
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "File Paths"])

        for date, paths in sorted(files_created.items()):
            writer.writerow([date, ", ".join(paths)])
            print(f"📝 Wrote {len(paths)} file(s) for {date}")

    print(f"\n📁 Results saved to: {output_file}")
