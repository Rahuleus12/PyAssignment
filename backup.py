import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    try:
        # Check if source directory exists
        if not os.path.exists(source_dir):
            print(f"Error: Source directory '{source_dir}' does not exist.")
            return

        # Check if destination directory exists, if not, create it
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Iterate through all files in the source directory
        for root, _, files in os.walk(source_dir):
            for file_name in files:
                source_file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(root, source_dir)
                dest_sub_dir = os.path.join(dest_dir, relative_path)

                # Ensure the sub-directory in destination exists
                if not os.path.exists(dest_sub_dir):
                    os.makedirs(dest_sub_dir)

                dest_file_path = os.path.join(dest_sub_dir, file_name)

                # If the file exists in destination, append a timestamp to the name
                if os.path.exists(dest_file_path):
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    file_name_without_ext, file_ext = os.path.splitext(file_name)
                    new_file_name = f"{file_name_without_ext}_{timestamp}{file_ext}"
                    dest_file_path = os.path.join(dest_sub_dir, new_file_name)

                # Copy the file
                shutil.copy2(source_file_path, dest_file_path)
                print(f"Copied: {source_file_path} -> {dest_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    backup_files(source_directory, destination_directory)

#python backup.py /path/to/source /path/to/destination
